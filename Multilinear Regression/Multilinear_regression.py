# Multiple linear regression

# Importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing Datasets 

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values 
y = dataset.iloc[:, 4].values

# Encoding categorical data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelEncoder_X = LabelEncoder()
X[:, -1] = labelEncoder_X.fit_transform(X[:, -1]) 

oneHotEncoder = OneHotEncoder(categorical_features = [-1])
X = oneHotEncoder.fit_transform(X).toarray()

# Avoiding the dummy variable trap

X = X[:, 1:]

# Splitting the dataset into training and test

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the training set

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict the test results

y_pred = regressor.predict(X_test)

# Building the optimal model using Backward Elimination

import statsmodels.formula.api as sm

X = np.append(np.ones((50,1)).astype(int), X, axis = 1)

X_opt = X[:, [0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 1, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 3, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 3]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()



