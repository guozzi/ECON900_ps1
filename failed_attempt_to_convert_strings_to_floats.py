import pandas as pd
import numpy as np
from sklearn import linear_model

dataset = pd.read_csv("boardgamegeek_dataset.csv",header=0)

print(dataset.head()) # Results show that parsed data are strings not floats

#Now convert strings to floats, the data used in this regression is Votes, Geek_Rating and Avg_Rating

try:
    dataset['Votes'] = dataset.Votes.astype(float)
except ValueError:
	dataset['Votes'] = 0
try:
    dataset['Geek_Rating'] = dataset.Geek_Rating.astype(float)
except ValueError:
	dataset['Geek_Rating'] = 0
try:
    dataset['Avg_Rating'] = dataset.Avg_Rating.astype(float)
except ValueError:
	dataset['Avg_Rating'] = 0


print(dataset.info())

#After many failed trails, I decided to use excel to clean the data.