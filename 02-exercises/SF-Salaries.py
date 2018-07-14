import pandas as pd
import numpy as np


sal = pd.read_csv('./02-exercises/Salaries.csv')
# print( sal.head() )
print(sal.head())
print(sal.info())

# print( sal.columns )

# avg BasePay
print( sal['BasePay'].mean() )

# highest amount of OvertimePay in the dataset
print( sal['OvertimePay'].max() )
print()

# What is the job title of JOSEPH DRISCOLL ?
print( sal[ sal['EmployeeName'] == 'JOSEPH DRISCOLL' ]['JobTitle'] )
print()

# How much does JOSEPH DRISCOLL make (including benefits)?
print(sal[ sal['EmployeeName'] == 'JOSEPH DRISCOLL' ]['TotalPayBenefits'] )
print()

# What is the name of highest paid person (including benefits)?
print(  sal[ sal['TotalPayBenefits']==sal['TotalPayBenefits'].max() ] )
print( sal.iloc[sal['TotalPayBenefits'].idxmax()]['EmployeeName'] )
print()

# What is the name of lowest paid person (including benefits)?
print( sal[ sal['TotalPayBenefits']==sal['TotalPayBenefits'].min() ] )
print()

# What was the average (mean) BasePay of all employees per year? (2011-2014) ?
print( sal.groupby('Year').mean()['BasePay'] )
print()

# How many unique job titles are there?
print( sal['JobTitle'].nunique() )
print()

# What are the top 5 most common jobs?
print( sal['JobTitle'].value_counts().head(5) )
print()

# How many Job Titles were represented by only one person in 2013?
print( ( sal[ sal['Year']==2013 ] ['JobTitle'].value_counts()==1 ).sum() )
print()

# Is there a correlation between length of the Job Title string and Salary?
sal['lengthOfTitle'] = sal['JobTitle'].apply(len)
print( sal[['lengthOfTitle', 'TotalPayBenefits']].corr() )










