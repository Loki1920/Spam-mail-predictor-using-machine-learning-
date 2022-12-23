# -*- coding: utf-8 -*-
"""spam_mail_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nDOnkYv9yqp4nYjVAKUSjVFsmgUUN1Rf
"""

import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score 
from sklearn.linear_model import LogisticRegression

"""Data collection and Pre-Processing"""

# loading data from csv file to pandas dataframe 
raw_mail_data = pd.read_csv('/content/mail_data.csv')



print(raw_mail_data)

#replace the null value with null string 
mail_data = raw_mail_data.where(pd.notnull(raw_mail_data),'')

#printing first five rows of data frame 
print(mail_data.head())

mail_data.shape

"""Label Encoding"""

#Label spam mail as 0 and ham mail as 1
mail_data.loc[mail_data['Category']=='spam','Category',]=0
mail_data.loc[mail_data['Category']=='ham','Category',] = 1

#seperating the data as texts and label 
X = mail_data['Message']
Y = mail_data['Category']

print(X)
print(Y)

"""splitting the data into training data and testing data"""

X_train , X_test , Y_train ,Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 3)

print(X.shape)
print(X_train.shape)
print(X_test.shape)



"""Feature Extraction"""

# transform the text data to feature vectors that can be used as input to the Logistic regression 
feature_extraction = TfidfVectorizer(min_df = 1,stop_words = 'english',lowercase = 'True')

X_train_features =  feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

#convrt Y_train and Y_test as integer 
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

print(X_train)

print(X_train_features)

"""Training a model 

Logistic Regression 

"""

model = LogisticRegression()

#training a logistic model with training dataset 

model.fit(X_train_features,Y_train)

"""Evaluating the trained model """

#prediction on training data 
prediction_on_training_data = model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train,prediction_on_training_data)

print('accuracy_on_training_data:',accuracy_on_training_data)

"""Accuracy on testing data

"""

prediction_on_test_data = model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test,prediction_on_test_data)

print("accuracy_on_test_data:",accuracy_on_test_data)

"""Building predictive system 

"""

input_mail = ["I've been searching for the right words to thank you for this breather. I promise i wont take your help for granted and will fulfil my promise. You have been wonderful and a blessing at all times"]
# convert text to feature vector 
input_data_features = feature_extraction.transform(input_mail)

#prediction
prediction = model.predict(input_data_features)
print(prediction)


if prediction[0]==1:
  print("Ham mail")
else:
  print("spam mail")