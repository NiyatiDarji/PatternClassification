# Find pearson Correlation Coefficient

import pandas as pd
import numpy as np

#Loading excel files data
pci = pd.read_excel('C:/Users/bhargav/Desktop/Pattern Classification Sem3/Assignments/assigData1.xls', sheet_name = 'PCI')
pci_q3 = pd.DataFrame(pci, columns= ['Q3'])
length = pd.DataFrame(pci, columns= ['Length'])
psipred = pd.read_excel('C:/Users/bhargav/Desktop/Pattern Classification Sem3/Assignments/assigData1.xls', sheet_name = 'PSIPRED')
psipred_q3 = pd.DataFrame(psipred, columns= ['Q3'])

x1 = pci_q3
x2 = psipred_q3
y = length

print("Pearson Correlation Coefficient between Q3 accuracy and protein length:")
print("\nFor PCI:\n")
print (np.corrcoef(x1.T,y.T))
print("\nFor PSPIRED:\n")
print(np.corrcoef(x2.T,y.T))