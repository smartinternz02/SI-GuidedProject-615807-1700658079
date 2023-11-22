# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:17:44 2023

@author: Tanmay sharma
"""

from flask import Flask, render_template, request 
from keras.models import load_model
from keras.preprocessing import image 
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
import numpy as np

app=Flask(__name__)

model = load_model('') #so this is where i will load the  model

model.make_predict_function()

def predict_label(img_path):
    img = load_img(img_path)
    img = img.resize((351,351))
    x = img_to_array(img)
    x = np.expand_dims(x,axis=0)
    a = np.argmax(model.predict(x),axis=1)
    class_names = [
        'Clams',
        'Corals',
        'Crabs',
        'Dolphin',
        'Eel',
        'Fish',
        'Jelly Fish',
        'Lobster',
        'Nudibranchs',
        'Octopus',
        'Otter',
        'Penguin',
        'Puffers',
        'Sea Rays',
        'Sea Urchins',
        'Seahorse',
        'Seal',
        'Sharks',
        'Shrimp',
        'Squid',
        'Starfish',
        'Turtle_Tortoise',
        'Whale',
    ]

    y_pred = model.predict(x)
    class_idx = np.argmax(y_pred,axis=1)[0]
    class_name = class_names[class_idx] #error
    return class_name

#routes 
@app.route("/",methods=['GET', 'POST'])
def main():
    return render_template("index.html")

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    return render_template("predict1.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
    if requests.method == 'POST':
        img = request.files['my_image']
        img_path = "static/" + img.filename
        img.save(img_path)
        p = predict_label(img_path)

    return render_template("predict.html",prediction = p,img_path = img_path)

if __name__ =='__main__':
    app.run(debug = True)