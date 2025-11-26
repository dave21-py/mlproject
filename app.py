from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import CustomData
from src.pipeline.prediction_pipeline import PredictPipeline
import os


application = Flask(__name__)

app = application


# Route for the home pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods = ['GET','POST'])
def predict_datapoint():
    if request.method == "GET":
        return render_template('home.html')
    else:
        data = CustomData(
            gender = request.form.get('gender'),
            race_ethnicity = request.form.get('ethnicity'),
            parental_level_of_education = request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course = request.form.get('test_preparation_course'),
            reading_score = float(request.form.get('reading_score')),
            writing_score = float(request.form.get('writing_score')),
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)


        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results = results[0]) # This is will be in list format

if __name__ == "__main__":
    # Get the port from the environment variable 'PORT', default to 5002 if not found
    port = int(os.environ.get("PORT", 5002))
    # Run the app. Ideally debug should be False in production.
    app.run(host="0.0.0.0", port=port)