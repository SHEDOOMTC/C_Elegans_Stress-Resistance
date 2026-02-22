#####for dose response curve (motility response of N2 strains in ethanol test)
#####for dose response curve

##Import libraries 
import os
os.getcwd()
os.chdir('Your working directory')
os.getcwd()

import pandas as pd
import matplotlib.pyplot as plt

#import CSV files
Dose1 = pd.read_csv("Dose_Response_H2O2.csv")
print(Dose1)

# force it to a datafra;e
ds1 = pd.DataFrame(Dose1)
print(ds1)
min(ds1)
max(ds1)

# lets make a scatterplot plot first
plt.figure(figsize=(10, 6))

#plt.scatter(ds1['H2O2'], ds1['N2'])

#plt.show()

#lets find regression lines up to the 5th degree for the N2
import numpy as np
import scipy.optimize as opt

modN1 = np.poly1d(np.polyfit(ds1['H2O2'], ds1['N2'], 1))
modN2 = np.poly1d(np.polyfit(ds1['H2O2'], ds1['N2'], 2))
modN3 = np.poly1d(np.polyfit(ds1['H2O2'], ds1['N2'], 3))
modN4 = np.poly1d(np.polyfit(ds1['H2O2'], ds1['N2'], 4))
modN5 = np.poly1d(np.polyfit(ds1['H2O2'], ds1['N2'], 5))

#Generate x and y values for the curve
polyline = np.linspace(0, 50, 200)


#plt.scatter(ds1['H2O2'], ds1['N2'], color='r', label='Data Points')
#plt.legend()
#plt.show()

#add fitted polynomial lines to scatterplot (we use fit 3)
#plt.plot(polyline, modN1(polyline), color='g')
#plt.plot(polyline, modN2(polyline), color='r')
#plt.plot(polyline, modN3(polyline), color='m')
#plt.plot(polyline, modN4(polyline), color='b')
#plt.plot(polyline, modN5(polyline), color='k')
#plt.grid() 
#plt.show()


#define function to calculate adjusted r-squared (#since the fourth curve gave the best fit, then we generate plot for the fourth curve)
def adjR(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y - ybar)**2)
    results['r_squared'] = 1- (((1-(ssreg/sstot))*(len(y)-1))/(len(y)-degree-1))

    return results

#calculated adjusted R-squared of each model
a = adjR(ds1['H2O2'], ds1['N2'], 1)
b = adjR(ds1['H2O2'], ds1['N2'], 2)
c = adjR(ds1['H2O2'], ds1['N2'], 3)
d = adjR(ds1['H2O2'], ds1['N2'], 4)
e = adjR(ds1['H2O2'], ds1['N2'], 5)

adjrall = (a, b, c, d, e)
results1 = []

for i in adjrall:
    results1.append(i)
    print(results1)



#lets find regression lines up to the 5th degree for the Daf2

modD1 = np.poly1d(np.polyfit(ds1['H2O2'], ds1['Daf-2'], 1))
modD2 = np.poly1d(np.polyfit(ds1['H2O2'], ds1['Daf-2'], 2))
modD3 = np.poly1d(np.polyfit(ds1['H2O2'], ds1['Daf-2'], 3))
modD4 = np.poly1d(np.polyfit(ds1['H2O2'], ds1['Daf-2'], 4))
modD5 = np.poly1d(np.polyfit(ds1['H2O2'], ds1['Daf-2'], 5))

#Generate x and y values for the curve
polyline = np.linspace(0, 50, 200)


#plt.scatter(ds1['H2O2'], ds1['Daf-2'], color='r', label='Data Points')
#plt.legend()
#plt.show()

#add fitted polynomial lines to scatterplot (we use the fit number 2)
#plt.plot(polyline, modD1(polyline), color='g')
#plt.plot(polyline, modD2(polyline), color='r')
#plt.plot(polyline, modD3(polyline), color='m')
#plt.plot(polyline, modD4(polyline), color='b')
#plt.plot(polyline, modD5(polyline), color='k')
#plt.grid() 
#plt.show()


#define function to calculate adjusted r-squared 
def adjR(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y - ybar)**2)
    results['r_squared'] = 1- (((1-(ssreg/sstot))*(len(y)-1))/(len(y)-degree-1))

    return results

#calculated adjusted R-squared of each model
a = adjR(ds1['H2O2'], ds1['Daf-2'], 1)
b = adjR(ds1['H2O2'], ds1['Daf-2'], 2)
c = adjR(ds1['H2O2'], ds1['Daf-2'], 3)
d = adjR(ds1['H2O2'], ds1['Daf-2'], 4)
e = adjR(ds1['H2O2'], ds1['Daf-2'], 5)

adjrall = (a, b, c, d, e)
results1 = []

for i in adjrall:
    results1.append(i)
    print(results1)





### Final grouped Plot

plt.plot(polyline, modN3(polyline), color='m', label = 'N2')
plt.plot(polyline, modD2(polyline), color='r', label = 'Daf-2')

plt.xlabel('H2O2(mM)', fontsize = 14)
plt.ylabel('Response(% Motile Worms)', fontsize = 14)
plt.legend()
plt.grid() 
plt.title('Dose Rsponse Curve for N2 & Daf-2 Strains in Hydrogen Peroxide Induced Stress')
plt.show()
