🩺 AI-Based Early Detection of Diabetic Retinopathy

An AI-powered deep learning application for the preliminary screening of Diabetic Retinopathy (DR) using retinal fundus images.

The project explores the use of Artificial Intelligence and Deep Learning to analyze retinal images and identify visual patterns associated with Diabetic Retinopathy.

<p align="center"> <a href="https://ai-based-early-detection-of-diabetic.onrender.com/"> <img src="https://img.shields.io/badge/Live%20Demo-Visit%20Website-2ea44f?style=for-the-badge" alt="Live Demo"> </a> <a href="https://github.com/PurnaTejitha12/AI-Based-Early-Detection-of-Diabetic-Retinopathy"> <img src="https://img.shields.io/badge/GitHub-Source%20Code-181717?style=for-the-badge&logo=github" alt="GitHub Repository"> </a> </p>

Disclaimer: This project is intended for educational, research, and demonstration purposes only. Predictions are not medical diagnoses and must not replace professional eye examinations or advice from qualified healthcare professionals.
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

Diabetic Retinopathy (DR) is a diabetes-related eye disease that damages the blood vessels of the retina. If left undetected and untreated, it can lead to vision impairment or blindness.

Traditional screening methods often require retinal imaging equipment, trained ophthalmologists, and access to specialized healthcare facilities. These requirements can make timely screening challenging, particularly in underserved areas.

AI-Based Early Detection of Diabetic Retinopathy is a deep learning application designed to analyze retinal fundus images and generate predictions based on the classes supported by its trained model.

The application demonstrates a typical medical image classification pipeline, including image submission, preprocessing, model inference, and prediction display.

Project Highlights
AI-assisted retinal fundus image analysis.
Deep learning-based image classification.
Retinal image upload through a web interface.
Automated prediction using a trained model.
Web application deployment using Render.
Opportunities for further experimentation and improvement.

The main objective is to explore AI-assisted retinal image analysis for preliminary screening research.

🎯 Problem Statement

Diabetic Retinopathy can develop without noticeable symptoms during its early stages. Delayed detection may increase the risk of serious vision complications.

Conventional screening requires appropriate retinal imaging, trained specialists, and access to healthcare facilities. Screening large populations can therefore present practical challenges.

This project explores the application of deep learning to retinal fundus image classification. The system aims to identify visual patterns associated with Diabetic Retinopathy and demonstrate how AI can assist research into more accessible screening workflows.

The application is a prototype and is not intended to independently diagnose patients or determine whether medical treatment is necessary.

🎯 Project Objectives
Develop an AI-based application for retinal fundus image analysis.
Apply deep learning techniques to medical image classification.
Generate predictions using a trained model.
Provide a user-friendly interface for image submission.
Display model predictions through a web application.
Understand image preprocessing and model inference.
Explore AI-assisted screening for resource-limited environments.
Demonstrate the deployment of a deep learning application.
Identify opportunities for future evaluation and improvement.
✨ Key Features
1. Retinal Image Upload

Allows users to submit retinal fundus images through the web application.

2. Image Preprocessing

Prepares the uploaded image according to the input requirements of the configured model.

3. Deep Learning Prediction

Uses a trained model to analyze the image and generate a prediction.

4. Classification Results

Displays the prediction for the classes supported by the model.

5. User-Friendly Interface

Provides a simple workflow for submitting images and viewing results.

6. Web Deployment

Makes the application accessible through a web browser.

7. Extensible Design

Provides a foundation for future experimentation, model evaluation, and feature development.

Note: Retain only the features implemented in the actual application.

🛠️ Technologies Used

The following table lists technologies that may be used in this type of application. Verify the repository's dependencies and source code before finalizing the list.

Technology	Purpose
Python	Core programming language
TensorFlow / Keras or PyTorch	Deep learning model development and inference
Flask / Streamlit / Other framework	Web application development
NumPy	Numerical computations
Pillow / OpenCV	Image preprocessing
Scikit-learn	Model evaluation, if used
Matplotlib / Seaborn	Data visualization, if used
Git	Version control
GitHub	Source code hosting
Render	Web application deployment

Important: Remove frameworks and libraries that are not actually used in your project.

🏗️ System Architecture

The application follows a deep learning inference pipeline.

                 +----------------------+
                 |         User         |
                 +----------------------+
                            |
                            v
                 +----------------------+
                 |   Image Upload       |
                 +----------------------+
                            |
                            v
                 +----------------------+
                 | Image Preprocessing  |
                 +----------------------+
                            |
                            v
                 +----------------------+
                 |  Trained AI Model    |
                 +----------------------+
                            |
                            v
                 +----------------------+
                 | DR Classification    |
                 +----------------------+
                            |
                            v
                 +----------------------+
                 | Prediction Result    |
                 +----------------------+


The exact preprocessing steps and model architecture depend on the implementation.

🔄 System Workflow

The application processes a retinal fundus image through the following steps.

Image Upload: The user uploads a retinal fundus image.
Image Validation: The application validates the uploaded file, if implemented.
Image Preprocessing: The image is resized or transformed according to the model's requirements.
Model Loading: The application loads or accesses the trained model.
Feature Extraction: The model processes the image to identify learned visual patterns.
Classification: The model generates a prediction for its supported classes.
Result Display: The application displays the prediction to the user.
📂 Project Structure

The following is an example structure for a Python-based project. Replace it with the actual files and directories present in your GitHub repository.

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

File and Directory Descriptions
File / Directory	Description
app.py	Main application entry point, if applicable
requirements.txt	List of required Python packages
README.md	Project documentation
.gitignore	Specifies files excluded from Git
LICENSE	License terms, if selected
models/	Trained model files, if stored locally
src/	Source code for preprocessing, training, and prediction, if organized this way
notebooks/	Jupyter notebooks used for experimentation, if present
dataset/	Dataset directories, if included

Note: This directory tree is illustrative. Do not document nonexistent files as part of the actual project.

Avoid committing confidential patient information or large datasets to a public repository. Large model files may require external storage or Git LFS.

⚙️ Installation and Setup

Follow these steps to set up the project locally.

Prerequisites
Python version compatible with the project dependencies.
pip package manager.
Git.
Required Python libraries.
Access to the trained model, if required.
Step 1: Clone the Repository

Open a terminal and execute:

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

If your repository contains a requirements.txt file, run:

pip install -r requirements.txt


Ensure that the installed packages are compatible with the Python version and trained model.

Step 5: Configure the Trained Model

Ensure that the trained model is available at the path specified in the application code.

For example:

models/
└── dr_detection_model.keras


The filename above is illustrative. Use the actual model path and file format configured in your project.

🚀 Running the Application

Use the command that matches the framework implemented in your repository.

For Flask
python app.py

For Streamlit
streamlit run app.py

For FastAPI
uvicorn app.main:app --reload


These commands are alternatives. Execute only the command that matches your implementation.

Once the application starts, open the local URL displayed in the terminal.

🧠 Model Training and Prediction
Model Training

If your repository contains a training script, use the command supported by that script.

For example:

python src/train.py


Alternatively, training may be performed through a Jupyter Notebook or Google Colab.

If the application uses an existing trained model and does not include training code, this step is not required to run the application.

Prediction

If your repository contains a prediction script that supports an --image argument, an example command is:

python src/predict.py --image path/to/retinal_image.jpg


This command applies only if the script implements that argument.

Otherwise, upload the retinal fundus image through the web interface and view the generated result.

Prediction Output

The application generates a prediction according to the classes and output format supported by the model.

The class labels, confidence scores, and interpretation depend on the actual implementation. A model confidence score should not be treated as a verified probability of disease without appropriate calibration and validation.

📊 Model Evaluation

Evaluate the trained model using an independent test dataset that was not used to train or tune it.

The following metrics can be used to assess classification performance.

Metric	Description
Accuracy	Proportion of correctly classified samples
Precision	Proportion of predicted positive cases that are actually positive
Recall / Sensitivity	Proportion of actual positive cases correctly identified
Specificity	Proportion of actual negative cases correctly identified
F1-Score	Harmonic mean of precision and recall
ROC-AUC	Measures discrimination across classification thresholds
Confusion Matrix	Summarizes correct and incorrect classifications

For medical screening research, sensitivity, specificity, class-wise performance, and independent validation are particularly important.

Evaluation Results

Add the actual evaluation results after testing the trained model.

Do not report unverified accuracy values or claim clinical effectiveness without supporting evidence.

☁️ Deployment

The project has a live deployment listed on Render.

Live Website: Open Application
GitHub Repository: View Source Code
General Deployment Steps
Push the application code to GitHub.
Ensure the dependency file is configured correctly.
Confirm that the trained model is accessible in the deployment environment.
Connect the GitHub repository to Render.
Configure the build and start commands.
Add required environment variables, if any.
Deploy the application.
Test image uploads, predictions, and result display.
Example Render Configuration for Flask

Build Command

pip install -r requirements.txt


Start Command

gunicorn app:app


This example assumes that the root-level app.py file exposes a Flask application object named app and that Gunicorn is included in the dependencies.

Use the correct configuration for your actual application framework and file structure.

🌍 Applications

Potential applications and research directions include:

Preliminary Diabetic Retinopathy screening research.
AI-assisted retinal fundus image analysis.
Medical image classification experiments.
Educational demonstrations of deep learning.
Research into screening workflows for underserved regions.
Development of future screening support systems after appropriate validation.

These are potential applications, not claims that the model is clinically approved or suitable for independent diagnosis.

🔮 Future Enhancements

The following improvements could be explored in future versions:

Transfer Learning: Experiment with pretrained convolutional neural networks.
Explainable AI: Explore Grad-CAM to visualize image regions influencing predictions.
Image Quality Assessment: Detect blurred or unsuitable images before inference.
Model Evaluation: Report independent test results and class-wise performance.
Robustness Testing: Evaluate performance across different cameras and populations.
Improved User Interface: Enhance accessibility, error handling, and user feedback.
Batch Processing: Support multiple image uploads, if appropriate.
Downloadable Reports: Generate prediction summaries with clear limitations.
Privacy and Security: Improve secure handling of uploaded retinal images.
Clinical Validation: Conduct independent and clinical validation before considering clinical use.
⚠️ Limitations and Disclaimer

This project is intended for educational, research, and demonstration purposes only.

Not a medical diagnosis: Predictions must not be used as the sole basis for medical decisions.
Possible errors: The model may incorrectly classify an image or fail to identify disease-related patterns.
Image quality: Poor lighting, blur, and other image issues may affect predictions.
Dataset limitations: Performance may vary across populations and retinal imaging equipment.
Clinical validation: The application should not be considered clinically validated without appropriate evidence.
Professional consultation: Users should consult qualified eye-care professionals for screening, diagnosis, and treatment.
Data privacy: Retinal images may contain sensitive health information. Use appropriate safeguards and avoid uploading identifiable patient images to public services without authorization.

A prediction indicating no detected disease does not rule out Diabetic Retinopathy. A prediction indicating possible disease does not confirm its presence.

Clinical deployment requires rigorous validation, privacy protections, safety assessments, and compliance with applicable regulations.

🙏 Acknowledgments

We acknowledge the researchers, dataset providers, open-source contributors, and developers whose work supports advancements in Artificial Intelligence and medical image analysis.

We also thank everyone who provided guidance, feedback, and support during the development of this academic project.

Add specific dataset sources, model architectures, research papers, or external resources here if they were used.

📄 License

Choose an appropriate open-source license and include its terms in a LICENSE file in the repository.

Until a license is selected and included, users should not assume that permission has been granted to reuse, modify, or redistribute the project.

📌 Project Information
Field	Details
Project Title	AI-Based Early Detection of Diabetic Retinopathy
Domain	Artificial Intelligence and Deep Learning
Application Area	Medical Image Analysis
Project Type	Academic Project
Input	Retinal Fundus Images
Objective	Explore AI-assisted retinal image classification
Source Code	GitHub Repository
Live Demo	Render Application
Deployment Platform	Render

<p align="center"> <strong>AI-Based Early Detection of Diabetic Retinopathy</strong> <br> Exploring the role of deep learning in retinal image analysis. </p>

<p align="center"> If you find this project useful for learning or research, consider giving the repository a ⭐ on GitHub. </p>