import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

df= pd.read_csv("titanic.csv")
print("First 5 rows")
print(df.head())
print("Info")
print(df.info())
print("Describe")
print(df.describe())
print("IS a null")
print(df.isnull().sum())

df['Age']=df['Age'].fillna(df['Age'].median())
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])
df.drop('Cabin', axis=1, inplace=True )

print(df.isnull().sum())

plt.figure()
plt.hist(df['Age'], bins=30)
plt.title("Age Histogram")
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

plt.figure()
plt.title("Fare")
plt.hist(df['Fare'], bins=30)
plt.xlabel("Fare")
plt.ylabel("Count")
plt.show()


plt.figure()
sns.boxplot(x='Survived', y='Fare', data=df)
plt.title("Fare Boxplot")
plt.show()

plt.figure()
sns.boxplot(x='Survived', y='Age', data=df)
plt.title("Age Boxplot")
plt.show()

plt.figure()
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Sex vs Survived")
plt.show()

plt.figure()
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Pclass vs Survived")
plt.show()

le=LabelEncoder()
df['Sex']=le.fit_transform(df['Sex'])
df['Embarked']=le.fit_transform(df['Embarked'])

corr = df.select_dtypes(include=['int64','float64']).corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()


sns.pairplot(df[['Survived','Age','Fare','Pclass']])
plt.show()
