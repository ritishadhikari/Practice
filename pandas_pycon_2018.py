import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

# Dataset 1 : Standard Open Policing Project

ri = pd.read_csv(r"C:\Users\Ritish Adhikari\Desktop\CSV File\police.csv")
print("Dataframe :\n",ri.head(),"\n")
print("Shape of Dataframe :\n",ri.shape,"\n")
print("Data Types :\n", ri.dtypes,"\n")

print("Finding The Null Value Counts for each Columns in the ri Dataframe :\n",ri.isnull().sum(),"\n")
ri.dropna(axis=1,thresh=1,inplace=True)
print("Removing the Columns which contains the Missing Values \n", ri.columns,"\n")

print("Checking Whether Men or Women Speed More than Often 1 : \n", pd.crosstab(index=ri['driver_gender'], columns=ri['violation'], values=ri['violation'],aggfunc='count', normalize='index'),"\n")
print("Checking Whether Men or Women Speed More than Often 2: \n",ri.driver_gender[ri['violation']=='Speeding'].value_counts(normalize=False),"\n")
print("Checking Whether Men or Women Speed More than Often 3: \n",ri.groupby('driver_gender')['violation'].value_counts(normalize=True),"\n")
print("Does Gender Effect who gets searched during a stop: 1 \n",pd.crosstab(index=ri['driver_gender'], columns=ri['search_conducted'], values=ri['search_conducted'],aggfunc='count',normalize='index'),"\n" )
print("Does Gender Effect who gets searched during a stop: 2 \n",ri.groupby('driver_gender')['search_conducted'].value_counts(normalize=True),"\n")
print("Does Gender Effect who gets searched during a stop: 3 \n",ri.groupby(['violation','driver_gender'])['search_conducted'].mean(),"\n")
#tr = ri.groupby(['violation','driver_gender'])['search_conducted'].mean()
#tr.plot(kind = 'bar')

print("Checking whether only for Search which were not conducted, for them only the Search Type threw Null Values : \n",ri.search_type[ri['search_conducted']==False].value_counts(dropna=False),"\n")
print("Finding the different values in Search Type Column and their Frequency :\n",ri['search_type'].value_counts(),"\n")
print("During a Search, how often is the driver frisked :\n ",ri['search_type'].str.contains('Protective Frisk').value_counts(dropna=True,normalize=False),"\n")

ri['stop_date']=pd.to_datetime(ri['stop_date'],dayfirst=True)
ri['stop_time']=pd.to_datetime(ri['stop_time'])
#print(type(ri['stop_date']))
ri['year']=pd.DatetimeIndex(ri['stop_date']).year
#print(ri['year'])
yearly_stops = ri.groupby('year')['stop_time'].count()
print(yearly_stops,"\n")
print("Which Year Had the least number of Stops : \n",yearly_stops.index[yearly_stops==yearly_stops.min()],"The number of Stops being ", yearly_stops.min(),"\n")


ri['stop_time_hour']=pd.DatetimeIndex(ri['stop_time']).hour
#print("How Does Drug Activity Change by Time of Day as a mean : \n", ri.groupby('stop_time_hour').drugs_related_stop.mean().plot(kind='bar'),"\n")

#print("Do Most Stops occur at night ? \n",ri.groupby('stop_time_hour').stop_time.count().plot(),"\n")

ri.replace(to_replace={'stop_duration' : ['1','2']},value=np.NAN,inplace=True)
print(ri.stop_duration.value_counts(dropna=False))

plt.show()