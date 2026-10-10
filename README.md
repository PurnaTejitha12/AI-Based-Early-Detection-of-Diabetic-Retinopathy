🩺 AI-Based Early Detection of Diabetic Retinopathy

An AI-powered deep learning application for the early screening of Diabetic Retinopathy (DR) using retinal fundus images.

<p align="center"> <a href="https://ai-based-early-detection-of-diabetic.onrender.com/"> <img src="https://img.shields.io/badge/Live%20Demo-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" alt="Live Demo"> </a> <a href="https://github.com/PurnaTejitha12/AI-Based-Early-Detection-of-Diabetic-Retinopathy"> <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub Repository"> </a> </p>

🌐 Live Demo

Live Website: AI-Based Early Detection of Diabetic Retinopathy

The application demonstrates how deep learning can be used to analyze retinal fundus images and generate predictions based on the classes supported by the trained model.

Medical Disclaimer: This project is intended for educational and research purposes. Its predictions are not a medical diagnosis and must not replace professional eye examinations or medical advice.
📑 Table of Contents
About the Project
Problem Statement
Project Objectives
Key Features
Technologies Used
System Architecture
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
Project Information
🩺 About the Project

Diabetic Retinopathy (DR) is a diabetes-related eye disease that damages the blood vessels of the retina. If left undetected and untreated, it can lead to severe vision impairment or blindness.

Traditional screening methods depend on trained ophthalmologists and specialized medical facilities. Limited access to eye-care services, increasing healthcare demands, and the growing prevalence of diabetes can make timely screening challenging.

AI-Based Early Detection of Diabetic Retinopathy explores the use of Artificial Intelligence (AI) and Deep Learning to analyze retinal fundus images and identify visual patterns associated with the disease.

The system uses a trained deep learning model to process retinal images and generate predictions based on the classes supported by the implemented model.

The primary goal is to demonstrate how AI-assisted image analysis can support preliminary screening research and contribute to the development of accessible retinal image analysis systems.

❗ Problem Statement

Diabetic Retinopathy can progress without noticeable symptoms during its early stages. Delayed screening may result in the disease being detected only after significant retinal damage has occurred.

Conventional retinal image assessment requires specialized expertise and can become resource-intensive when large numbers of patients need screening. These limitations may delay the identification of individuals who require further examination.

Therefore, an AI-based approach is explored to automate aspects of retinal image analysis, identify patterns associated with Diabetic Retinopathy, and support timely referral for professional evaluation.

🎯 Project Objectives
Develop an AI-based system for analyzing retinal fundus images.
Apply deep learning techniques to medical image classification.
Identify visual patterns associated with Diabetic Retinopathy.
Generate predictions using a trained model.
Provide a user-friendly interface for retinal image submission.
Explore AI-assisted screening solutions for resource-limited healthcare environments.
Demonstrate the integration and deployment of a deep learning application.
✨ Key Features
Retinal Image Upload: Allows users to submit retinal fundus images for analysis.
Automated Image Preprocessing: Prepares input images according to the model's requirements.
Deep Learning Prediction: Uses a trained model to generate predictions.
Classification Results: Displays the predicted class or severity category supported by the model.
User-Friendly Interface: Simplifies image submission and result viewing.
Web-Based Access: Makes the application accessible through a deployed website.
Extensible Design: Provides a foundation for future improvements to the model and application.

Feature availability depends on the actual implementation.

🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
TensorFlow / Keras or PyTorch	Deep learning model inference, depending on implementation
Flask, Streamlit, or another framework	Web application development, depending on implementation
NumPy	Numerical computations
Pillow / OpenCV	Image preprocessing
Scikit-learn	Model evaluation, if used
Matplotlib / Seaborn	Data visualization, if used
Git and GitHub	Version control and source-code management
Render	Web application deployment

Retain only the technologies actually used in the project.

🏗️ System Architecture

The system follows a general deep learning inference architecture.

       ┌──────────────────────────┐
       │          User            │
       └────────────┬─────────────┘
                    │
                    ▼
       ┌──────────────────────────┐
       │   Retinal Fundus Image   │
       │         Upload           │
       └────────────┬─────────────┘
                    │
                    ▼
       ┌──────────────────────────┐
       │    Image Preprocessing   │
       └────────────┬─────────────┘
                    │
                    ▼
       ┌──────────────────────────┐
       │  Trained Deep Learning   │
       │          Model           │
       └────────────┬─────────────┘
                    │
                    ▼
       ┌──────────────────────────┐
       │   DR Classification      │
       └────────────┬─────────────┘
                    │
                    ▼
       ┌──────────────────────────┐
       │   Prediction Display     │
       └──────────────────────────┘

🔄 System Workflow

The application follows these steps:

Image Input: The user uploads a retinal fundus image.
Preprocessing: The image is resized and normalized according to the model's input requirements.
Model Loading: The application loads the trained or pretrained deep learning model.
Feature Analysis: The model processes the image to identify learned visual patterns.
Classification: The model generates a prediction for the supported class or severity category.
Result Generation: The predicted result is presented through the application's interface.
📁 Project Structure

The following is a suggested structure. Adjust it to match the actual files in your repository.

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
File / Directory	Description
app.py	Main application entry point, if applicable
requirements.txt	Lists the required Python dependencies
.gitignore	Specifies files excluded from Git tracking
models/	Stores trained model files, if included locally
src/	Contains preprocessing, training, and prediction scripts
notebooks/	Contains experimentation and training notebooks
dataset/	Contains dataset images, if stored locally
README.md	Project documentation
LICENSE	Defines reuse and distribution terms

Large datasets and trained model files may require external storage or Git LFS. Avoid committing confidential patient information or sensitive medical images to a public repository.

⚙️ Installation and Setup
Prerequisites
Python compatible with the project's dependencies
pip package manager
Git
A trained model for prediction
A compatible labeled dataset if training is required
Step 1: Clone the Repository
git clone https://github.com/PurnaTejitha12/AI-Based-Early-Detection-of-Diabetic-Retinopathy.git


Navigate to the project directory:

cd AI-Based-Early-Detection-of-Diabetic-Retinopathy

Step 2: Create a Virtual Environment
python -m venv venv


Activate the environment on Windows:

venv\Scripts\activate


On Linux or macOS:

source venv/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt


Ensure that requirements.txt contains the libraries required by your actual application and deep learning framework.

Step 4: Configure the Trained Model

Ensure that the model is available at the path expected by your application.

Example:

models/dr_detection_model.keras


This is an example filename. Use the actual model filename and format used by your project.

If the model is hosted externally, configure the application to retrieve it securely at runtime.

🧠 Model Training and Prediction
Model Training

If the repository contains a training script, execute:

python src/train.py


Alternatively, use the model training notebook in Jupyter Notebook or Google Colab.

Training requires an appropriately labeled dataset and the preprocessing steps expected by the model.

If the project uses an existing pretrained model and does not include training code, this step can be omitted.

Prediction

If the project includes a command-line prediction script that accepts an --image argument, execute:

python src/predict.py --image path/to/retinal_image.jpg


This command assumes that predict.py supports the --image argument. Adjust it according to the actual implementation.

If prediction is available only through the web interface, upload an image using the application instead.

Running the Application Locally

Use the command appropriate for the framework implemented in the project.

Flask:

python app.py


Streamlit:

streamlit run app.py


FastAPI:

uvicorn app.main:app --reload


These are alternative commands. Use only the one corresponding to your project's framework and file structure.

📊 Model Evaluation

Model performance should be measured using an independent test dataset that was not used for training or model selection.

Metric	Description
Accuracy	Overall proportion of correct predictions
Precision	Proportion of positive predictions that are correct
Recall / Sensitivity	Ability to identify positive cases
Specificity	Ability to identify negative cases
F1-Score	Balance between precision and recall
ROC-AUC	Ability to distinguish between classes
Confusion Matrix	Summary of correct and incorrect predictions

For medical screening, sensitivity, specificity, class-wise performance, image-quality robustness, and external validation are particularly important.

Note: Actual evaluation results should be added only after testing the trained model. Accuracy alone does not establish clinical suitability.

🌐 Deployment

The application is deployed using Render.

Live Application

Website: https://ai-based-early-detection-of-diabetic.onrender.com/

Deployment Process
Push the application code to GitHub.
Ensure that requirements.txt is present in the repository.
Ensure that the trained model is accessible to the application.
Connect the GitHub repository to Render.
Configure the build and start commands for the selected framework.
Configure required environment variables securely.
Deploy the application and test its functionality.
Example Render Configuration for Flask

Build Command:

pip install -r requirements.txt


Start Command:

gunicorn app:app


The example assumes that the main file is app.py in the repository root and that the Flask application object is named app. Adjust the command to match your implementation.

🏥 Applications

Potential applications and research uses include:

Preliminary Diabetic Retinopathy screening research.
AI-assisted retinal image analysis.
Medical image classification experiments.
Educational demonstrations of deep learning in healthcare.
Research into screening solutions for underserved regions.
Future integration with clinical screening workflows following appropriate validation.
🚀 Future Enhancements
Explore transfer learning using pretrained CNN architectures.
Integrate Explainable AI techniques such as Grad-CAM.
Improve the handling of blurred and low-quality retinal images.
Evaluate robustness across different retinal cameras and patient populations.
Add secure patient screening records where appropriate.
Improve inference speed and deployment efficiency.
Introduce batch image processing and downloadable reports.
Conduct independent validation and clinical evaluation before real-world deployment.
⚠️ Limitations and Disclaimer

This project is intended for educational, research, and demonstration purposes.

The model's predictions are not a medical diagnosis and should not be used independently to make treatment decisions. Predictions may be affected by image quality, dataset limitations, differences in patient populations, and variations in retinal imaging equipment.

A prediction indicating no detected disease does not rule out Diabetic Retinopathy. Users should consult qualified eye-care professionals for appropriate screening, diagnosis, and treatment.

Clinical deployment requires rigorous validation, privacy protections, safety assessments, and compliance with applicable regulations.

🙏 Acknowledgments

We acknowledge the researchers, dataset providers, open-source contributors, and developers whose work supports advances in artificial intelligence and medical image analysis.

We also thank everyone who provided guidance, feedback, and support during the development of this project.

📄 License

Choose an appropriate open-source license and include it in the repository's LICENSE file.

Until a license is selected, no specific permission to reuse, modify, or redistribute the project's code should be assumed.

📌 Project Information
Field	Details
Project Title	AI-Based Early Detection of Diabetic Retinopathy
Domain	Artificial Intelligence, Deep Learning, Medical Image Analysis
Primary Objective	Explore AI-assisted early screening using retinal fundus images
Source Code	GitHub Repository
Live Demo	Render Application
Project Type	Final-Year Academic Project

<p align="center"> <b>AI-Based Early Detection of Diabetic Retinopathy</b><br> <i>Exploring the role of deep learning in retinal image analysis.</i> </p>