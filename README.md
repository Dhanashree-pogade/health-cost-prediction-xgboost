# 🩺 Health Cost Prediction using XGBoost

A Machine Learning web application that predicts **healthcare/insurance costs** based on patient information such as age, sex, BMI, number of children, smoking status, and region.

The model is built using **XGBoost Regressor** and deployed as a web application using **Flask** and **Gunicorn**.

## 🌐 Live Demo

🚀 **Try the application here:**

https://health-cost-prediction-xgboost-1.onrender.com/

---

## 🚀 Features

* 🧠 XGBoost Regression model
* 👤 Patient information input
* 📊 Healthcare cost prediction
* 🎨 Attractive and responsive web interface
* 🌐 Flask-based web application
* ⚡ Gunicorn production server
* ☁️ Deployed on Render
* 📱 Responsive design for desktop and mobile

---

## 🛠️ Technologies Used

* **Python**
* **XGBoost**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Flask**
* **Gunicorn**
* **HTML**
* **CSS**
* **Render**

---

## 📋 Input Features

The model uses the following six features:

| Feature  | Description                   |
| -------- | ----------------------------- |
| Age      | Age of the individual         |
| Sex      | Gender of the individual      |
| BMI      | Body Mass Index               |
| Children | Number of children/dependents |
| Smoker   | Smoking status                |
| Region   | Residential region            |

---

## 🧠 Machine Learning Model

The project uses an **XGBoost Regressor** to predict healthcare/insurance costs.

The trained model is saved as:

```text
xgboost.pkl
```

The Flask application loads this model and uses the user's input to generate a prediction.

---

## 📂 Project Structure

```text
health-cost-prediction-xgboost/
│
├── app.py
├── xgboost.pkl
├── requirements.txt
└── README.md
```

### File Description

**app.py**
Contains the Flask application, user interface, input processing, and prediction logic.

**xgboost.pkl**
Contains the trained XGBoost regression model.

**requirements.txt**
Contains the Python dependencies required to run the application.

**README.md**
Project documentation.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/health-cost-prediction-xgboost.git
```

### 2. Navigate to the project folder

```bash
cd health-cost-prediction-xgboost
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application Locally

Run:

```bash
python app.py
```

Then open your browser and visit:

```text
http://localhost:5000
```

---

## 🌐 Deployment on Render

This project is deployed on **Render** and is ready for cloud deployment.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

Make sure the repository contains:

```text
app.py
xgboost.pkl
requirements.txt
```

---

## 🔮 How It Works

```text
User Input
    ↓
Patient Information
    ↓
Data Preprocessing
    ↓
XGBoost Regression Model
    ↓
Predicted Healthcare Cost
    ↓
Result Displayed on Web Interface
```

---

## 📊 Prediction Process

The application collects:

* Age
* Sex
* BMI
* Number of children
* Smoking status
* Region

These values are converted into the format expected by the trained model and passed to the **XGBoost Regressor**.

The model then returns the estimated healthcare/insurance cost.

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how a trained Machine Learning regression model can be integrated into a web application and deployed online.

It combines:

**Machine Learning + Flask + Web Development + Cloud Deployment**

---

## ⚠️ Disclaimer

This application is developed for **educational and demonstration purposes only**.

The predictions should not be considered professional medical, financial, or insurance advice.

---

## 👩‍💻 Author

**Dhanashree Pogade**

B.Tech Data Science Graduate

Interested in Data Analytics, Machine Learning, and AI.

---

## ⭐ If You Like This Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
