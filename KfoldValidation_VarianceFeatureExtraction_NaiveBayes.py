# The program will first extract features using Variance threshold method
# Does Kfold cross validation on original data
# Does Kfold cross validation on selected feature data


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import VarianceThreshold
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score, cross_val_predict, train_test_split
from sklearn.metrics import precision_recall_curve, roc_curve,confusion_matrix,classification_report,accuracy_score


# Loading CSV file
file = pd.read_csv('C:/Users/bhargav/Desktop/Pattern Classification Sem3/Assignments/assigData4.csv', header = None)

# Feature selection using variance threshold
x = file.iloc[:, :-1]  # remove the last column as it is the target column
selection = VarianceThreshold(threshold=(.8 * (1 - .8)))
features = selection.fit_transform(x)
non_constant_columns = [column for column in x.columns
                        if column in x.columns[selection.get_support()]]

print("No. of features selected:",len(non_constant_columns))
print("The column number of selected features:")
column = []
for c in non_constant_columns:
    column.append(c)
print(column)

#5-fold cross validation test using naive bayes classifier
#x = pd.DataFrame(file.iloc[:, :-1])
# use this for selected feature prediction
x= pd.DataFrame(file.iloc[:,column])
y =[]
for i in range(0,7200):
    y.append(file.iloc[i,-1])
clf = GaussianNB()

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=.2,random_state=100)
clf.fit(x_train,y_train)
y_predict = cross_val_predict(clf,x_test,y_test,cv=5)
y_score = (clf.predict_proba(x_test))[:,1]

precision, recall, _ = precision_recall_curve(y, y_score)
plt.plot(recall,precision)
plt.title('Precision-Recall Curve')
plt.xlabel('Recall i.e. Sensitivity')
plt.ylabel('Precision')
plt.grid(True)
plt.show()

fpr, tpr,_ = roc_curve(y,y_score)
plt.plot(fpr,tpr)
plt.grid(True)
plt.xlabel('False Positive Rate i.e. (1-Specificity)')
plt.ylabel('True Positive Rate i.e. Sensitivity')
plt.title('ROC Curve')
plt.show()

print("Confusion matrix:\n",confusion_matrix(y_test, y_predict))
print("Classification report:\n",classification_report(y_test,y_predict))
print("Accuracy score:",accuracy_score(y_test,y_predict))
