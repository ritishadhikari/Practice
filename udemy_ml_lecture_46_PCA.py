from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle

iris = load_iris()
numsamples, numfeatures = iris.data.shape
print("Number of Data :\n", numsamples,"\n")
print("Number of features :\n",numfeatures,"\n")
print("Target Names : ", iris.target_names,"\n  ")

X= iris.data
pca = PCA(n_components=2,whiten=True).fit(X)
print("pca values :\n",dir(pca),"\n")
X_pca = pca.transform(X)
print("PCA Components :\n",pca.components_,"\n")

print("Information that have been managed to be preserved : \n",pca.explained_variance_ratio_,"\n")
print("Total Information that have been managed to be preserved : \n",sum(pca.explained_variance_ratio_),"\n")
