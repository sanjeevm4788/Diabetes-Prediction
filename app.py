import numpy as np
import pickle
from flask import Flask, request, render_template

# Load ML model
model = pickle.load(open('model/diabetes.pkl', 'rb')) 

# Create application
app = Flask(__name__)

# home function
@app.route('/')
def home():
    return render_template('diabetes.html')

# predict function 
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Predict output
    output = model.predict([features])[0]
    
    # Check the output values and retrive the result 
    if output == 1:
        return render_template('diabetes.html', 
                               result = 'You may have diabetes, Consult a Doctor!!!!!')
    else:
        return render_template('diabetes.html', 
                               result = 'You are not likely to have diabetes!')

if __name__ == '__main__':
#Run the application
    app.run(host='0.0.0.0', port=port, debug=True)
