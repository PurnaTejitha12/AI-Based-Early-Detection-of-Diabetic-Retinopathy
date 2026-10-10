AI-Based Early Detection of Diabetic Retinopathy

An AI-powered deep learning application for the early screening of Diabetic Retinopathy (DR) using retinal fundus images.

Live Demo
Live Website: https://ai-based-early-detection-of-diabetic.onrender.com/
GitHub Repository: https://github.com/PurnaTejitha12/AI-Based-Early-Detection-of-Diabetic-Retinopathy
Disclaimer: This project is intended for educational and research purposes. Predictions are not a medical diagnosis and must not replace professional eye examinations.
Table of Contents
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
1. About the Project

Diabetic Retinopathy (DR) is a diabetes-related eye disease that damages the blood vessels of the retina. If left undetected and untreated, it can lead to vision impairment or blindness.

Traditional screening methods rely on trained ophthalmologists and specialized medical facilities. Limited access to eye-care services and the increasing prevalence of diabetes can make timely screening challenging.

AI-Based Early Detection of Diabetic Retinopathy uses Artificial Intelligence (AI) and Deep Learning techniques to analyze retinal fundus images and identify patterns associated with the disease.

The application uses a trained deep learning model to process retinal images and generate predictions based on the classes supported by the model.

The primary objective is to explore AI-assisted retinal image analysis and demonstrate its potential for preliminary screening research.

2. Problem Statement

Diabetic Retinopathy may progress without noticeable symptoms during its early stages. Delayed detection can increase the risk of severe vision complications.

Conventional retinal image assessment requires specialized expertise and can be time-consuming when large numbers of patients need screening.

Therefore, an AI-based system can help automate aspects of retinal image analysis, identify patterns associated with Diabetic Retinopathy, and support timely referral for professional evaluation.

3. Project Objectives
Develop an AI-based system for retinal fundus image analysis.
Apply deep learning techniques to medical image classification.
Identify visual patterns associated with Diabetic Retinopathy.
Generate predictions using a trained model.
Provide a user-friendly interface for image submission.
Explore AI-assisted screening for resource-limited healthcare environments.
Demonstrate the deployment of a deep learning application.
4. Key Features
Retinal Image Upload: Allows users to submit retinal fundus images.
Image Preprocessing: Prepares images according to model requirements.
Deep Learning Prediction: Uses a trained model to analyze retinal images.
Classification Results: Displays predictions for supported classes.
User-Friendly Interface: Simplifies image submission and result viewing.
Web Deployment: Makes the application accessible online.
Extensible Design: Supports future improvements and additional features.

Features should reflect the functionality implemented in the application.

5. Technologies Used
Technology	Purpose
Python	Core programming language
TensorFlow / Keras or PyTorch	Deep learning model
Flask, Streamlit, or another framework	Web application
NumPy	Numerical computations
Pillow / OpenCV	Image preprocessing
Scikit-learn	Model evaluation, if used
Matplotlib / Seaborn	Data visualization, if used
Git and GitHub	Version control
Render	Application deployment

Keep only the technologies actually used in your project.

6. System Architecture

The application follows a deep learning inference pipeline.

        User
         |
         v
  Retinal Fundus Image
         |
         v
  Image Preprocessing
         |
         v
  Trained Deep Learning Model
         |
         v
  DR Classification
         |
         v
  Prediction Result

7. System Workflow
Image Input: The user uploads a retinal fundus image.
Preprocessing: The image is resized and normalized.
Model Loading: The application loads the trained model.
Feature Analysis: The model processes the image.
Classification: The model predicts a supported class.
Result Display: The application displays the prediction.
8. Project Structure

The following is an example structure. Adjust it to match your actual repository.

AI-Based-Early-Detection-of-Diabetic-Retinopathy/
|
|-- app.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- LICENSE
|
|-- models/
|   |-- dr_detection_model.keras
|
|-- src/
|   |-- preprocessing.py
|   |-- predict.py
|   |-- train.py
|
|-- notebooks/
|   |-- model_training.ipynb
|
|-- dataset/
    |-- train/
    |-- validation/
    |-- test/

Directory Description
app.py — Main application file.
requirements.txt — Python dependencies.
.gitignore — Files excluded from Git.
models/ — Trained model files.
src/ — Preprocessing, training, and prediction scripts.
notebooks/ — Model development notebooks.
dataset/ — Training, validation, and testing images.
README.md — Project documentation.
LICENSE — Project licensing terms.

Only include files and directories that exist in your repository.

Large datasets and model files may require external storage or Git LFS. Avoid uploading confidential patient data to a public repository.

9. Installation and Setup
Prerequisites
Python
pip package manager
Git
Required Python libraries
A trained model for prediction
Step 1: Clone the Repository
git clone https://github.com/PurnaTejitha12/AI-Based-Early-Detection-of-Diabetic-Retinopathy.git

Step 2: Navigate to the Project Directory
cd AI-Based-Early-Detection-of-Diabetic-Retinopathy

Step 3: Create a Virtual Environment
python -m venv venv


Activate it on Windows:

venv\Scripts\activate

Step 4: Install Dependencies
pip install -r requirements.txt

Step 5: Configure the Model

Ensure the trained model is available at the path specified in your application.

Example:

models/dr_detection_model.keras


Use the actual model filename and format from your project.

10. Model Training and Prediction
Model Training

If your project includes a training script, execute:

python src/train.py


Alternatively, run the training notebook in Jupyter Notebook or Google Colab.

If the application uses an existing pretrained model without a training script, this step is not required.

Prediction

If your prediction script supports an --image argument, execute:

python src/predict.py --image path/to/retinal_image.jpg


Otherwise, upload the retinal image through the web application.

Run the Application Locally

Use the command appropriate for your framework.

Flask:

python app.py


Streamlit:

streamlit run app.py


FastAPI:

uvicorn app.main:app --reload


These commands are alternatives. Use only the command corresponding to your implementation.

11. Model Evaluation

Evaluate the model using an independent test dataset.

Metric	Description
Accuracy	Overall proportion of correct predictions
Precision	Correctness of positive predictions
Recall / Sensitivity	Ability to identify positive cases
Specificity	Ability to identify negative cases
F1-Score	Balance between precision and recall
ROC-AUC	Ability to distinguish between classes
Confusion Matrix	Summary of correct and incorrect predictions

For medical screening, sensitivity, specificity, class-wise performance, and independent validation are particularly important.

Note: Add actual performance results only after evaluating your model. Do not claim unverified accuracy or clinical effectiveness.

12. Deployment

The application is deployed using Render.

Live Application

https://ai-based-early-detection-of-diabetic.onrender.com/

Deployment Steps
Push the project code to GitHub.
Ensure requirements.txt is present.
Ensure the trained model is accessible to the application.
Connect the GitHub repository to Render.
Configure the build and start commands.
Configure environment variables, if required.
Deploy the application and test its functionality.
Example Render Configuration for Flask

Build Command:

pip install -r requirements.txt


Start Command:

gunicorn app:app


This command assumes your root-level app.py contains a Flask application object named app. Adjust it to match your actual project structure.

13. Applications
Preliminary Diabetic Retinopathy screening research.
AI-assisted retinal image analysis.
Medical image classification experiments.
Educational demonstrations of deep learning.
Research into screening solutions for underserved regions.
Future clinical screening applications following appropriate validation.
14. Future Enhancements
Explore transfer learning using pretrained CNN architectures.
Integrate Explainable AI techniques such as Grad-CAM.
Improve detection robustness for low-quality images.
Evaluate the model across different retinal cameras and populations.
Add secure patient screening records where appropriate.
Improve inference speed and deployment efficiency.
Introduce batch image processing and downloadable reports.
Conduct independent and clinical validation.
15. Limitations and Disclaimer

This project is intended for educational, research, and demonstration purposes.

The model may produce incorrect predictions due to image quality, dataset limitations, population differences, and variations in retinal imaging equipment.

A prediction indicating no detected disease does not rule out Diabetic Retinopathy. The application must not be used as a substitute for professional medical diagnosis or treatment.

Users should consult qualified eye-care professionals for appropriate screening and medical decisions.

Clinical deployment requires rigorous validation, privacy protections, safety assessments, and compliance with applicable regulations.

16. Acknowledgments

We acknowledge the researchers, dataset providers, open-source contributors, and developers whose work supports advancements in Artificial Intelligence and medical image analysis.

We also thank everyone who provided guidance, feedback, and support during the development of this project.

17. License

Choose an appropriate open-source license and include it in the LICENSE file.

Until a license is selected, no specific permission to reuse, modify, or redistribute the project should be assumed.

18. Project Information
Field	Details
Project Title	AI-Based Early Detection of Diabetic Retinopathy
Domain	Artificial Intelligence and Deep Learning
Application Area	Medical Image Analysis
Project Type	Final-Year Academic Project
Source Code	GitHub Repository
Live Demo	Render Application

AI-Based Early Detection of Diabetic Retinopathy

Exploring the role of deep learning in retinal image analysis.