from sklearn import linear_model
import pandas as pd
#This regression is to find the linear relationship between Avg_Rating and Geek_Rating. 
#Games have to obtain more than 29 votes to get a geek rating. So only columns with a valid geek rating will be used for the regression.
dataset = pd.read_csv("dataset_cleaned.csv")

#print(dataset.info())

data_regression = dataset.dropna()

print(data_regression.info())
print(data_regression.head())