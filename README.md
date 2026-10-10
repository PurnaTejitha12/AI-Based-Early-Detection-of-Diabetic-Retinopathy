AI-Based Early Detection of Diabetic Retinopathy

An AI-powered deep learning application for the early screening of Diabetic Retinopathy (DR) using retinal fundus images.

🚀 Live Demo : https://ai-based-early-detection-of-diabetic.onrender.com/

🌐 Live Website: View AI-Based Diabetic Retinopathy Detection

Upload a retinal fundus image to explore the application's prediction capabilities.

Disclaimer: This application is intended for educational and research purposes. Its predictions are not a medical diagnosis and must not replace professional eye examinations.
📌 Table of Contents
About the Project
Problem Statement
Project Objectives
Key Features
Technologies Used
System Workflow
Project Structure
Installation and Setup
Model Training and Prediction
Model Evaluation
Deployment
Applications
Future Enhancements
Limitations and Disclaimer
Acknowledgments
License
🩺 About the Project

Diabetic Retinopathy (DR) is a diabetes-related eye disease that damages the blood vessels of the retina. If left undetected and untreated, it can lead to severe vision impairment or blindness.

Traditional screening methods depend on trained ophthalmologists and specialized medical facilities. Limited access to eye-care services, increasing healthcare demands, and the growing prevalence of diabetes can make timely screening challenging.

AI-Based Early Detection of Diabetic Retinopathy explores the use of Artificial Intelligence (AI) and Deep Learning to analyze retinal fundus images and identify visual patterns associated with the disease.

The system uses a trained deep learning model to process retinal images and generate predictions based on the classes supported by the implemented model.

The primary goal is to demonstrate how AI-assisted image analysis can support preliminary screening and research in medical image analysis.

❗ Problem Statement

Diabetic Retinopathy can progress without noticeable symptoms during its early stages. Delayed screening may result in the disease being detected only after significant retinal damage has occurred.

Manual retinal image assessment requires trained professionals and can become resource-intensive when large numbers of patients need screening.

Therefore, an AI-based approach can be explored to automate aspects of retinal image analysis, recognize patterns associated with Diabetic Retinopathy, and support timely referral for professional evaluation.

The proposed project uses deep learning to investigate automated retinal image classification.

🎯 Project Objectives
Develop an AI-based system for analyzing retinal fundus images.
Apply deep learning techniques to medical image classification.
Identify image patterns associated with Diabetic Retinopathy.
Generate predictions using a trained model.
Provide a simple interface for submitting retinal images.
Explore AI-assisted screening for resource-limited healthcare environments.
Demonstrate the integration of deep learning into a deployable application.
✨ Key Features
Retinal Image Upload: Submit retinal fundus images for analysis.
Automated Image Processing: Prepare images according to the model's input requirements.
Deep Learning Prediction: Use a trained model to generate predictions.
Classification Results: Display the predicted class or severity category supported by the model.
User-Friendly Interface: Make image submission and result viewing straightforward.
Web Deployment: Access the application through its deployed website.
Extensible Architecture: Provide a foundation for future model improvements and additional features.

The availability of individual features depends on the actual implementation.

🛠️ Technologies Used
Technology	Purpose
Python	Application development
TensorFlow / Keras or PyTorch	Deep learning inference, depending on the model
Flask, Streamlit, or another framework	Web application interface, depending on implementation
NumPy	Numerical computations
Pillow / OpenCV	Image processing
Scikit-learn	Model evaluation, if used
Matplotlib / Seaborn	Visualization, if used
Git and GitHub	Version control and source-code hosting
Render or another hosting platform	Application deployment

Only the technologies actually used in the implementation should be retained in this list.

🔄 System Workflow

The application follows this general workflow:

Image Input: The user uploads a retinal fundus image.
Image Preprocessing: The image is resized and normalized according to the trained model's requirements.
Model Loading: The application loads the pretrained deep learning model.
Feature Analysis: The model processes the image to identify learned visual patterns.
Classification: The model generates a prediction for the supported class or severity level.
Result Display: The application displays the prediction to the user.
Workflow Diagram
       Retinal Fundus Image
                |
                v
        Image Preprocessing
                |
                v
       Pretrained Deep Learning
                Model
                |
                v
        Feature Extraction
                |
                v
        DR Classification
                |
                v
        Prediction Result

📁 Project Structure

The following is a suggested structure. Update it to match the actual files in your repository.

AI-Based-Early-Detection-of-Diabetic-Retinopathy/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
│
├── models/
│   └── dr_detection_model.keras
│
├── src/
│   ├── preprocessing.py
│   ├── predict.py
│   └── train.py
│
├── notebooks/
│   └── model_training.ipynb
│
└── dataset/
    ├── train/
    ├── validation/
    └── test/

Directory Description
app.py — Application entry point, if applicable.
requirements.txt — Python package dependencies.
.gitignore — Files and directories excluded from version control.
models/ — Trained model files, if stored locally.
src/ — Image preprocessing, training, and prediction code.
notebooks/ — Model development and experimentation notebooks.
dataset/ — Training, validation, and test images, if stored locally.
README.md — Project documentation.

Large datasets and model files may need external storage or Git LFS. Do not upload confidential patient images or sensitive information to a public repository.

⚙️ Installation and Setup
Prerequisites
Python compatible with the project's dependencies
pip package manager
Git
A compatible retinal fundus image dataset for training, if required
A trained model for inference
1. Clone the Repository

https://github.com/PurnaTejitha12/AI-Based-Early-Detection-of-Diabetic-Retinopathy

cd AI-Based-Early-Detection-of-Diabetic-Retinopathy

https://github.com/PurnaTejitha12/AI-Based-Early-Detection-of-Diabetic-Retinopathy

2. Create a Virtual Environment
python -m venv venv


Activate it on Windows:

venv\Scripts\activate


On Linux or macOS:

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt


Ensure that requirements.txt includes the packages required by the application and the selected deep learning framework.

4. Configure the Trained Model

Ensure that the application can access the trained model at the path configured in the code.

For example:

models/dr_detection_model.keras


This is an example path. Use the actual model filename and format from your project.

If the model is hosted externally, configure the application to retrieve it securely at runtime.

🧠 Model Training and Prediction
Model Training

If the repository includes a training script, run:

python src/train.py


Alternatively, execute the training notebook in Jupyter Notebook or Google Colab.

Training requires an appropriately labeled dataset and the preprocessing steps expected by the model.

If the project uses an existing pretrained model and does not include training code, this step can be omitted.

Prediction

If the project includes a command-line prediction script that accepts an --image argument, run:

python src/predict.py --image path/to/retinal_image.jpg


The command depends on the actual implementation of predict.py.

If predictions are available only through the web application, upload an image through the application's interface instead.

Running the Application Locally

Use the command appropriate for your framework.

For Flask:

python app.py


For Streamlit:

streamlit run app.py


For FastAPI:

uvicorn app.main:app --reload


These commands are alternatives, not commands to run together. Select the one corresponding to your application's framework and file structure.

📊 Model Evaluation

Evaluate the model using a separate test dataset that was not used for training or model selection.

Metric	Description
Accuracy	Overall proportion of correct predictions
Precision	Proportion of positive predictions that are correct
Recall / Sensitivity	Ability to identify positive cases
Specificity	Ability to identify negative cases
F1-Score	Balance between precision and recall
ROC-AUC	Discriminative performance for supported classification tasks
Confusion Matrix	Summary of correct and incorrect predictions

For medical screening, sensitivity, specificity, class-wise performance, image-quality robustness, and independent validation are particularly important.

Note: Add actual evaluation scores only after running and documenting the model evaluation. Do not assume that high accuracy alone establishes clinical suitability.

🌐 Deployment

The application can be deployed to a compatible hosting platform, such as Render, depending on its framework and resource requirements.

General Deployment Steps
Push the application code to GitHub.
Confirm that requirements.txt is present in the repository.
Ensure the trained model is accessible to the deployed application.
Create a web service on the chosen hosting platform.
Configure the appropriate build and start commands.
Set required environment variables securely.
Deploy and test the application using sample images.
Example Render Configuration for Flask

Build Command:

pip install -r requirements.txt


Start Command, if the Flask application variable is named app in the root-level app.py file:

gunicorn app:app


If your project uses another framework or a different file structure, configure the corresponding start command instead.

Live Application

Visit the deployed application here:

Open the Live Diabetic Retinopathy Detection Website

Replace YOUR_DEPLOYMENT_URL with your actual deployment link.

🏥 Applications

Potential applications and research uses include:

Preliminary diabetic retinopathy screening research.
AI-assisted retinal image analysis.
Medical image classification experiments.
Educational demonstrations of deep learning in healthcare.
Research into screening solutions for underserved regions.
Future integration with clinical screening workflows after appropriate validation.
🚀 Future Enhancements
Explore transfer learning using pretrained CNN architectures.
Add Explainable AI techniques such as Grad-CAM.
Improve handling of low-quality and blurred retinal images.
Evaluate robustness across different retinal cameras and populations.
Add secure patient screening records where appropriate.
Improve inference speed and deployment efficiency.
Add batch image processing and downloadable reports.
Perform external validation and clinical evaluation before considering real-world use.
⚠️ Limitations and Disclaimer

This project is intended for educational, research, and demonstration purposes.

The model's predictions are not a medical diagnosis and should not be used independently to make treatment decisions. The system may produce incorrect results due to image quality, dataset limitations, differences in patient populations, and variations in retinal imaging equipment.

A prediction indicating no detected disease does not rule out Diabetic Retinopathy. Users should consult qualified eye-care professionals for appropriate screening, diagnosis, and treatment.

Clinical deployment requires rigorous validation, privacy protections, safety assessments, and compliance with applicable regulations.

🙏 Acknowledgments

We acknowledge the researchers, dataset providers, open-source contributors, and developers whose work supports advances in artificial intelligence and medical image analysis.

We also appreciate everyone who contributed guidance, feedback, and support during the development of this project.

📄 License

Choose an appropriate open-source license and include it in the repository's LICENSE file.

Until a license is selected, no specific permission to reuse, modify, or redistribute the project should be assumed.

📌 Project Information
Project Title: AI-Based Early Detection of Diabetic Retinopathy
Domain: Artificial Intelligence | Deep Learning | Medical Image Analysis
Primary Objective: Explore AI-assisted early screening of Diabetic Retinopathy using retinal fundus images.
Live Demo: https://ai-based-early-detection-of-diabetic.onrender.com/