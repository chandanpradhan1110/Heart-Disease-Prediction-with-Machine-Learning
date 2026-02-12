from flask import Flask,request,render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load Daved Artifacts
model = pickle.load(open('knn_model.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    # Collect form inputs
    data = [
        float(request.form["age"]),
        float(request.form["trestbps"]),
        float(request.form["chol"]),
        float(request.form["thalach"]),
        float(request.form["oldpeak"]),
        int(request.form["sex"]),
        int(request.form["cp"]),
        int(request.form["fbs"]),
        int(request.form["restecg"]),
        int(request.form["exang"]),
        int(request.form["slope"]),
        int(request.form["ca"]),
        int(request.form["thal"])
    ]

    # Scale & predict
    data_scaled = scaler.transform([data])
    prediction = model.predict(data_scaled)

    result = "Heart Disease Detected 😟" if prediction[0] == 1 else "No Heart Disease 😊"
    return render_template("result.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
    