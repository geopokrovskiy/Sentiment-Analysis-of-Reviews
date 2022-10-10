import joblib

class SentimentClassifier(object):
    def __init__(self):
        self.model = joblib.load('sentiment_classifier.pkl')
        self.classes_dict = {0: 'Negative review', 1: 'Positive review', -1: 'Prediction error'}
        
    def predict_text(self, text):
        try:
            lst = []
            lst.append(text)
            return self.model.predict(lst)[0]
        except:
            print("Prediction error")
            return -1
        
    def get_prediction_message(self, text):
        prediction = self.predict_text(text)
        return self.classes_dict[prediction]