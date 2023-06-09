# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/146dtK2_vF0dDZwVypwuw-w563gyhwE1Y
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('Housing.csv')

#univariate analysis
plt.hist(data['price'], bins=100)  
plt.xlabel('Variable')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

#bivariate analysis
x = data['price']
y = data['area']
plt.scatter(x, y)
plt.xlabel('X Variable')
plt.ylabel('Y Variable')
plt.title('Scatter Plot')
plt.show()

#multivariate
sns.pairplot(data)
plt.title('Pair Plot')
plt.show()

import pandas as pd

data = pd.read_csv('Housing.csv')

statistics = data.describe()

print(statistics)

import pandas as pd

data = pd.read_csv('Housing.csv')

missing_values = data.isnull().sum()

columns_with_missing_values = missing_values[missing_values > 0]

data = data.dropna()

data_filled = data.fillna(4)

data_interpolated = data.interpolate()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Housing.csv')

columns_to_check = ['area', 'bedrooms', 'bathrooms']

z_scores = np.abs((data[columns_to_check] - data[columns_to_check].mean()) / data[columns_to_check].std())

threshold = 3

outliers = (z_scores > threshold).any(axis=1)

data_no_outliers = data[~outliers]

replacement_value = 4
data_corrected = data.copy()
data_corrected.loc[outliers, columns_to_check] = replacement_value

import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('Housing.csv')

categorical_columns = data.select_dtypes(include=['object', 'category']).columns

label_encoder = LabelEncoder()

for column in categorical_columns:
    data[column] = label_encoder.fit_transform(data[column].astype(str))

import pandas as pd

data = pd.read_csv('Housing.csv')

y = data['price']

X = data[['area', 'bedrooms', 'bathrooms']]

import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('Housing.csv')

X = data[['area', 'bedrooms', 'bathrooms']]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('Housing.csv')

y = data['price']

X = data[['area', 'bedrooms', 'bathrooms']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#build the model
data = pd.read_csv('Housing.csv')

y = data['price']

X = data[['area', 'bedrooms', 'bathrooms']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()  
model.fit(X_train, y_train)

y_pred = model.predict(X_test) 
mse = mean_squared_error(y_test, y_pred)

from sklearn.linear_model import LinearRegression
#Train the model
model = LinearRegression()

model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)

from sklearn.metrics import mean_squared_error
#Test the model
y_test_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_test_pred)

print('Mean Squared Error:', mse)

from sklearn.metrics import mean_squared_error, r2_score

y_test_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_test_pred)
r2 = r2_score(y_test, y_test_pred)

print('Mean Squared Error:', mse)
print('R-squared:', r2)