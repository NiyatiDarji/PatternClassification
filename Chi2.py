# chi2 test implementation

import numpy as np
from scipy.stats import chi2_contingency, chi2
chi_square, p, dof, ex = chi2_contingency(observed = np.array([[3,4,7],[2,6,4],[1,6,4],[6,5,2]]))
print("chi_square:",chi_square)
print("p value:",p)
print("degree of freedom dof:",dof)
print("Expected contingency table:\n",ex)

# Find the critical value of chi2 for dof = dof and confidence= 95%
critical_value = chi2.ppf(q = 0.95, df = dof)
print("Critical value:",critical_value)

if chi_square>critical_value:
    print("Reject the null hypothesis")
else:
    print("Cannot reject the null hypothesis")