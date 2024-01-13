import os
import sys
from dataclasses import dataclass, field

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split, GridSearchCV

from exception import CustomException
from logger import logging
from utils import save_object

BEST_MODEL_SELECTION_THRESHOLD = 0.6

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")
    preprocessor_file_path = os.path.join("artifacts", "preprocessor.pkl")

class ModelTrainer:
    """Trains a text classification model and saves it to a file.
    """

    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self, X, y):
        try:
            logging.info("Splitting data into training and testing sets")
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Text preprocessing - TF-IDF Vectorization
            logging.info("Vectorizing text data")
            vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
            X_train = vectorizer.fit_transform(X_train)
            X_test = vectorizer.transform(X_test)

            models = {
                "Logistic Regression": LogisticRegression(),
                "Random Forest": RandomForestClassifier(),
                "SVM": SVC(),
                "Naive Bayes": MultinomialNB(),
            }

            params = {
                "Logistic Regression": {
                    'C': [0.1, 1, 10],
                },
                "Random Forest": {
                    'n_estimators': [10, 50, 100],
                },
                "SVM": {
                    'C': [0.1, 1, 10],
                    'kernel': ['linear', 'rbf'],
                },
                "Naive Bayes": {},
            }

            model_report = {}
            for name, model in models.items():
                logging.info(f"Training {name}")
                if name in params:
                    model = GridSearchCV(model, params[name], cv=5, scoring='f1')
                model.fit(X_train, y_train)
                predictions = model.predict(X_test)
                accuracy = accuracy_score(y_test, predictions)
                precision = precision_score(y_test, predictions)
                recall = recall_score(y_test, predictions)
                f1 = f1_score(y_test, predictions)
                model_report[name] = f1
                logging.info(f"Model {name} - Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1 Score: {f1}")

            best_model_score = max(model_report.values())
            best_model_name = max(model_report, key=model_report.get)
            best_model = models[best_model_name]

            # if best_model_score < BEST_MODEL_SELECTION_THRESHOLD:
            #    raise CustomException("No best model found for the given threshold")
            
            logging.info(f"Best model found on train and test dataset: {best_model_name}")

            # Save the best model and the vectorizer
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            save_object(
                file_path=self.model_trainer_config.preprocessor_file_path,
                obj=vectorizer
            )

            logging.info("Model and preprocessor saved to disk successfully")

            return {
                "best_model_name": best_model_name,
                "best_model_score": best_model_score,
                "accuracy": accuracy_score(y_test, best_model.predict(X_test)),
                "precision": precision_score(y_test, best_model.predict(X_test)),
                "recall": recall_score(y_test, best_model.predict(X_test)),
                "f1_score": f1_score(y_test, best_model.predict(X_test))
            }

        except Exception as e:
            raise CustomException(e, sys)