'''
Pandas
The core library used in data manipulation

Features of Pandas:
Easy to handle data
Perprocessing and data cleaning
Efficient for data analysis
Integration with other libraries

There are two Types of Data Structure
1. Series
2. Dataframe

Series:
It is a pandas data structure which is a 1 dimensional labeled array, it can hold any data

Syntax to create a series:
import pandas as pd
var = pd.Series(array)


DataFrame
a string dataa in a structured way
table like structure
rows and columns

Syntax:
import pandas as pd
var = pd.DataFrame(Collection)

the collection should be dictionary

Example:
import pandas as pd
a = {'sname' : ['Rahul', 'Chandan', 'Ansh'], 'roll' : [1, 2, 3], 'mark' : [23, 45, 65], 'mock' : ['A', 'B', 'C']}
d = pd.DataFrame(a)
d
'''