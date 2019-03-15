#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:03:54 2019

@author: abhijithneilabraham
"""

from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
seed = 2
numpy.random.seed(seed)
# load pima indians dataset
#dataset = numpy.loadtxt("choleraprediction.csv", delimiter=",")
dataset = numpy.loadtxt("dataset2.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]
print(Y)
# create model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=150, batch_size=10,  verbose=2)
# calculate predictions
 #diarrhea and vomiting=1
 #presence of fever above 100 degree Fahrenheit
 #Dehydration
 #nausea
 #loss of appetite
 #heart beat rate
 #shriveled skin 
print(X[-1])


predictions = model.predict(X)
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
# round predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)