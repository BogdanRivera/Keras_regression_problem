# -*- coding: utf-8 -*-
"""Regression_keras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dRUfHc5scvxYu7S-hQKWgzYzgUfswe5y

# Regression problem with Keras
In this project a dataset from construction is used. The predictors are Cement, Blast Furnace Slag, Fly Ash, Water, Superplasticizer, Coarse Aggregate, Fine Aggregate and Age. The target is predict the Strength of the construction. A Neuronal network created in Keras is used to predict the value.
"""

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DL0101EN/labs/data/concrete_data.csv')
data.head()

print(data.shape)
data.isnull().sum() #View if null data is in the dataset

columns = data.columns
predictors = data[columns[columns!='Strength']] #All columns except Strength
target = data['Strength'] #Only strength values

#Data scaled
predictors_scaled = StandardScaler().fit_transform(predictors)  #Scale of data
predictors_scaled

n_cols = predictors_scaled.shape[1] #Number of columns
n_cols

def regresion_model():
  model = Sequential() #Create Neuronal Network
  model.add(Dense(40,activation='relu', input_shape=(n_cols,))) #Add first hidden layer w
  model.add(Dense(50, activation='relu')) # Add second hidden layer
  model.add(Dense(1)) #Output
  model.compile(optimizer='adam', loss='mean_squared_error') #Compile the Neuronal Network
  return model

model = regresion_model()
model.fit(predictors_scaled,target,validation_split=0.3,epochs = 100,verbose = 2) #Training model

model.predict(predictors_scaled[6:12]) #Some predictions

print(target[6:12])

"""The predict values are so close from the original values"""

