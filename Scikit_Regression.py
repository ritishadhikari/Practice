from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from scipy import stats
import seaborn as sns
import pandas as pd
import numpy as np
import statsmodels.api as sn
from sklearn.preprocessing import StandardScaler

data =pd.read_csv(r"C:\Users\ritis\PycharmProjects\CSV Files\Advertising.csv", index_col=0)
print("Printing the Sample Data \n",data.head(50),"\n")
#sns.pairplot(data,x_vars=['TV','radio','newspaper'], y_vars='sales',aspect=0.5,size=7,kind='reg')
feature = ['TV','radio','newspaper']
X = data[feature]
y= data['sales']
X_Train, X_Test, y_Train, y_Test = train_test_split(X,y, test_size=0.25,random_state=3)

lng = LinearRegression()
print("Tuning Parameters of Linear Regression :",lng, "\n")
lng.fit(X_Train,y_Train)
print("R Score Training:",lng.score(X_Train,y_Train),"\n")
print("R Score Testing:",lng.score(X_Test,y_Test),"\n")
print("Linear Regression has the following internal attributes : \n ",dir(lng), "\n")
print("The Intercept value of the Training Data set is :",lng.intercept_," and the coeficients are :", lng.coef_,"\n")

featuredict = {}
p=0
for i in feature:
    featuredict[i]= lng.coef_[p]
    p+=1
print("The Coeficient Values of the attributes are : \n",featuredict, "\n")

y_pred = lng.predict(X_Test)
m= np.sqrt(mean_squared_error(y_Test,y_pred))
n = r2_score(y_Test,y_pred)
print(" The root square mean value is :",m, "\n")
print(" The r2 value is :",n, "\n")

print( "Predicting the Unit Sales for the the given value of attributes : \n ",lng.predict([[240,85,100]]),"\n")

#plt.scatter(data['newspaper'],data['sales'])

print("x feature before transformation : ", X[feature],"\n")
scale =StandardScaler()
X[feature]= scale.fit_transform(X[feature].as_matrix())
print("x feature after transformation : ", X[feature],"\n")
est = sn.OLS(y,X).fit()
print("Summary : \n", est.summary(),"\n")
plt.show()
