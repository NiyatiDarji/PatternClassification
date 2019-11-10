# Determine the skewness and outliers in features.
# Also find the change in mean , median after outliers are removed

import pandas as pd
import numpy as np
from scipy.stats import iqr

#read tsv file into dataframe
df = pd.read_csv('C:/Users/bhargav/Desktop/Pattern Classification Sem3/Assignments/assigData2.tsv', sep = '\t', header = None)

W_apl = []; W_orng = []; W_grp = []
D_apl = []; D_orng = []; D_grp = []
for index  in range(0, 100):
    W_apl.append(df[0][index])
    W_orng.append(df[1][index])
    W_grp.append(df[2][index])
    D_apl.append(df[3][index])
    D_orng.append(df[4][index])
    D_grp.append(df[5][index])

# Skewness of apple features....2a
apl_weight = pd.DataFrame({'apple_weight':W_apl})
apl_diameter = pd.DataFrame({'apple_diameter':D_apl})
print(apl_weight.skew(axis = 0, skipna = True))
print(apl_diameter.skew(axis = 0, skipna = True))

#Determine outliers in weight feature...........2b
#For apple
apl_weight = sorted(W_apl)
apl_q1, apl_q3= np.percentile(apl_weight,[25,75])
apl_iqr = apl_q3 - apl_q1
apl_lower_bound = apl_q1 -(1.5 * apl_iqr)
apl_upper_bound = apl_q3 +(1.5 * apl_iqr)
print("Lower bound for apple weight",apl_lower_bound)
print("Upper bound for apple weight",apl_upper_bound)
status = 0
W_apl_1 = sorted(W_apl)
for i in apl_weight:
    if i < apl_lower_bound or i > apl_upper_bound:
        print("Outlier for apple weight is :" , i)
        W_apl_1.remove(i)
        status = 1
if status==0:
       print("No outlier in apple weight")
#Change in mean and median after removing outlier for apple weight
print("Mean_before: ", float(np.mean(sorted(W_apl))))
print("Median_before: ", float(np.median(sorted(W_apl))))
print("Mean_after: ", float(np.mean(W_apl_1)))
print("Median_after: ", float(np.median(W_apl_1)))

#For Orange
#orng_weight = sorted(W_orng)
#orng_q1, orng_q3= np.percentile(orng_weight,[25,75])
#orng_iqr = orng_q3 - orng_q1
#orng_lower_bound = orng_q1 -(1.5 * orng_iqr)
#orng_upper_bound = orng_q3 +(1.5 * orng_iqr)
#print("Lower bound for orange weight",orng_lower_bound)
#print("Upper bound for orange weight",orng_upper_bound)
#status = 0
#for i in orng_weight:
#   if i < orng_lower_bound or i > orng_upper_bound:
#      status = 1
#     print("Outlier for orange weight is :" , i)
#if status==0:
#       print("No outlier in orange weight")

#For Grape
#grp_weight = sorted(W_grp)
#grp_q1, grp_q3= np.percentile(grp_weight,[25,75])
#grp_iqr = grp_q3 - grp_q1
#grp_lower_bound = grp_q1 -(1.5 * grp_iqr)
#grp_upper_bound = grp_q3 +(1.5 * grp_iqr)
#print("Lower bound for Grape weight",grp_lower_bound)
#print("Upper bound for Grape weight",grp_upper_bound)
#status = 0
#for i in grp_weight:
#   if i < grp_lower_bound or i > grp_upper_bound:
#      status = 1
#     print("Outlier for Grape weight is :" , i)
#if status==0:
#       print("No outlier in Grape weight")

# Min,Max,Range,IQR of D_apl.................2c
print("Min of D_apl:",min(D_apl))
print("Max of D_apl:",max(D_apl))
print("IQR of D_apl:",iqr(D_apl))