# Program to find the spearman's correlation coefficient and
# interpret its significance with Classical statistical test and permutation test

import pandas as pd
import warnings
from scipy.stats import spearmanr
from mlxtend.evaluate import permutation_test

#to suppress warnings
warnings.filterwarnings("ignore")
#Loading excel files data
psipred = pd.read_excel('C:/Users/bhargav/Desktop/Pattern Classification Sem3/Assignments/assigData1.xls', sheet_name = 'PSIPRED')
psipred_q3 = pd.DataFrame(psipred, columns= ['Q3'])
psipred_cc = pd.DataFrame(psipred, columns= ['CC_AVG'])

# Calculate spearman's correlation coefficient
coefficient, p = spearmanr(psipred_q3, psipred_cc)
print("Spearman's coefficient: ",coefficient)
print('Spearmans rank correlation p-value=%.3f' % p)

# Classical statistical test to interpret the significance
# p value is outputed
print("Classical statistical test interpretation")
if p > 0.05:
	print("Samples are significantly not correlated, cannot reject the null hypothesis")
else:
	print("Samples are significantly correlated, reject the null hypothesis")

# permutation test to interpret the significance
x = psipred_q3.to_numpy()
y = psipred_cc.to_numpy()
p_value = permutation_test(x, y, method='approximate', num_rounds=10000, seed=0)
print('Permutation test p_value=%.3f' % p_value)
print("permutation test interpretation")
if p_value > 0.05:
	print("Samples are significantly not correlated, cannot reject the null hypothesis")
else:
	print("Samples are significantly correlated, reject the null hypothesis")
