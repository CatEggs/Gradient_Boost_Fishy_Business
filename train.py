import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump
from preprocess import prep_data

df = pd.read_csv("fish_participant.csv")

X, y = prep_data(df)

lr = LinearRegression()
lr.fit(X, y)

dump(lr, "reg.joblib")