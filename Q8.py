import pandas as pd

df = pd.read_csv("employee.csv")

print("Average Salary:",df["Salary"].mean())
print("Maximum Salary:",df["Salary"].max())
print("Minimum Salary:",df["Salary"].min())

print("\nDepartment Wise Average Salary")
print(df.groupby("Department")["Salary"].mean())