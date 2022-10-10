# Sentiment-Analysis-of-Reviews
Visualisation of a sentiment classifier trained on parsed reviews

This is an application demonstrating the work of a review classifier. The classifier is based on TF-IDF model and is fitted on reviews obtained by parsing of the areviews.ru site. 

1) The Parsing, training and pickling of a classifier.ipynb file contains a parser as well as the classifier training. The fitting of its optimal parameters is provided as well. Pickling of the classifier for the further usage is done in the very end of the iPython Notebook (the file sentiment_classifier.pkl is thus created).

2) The sentiment_classifier.py contains a class with the pickled classifier. It is necessary for the work of a Flask application which is a user interface for sentiment analysis of reviews.

3) The file Sentiment_Analysis_Interface.ipynb contains an iPython Notebook for a Flask App. 

4) The file index.html contains the form which will be rendered with the Flask App. THE FILE SHOULD BE PLACED IN THE templates/ folder!
