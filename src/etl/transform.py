from transformers import pipeline
import pandas as pd
from exception import CustomException
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

HATE_PROB_THRESHOLD = 0.2
class Classifier:
    def __init__(self, model):
        # self.pipeline = pipeline('text-classification', model=model)
        # Load pre-trained model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained("facebook/roberta-hate-speech-dynabench-r4-target")
        self.model = AutoModelForSequenceClassification.from_pretrained(model)
        
    def classify_hate_speech(self, text):
        try:
            # Encode the text using the tokenizer
            inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
            # Get model predictions
            outputs = self.model(**inputs)
            # Convert logits to probabilities
            probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
            # Get the probability of the "toxic" label
            toxic_prob = probs[:, 1].item()

            return 1 if toxic_prob>HATE_PROB_THRESHOLD else 0
        
        except CustomException as e:
            return "error", 0
    
    def label_dataset(self, df):  # Added self as the first parameter
        df['content'] = df['content'].astype(str)
        df['y'] = df['content'].apply(self.classify_hate_speech)

        return df