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
'''
