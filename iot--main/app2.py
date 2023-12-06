import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__,template_folder="templates")
model = pickle.load(open('jio.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    gas_level = float(request.form['gas_level'])
    water_level = float(request.form['water_level'])
    sensor_data = np.array([[temperature, humidity, gas_level, water_level]])
    prediction = model.predict(sensor_data)
     
    if(prediction==1):
        prediction = 'UnSafe!!!'
    else:
        prediction = 'Safe!!!'
    return render_template('out.html', output=prediction)

if __name__ == "__main__":
    app.run(debug=True)