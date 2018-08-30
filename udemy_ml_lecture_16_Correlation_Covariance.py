import numpy as np

pagespeeds = np.random.normal(loc=3,scale=1,size=1000)
purchaseamount =np.random.normal(loc=50,scale=10,size=1000)
print("Correlation Coeficient : ",np.corrcoef(pagespeeds,purchaseamount)[0,1], "\n")
print("Covariance : ",np.cov(pagespeeds,purchaseamount)[0,1], "\n")
