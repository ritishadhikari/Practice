from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from sklearn import metrics
from sklearn.preprocessing import binarize
import pandas as pd

pima = pd.read_csv("C:/Users/Ritish Adhikari/Desktop/CSV File/diabetes.csv")
print("Pima Dataframe :\n",pima.head(),"\n")
#print(pima.columns)
feature_cols = ['Pregnancies','Insulin','BMI','Age']
X= pima[feature_cols]
y = pima['Outcome']
X_Train, X_Test, y_Train, y_Test = train_test_split(X,y,random_state=1)
Lgg = LogisticRegression()
Lgg.fit(X_Train,y_Train)
y_pred_class = Lgg.predict(X_Test)
#print(y_pred_class)
print("Accuracy : ",accuracy_score(y_Test,y_pred_class),"\n")
print("Y Test Value Count :\n",y_Test.value_counts(),"\n")
print("Percentage of 1 :",y_Test[y_Test==1].count()/y_Test.count(),"\n")
print("Percentage of 0 :",y_Test[y_Test==0].count()/y_Test.count(),"\n")
print("Null Accuracy :", max(y_Test[y_Test==1].count()/y_Test.count(),y_Test[y_Test==0].count()/y_Test.count()),"\n")
print("True : ",y_Test.values[0:25])
print("Pred : ",y_pred_class[0:25],"\n")

confusion = confusion_matrix(y_Test,y_pred_class)
print("Confusion Matrix : \n ",confusion, '\n')
TP = confusion[1,1]
TN = confusion[0,0]
FP = confusion[0,1]
FN = confusion[1,0]
#print(TP,TN,FP,FN)
print("Accuracy can also be found by :", (TP+TN)/sum(confusion.ravel()),"\n")
print("Classification Error can be found by : ", (FP+FN)/sum(confusion.ravel()),"\n")
print("Sensitivity - When the actual value is positive, how often is the prediction positive :", TP/(TP+FN),"\n")
print("Specificity - When the actual value is negative, how often is the prediction negative :", TN/(TN+FP),"\n")
print("False Positives - When the actual value is negative, how often is the prediction incorrect :", FP/(FP+TN),"\n")
print("Precision - When a Positive value is predicted, how often is it actually positive :", TP/(TP+FP),"\n")

#print(X_Test.values[0:10])
print("Printing the First 25 predicted response : ",Lgg.predict(X_Test)[0:25],"\n")
print("Printing the First 25 predicted probabilities : \n ",Lgg.predict_proba(X_Test)[0:25],"\n")

y_pred_prob = Lgg.predict_proba(X_Test)[:,1]
#print(y_pred_prob)

plt.subplot(2,2,1)
plt.hist(y_pred_prob, bins=8, rwidth=0.96)
plt.xlim(0,1)
plt.title("Histogram of predicted Probabilities")
plt.xlabel("Predicted Probability of Diabetes")
plt.ylabel("Frequency")


y_pred_class_later = binarize([y_pred_prob],0.35)[0]
print ("The first 10 values of y_pred_prob :",y_pred_prob[0:10], "\n")
print ("The first 10 predicted value : ",y_pred_class_later[0:10], "\n")
print("Accuracy : ",accuracy_score(y_Test,y_pred_class_later),"\n")
confusion = confusion_matrix(y_Test,y_pred_class_later)
print("Confusion Matrix : \n ",confusion, '\n')
TP = confusion[1,1]
TN = confusion[0,0]
FP = confusion[0,1]
FN = confusion[1,0]
print("New Accuracy can also be found by :", (TP+TN)/sum(confusion.ravel()),"\n")
print("New Classification Error can be found by : ", (FP+FN)/sum(confusion.ravel()),"\n")
print("New Sensitivity - When the actual value is positive, how often is the prediction positive :", TP/(TP+FN),"\n")
print("New Specificity - When the actual value is negative, how often is the prediction negative :", TN/(TN+FP),"\n")
print("New False Positives - When the actual value is negative, how often is the prediction incorrect :", FP/(FP+TN),"\n")
print("New Precision - When a Positive value is predicted, how often is it actually positive :", TP/(TP+FP),"\n")


fpr,tpr,thresholds = roc_curve(y_Test,y_pred_prob)
plt.subplot(2,2,2)
plt.plot(fpr,tpr)
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("False Positive Rate (1-Specificity)")
plt.ylabel("True Positive Rate (Sensitivity)")
plt.title("ROC Curve")


def evaluate_threshold(thresold):
    print("sensitivity :", tpr[thresholds >thresold][-1])
    print("specificity :", 1- fpr[thresholds > thresold][-1])

evaluate_threshold(0.3)

plt.show()
