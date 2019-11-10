# bootstrap test to obtain a 95% confidence interval on the precision at a
# recall rate of 90%.

import numpy as np
import pandas as pd
from sklearn.utils import resample

# load dataset
df = pd.read_csv('C:/Users/bhargav/Desktop/Pattern Classification Sem3/Assignments/assigData3.tsv', sep='\t',
                 header=None)
score = [];
true_class = []
for index in range(0, 2000):
    score.append(df[0][index])
    true_class.append(df[1][index])

# configure bootstrap
k = 2000
# run bootstrap
stats = list()
for i in range(k):
    samples = resample(score, replace=True, n_samples=2000)
    stats.append(np.percentile(samples, 0.60))
# Sort values
stats.sort()
# 95% confidence intervals
lower_bound = int(k*0.025)
upper_bound = int(k*0.975)
lower = stats[lower_bound]
upper = stats[upper_bound]
print("95% confidence interval lower bound: ",lower,"upper bound", upper)
