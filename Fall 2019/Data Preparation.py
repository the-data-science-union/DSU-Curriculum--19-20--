import pandas as pd
import numpy as np


#Cleansing Data
##Usually applies to data entries when they don't have a certain value or a value is inconsistent with the rest
data = pd.Series([1, np.nan, 'hello', None])
data
##Fixing Null Values
###Finding null values

data.isnull()
data[data.notnull()]

##Removing Null Values
###Be careful with this, you don't wanna get ahead of yourself

data.dropna()

df = pd.DataFrame([[1,      np.nan, 2],
                   [2,      3,      5],
                   [np.nan, 4,      6]])
df

df.dropna()
df.dropna(axis='columns')
df[3] = np.nan
df
df.dropna(axis='columns', how='all')


##Filling NA Values
###This is a much preferred method to dealing with NA values

data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
data

data.fillna(0)
###forward-fill
data.fillna(method='ffill')
### back-fill
data.fillna(method='bfill')
###On dataframes
df.fillna(method='ffill', axis=1)



##Fixing redundent Whitespace
###Usually, applies to columns more than anything to keep uniform syntax
###White spaces can cause errors and bugs when indexing for analysis
###Errors in strings if data frame has white space between characters in strings in some languages can ouput as NA

my_string = "  This   sentence    contains many redundant    whitespaces    !!!  "
my_string_1 = my_string.strip()
print(my_string_1)
my_string_2 = my_string.rstrip()
print(my_string_2)
my_string_3 = my_string.lstrip()
print(my_string_3)

my_string_4 = my_string.replace(" ", "")
print(my_string_4)



#Regular Expressions
import re

#substitution
my_string_5 = re.sub(" +", " ",my_string)
print(my_string_5)

#compilation
string1 = " Retreat was lit, it was lit also"
pattern = re.compile("was lit")
result=pattern.findall(string1)
print(result)


#Data Transformation
data = pd.DataFrame({'k1': ['one'] * 3 + ['two'] * 4,'k2': [1, 1, 2, 3, 3, 4, 4]})
data

#which entries are duplicated?
data.duplicated()
#lets drop them
data.drop_duplicates()

#Mapping Data 
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami','corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'], 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
data

##Create map
meat_to_animal = {
 'bacon': 'pig',
 'pulled pork': 'pig',
 'pastrami': 'cow',
 'corned beef': 'cow',
 'honey ham': 'pig',
 'nova lox': 'salmon'
}

data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
data

#Replacing Values
data = pd.Series([1., -999., 2., -999., -1000., 3.])
data

data.replace(-999, np.nan)

data.replace([-999, -1000], np.nan)

data.replace([-999, -1000], [np.nan, 0])

data.replace({-999: np.nan, -1000: 0})

#Renaming Index Axis
data = pd.DataFrame(np.arange(12).reshape((3, 4)),index=['Ohio', 'Colorado', 'New York'],columns=['one', 'two', 'three', 'four']) 
data.index.map(str.upper)

#Make Index all Uppercase
data.index = data.index.map(str.upper)
   
#Rename column names and index
data.rename(index=str.title, columns=str.upper)
 
data.rename(index={'OHIO': 'INDIANA'},columns={'three': 'peekaboo'})
  
_ = data.rename(index={'OHIO': 'INDIANA'}, inplace=True)
data
 
#Dummy Variables, useful when using categoircal data
df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],'data1': range(6)})
df

pd.get_dummies(df['key'])
 
dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)
df_with_dummy

#Data Integration
##Merging Tables

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1': range(7)})

df2 = pd.DataFrame({'key': ['a', 'b', 'd'],'data2': range(3)})

pd.merge(df1, df2, on='key')
  

##Follow the keys
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1': range(7)})

df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],'data2': range(3)})

pd.merge(df3, df4, left_on='lkey', right_on='rkey')

##Outer Join (try to include everything in the merge) 
pd.merge(df1, df2, how='outer')
  
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],'data1': range(6)})
 
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],'data2': range(5)})

df1
df2
##Left Join (joining on df1)
pd.merge(df1, df2, on='key', how='left')
 
##Inner Join (only include the similarites)
pd.merge(df1, df2, how='inner')
 
left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],'key2': ['one', 'two', 'one'],'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],'key2': ['one', 'one', 'one', 'two'],'rval': [4, 5, 6, 7]})

##Merging on two keys
pd.merge(left, right, on=['key1', 'key2'], how='outer')
 
#Overlapping column names 
pd.merge(left, right, on='key1', suffixes=('_left', '_right'))

#Concatenation (pasting values together) 
arr = np.arange(12).reshape((3, 4))
arr
   
np.concatenate([arr, arr], axis=1) #Axis 1 = by column
 
s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
 
pd.concat([s1, s2, s3])


pd.concat([s1, s2, s3], axis=1)

s4 = pd.concat([s1 * 5, s3])
s4 

pd.concat([s1, s4], axis=1) 
  
pd.concat([s1, s4], axis=1, join='inner')
##Concat using axes
pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])
 
#Reshaping
data = pd.DataFrame(np.arange(6).reshape((2, 3)),index=pd.Index(['Ohio', 'Colorado'], name='state'),columns=pd.Index(['one', 'two', 'three'], name='number'))
data

##Stack by index  
result = data.stack()
result
 
result.unstack()
 
##Unstack with columns being the index
result.unstack(0)

  
result.unstack('state')
  


s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
data2 = pd.concat([s1, s2], keys=['one', 'two'])
data2
data2.unstack()

data2.unstack().stack()
data2.unstack().stack(dropna=False)
 
 