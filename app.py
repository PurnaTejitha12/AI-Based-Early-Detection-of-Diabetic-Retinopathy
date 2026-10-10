from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
    abort,
)
from werkzeug.utils import secure_filename
from pathlib import Path
from datetime import datetime
from uuid import uuid4
from PIL import Image
import sqlite3
import logging
import random

from utils import generate_pdf


# --------------------------------------------------
# APPLICATION CONFIGURATION
# --------------------------------------------------

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent

DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "database.db"

UPLOAD_FOLDER = BASE_DIR / "static" / "uploads"
GRADCAM_FOLDER = BASE_DIR / "static" / "gradcam"
REPORT_FOLDER = BASE_DIR / "static" / "reports"

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "bmp", "tif", "tiff"}
MAX_FILE_SIZE = 10 * 1024 * 1024

app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE

for folder in (
    DATABASE_DIR,
    UPLOAD_FOLDER,
    GRADCAM_FOLDER,
    REPORT_FOLDER,
):
    folder.mkdir(parents=True, exist_ok=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# --------------------------------------------------
# DATABASE
# --------------------------------------------------

def get_db_connection():
    conn = sqlite3.connect(str(DATABASE_PATH), timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                prediction TEXT NOT NULL,
                confidence REAL NOT NULL,
                date TEXT NOT NULL,
                report_path TEXT
            )
        """)


init_db()


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def allowed_file(filename):
    return (
        bool(filename)
        and "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


def generate_demo_result():
    """
    Generate a RANDOM DEMONSTRATION RESULT.

    This function does not analyze the retinal image.
    Do not use its output for medical decisions.
    """
    demo_results = [
        ("No DR", 96.2),
        ("Mild DR", 87.5),
        ("Moderate DR", 91.3),
        ("Severe DR", 82.6),
        ("Proliferative DR", 89.1),
    ]

    return random.choice(demo_results)


def generate_demo_visualization(image_path, filename):
    """
    Save a copy of the uploaded image for interface demonstration.
    This is NOT a real Grad-CAM heatmap.
    """
    output_name = f"{Path(filename).stem}_preview.png"
    output_path = GRADCAM_FOLDER / output_name

    with Image.open(image_path) as image:
        image.convert("RGB").save(output_path, format="PNG")

    return output_name


# --------------------------------------------------
# HOME
# --------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


# --------------------------------------------------
# IMAGE UPLOAD AND DEMO RESULT
# --------------------------------------------------

@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "GET":
        return redirect(url_for("index"))

    if "file" not in request.files:
        return "Please upload an image.", 400

    file = request.files["file"]

    if not file or not file.filename:
        return "Please select an image.", 400

    if not allowed_file(file.filename):
        return (
            "Unsupported image format. Upload JPG, JPEG, PNG, BMP, TIF, or TIFF.",
            400,
        )

    original_name = secure_filename(file.filename)

    if not original_name:
        return "Invalid filename.", 400

    # Save the file with a unique name.
    extension = original_name.rsplit(".", 1)[1].lower()
    filename = f"{uuid4().hex}.{extension}"
    image_path = UPLOAD_FOLDER / filename

    try:
        # Verify that the uploaded file is a readable image.
        file.stream.seek(0)

        with Image.open(file.stream) as image:
            image.verify()

        file.stream.seek(0)

        # Save uploaded image.
        file.save(str(image_path))

        logger.info("Uploaded image: %s", filename)

        # Generate a random demonstration result.
        prediction, confidence = generate_demo_result()

        # Create a preview copy, not a real Grad-CAM heatmap.
        preview_filename = generate_demo_visualization(
            str(image_path),
            filename,
        )

        # Generate PDF report.
        report_name = f"{Path(filename).stem}_report.pdf"

        report_path = generate_pdf(
            filename,
            prediction,
            confidence,
            str(image_path),
            str(GRADCAM_FOLDER / preview_filename),
        )

        # Store only the report filename for safe downloads.
        if report_path:
            report_file = Path(report_path)

            if not report_file.is_absolute():
                report_file = BASE_DIR / report_file

            report_file = report_file.resolve()

            if not report_file.is_relative_to(REPORT_FOLDER.resolve()):
                raise ValueError(
                    "The generated PDF must be inside static/reports/."
                )

            if not report_file.is_file():
                raise FileNotFoundError("PDF report was not generated.")

            report_name = report_file.name
        else:
            report_name = None

        # Save history.
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with get_db_connection() as conn:
            conn.execute(
                """
                INSERT INTO history
                    (filename, prediction, confidence, date, report_path)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    filename,
                    prediction,
                    confidence,
                    current_time,
                    report_name,
                ),
            )

        # Display result.
        return render_template(
            "result.html",
            prediction=prediction,
            confidence=confidence,
            filename=filename,
            gradcam_file=f"gradcam/{preview_filename}",
            report_path=report_name,
            demo_mode=True,
        )

    except Exception:
        logger.exception("Image processing failed.")

        return (
            "Image processing failed. Check the Command Prompt for details.",
            500,
        )


# --------------------------------------------------
# HISTORY
# --------------------------------------------------

@app.route("/history")
def history():

    try:
        with get_db_connection() as conn:
            rows = conn.execute("""
                SELECT id, filename, prediction, confidence, date, report_path
                FROM history
                ORDER BY date DESC, id DESC
            """).fetchall()

        return render_template(
            "history.html",
            data=[tuple(row) for row in rows],
        )

    except sqlite3.Error:
        logger.exception("Could not load prediction history.")
        return "Unable to load history.", 500


# --------------------------------------------------
# PDF DOWNLOAD
# --------------------------------------------------

@app.route("/download/<path:filename>")
def download(filename):

    if not filename or Path(filename).name != filename:
        abort(400)

    report_file = REPORT_FOLDER / filename

    if not report_file.is_file() or report_file.suffix.lower() != ".pdf":
        abort(404)

    return send_from_directory(
        str(REPORT_FOLDER),
        filename,
        as_attachment=True,
    )


# --------------------------------------------------
# UPLOAD SIZE ERROR
# --------------------------------------------------

@app.errorhandler(413)
def file_too_large(error):
    return "File too large. Maximum allowed size is 10 MB.", 413


# --------------------------------------------------
# RUN APPLICATION
# --------------------------------------------------

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
    )