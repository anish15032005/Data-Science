import pandas as pd  
import numpy as np 
import xlrd # for reading excel files
s = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])
# print(s)
data = {
    'name':['Handey', 'Katherine','Preity','Annie'],
    'nickname':['Hayat', 'Hannah','Zara', 'Selina'],
    'Country':['Turkiye','Australia','India','USA'],
    'Age':[25, 30, 22, 28],
}
df = pd.DataFrame(data)
# df.to_csv('data.csv', index=False)
# print(df)

# in other way 
data1 = [
    ['Sanjay','Soldier'],['Raju','Travel Service'],['Afroz', 'Village Head'],['Manoj', 'Builder']
]
df1 = pd.DataFrame(data1, columns=['Name', 'Profession'])
# print(df1)
# df1.to_csv('data1.csv', index=False)

array1 = np.array([[1, 2, 3], [4, 5, 6]])
df_arr = pd.DataFrame(array1, columns=['Column1', 'Column2', 'Column3'])
# print(df_arr)

df_xl = pd.read_excel('sample.xls')
print(df_xl)