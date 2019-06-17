from sklearn import datasets
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.base import clone

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

diabetes = datasets.load_breast_cancer()
examples, diabetes_risks = diabetes['data'], diabetes['target']
print(f"{len(examples)} examples in the dataset")

print(f"examples shape:{examples.shape}")
print(f"no. of examples:{examples.shape[0]}")
print(f"feature per example:{examples.shape[1]}")