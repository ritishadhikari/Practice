import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
import numpy as np
from matplotlib import pyplot as pt

df = pd.read_csv(r"C:\Users\Ritish Adhikari\Desktop\CSV File\aapl_no_dates.csv")
rows, columns = df.shape
#print("Printing the original DF Dataframe")
#print(df)
print()
print("------------Putting a date range to the DF Dataframe with US holiday list and printing the dataframe with date time index---------")
USB = CustomBusinessDay(calendar=USFederalHolidayCalendar())
dt = pd.date_range(start='2018-07-01',periods= rows ,freq=USB)
df.set_index(dt,inplace=True)
print(df)


print()
print("----------------------Printing Indian Calendar Now-------------------------------")

from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, nearest_workday

class MyBirthdayCalendar(AbstractHolidayCalendar):

       rules = [
        Holiday('My Birthday', month=7, day=6, observance=nearest_workday),
        Holiday('Dada''s Birthday', month=7, day=8, observance=nearest_workday)
    ]

df = pd.read_csv(r"C:\Users\Ritish Adhikari\Desktop\CSV File\aapl_no_dates.csv")
rows, columns = df.shape
#print("Printing the original DF Dataframe")
#print(df)
print()
print("Putting a date range to the DF Dataframe with US holiday list and printing the dataframe with date time index")
MBC = CustomBusinessDay(calendar=MyBirthdayCalendar())
dt = pd.date_range(start='2018-07-01',periods= rows ,freq=MBC)
df.set_index(dt,inplace=True)
print(df)


print()
print("----------------------Printing Saudi Calendar Now with Sunday to Thursday as Working-------------------------------")

from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, nearest_workday


class MyBirthdayCalendar(AbstractHolidayCalendar):

    rules = [
        Holiday('Aman''s Birthday', month=7, day=5), #observance=nearest_workday),
        Holiday('Dada''s Birthday', month=7, day=8) #observance=nearest_workday)
    ]


print()
print("----------------------Printing Saudi Calendar Now with Sunday to Thursday as Working without calling the MyBirthdayCalendar Class-------------------------------")
df = pd.read_csv(r"C:\Users\Ritish Adhikari\Desktop\CSV File\aapl_no_dates.csv")
rows, columns = df.shape
#print("Printing the original DF Dataframe")
#print(df)
print()
print("Putting a date range to the DF Dataframe with US holiday list and printing the dataframe with date time index")
MBC = CustomBusinessDay(weekmask='Sun Mon Tue Wed Thu',holidays=['2018-07-05','2018-07-08'])
dt = pd.date_range(start='2018-07-01',periods= rows ,freq=MBC)
df.set_index(dt,inplace=True)
print(df)

