import cv2
from reportlab.pdfgen import canvas

def generate_gradcam(img_path, filename):
    try:
        img = cv2.imread(img_path)

        if img is None:
            return "uploads/" + filename

        heatmap = cv2.applyColorMap(img, cv2.COLORMAP_JET)

        output_path = "static/gradcam/" + filename
        cv2.imwrite(output_path, heatmap)

        return "gradcam/" + filename

    except Exception as e:
        print("❌ GradCAM Error:", e)
        return "uploads/" + filename


def generate_pdf(filename, prediction, confidence, img_path, gradcam_path):
    report_path = "static/reports/" + filename + ".pdf"

    try:
        c = canvas.Canvas(report_path)
        c.drawString(50, 800, "DR Detection Report")
        c.drawString(50, 770, f"Prediction: {prediction}")
        c.drawString(50, 750, f"Confidence: {confidence}%")
        c.save()
    except Exception as e:
        print("❌ PDF Error:", e)

    return report_path
