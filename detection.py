import numpy as np 
import pandas as pd
from flask import Flask,request,render_template,Response
import joblib


model=joblib.load(r"detection_model")
app= Flask(__name__)

@app.route("/")
def index():
    return (render_template('index.html'))

@app.route("/predict",methods=["POST","GET"])

def predict():
    Product=(request.form["Product"])
    category=(request.form["category"])
    Price=int(request.form["Price"])
    seller_rating=float(request.form["seller_rating"])
    product_rating=float(request.form["product_rating"])
    is_verified_seller=str(request.form["is_verified_seller"])
    
    if category=="Footwear":
        category=0
    elif category=="Clothing":
        category=1
    elif category=="Electronics":
        category=2
    elif category=="Home":
        category=3
    elif category=="Watches":
        category=4
        
    if is_verified_seller=="Yes":
        is_verified_seller=0
    elif is_verified_seller=="No":
        is_verified_seller=1
        
    
    
    
    data=pd.DataFrame({"category":category,
                       "price":Price,
                       "seller_rating":seller_rating,
                       "product_rating":product_rating,
                       "is_verified_seller":is_verified_seller},index=[0])
    prediction=model.predict(data)
    if prediction==int(0):
        prediction="Fake"
    if prediction==int(1):
        prediction="Genuine"
        
    return render_template('index.html',prediction=f"Your {Product} Is {prediction}")
        
    
    
    
    
if __name__=="__main__":
    app.run(debug=True)
