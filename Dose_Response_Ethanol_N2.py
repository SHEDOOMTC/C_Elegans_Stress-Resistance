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
Dose1 = pd.read_csv("Dose_Response_Ethanol_N2.csv")
print(Dose1)

# force it to a datafra;e
ds1 = pd.DataFrame(Dose1)
print(ds1)
max(ds1)

# lets make a scatterplot plot first
plt.figure(figsize=(10, 6))

#plt.scatter(ds1['EtOH'], ds1['10min'])

#plt.show()

#lets find regression lines up to the 5th degree for the 10min
import numpy as np
import scipy.optimize as opt

#mod11 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['10min'], 1))
#mod12 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['10min'], 2))
#mod13 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['10min'], 3))
mod14 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['10min'], 4))
#mod15 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['10min'], 5))

#Generate x and y values for the curve
polyline = np.linspace(0, 1714, 500)


#plt.scatter(ds1['EtOH'], ds1['10min'], color='r', label='Data Points')
plt.legend()
#plt.show()

#add fitted polynomial lines to scatterplot 
#plt.plot(polyline, mod11(polyline), color='g')
#plt.plot(polyline, mod12(polyline), color='r')
#plt.plot(polyline, mod13(polyline), color='m')
#plt.plot(polyline, mod14(polyline), color='b', label = '10mins')
#plt.plot(polyline, mod15(polyline), color='k')
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
a = adjR(ds1['EtOH'], ds1['10min'], 1)
b = adjR(ds1['EtOH'], ds1['10min'], 2)
c = adjR(ds1['EtOH'], ds1['10min'], 3)
d = adjR(ds1['EtOH'], ds1['10min'], 4)
e = adjR(ds1['EtOH'], ds1['10min'], 5)

adjrall = (a, b, c, d, e)
results1 = []

for i in adjrall:
    results1.append(i)
    print(results1)



#lets find regression lines up to the 5th degree for the 20min

mod21 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['20min'], 1))
mod22 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['20min'], 2))
mod23 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['20min'], 3))
mod24 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['20min'], 4))
mod25 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['20min'], 5))

#Generate x and y values for the curve
polyline = np.linspace(0, 1714, 500)


#plt.scatter(ds1['EtOH'], ds1['20min'], color='r', label='Data Points')
plt.legend()
#plt.show()

#add fitted polynomial lines to scatterplot (third degree performed best)
#plt.plot(polyline, mod21(polyline), color='g')
#plt.plot(polyline, mod22(polyline), color='r')
#plt.plot(polyline, mod23(polyline), color='m', label = '20mins')
#plt.plot(polyline, mod24(polyline), color='b', label = '20mins')
#plt.plot(polyline, mod25(polyline), color='k')
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
a = adjR(ds1['EtOH'], ds1['20min'], 1)
b = adjR(ds1['EtOH'], ds1['20min'], 2)
c = adjR(ds1['EtOH'], ds1['20min'], 3)
d = adjR(ds1['EtOH'], ds1['20min'], 4)
e = adjR(ds1['EtOH'], ds1['20min'], 5)

adjrall = (a, b, c, d, e)
results1 = []

for i in adjrall:
    results1.append(i)
    print(results1)



#lets find regression lines up to the 5th degree for the 30min

mod31 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['30min'], 1))
mod32 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['30min'], 2))
mod33 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['30min'], 3))
mod34 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['30min'], 4))
mod35 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['30min'], 5))

#Generate x and y values for the curve
polyline = np.linspace(0, 1714, 500)


#plt.scatter(ds1['EtOH'], ds1['30min'], color='r', label='Data Points')
plt.legend()
#plt.show()

#add fitted polynomial lines to scatterplot (third fit performed best)
#plt.plot(polyline, mod31(polyline), color='g')
#plt.plot(polyline, mod32(polyline), color='r')
#plt.plot(polyline, mod33(polyline), color='m')
#plt.plot(polyline, mod34(polyline), color='b')
#plt.plot(polyline, mod35(polyline), color='k')
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
a = adjR(ds1['EtOH'], ds1['30min'], 1)
b = adjR(ds1['EtOH'], ds1['30min'], 2)
c = adjR(ds1['EtOH'], ds1['30min'], 3)
d = adjR(ds1['EtOH'], ds1['30min'], 4)
e = adjR(ds1['EtOH'], ds1['30min'], 5)

adjrall = (a, b, c, d, e)
results1 = []

for i in adjrall:
    results1.append(i)
    print(results1)



#lets find regression lines up to the 5th degree for the 40min

mod41 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['40min'], 1))
mod42 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['40min'], 2))
mod43 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['40min'], 3))
mod44 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['40min'], 4))
mod45 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['40min'], 5))

#Generate x and y values for the curve
polyline = np.linspace(0, 1714, 500)


#plt.scatter(ds1['EtOH'], ds1['40min'], color='r', label='Data Points')
plt.legend()
#plt.show()

#add fitted polynomial lines to scatterplot  (the third fit performed best)
#plt.plot(polyline, mod41(polyline), color='g')
#plt.plot(polyline, mod42(polyline), color='r')
#plt.plot(polyline, mod43(polyline), color='m')
#plt.plot(polyline, mod44(polyline), color='b', label = '0mins')
#plt.plot(polyline, mod45(polyline), color='k')
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
a = adjR(ds1['EtOH'], ds1['40min'], 1)
b = adjR(ds1['EtOH'], ds1['40min'], 2)
c = adjR(ds1['EtOH'], ds1['40min'], 3)
d = adjR(ds1['EtOH'], ds1['40min'], 4)
e = adjR(ds1['EtOH'], ds1['40min'], 5)

adjrall = (a, b, c, d, e)
results1 = []

for i in adjrall:
    results1.append(i)
    print(results1)



#lets find regression lines up to the 5th degree for the 50min

mod51 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['50min'], 1))
mod52 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['50min'], 2))
mod53 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['50min'], 3))
mod54 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['50min'], 4))
mod55 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['50min'], 5))

#Generate x and y values for the curve
polyline = np.linspace(0, 1714, 500)


#plt.scatter(ds1['EtOH'], ds1['50min'], color='r', label='Data Points')
plt.legend()
#plt.show()

#add fitted polynomial lines to scatterplot (the third fit outperformed)
#plt.plot(polyline, mod51(polyline), color='g')
#plt.plot(polyline, mod52(polyline), color='r')
#plt.plot(polyline, mod53(polyline), color='m')
#plt.plot(polyline, mod54(polyline), color='b', label = '20mins')
#plt.plot(polyline, mod55(polyline), color='k')
#plt.show()



# define function to calculate adjusted r-squared 
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
a = adjR(ds1['EtOH'], ds1['50min'], 1)
b = adjR(ds1['EtOH'], ds1['50min'], 2)
c = adjR(ds1['EtOH'], ds1['50min'], 3)
d = adjR(ds1['EtOH'], ds1['50min'], 4)
e = adjR(ds1['EtOH'], ds1['50min'], 5)

adjrall = (a, b, c, d, e)
results1 = []

for i in adjrall:
    results1.append(i)
    print(results1)



#lets find regression lines up to the 5th degree for the 60min

mod61 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['60min'], 1))
mod62 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['60min'], 2))
mod63 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['60min'], 3))
mod64 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['60min'], 4))
mod65 = np.poly1d(np.polyfit(ds1['EtOH'], ds1['60min'], 5))

#Generate x and y values for the curve
polyline = np.linspace(0, 1714, 500)


#plt.scatter(ds1['EtOH'], ds1['60min'], color='r', label='Data Points')
plt.legend()
#plt.show()

#add fitted polynomial lines to scatterplot (the third fit outperformed)
#plt.plot(polyline, mod61(polyline), color='g')
#plt.plot(polyline, mod62(polyline), color='r')
#plt.plot(polyline, mod63(polyline), color='m')
#plt.plot(polyline, mod64(polyline), color='b', label = '20mins')
#plt.plot(polyline, mod65(polyline), color='k')
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
a = adjR(ds1['EtOH'], ds1['60min'], 1)
b = adjR(ds1['EtOH'], ds1['60min'], 2)
c = adjR(ds1['EtOH'], ds1['60min'], 3)
d = adjR(ds1['EtOH'], ds1['60min'], 4)
e = adjR(ds1['EtOH'], ds1['60min'], 5)

adjrall = (a, b, c, d, e)
results1 = []

for i in adjrall:
    results1.append(i)
    print(results1)


### Final Plot

plt.plot(polyline, mod14(polyline), color='b', label = '10mins')
plt.plot(polyline, mod23(polyline), color='m', label = '20mins')
plt.plot(polyline, mod33(polyline), color='g', label = '30mins')
plt.plot(polyline, mod43(polyline), color='r', label = '40mins')
plt.plot(polyline, mod52(polyline), color='k', label = '50mins')
plt.plot(polyline, mod63(polyline), color='c', label = '60mins')

plt.xlabel('EtOH(mM)', fontsize = 14)
plt.ylabel('Response(% Motile Worms)', fontsize = 14)
plt.legend()
plt.grid() 
plt.title('Dose Response Curve for N2 Strain in Ethanol Induced Stress')
plt.show()


