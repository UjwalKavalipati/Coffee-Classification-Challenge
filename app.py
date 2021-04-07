from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import pandas as pd
import xgboost as xgb
import sklearn

app = Flask(__name__)
model = pickle.load(open('xg_boost_classification_model.pkl', 'rb'))
names=model.feature_names
ddf = pd.DataFrame(columns=names)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    Total_Cup_Points=0
    if request.method == 'POST':
        Sweetness = float(request.form['Sweetness'])
        Balance = float(request.form['Balance'])
        Body = float(request.form['Body'])
        Acidity = float(request.form['Acidity'])
        Aftertaste = float(request.form['Aftertaste'])
        Flavor = float(request.form['Flavor'])
        Uniformity = float(request.form['Uniformity'])
        CupperPoints = float(request.form['CupperPoints'])
        Aroma = float(request.form['Aroma'])
        CleanCup = float(request.form['CleanCup'])
        CatOne = int(request.form['CatOne'])
        CatTwo = int(request.form['CatTwo'])
        Moisture = float(request.form['Moisture'])
        Total_Cup_Points=Sweetness+Balance+Body+Acidity+Aftertaste+Flavor+Uniformity+CupperPoints+Aroma+CleanCup
        ddf.loc[0]=[Sweetness,Total_Cup_Points,Balance,CatOne,Body,Acidity,Aftertaste,Flavor,Uniformity,CupperPoints,Aroma,CleanCup,CatTwo,Moisture]
        dtest=xgb.DMatrix(ddf)
        prediction=model.predict(dtest)
        output=np.argmax(prediction)
        if output==0:
            return render_template('index.html',prediction_text="The predicted coffee type is Robusta")
        else:
            return render_template('index.html',prediction_text="The predicted coffee type is Arabica")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

