import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

df= pd.read_csv("titanic.csv")

print("First 5 rows")
print(df.head())

print("dataset info")
print(df.info())

print(df.isnull().sum())
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

df.drop('Cabin', axis=1, inplace=True)
print(df.isnull().sum())

le=LabelEncoder()
df['Sex']=le.fit_transform(df['Sex'])
df['Embarked']=le.fit_transform(df['Embarked'])

scaler=StandardScaler()
df[['Age','Fare']]=scaler.fit_transform(df[['Age','Fare']])

plt.figure(figsize=(8,5))
sns.boxplot(x=df['Fare'])
plt.title("Fare Outliers")
plt.show()

Q1=df['Fare'].quantile(0.25)
Q3=df['Fare'].quantile(0.75)

IQR=Q3-Q1
df=df[(df['Fare']>=Q1-1.5*IQR) & (df['Fare']<=Q3+1.5*IQR)]

print("Final Dataset", df.shape)

df.to_csv("cleanedtitanic.csv", index=False)
print("File saved successfully")