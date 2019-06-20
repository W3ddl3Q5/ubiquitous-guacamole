import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from urllib.request import URLopener
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


sns.set()
sns.set_style("whitegrid")

#Load data in to a variable
diamonds = pd.read_csv("diamonds.csv")
y = diamonds['price'] #target columm
x = diamonds.iloc[:,1:11] #independent features

# find names of categorical features
categoricals = [ feat for feat in diamonds.columns  if str(diamonds[feat].dtype) == "cut"]
# tell pandas which features are categoical
for feature in categoricals:
    diamonds[feature] =  diamonds[feature].astype("category")
        
# create a copy of the dataframe to write preprocessed features into
pp_credit_df = diamonds.copy()

for feature in categoricals:
    pp_credit_df[feature] = pp_credit_df[feature].cat.codes
    
categoricals = [ feat for feat in diamonds.columns  if str(diamonds[feat].dtype) == "price"]
pp_credit_df = pd.get_dummies(data=pp_credit_df, columns=categoricals)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, shuffle=True) # 70% training and 30% test
clf=RandomForestClassifier(n_estimators=100)
#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)


# prediction on test set
y_pred=clf.predict(X_test)
print("Accuracy:", diamonds.accuracy_score(y_test, y_pred))
