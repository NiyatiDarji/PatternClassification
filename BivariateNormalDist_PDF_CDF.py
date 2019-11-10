# Generating data drawn from bivariate normal distribution & draw CDF and PDF plots

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import math
import matplotlib as mpl

# Generate 1000 samples drawn from a bivariate normal distribution with mue1=1.2, mue2=3.1, sigma=[1.2 .7
#                                                                                                  .7  3.3]
mu1 = [1.2, 0]
mu2 = [3.1,0]
sigma = [[1.2, 0.7], [0.7, 3.3]]
x= np.random.multivariate_normal(mu1,sigma,1000).T
y= np.random.multivariate_normal(mu2,sigma,1000).T

#Ploting bivariate normal distribution
plt.plot(x, y, 'x')
plt.axis('equal')
plt.show()

#Determine Sigma and its trace
print("Determinant of Sigma: ",np.linalg.det(sigma))
print("Trace of Sigma: ", np.trace(sigma))

# Calculate the two eigenvectors and eigenvalues of sigma
print("eigenvectors and eigenvalues: ", np.linalg.eig(sigma))

# plot the PDF and CDF for a 1D normal distribution with mue=2.2 and sigma^2=0.8.
#PDF
x= np.arange(-3,6,0.1)
y= norm.pdf(x,2.2,math.sqrt(0.8))
plt.plot(x,y)
plt.show()

#CDF
x= np.arange(-3,6,0.1)
pdf_norm= norm.pdf(x,2.2,math.sqrt(0.8))
plt.hist(pdf_norm,cumulative=True, density= 1,histtype='step')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.show()