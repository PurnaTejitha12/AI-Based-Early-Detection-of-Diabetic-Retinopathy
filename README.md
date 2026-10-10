🩺 AI-Based Early Detection of Diabetic Retinopathy

An AI-powered deep learning application for the preliminary screening of Diabetic Retinopathy (DR) using retinal fundus images.

The project explores how Artificial Intelligence and Deep Learning can be applied to medical image classification to identify visual patterns associated with Diabetic Retinopathy.

<p align="center">

<a href="https://ai-based-early-detection-of-diabetic.onrender.com/"> <img src="https://img.shields.io/badge/Live%20Demo-Visit%20Website-2ea44f?style=for-the-badge" alt="Live Demo"> </a> <a href="https://github.com/PurnaTejitha12/AI-Based-Early-Detection-of-Diabetic-Retinopathy"> <img src="https://img.shields.io/badge/GitHub-Source%20Code-181717?style=for-the-badge&logo=github" alt="GitHub Repository"> </a>

</p>

Disclaimer: This project is intended for educational, research, and demonstration purposes only. Its predictions are not medical diagnoses and must not replace professional eye examinations or advice from qualified healthcare professionals.
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
Running the Application
Model Training and Prediction
Model Evaluation
Deployment
Applications
Future Enhancements
Limitations and Disclaimer
Acknowledgments
License
Project Information
🔍 About the Project

Diabetic Retinopathy (DR) is a diabetes-related eye disease that damages the blood vessels of the retina. If it is not detected and managed appropriately, it can lead to vision impairment or blindness.

Traditional screening often requires retinal imaging equipment, trained eye-care professionals, and access to specialized medical facilities. These requirements can make timely screening challenging, particularly in underserved areas.

AI-Based Early Detection of Diabetic Retinopathy is a deep learning project designed to analyze retinal fundus images and generate predictions based on the classes supported by its trained model.

The application demonstrates a typical AI-based image classification pipeline, from image submission and preprocessing to model inference and result presentation.

Project Highlights
AI-assisted retinal fundus image analysis.
Deep learning-based image classification.
A web interface for submitting retinal images.
Automated prediction using a trained model.
Online deployment for demonstration and experimentation.

The primary goal is to explore the potential of AI-assisted retinal image analysis as a preliminary screening research tool.

🎯 Problem Statement

Diabetic Retinopathy can develop without noticeable symptoms during its early stages. Delayed detection may increase the risk of serious vision complications.

Conventional screening depends on appropriate retinal imaging, trained specialists, and available healthcare infrastructure. Screening large populations can therefore present practical challenges.

This project explores whether a deep learning model can analyze retinal fundus images and identify patterns associated with Diabetic Retinopathy, potentially supporting research into accessible screening workflows.

The application is a prototype and is not intended to independently diagnose patients or determine whether medical care is necessary.

🎯 Project Objectives
Develop an AI-based application for retinal fundus image analysis.
Apply deep learning techniques to medical image classification.
Generate predictions using a trained model.
Provide a simple interface for image submission and result viewing.
Understand image preprocessing and model inference workflows.
Explore AI-assisted screening in resource-limited environments.
Demonstrate the deployment of a deep learning application.
Identify opportunities for future model evaluation and improvement.
✨ Key Features
Retinal Image Upload: Submit retinal fundus images through the application.
Image Preprocessing: Prepare uploaded images according to the model's input requirements.
Deep Learning Inference: Process images using the configured trained model.
Classification Results: Display predictions for the classes supported by the model.
User-Friendly Interface: Provide a straightforward image submission and result-viewing experience.
Web Accessibility: Access the deployed application through a web browser.
Extensible Design: Provide a foundation for future experimentation and enhancements.

Note: The feature list should be aligned with the functionality actually implemented in the current application.

🛠️ Technologies Used

The project uses AI, image processing, and web development concepts. Confirm the exact libraries and frameworks from the repository before finalizing this table.

Technology	Purpose
Python	Core programming language
TensorFlow / Keras or PyTorch	Deep learning model development and inference, if used
Flask / Streamlit / Other framework	Web application, depending on the implementation
NumPy	Numerical computations, if used
Pillow / OpenCV	Image preprocessing, if used
Scikit-learn	Evaluation metrics, if used
Matplotlib / Seaborn	Data visualization, if used
Git and GitHub	Version control and source code hosting
Render	Application hosting and deployment
Remove unused technologies and retain only the packages and services actually used by your project.
🏗️ System Architecture

The application follows a deep learning inference pipeline.

        ┌──────────────────────┐
        │        User          │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  Retinal Fundus Image │
        │        Upload        │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ Image Preprocessing   │
        │ Resize / Normalize*   │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  Trained Deep Learning│
        │        Model          │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  Classification       │
        │  and Prediction       │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ Display Prediction    │
        │    to the User        │
        └──────────────────────┘


Preprocessing operations depend on the actual model implementation.

🔄 System Workflow
Image Input: The user uploads a retinal fundus image.
Image Validation: The application checks the uploaded file, if implemented.
Preprocessing: The image is prepared according to the model's expected dimensions and input format.
Model Loading: The application loads or accesses the trained model.
Feature Extraction: The model processes the image to identify learned visual patterns.
Classification: The model generates a prediction for its supported classes.
Result Display: The application presents the prediction to the user.
📂 Project Structure

The following is an example structure for a Python-based application. Modify it to match the files and directories present in the actual GitHub repository.

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

Directory and File Descriptions
File / Directory	Description
app.py	Main web application entry point, if applicable
requirements.txt	Python dependency list
models/	Trained model files, if stored locally
src/	Model training, preprocessing, and prediction code, if organized this way
notebooks/	Jupyter notebooks used for experiments, if present
dataset/	Dataset organization, if included
.gitignore	Specifies files excluded from Git
README.md	Project documentation
LICENSE	License terms, if a license has been selected

Important: This tree is illustrative. Do not add nonexistent files to the documentation or commit confidential patient data. Large model files and datasets may need external storage or Git LFS.

⚙️ Installation and Setup
Prerequisites

Install the following tools before setting up the application:

Python version compatible with the project's dependencies.
pip package manager.
Git.
Access to the trained model, if required by the application.
Step 1: Clone the Repository
git clone https://github.com/PurnaTejitha12/AI-Based-Early-Detection-of-Diabetic-Retinopathy.git

Step 2: Navigate to the Project Directory
cd AI-Based-Early-Detection-of-Diabetic-Retinopathy

Step 3: Create a Virtual Environment
python -m venv venv


Activate the environment on Windows:

venv\Scripts\activate


On macOS or Linux:

source venv/bin/activate

Step 4: Install Dependencies

If the repository contains a requirements.txt file, run:

pip install -r requirements.txt


If the file is not present, install the dependencies specified by the actual application. Avoid installing arbitrary framework or machine learning packages without checking compatibility.

Step 5: Configure the Trained Model

Ensure the trained model is available at the path expected by the application.

For example:

models/
└── dr_detection_model.keras


The filename and format above are illustrative. Use the actual model path and file format configured in your code.

🚀 Running the Application

Run the application using the command corresponding to the framework implemented in your repository.

For Flask:

python app.py


For Streamlit:

streamlit run app.py


For FastAPI with Uvicorn:

uvicorn app.main:app --reload


These are alternative commands, not commands to execute together. Choose the one appropriate for your project.

Once the application starts, open the local URL printed in the terminal. For example, Flask or Streamlit applications commonly provide a local development address.

🧠 Model Training and Prediction
Model Training

If the repository contains a training script, use the command configured for that script.

For example:

python src/train.py


Alternatively, model training may be performed through a Jupyter Notebook or Google Colab.

If the application uses an existing trained model and does not include a training pipeline, model training is not required to run the application.

Prediction

If the repository includes a prediction script that accepts an image argument, an example command may look like this:

python src/predict.py --image path/to/retinal_image.jpg


This command is applicable only if the prediction script supports the --image argument.

Otherwise, upload the retinal fundus image through the web interface and view the result returned by the application.

Prediction Output

The application generates a prediction according to the classes and output format supported by the configured model.

The precise class labels, confidence scores, and output interpretation depend on the implementation. A model confidence score should not be interpreted as a verified probability of disease or as a clinical diagnosis without appropriate validation and calibration.

📊 Model Evaluation

A reliable evaluation should use an independent test dataset that was not used to train or tune the model.

The following metrics may be considered when evaluating the model:

Metric	Description
Accuracy	Proportion of correctly classified samples
Precision	Proportion of predicted positive cases that are actually positive
Recall / Sensitivity	Proportion of actual positive cases correctly identified
Specificity	Proportion of actual negative cases correctly identified
F1-Score	Harmonic mean of precision and recall
ROC-AUC	Measures discrimination across classification thresholds
Confusion Matrix	Summarizes correct and incorrect classifications

For medical screening research, sensitivity, specificity, class-wise performance, image quality, and independent validation are particularly important.

Evaluation results: Add actual metrics, dataset details, and test conditions only after running and documenting the evaluation. Do not report unverified accuracy figures or claim clinical effectiveness without supporting evidence.

☁️ Deployment

The project has a live deployment listed on Render.

Live Application: https://ai-based-early-detection-of-diabetic.onrender.com/
Source Repository: https://github.com/PurnaTejitha12/AI-Based-Early-Detection-of-Diabetic-Retinopathy
General Deployment Workflow
Push the application code to GitHub.
Ensure the dependency file is configured correctly.
Confirm that the trained model is accessible in the deployment environment.
Connect the repository to Render.
Configure the appropriate build and start commands.
Add any required environment variables.
Deploy the application.
Test image uploads, model inference, and result display in the deployed environment.
Example Render Configuration for Flask

Build Command

pip install -r requirements.txt


Start Command

gunicorn app:app


The example start command assumes that the root-level app.py file exposes a Flask application object named app and that Gunicorn is included in the dependencies. Adjust the command to match the actual project.

For other frameworks, use the appropriate start command and deployment configuration.

🌍 Applications

Potential applications and research directions include:

Preliminary Diabetic Retinopathy screening research.
AI-assisted retinal fundus image analysis.
Medical image classification experiments.
Academic demonstrations of deep learning.
Research into screening workflows for underserved regions.
Development of future screening support tools following appropriate validation.

These are potential applications and research directions, not claims of established clinical suitability.

🔮 Future Enhancements
Transfer Learning: Explore pretrained convolutional neural networks for image classification.
Explainable AI: Investigate Grad-CAM and related techniques to visualize model attention.
Image Quality Assessment: Detect unsuitable or low-quality retinal images before inference.
Model Evaluation: Evaluate class-wise performance using independent datasets.
Robustness Testing: Assess performance across different retinal cameras and populations.
User Experience: Improve image upload feedback, error handling, and accessibility.
Batch Processing: Explore processing multiple images in a single workflow.
Reporting: Add downloadable prediction summaries with appropriate limitations.
Privacy and Security: Implement appropriate data protection and secure handling of uploaded images.
Clinical Validation: Conduct rigorous independent and clinical validation before considering clinical use.
⚠️ Limitations and Disclaimer

This project is developed for educational, research, and demonstration purposes.

Not a medical diagnosis: Predictions must not be used as the sole basis for medical decisions.
Model limitations: Results may be affected by image quality, dataset limitations, model architecture, and preprocessing.
Generalization: Performance may vary across populations, retinal cameras, and imaging conditions.
False predictions: The model may incorrectly classify images or fail to identify disease-related patterns.
Clinical validation: The application should not be considered clinically validated unless appropriate evidence establishes this.
Professional consultation: Users should consult qualified eye-care professionals for screening, diagnosis, and treatment decisions.
Data privacy: Retinal images may contain sensitive health information. Use appropriate safeguards and avoid uploading identifiable patient images to public services without authorization.

A prediction indicating no detected disease does not rule out Diabetic Retinopathy. A prediction indicating possible disease does not confirm its presence.

Clinical deployment would require rigorous validation, appropriate privacy and security measures, safety assessments, and compliance with applicable regulations.

🙏 Acknowledgments

We acknowledge the researchers, dataset providers, open-source contributors, and developers whose work supports advancements in Artificial Intelligence and medical image analysis.

We also appreciate the guidance, feedback, and support received during the development of this academic project.

Any specific dataset, model architecture, research paper, or external resource used should be credited here.

📄 License

Add the selected open-source license to the repository and include its terms in the LICENSE file.

Until a license is selected and included, users should not assume that permission has been granted to reuse, modify, or redistribute the project's code.

📌 Project Information
Field	Details
Project Title	AI-Based Early Detection of Diabetic Retinopathy
Domain	Artificial Intelligence and Deep Learning
Application Area	Medical Image Analysis
Project Type	Academic Project
Primary Input	Retinal Fundus Images
Main Objective	Explore AI-assisted DR image classification
Source Code	GitHub Repository
Live Demo	Open Application
Deployment Platform	Render

<p align="center">

AI-Based Early Detection of Diabetic Retinopathy

Exploring the role of deep learning in retinal image analysis.

</p>

<p align="center"> If you find this project useful for learning or research, consider starring the repository on GitHub. </p>