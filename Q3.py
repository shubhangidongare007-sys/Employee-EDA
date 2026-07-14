import pandas as pd

df = pd.read_csv("employee.csv")

print("Missing Values:")
print(df.isnull().sum())