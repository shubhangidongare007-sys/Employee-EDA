import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("employee.csv")

plt.figure(figsize=(8,5))
sns.boxplot(x="Department",y="Salary",data=df)
plt.title("Department vs Salary")
plt.show()

plt.figure(figsize=(6,5))
sns.boxplot(x="Gender",y="Salary",data=df)
plt.title("Gender vs Salary")
plt.show()