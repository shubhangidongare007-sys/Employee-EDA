import pandas as pd

df = pd.read_csv("employee.csv")

print("Shape:", df.shape)

print("\nInformation:")
df.info()

print("\nStatistical Summary:")
print(df.describe())