from flask import Flask, request,jsonify
import pickle
import numpy as np

app=Flask(__name__)
# CORS(app)
@app.route("/")
def home():
    return jsonify({"key":"This is flask api"})

@app.route("/predict",methods=['POST'])
def predict():
        try:
            
            data=request.get_json()  # to get the data inform of json
   
#    to get the data in form of form-data
            # Company=request.form.get("Company")
            # TypeName=request.form.get("TypeName")	
            # Inches=request.form.get("Inches")
            # Ram =request.form.get("Ram")	
            # Weight=request.form.get("Weight")
            # Touchscreen=request.form.get("Touchscreen")
            # ips=request.form.get("ips")
            # X_res=request.form.get("X_res")	
            # Y_res=request.form.get("Y_res")	
            # Cpu_brand=request.form.get("Cpu")	
            # HDD=request.form.get("HDD")
            # SSD=request.form.get("SSD")
            # Gpu_Brand=request.form.get("Gpu_Brand")	
            # Os=request.form.get("Os")

            # input_query=np.array([[Company,TypeName,Inches,
            #                Ram,Weight,Touchscreen,
            #                ips,X_res,Y_res,Cpu_brand,
            #                HDD,SSD,Gpu_Brand,Os]])
            input_query=np.array([[data['Company'],data['TypeName'],
                           float( data['Inches']),data['Ram'] ,float(data['Weight']),
                            int(data['Touchscreen']),int(data['ips']),int(data['X_res']),
                            int(data['Y_res']),data['Cpu_brand'],int(data['HDD']),
                            int(data['SSD']),data['Gpu_Brand'],data['Os']
                             ]])
            model=pickle.load(open("pipeline.pkl","rb"))
        except Exception as e:
           print(e)
        return jsonify({"price": np.exp((model.predict(input_query)[0]))})  
    #   return jsonify(data)

if __name__=='__main__':
     app.run(debug=True)