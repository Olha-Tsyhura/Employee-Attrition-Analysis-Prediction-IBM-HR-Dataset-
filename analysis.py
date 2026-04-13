# %%
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('/Users/olga/PycharmProjects/employee-attrition-analysis/Data/Employee-Attrition.csv')
df.head()
df.shape()
df.info()
df.describe()
# %%
df["Attrition"].value_counts()
# %%
sns.countplot(x="Attrition", data=df)
plt.title("Attrition Distribution")
plt.show()
# %% [markdown]
# Fewer employees leave than stay
# %%
sns.countplot(x="OverTime", hue="Attrition", data=df)
plt.title("Overtime Impact on Attrition")
plt.show()
# %% [markdown]
# Employees working overtime are more likely to leave
# %%
sns.boxplot(x="Attrition", y="MonthlyIncome", data=df)
plt.show()
# %% [markdown]
#  Higher income appears to be associated with better employee retention.
# %%
sns.boxplot(x="Attrition", y="Age", data=df)
plt.show()
# %% [markdown]
# Age appears to be negatively correlated with attrition – younger employees show a higher tendency to leave the company
# %%
df_pct = (
    df.groupby("OverTime")["Attrition"]
    .value_counts(normalize=True)
    .rename("percentage")
    .mul(100)
    .reset_index()
)
df_pct.head()
# %%
sns.barplot(
    x="OverTime",
    y="percentage",
    hue="Attrition",
    data=df_pct,
    palette={"Yes": "#EB0600", "No": "#1BF738"}
)

plt.ylabel("Percentage (%)")
plt.title("Overtime vs Attrition (Percentage)")
plt.show()
# %% [markdown]
# 