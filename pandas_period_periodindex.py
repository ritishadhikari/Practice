import pandas as pd
from matplotlib import pyplot as plt
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
import numpy as np
from matplotlib import pyplot as pt


#df = pd.read_csv(r"C:\Users\Ritish Adhikari\Desktop\CSV File\wmt.csv")
Y = pd.Period('2016', freq ='Y')
print("Period Details for Year :",Y)
print("Type in Y :", dir(Y))
print("Next Year : ", Y+1)
print("Start Time of Y : ", Y.start_time)
print("End Time of Y : ", Y.end_time)

print()
M =pd.Period("2018-01", freq ='M')
print("Period Details for Month :",M)
print("Type in M :", dir(M))
print("Next Month : ", M+1)
print("Start Time of M : ", M.start_time)
print("End Time of M : ", M.end_time)

print()
D =pd.Period("2016-02-28", freq ='D')
print("Period Details for Day:",D)
print("Type in D :", dir(D))
print("Next Day : ", D+1)
print("Start Time of D : ", D.start_time)
print("End Time of D : ", D.end_time)

print()
H =pd.Period("2016-02-28 21:33:25", freq ='H')
print("Period Details for Hour:",H)
print("Type in H :", dir(H))
print("Next Hour : ", H+1)
print("Start Time of D : ", H.start_time)
print("End Time of D : ", H.end_time)
print()
QA= pd.Period('2017Q1', freq = 'Q-Mar')
QB =pd.Period('2018Q2', freq = 'Q-Mar')
print("Period Details for Quarter:",QA)
print("Type in Q :", dir(QA))
print("Next Quarter : ", QA+1)
print("Start Time of Q : ", QA.start_time)
print("End Time of Q : ", QA.end_time)
print("Difference between two Quarters :", QB-QA)
print()
print("Converting Quarterly Frequency to Monthly Frequency ")
print("Beginning of the month : ", QA.asfreq('M', how ='start'))
print("End of the month : ", QA.asfreq('M', how ='end'))

print()
print('---Period Range Function ----')
idx = pd.period_range(start='2011',end='2017',freq='Q-mar')
ldx =pd.period_range(start='2011', periods=len(idx)   , freq='Q-mar')
print('idx\n',idx)
print('ldx\n',ldx)
print("-----------------Start Time of idx dataframe --------------")
print(idx.start_time)
print("Beginning of the month : ", idx.asfreq('M', how ='start'))
rows = idx.shape
print(idx[1].start_time)
print(idx[1].end_time)
print(idx[4] -idx[2])

print('------------Assigning Test Numbers to idx--------')
test = pd.DataFrame(np.random.random(rows), index=idx)
print(test)
print('------------Printing the Fiscals for the year from 2011 to 2013--------')
print(test['2011':'2013'])

print('------------Assigning Timestamp to test dataframe--------')
pst =test.to_timestamp()
print(pst)

print('------------Assigning period to timestamp dataframe--------')
testback = pst.to_period()
print(testback)


print("---------Working on Use Case----------")
df = pd.read_csv(r"C:\Users\Ritish Adhikari\Desktop\CSV File\wmt.csv", index_col='Line Item')
print(df)
print()
print("Transposing the array")
df =df.T
print(df)
print("Original Index Variable : ",df.index)
df.index =pd.PeriodIndex(df.index,freq ='Q-JAN')
print("Revised Index : ", df.index)
print()
print("Appending the Two Columns - Starttime and End Time")
df ['Start Date'] = df.index.start_time
df ['End Date'] = df.index.end_time
print(df)
print()
print('----------------------Adding a New Column Altogather------------------')
z= [4,6,7,8,6]

df['t']=pd.Series(z, index=df.index)
print(df)
