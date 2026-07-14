import pandas as pd

df = pd.read_csv("employee.csv")

numerical = df.select_dtypes(include=['int64','float64']).columns
categorical = df.select_dtypes(include=['object']).columns

print("Numerical Columns:")
print(numerical)

print("\nCategorical Columns:")
print(categorical)