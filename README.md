# Heart-Disease-Prediction-with-Machine-Learning

Heart Disease Prediction using Machine Learning to classify whether a patient has cardiovascular disease based on clinical data. This project includes data preprocessing, EDA, feature engineering, and model building using algorithms like Logistic Regression, Random Forest, and SVM with performance evaluation using accuracy and ROC-AUC.



# ❤️ Heart Disease Prediction using Machine Learning

This project uses machine learning techniques to predict whether a person has heart disease based on clinical and medical data. It includes data preprocessing, exploratory analysis, model training, and a web application for real-time prediction using Flask.

## 🧠 Project Overview

Heart disease is one of the leading causes of death globally. Early prediction can help doctors intervene sooner and save lives. This project builds a classification model using features like age, blood pressure, cholesterol, etc., to determine the presence of heart disease. :contentReference[oaicite:0]{index=0}

## 📁 Repository Structure


Heart-Disease-Prediction-with-Machine-Learning/

│── app.py

│── heart.csv

│── requirements.txt

│── Heart_diseases.ipynb

├── templates/

│     ├── index.html

│     └── result.html

└── static/

└── style.css



## 🛠️ Features

- ✔️ Data cleaning & preprocessing
- ✔️ Exploratory Data Analysis (EDA)
- ✔️ Feature engineering
- ✔️ Model training using ML algorithms
- ✔️ Flask web app for prediction
- ✔️ User input form for real-time prediction

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/chandanpradhan1110/Heart-Disease-Prediction-with-Machine-Learning.git
   cd Heart-Disease-Prediction-with-Machine-Learning
   ```


2. **Create a virtual environment**
   <pre class="overflow-visible! px-0!" data-start="1653" data-end="1736"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>conda create -n heart_env python=3.10
   conda activate heart_env
   </span></span></code></div></div></pre>
3. **Install dependencies**
   <pre class="overflow-visible! px-0!" data-start="1769" data-end="1818"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install -r requirements.txt
   </span></span></code></div></div></pre>

## 🚀 How to Run

### 🧪 Notebook

The Jupyter notebook `Heart_diseases.ipynb` contains:

* Data exploration
* Visualization
* Model training and evaluation

Run it locally or in Google Colab.

### 💻 Flask Web App

Start the Flask application:

<pre class="overflow-visible! px-0!" data-start="2064" data-end="2089"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python app.py
</span></span></code></div></div></pre>

Open your browser and go to:

<pre class="overflow-visible! px-0!" data-start="2121" data-end="2150"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>http:</span><span>//127.0.0.1:5000</span><span>
</span></span></code></div></div></pre>

Enter patient details and get a prediction.

## 📊 Model & Prediction

The deployed model takes clinical parameters such as age, sex, blood pressure, cholesterol, etc., and predicts heart disease risk with good accuracy. The prediction result will display:

* **Heart Disease Detected**
* **No Heart Disease**

## 💡 Screenshots

*(Add screenshots of the web app here for a better presentation)*

## 💬 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📜 License

This project is open source and available under the MIT License.

<pre class="overflow-visible! px-0!" data-start="2731" data-end="2900" data-is-last-node=""><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"></div></div></pre>
