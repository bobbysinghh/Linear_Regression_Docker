import pandas as pd
dataset = pd.read_csv("Dataset.csv")
x=dataset["YearsExperience"].values.reshape(-1,1)
y=dataset["Salary"].values.reshape(-1,1)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x,y)
model.coef_
model.predict([[2]])
import joblib
joblib.dump(model,"model.pk1")
