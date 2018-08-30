import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\Ritish Adhikari\Canopy\DataScience-Python3\PastHires.csv")
print("Printing the Head of the Data : \n ",df.head(), "\n")
print("Printing the Tail of the Data : \n ",df.tail(4), "\n")
print("Printing the Shape of the Data : \n ",df.shape, "\n")
print("Printing the Size of the Data : \n ",df.size, "\n")
print("Printing the Columns of the Data : \n ",df.columns, "\n")
print("Printing the First Five Rows of the Hired Column : \n ",df["Hired"][0:5], "\n")
print("Printing two columns from the dataframe Years Experience and Hired  : \n ",df[["Years Experience","Hired"]], "\n")
print("Printing the Data Frame with sorted values of Years of Experiance : \n ",df.sort_values(['Years Experience']), "\n")
print("Printing the Level of Education Value Count wise : \n ",df['Level of Education'].value_counts(dropna=False), "\n")
print("Putting the Level of Education Value in Graphs \n", df['Level of Education'].value_counts(dropna=False).plot(kind='bar'))
dfnew = df[['Previous employers','Hired']][5:10]
dfnew.plot(kind='bar')
plt.show()