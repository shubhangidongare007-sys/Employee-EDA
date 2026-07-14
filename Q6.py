import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("employee.csv")

columns = ["Gender","Department","City"]

for col in columns:
    plt.figure(figsize=(6,4))
    sns.countplot(x=col,data=df)
    plt.title(col)
    plt.show()