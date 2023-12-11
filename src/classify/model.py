from transformers import pipeline

class Classifier:
    def __init__(self, model):
        self.pipeline = pipeline('text-classification', model=model)


    def predict_hate_label(text):
        try:
            prediction = pipeline(text)[0]
            label = 1 if prediction['label'] == 'hate' else 0
            score = prediction['score']
            return label, score
        except Exception as e:
            return "error", 0


