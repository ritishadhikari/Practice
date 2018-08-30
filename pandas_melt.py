import pandas as pd
df = pd.read_csv(r"C:\Users\Ritish Adhikari\Desktop\CSV File\weather_melt.csv")
print("------------------------------The Original Dataframe------------------------------")
print (df,"\n")
print("------------------------------Printing the Melt Data Frame------------------------------")
melt = df.melt(id_vars=['day'], value_vars=['chicago','chennai','berlin'],var_name='City', value_name='Temperature')
print(melt,"\n")
print(melt[melt['City']=='chicago'])

