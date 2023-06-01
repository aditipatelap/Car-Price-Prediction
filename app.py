from flask import Flask, render_template, request
import joblib

import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model
model = joblib.load(open('model.joblib', 'rb'))

@app.route('/',methods=['GET'])

def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])

def predict():
    # Get user inputs from the form
    fueltype = request.form['fueltype']
    if(fueltype == "gas"):
        fueltype = 1
    else:
        fueltype = 0 # Diesel

    aspiration = request.form['aspiration']
    if(aspiration == "std"):
        aspiration = 0
    else:
        aspiration = 1 # Turbo

    doornumber = request.form['doornumber']
    if(doornumber == "two"):
        doornumber = 1
    elif(doornumber == "four"):
        doornumber = 0

    carbody = request.form['carbody']
    if(carbody == "convertible"):
        carbody = 0
    elif(carbody == "hardtop"):
        carbody = 1
    elif(carbody == "hatchback"):
        carbody = 2
    elif(carbody == "sedan"):
        carbody = 3
    elif(carbody == "wagon"):
        carbody = 4

    drivewheel = request.form['drivewheel']
    if(drivewheel == "4wd"):
        drivewheel = 0
    elif(drivewheel == "fwd"):
        drivewheel = 1
    elif(drivewheel == "rwd"):
        drivewheel = 2

    enginelocation = request.form['enginelocation']
    if(enginelocation == "front"):
        enginelocation = 0
    else:
        enginelocation = 1
    
    wheelbase = float(request.form['wheelbase'])
    
    carlength = float(request.form['carlength'])
    carwidth = float(request.form['carwidth'])
    carheight = float(request.form['carheight'])
    curbweight = float(request.form['curbweight'])

    cylindernumber = request.form['cylindernumber']
    if(cylindernumber == "two"):
        cylindernumber = 6
    elif(cylindernumber == "three"):
        cylindernumber = 4
    elif(cylindernumber == "four"):
        cylindernumber = 2
    elif(cylindernumber == "five"):
        cylindernumber = 1
    elif(cylindernumber == "fix"):
        cylindernumber = 3
    elif(cylindernumber == "eight"):
        cylindernumber = 0
    elif(cylindernumber == "twelve"):
        cylindernumber = 5
        
    enginesize = float(request.form['enginesize'])
    boreratio = float(request.form['boreratio'])
    stroke = float(request.form['stroke'])
    compressionratio = float(request.form['compressionratio'])
    horsepower = float(request.form['horsepower'])
    peakrpm = float(request.form['peakrpm'])
    citympg = float(request.form['citympg'])
    highwaympg = float(request.form['highwaympg'])

    # Make the prediction using the loaded model
    features = [[fueltype, aspiration, doornumber, carbody, drivewheel,
       enginelocation, wheelbase, carlength, carwidth, carheight,
       curbweight, cylindernumber, enginesize, boreratio, stroke,
       compressionratio, horsepower, peakrpm, citympg, highwaympg]]
    
    estimated_price = model.predict(features)

    # Render the results template with the estimated price
    return render_template('index.html', price=estimated_price[0])
    
if __name__=="__main__":
    app.run(debug=True)
