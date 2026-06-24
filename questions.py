'''
TITANIC

1. 
import pandas as pd
df = pd.read_csv('/content/titanic (1).csv', encoding = 'ISO-8859-1')
df.head()

2.
# embarked = 'S'
df[df['embarked'] == 'S']

3.
# fare between 20 to 40 
df[(df['fare'] >= 20) & (df['fare'] <= 40)]

4.
# data where age is missing (Age = NaN)
df[(df['age'].isnull())]

5.
# had sbsp>0
df[(df['sibsp'] > 0)]

6.
# survived and paid more than median fare
df[(df['survived'] == 1) & (df['fare'] > df['fare'].median())]

7.
# age < 18
df[df['age'] < 18]

8.
# female and survived
df[(df['sex'] == 'female') & (df['survived'] == 1)]

9.
#either in first or second class
df[(df['pclass'] == 1) | (df['pclass'] == 2)]

10.
# less than 18 and survived
df[(df['age'] < 18) & (df['survived'] == 1)]

11.
# females traveled in firstclass
df[(df['sex'] == 'female') & (df['pclass'] == 1)]

12.

'''
