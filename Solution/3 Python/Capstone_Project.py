import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('marketing_campaign.csv')
# print(df)

# Exploratory Data Analysis

# Task 1: General Data Overview:
# a. Check the first few rows of the dataset to understand its structure
# b. Check the data types of each column
# c. Check for any missing values in the dataset

# a.
print("First few rows : \n")
print(df.head())
# b.
print("\n\nColumns : \n")
print(df.columns)

print("\n\nDescription : \n")
print(df.describe())

# c.
print("\n\nMissing Values : \n")
print(df.isna().sum())

# Filling null values
median_income = df['Income'].median()
print('\n\nMedian Income : ' ,median_income,'\n\n')

# Old version statement
# df['Income'].fillna(median_income, inplace=True)
# --------- OR ------------
df.fillna({'Income':median_income}, inplace=True)

print(df.isna().sum())

print('\n\n')
print(df)
df.to_csv('marketing_campaign_output.csv')






# Task 2: Descriptive Statistics:
# a. Compute summary statistics for numerical columns (mean, median, min, max, and standard deviation)
# b. Explore the distribution of numerical variables using histograms or box plots

# a.
summary_stats = df.describe()
print('\n\nSummary statistics of numeric cols : \n',summary_stats)

# b.
# Define numeric columns
num_cols = df.select_dtypes(include=[np.number]).columns
print('\n\nNumeric columns : \n',num_cols)
print('\n\nNumber of numeric columns : \n',len(num_cols))



# Histogram for Numeric Columns :
for col in num_cols:
    plt.figure(figsize = (8,6))
    sns.histplot(df[col], kde = True, color = 'skyblue')
    plt.title(f'Histogram Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()


# Box for Numeric Values :
for col in num_cols:
    plt.figure(figsize = (8,6))
    sns.boxplot(df[col], color = 'lightgreen')
    plt.title(f'Boxplot of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()







# Task 3: Univariate Analysis:
# a. Explore the distribution of each numerical variable using histograms or kernel density plots
# b. Explore the distribution of each categorical variable using bar plots or pie charts
# c. Identify outliers in numerical variables using box plots or scatter plots

# a.
# Univariable Analysis
# Numeric Variable

num_cols1 = df.select_dtypes(include = np.number).columns
for cols in num_cols1:
    sns.histplot(df[cols], kde= True)   # Kde is kernel density that provides soft edges
    plt.title(cols)
    plt.show()


# b.
# Category Variable

cat_col = df.select_dtypes(exclude = np.number).columns
for col in cat_col:
    sns.countplot(data = df,x=col)
    plt.title(col)
    plt.xticks(rotation = 45)
    plt.show()






# Task 4: Bivariate Analysis:
# a. Explore the relationship between numerical variables and the target variable (Response) using scatter plots or correlation matrices
# b. Explore the relationship between categorical variables and the target variable using bar plots or chi-square tests
# c. Explore the relationship between numerical and categorical variables using box plots or violin plots

# a.
# Bivariate Analysis
# Numerical vs Target Variables

num_cols = df.select_dtypes(include = np.number).columns

for col in num_cols:
    sns.boxplot(data  = df, x = 'Response', y = col)
    plt.title(col+' vs. Response')
    plt.show()


# b.
# Bivariate Analysis
# Categorical vs Target Variables

cat_cols = df.select_dtypes(exclude = np.number).columns

for col in cat_cols:
    sns.countplot(data  = df, x = col, hue = 'Response')
    plt.title(col+' vs. Response')
    plt.xticks(rotation = 45)
    plt.show()

# ****************** Important ******************
# c.
# Correlational Analysis

plt.figure(figsize = (16,16))
corr_matrix = df.select_dtypes([np.number]).corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()









