import pandas as pd
import numpy as np
import matplotlib.pyplot as py

print("-----------------------------------Introduction---------------------------------------------------------------------")

xyz_web = { "Day" :[1,2,3,4,5,6], "Visitors" : [1000,700,6000,1000,400,350], "Bounce Rate" : [20,20,23,15,10,34]}
df = pd.DataFrame(xyz_web, index= [1,2,3,4,5,6])
print(df)

print("-----------------------------------Slicing---------------------------------------------------------------------")

xyz_web = { "Day" :[1,2,3,4,5,6], "Visitors" : [1000,700,6000,1000,400,350], "Bounce Rate" : [20,20,23,15,10,34]}
df = pd.DataFrame(xyz_web)
print(df.head(2))

print("-----------------------------------Merging---------------------------------------------------------------------")

df1 =pd.DataFrame({"HPI": [80,90,40,60], "Int_Rate" :[ 2,1,2,3], "Int_GDP": [50,45,45,67]}, index= [2001, 2002, 2003, 2004])
df2 =pd.DataFrame({"HPI": [80,90,30,60], "Int_Rate" :[ 2,1,2,3], "Int_GDP": [50,45,45,57]}, index= [2005, 2006, 2007, 2008])
merge = pd.merge(df1,df2, on = "HPI")
print("merge : \n", merge,"\n")
merge_outer =pd.merge(df1,df2,on= "HPI", how='outer',indicator=True, suffixes= ['_left','_right'])
print("merge outer : \n", merge_outer,"\n")
merge_left =pd.merge(df1,df2,on= "HPI", how='left',indicator=True)
print("merge left:\n", merge_left,"\n")
merge_right =pd.merge(df1,df2,on= "HPI", how='right', indicator=True)
print("merge right: \n", merge_right,"\n")

print("-----------------------------------Joining---------------------------------------------------------------------")


df1 =pd.DataFrame({ "Int_Rate" :[ 2,1,2,3], "Int_GDP": [50,45,45,67]}, index= [2001, 2002, 2003, 2004])
df2 =pd.DataFrame({ "Low_Tier_HPI" :[ 50,45,67,34], "Unemployment": [1,3,5,6]}, index= [2001, 2003, 2004, 2005])
joined_LHS = df1.join(df2, how="outer")
joined_RHS = df2.join(df1)
print("Outer Join : \n", joined_LHS, "\n")
print("Inner Join : \n", joined_RHS, "\n")


print("-----------------------------------Changing Index---------------------------------------------------------------------")
df = {"Day" :[1,2,3,4], "Visitors" :[200,100,230,300], "Bounce_Rate" :[20,45,60,10]}
k = pd.DataFrame(df)
k.set_index("Day", inplace=True)
print("First Row Information : \n",k.loc[1], "\n")
print(k)


print("-----------------------------------Changing Column Headers Name---------------------------------------------------------------------")
df = {"Day" :[1,2,3,4], "Visitors" :[200,100,230,300], "Bounce_Rate" :[20,45,60,10], "Time": ['Morning', 'Afternoon', 'Evening', 'Night']}
k = pd.DataFrame(df)
k = k.rename(columns ={"Visitors":"Users"})
print(k)

print("-----------------------------------Concatenation---------------------------------------------------------------------")

df1 =pd.DataFrame({"HPI": [80,90,40,60], "Int_Rate" :[ 2,1,2,3], "Int_GDP": [50,45,45,67]}, index= [2001, 2002, 2003, 2004])
df2 =pd.DataFrame({"HPI": [80,90,30,60], "Int_Rate" :[ 2,1,2,3], "Int_GDP": [50,45,45,57]}, index= [2005, 2006, 2007, 2008])
Concatenate = pd.concat([df1,df2],axis=0,ignore_index=False)
print(Concatenate)

print("-----------------------------------Data Munging---------------------------------------------------------------------")

