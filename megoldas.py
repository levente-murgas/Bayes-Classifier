import pandas as pd
import numpy as np
from pathlib import Path
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import HungarianStemmer
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes
import csv

np.random.seed(100)

# Read dataset
Corpus = pd.read_csv(r"C:\Users\Murgi\Documents\GitHub\MIverseny\adat.csv", encoding='utf-8')

#----------------DATA PREPROCESSING------------#
Corpus['szoveg'].dropna(inplace=True)

def text_preprocessing(text):
    text = text.lower()

    text_words_list = word_tokenize(text)

    stemmer = HungarianStemmer()
    res_list = []
    for word in text_words_list:
        stem = stemmer.stem(word)
        res_list.append(stem)

    return str(res_list)


Corpus['szoveg_vegleges'] = Corpus['szoveg'].map(text_preprocessing)
#--------------------------------------------#


# Splitting the model into testing/training sets in 30%-70% ratio
Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(Corpus['szoveg_vegleges'], Corpus['label'],
                                                                    test_size=0.3)

Encoder = LabelEncoder()
Encoder.fit(Train_Y)
Train_Y = Encoder.transform(Train_Y)
Test_Y = Encoder.transform(Test_Y)

#TF-IDF algorithm for determining how important a feature is in the given context vs in the whole corpus
Tfidf_vect = TfidfVectorizer(max_features=5000)
Tfidf_vect.fit(Corpus['szoveg_vegleges'])

Train_X_Tfidf = Tfidf_vect.transform(Train_X)
Test_X_Tfidf = Tfidf_vect.transform(Test_X)


# using Naive Bayes classifier for classification
Naive = naive_bayes.MultinomialNB()
Naive.fit(Train_X_Tfidf, Train_Y)

# predict the labels on validation dataset
predictions = Naive.predict(Test_X_Tfidf)

# inference test data
p = Path(__file__).with_name('test.csv')
test_set = pd.read_csv(p, encoding='utf-8')

test_set['szoveg_vegleges'] = test_set['szoveg'].map(text_preprocessing)
test_set_processed_vectorized = Tfidf_vect.transform(test_set['szoveg_vegleges'])
test_predictions = Naive.predict_proba(test_set_processed_vectorized)

results = []
for count, record in enumerate(test_set['szoveg']):
    results.append([test_predictions[count][0],record])

# write results to output file prediction.csv
with open('prediction.csv', 'w', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(results)