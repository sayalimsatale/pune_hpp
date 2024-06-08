from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

# Load the trained model (assuming the model is saved as 'model.pkl')
with open('lr_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data
    age = int(request.form['age'])
    sex = request.form['sex']
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = request.form['smoker']
    region = request.form['region']
    
    # Convert categorical data to numerical (using predefined values from your model training)
    sex = 1 if sex == 'male' else 0
    smoker = 1 if smoker == 'yes' else 0
    region_dict = {'northeast': 3, 'northwest': 4, 'southeast': 1, 'southwest': 2}
    region = region_dict.get(region.lower(), -1)
    
    # Make prediction
    features = np.array([[age, sex, bmi, children, smoker, region]])
    prediction = model.predict(features)[0]

    return render_template('index.html', prediction_text=f'Predicted Charges: ${prediction:.2f}')

if __name__ == '__main__':
    app.run(debug=False,port=8080,host='0.0.0.0')