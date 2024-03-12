from flask import Flask, request,jsonify
import pickle
import numpy as np
model=pickle.load(open("pipeline.pkl","rb"))
app=Flask(__name__)

@app.route("/")
def home():
    return "This is flask api"

@app.route("/predict",methods=['POST'])
def predict():
    Company=request.form.get("Company")
    TypeName=request.form.get("TypeName")	
    Inches=	request.form.get("Inches")
    Ram =request.form.get("Ram")	
    Weight	=request.form.get("Weight")
    Touchscreen	=request.form.get("Touchscreen")
    ips	=request.form.get("ips")
    X_res=request.form.get("X_res")	
    Y_res=request.form.get("Y_res")	
    Cpu_brand=request.form.get("Cpu")	
    HDD	=request.form.get("HDD")
    SSD	=request.form.get("SSD")
    Gpu_Brand=request.form.get("Gpu_Brand")	
    Os=request.form.get("Os")
    input_query=np.array([[Company,TypeName,Inches,Ram,Weight,Touchscreen,ips,X_res,Y_res,Cpu_brand,HDD,SSD,Gpu_Brand,Os]])
    price=np.exp((model.predict(input_query)[0]))
    return jsonify({"price":price})

