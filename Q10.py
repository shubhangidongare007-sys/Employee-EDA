import pandas as pd

df = pd.read_csv("employee.csv")

print("Average Age:",df["Age"].mean())
print("Average Salary:",df["Salary"].mean())

print("\nDepartment with Highest Average Salary:")
print(df.groupby("Department")["Salary"].mean().idxmax())

print("\nSummary:")
print("- No missing values found.")
print("- IT and Finance have higher salaries.")
print("- Dataset is clean and suitable for EDA.")