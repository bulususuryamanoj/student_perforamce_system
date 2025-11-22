import numpy 
import pickle
from flask import Flask,render_template,request
app=Flask(__name__)
app.name = "Student Performamce System"
dcmodel = r"d:\python\Student_performance\dcmodel"
with open("dcmodel",'rb') as f:
    model = pickle.load(f)
@app.route("/")
def home():
    return render_template('index.html')
@app.route('/predict',methods = ['POST'])
def predict():
    