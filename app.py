from flask import Flask, render_template, request, send_file, redirect, url_for
import os
import sqlite3
from datetime import datetime
from model import predict_image
from utils import generate_gradcam, generate_pdf

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
GRADCAM_FOLDER = "static/gradcam"
REPORT_FOLDER = "static/reports"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(GRADCAM_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

def get_db_connection():
    # check_same_thread=False is important for Flask + SQLite
    conn = sqlite3.connect("database.db", check_same_thread=False)
    return conn

# Initialize DB
def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  filename TEXT,
                  prediction TEXT,
                  confidence REAL,
                  date TEXT,
                  report_path TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template("index.html")

# Modified to handle both GET and POST to prevent 405 errors
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return redirect(url_for('index'))

    try:
        print("Request received")

        if 'file' not in request.files:
            return "❌ No file uploaded"

        file = request.files['file']

        if file.filename == '':
            return "❌ No selected file"

        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        print("Saving file:", filepath)
        file.save(filepath)

        print("Running prediction...")
        prediction, confidence = predict_image(filepath)

        print("Generating GradCAM...")
        gradcam_path = generate_gradcam(filepath, filename)

        print("Generating report...")
        report_path = generate_pdf(filename, prediction, confidence, filepath, gradcam_path)

        print("Saving to database...")
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("INSERT INTO history (filename, prediction, confidence, date, report_path) VALUES (?, ?, ?, ?, ?)",
                  (filename, prediction, round(float(confidence), 2), str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), report_path))
        conn.commit()
        conn.close()

        print("Rendering result page...")
        return render_template("result.html",
                               prediction=prediction,
                               confidence=confidence,
                               filename=filename,
                               gradcam_file="gradcam/" + filename,
                               report_path=report_path)

    except Exception as e:
        print("🔥 ERROR:", e)
        return f"<h2>Error Occurred:</h2><p>{e}</p>"

@app.route('/history')
def history():
    try:
        conn = get_db_connection()
        c = conn.cursor()
        data = c.execute("SELECT * FROM history ORDER BY date DESC").fetchall()
        conn.close()
        return render_template("history.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/download/<path:filename>')
def download(filename):
    try:
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True, port=5000) # Explicitly setting port 5000