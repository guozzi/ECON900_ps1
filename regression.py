from sklearn import linear_model
import numpy as np
import pandas as pd
#This regression is to find the linear relationship between Avg_Rating and Geek_Rating. 

dataset = pd.read_csv("dataset_cleaned.csv")

#print(dataset.info())
#Games have to obtain more than 29 votes to get a geek rating. So only columns with a valid geek rating will be used for the regression.

data_regression = dataset.dropna()

print(data_regression.info())
print(data_regression.head())

target = data_regression.iloc[:,1].values
print(target)

data = data_regression.iloc[:,2:3].values

print(data)

regression = linear_model.LinearRegression()

regression.fit(data, target)
#Selected 4 Geek rating levels corresponding to top 100, top 50, top 25 and top 10 ratings
X = [
	[7.447],
	[7.651],
	[7.889],
	[8.072]
]

results = regression.predict(X)

print(results)
