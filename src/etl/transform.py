from transformers import pipeline
import pandas as pd
from exception import CustomException
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class Classifier:
    def __init__(self, model):
        self.pipeline = pipeline('text-classification', model=model)

    def predict_hate_label(self, text):
        try:
            prediction = self.pipeline(text)[0]  # Use self.pipeline
            label = 1 if prediction['label'] == 'hate' else 0
            score = prediction['score']
            return label
        except CustomException as e:
            return "error", 0  # Consider handling this differently
    
    def label_dataset(self, df):  # Added self as the first parameter
        df['y'] = df['content'].apply(self.predict_hate_label)  # Use self.predict_hate_label
        return df