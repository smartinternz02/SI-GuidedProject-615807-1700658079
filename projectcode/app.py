
"""
Created on Tue Nov 21 16:17:44 2023

@author: Tanmay sharma
"""

from flask import Flask, render_template, request 
from keras.models import load_model
from keras.preprocessing import image 
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import numpy as np

app=Flask(__name__)

model = load_model('seaanimal3.h5') #so this is where i will load the  model

model.make_predict_function()

def predict_label(img_path):
    img = load_img(img_path)
    img = img.resize((351,351))
    x = img_to_array(img)
    x = np.expand_dims(x,axis=0)
    #a = np.argmax(model.predict(x),axis=1)
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
    class_name = class_names[class_idx]
    return class_name


#routes 
@app.route("/",methods=['GET', 'POST'])
def main():
    return render_template("home.html")

@app.route("/intro",methods=['GET', 'POST'])
def intro():
    return render_template("intro.html")

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    return render_template("predict.html")



@app.route("/upload", methods = ['GET', 'POST'])
def get_output():
    
    if request.method == 'POST' and 'my_image' in request.files:
        img = request.files['my_image']

        if img.filename != '':
            img_path = "uploads/" + img.filename
            img.save(img_path)

            try:
                prediction = predict_label(img_path)
                return render_template("predict.html", prediction=prediction, img_path=img_path)
            except Exception as e:
                return f"Error: {str(e)}"


    return "No image selected for prediction."

    


if __name__ =='__main__':
    app.run(debug = True)



