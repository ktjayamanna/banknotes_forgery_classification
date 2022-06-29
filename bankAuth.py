#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 10:22:03 2022

@author: kjayamanna
"""

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle
#%%
df = pd.read_csv('/home/kjayamanna/Documents/MLProjects/BankAuth/BankNote_Authentication.csv')
#%% Seperate dependent vs independent variables
x = df.iloc[:, :-1]
y = df.iloc[:, -1]
#%% Split into train/test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)
#%% Fit into random forest
classifier = RandomForestClassifier()
classifier.fit(x_train, y_train)
#%% Make predictions
y_pred = classifier.predict(x_test)
acc = accuracy_score(y_test, y_pred)
con_mat = confusion_matrix(y_test, y_pred)
#%% serialize the classifier
pickle_output = open('random_f.pkl', 'wb')
pickle.dump(classifier, pickle_output)
pickle_output.close()

