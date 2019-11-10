# Normality test to determine if data is normally distributed

import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np
from statsmodels.graphics.gofplots import qqplot
#read tsv file into dataframe
df = pd.read_csv('C:/Users/bhargav/Desktop/Pattern Classification Sem3/Assignments/assigData2.tsv', sep = '\t', header = None)

W_apl = []; W_orng = []; W_grp = []
weight = []
D_apl = []; D_orng = []; D_grp = []
for index  in range(0, 100):
    W_apl.append(round(df[0][index]))
    W_orng.append(round(df[1][index]))
    W_grp.append(round(df[2][index]))
weight =  W_apl+W_orng+W_grp

qqplot(np.array(weight),line='s')
plt.show()
