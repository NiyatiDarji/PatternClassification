# Plot ROC-AUC curves for 90% sensitivity
# Plot Precision-recall curves

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import precision_recall_curve
#read tsv file into dataframe
df = pd.read_csv('C:/Users/bhargav/Desktop/Pattern Classification Sem3/Assignments/assigData3.tsv', sep = '\t', header = None)
score = []; true_class = []
for index  in range(0, 2000):
    score.append(df[0][index])
    true_class.append(df[1][index])
#ROC Curve
fpr, tpr, thresholds = metrics.roc_curve(true_class, score)
plt.plot(fpr,tpr)
for i_x, i_y in zip(fpr, tpr):
    if i_y == 0.901:
        plt.plot(i_x, i_y, ls="", marker="x",color = 'r')
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.grid(True)
plt.xlabel('False Positive Rate i.e. (1-Specificity)')
plt.ylabel('True Positive Rate i.e. Sensitivity')
plt.title('ROC Curve')
plt.show()
#AUC Score
print(metrics.roc_auc_score(true_class,score))

# Precision-recall curve
precision, recall, _ = precision_recall_curve(true_class, score)
plt.plot(recall,precision)
for i_x, i_y in zip(recall, precision):
    if i_x == 0.901:
        plt.plot(i_x, i_y, ls="", marker="x",color = 'r')
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.title('Precision-Recall Curve')
plt.xlabel('Recall i.e. Sensitivity')
plt.ylabel('Precision')
plt.grid(True)
plt.show()
# By Algorithm
#fpr = [];tpr = []
#N = 1000
#P = 1000
#for threshold in range(int(min(score)),int(max(score))):
 #   FP = 0
  #  TP = 0
   # index = 0
    #for score_value in score:
     #   if score_value>threshold:
      #      if true_class[index]==1:
       #         TP = TP+1
        #    else:
         #       FP = FP+1
        #index=index+1
    #fpr.append(FP/N)
    #tpr.append(TP/P)
#plt.plot(fpr,tpr,marker = 'x')
#plt.grid(True)
#plt.xlabel('False Positive Rate')
#plt.ylabel('True Positive Rate')
#plt.title('ROC Curve')
#plt.show()

