import pandas as pd

print("-----------------------------------------Read from Excel-----------------")

df = pd.read_excel(r"C:\Users\Ritish Adhikari\Desktop\CSV File\Excel File\weather_data.xlsx","Sheet1")
print(df)


print("-----------------------------------------Read from a Tuple-----------------")
weather_data = [
    ('01-01-2017',32,6,'Rain'),
    ('02-01-2017',35,7,'Sunny'),
    ('03-01-2017',28,2,'Snow')]
df = pd.DataFrame(weather_data,columns=('day','temperature','windspeed','event'),index=[1,2,3])
print(df)

print("-----------------------------------------Read from CSV-----------------")
df = pd.read_csv(r"C:\Users\Ritish Adhikari\Desktop\CSV File\stock_data.csv", na_values={
    'eps' : ['not available','n.a.'],
    'revenue': ['not available','n.a.',-1],
    'people' :['not available','n.a.',-1],
    'price': ['not available','n.a.',-1] },
                 nrows=5, header=0)
print(" Not Available Values(na_values), first n rows(nrows) :")
print(df)