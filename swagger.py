from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

# **********************
# Define the starting point for the flask app
app = Flask(__name__)
Swagger(app)
pickle_input = open("random_f.pkl", "rb")
classifier = pickle.load(pickle_input)

# homepage
@app.route("/")
def homePage():
    return "Dr.Dre says hell yeah..."


@app.route("/predict")
def predict_forgery():
    """Here, you can predict a single input.
    ---
    parameters:
      - name: var
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: Forgery Status

    """
    var = request.args.get("var")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")
    prediction = classifier.predict([[var, skewness, curtosis, entropy]])
    output_map = {0: "Genuine", 1: "Forged"}
    return f"The banknote is {output_map[prediction[0]]}"


@app.route("/predict_batches", methods=["POST"])
def predict_forgery_batches():
    """Here, you can predict batches.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true

    responses:
        200:
            description: Forgery Status

    """
    df_test = pd.read_csv(request.files.get("file"))
    output_map = {0: "Genuine", 1: "Forged"}
    prediction = classifier.predict(df_test)
    return f"The banknotes are {[output_map[i] for i in prediction]}"


# run the app
if __name__ == "__main__":
    app.run()
