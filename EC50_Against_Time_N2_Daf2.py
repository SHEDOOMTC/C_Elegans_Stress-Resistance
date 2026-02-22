#####for line plot (EC50 of strains at different times in ethanol test)

import os
os.getcwd()
os.chdir('Your working directory')
os.getcwd()

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("plots_Ethanol.csv")
print(data)
print(data.head(3))



# force it to a datafra;e
df = pd.DataFrame(data)
print(df)


# lets make the plot
plt.figure(figsize=(10, 6))

plt.plot(df["Time"], df["N2"], label='N2_Strain', color = 'blue', marker = 'o')
plt.plot(df["Time"], df["Daf2"], label='Daf2_Mutant', color = 'red', marker = '^')
 
plt.xlabel('Time(Mins)', fontsize = 14) 
plt.ylabel('EC50(mM)', fontsize = 14) 
plt.title('Plot of EC50 against Time for C. Elegans in Ethanol Resistance Test', fontsize = 14) 
plt.grid() 

# Display the legend
plt.legend()

#show the plot
plt.show()


#####for the barplot (EC50 of strains in H2O2 test)
#####for the barplot
bar = pd.read_csv("bar_H2O2.csv")
print(bar)
print(bar.head(3))


# force it to a datafra;e
bf = pd.DataFrame(bar)
print(bf)


# lets continue
plt.figure(figsize=(10, 6))

plt.bar(bf["Strain"], bf["EC50(mM)"], width = 0.50, color = 'blue',)
#plt.xlabel('Time(Mins)', fontsize = 14) 
#plt.xlabel(fontsize = 14) 
plt.ylabel('EC50(mM)', fontsize = 14) 
plt.title('Plot of EC50 against Strain for C. Elegans in H2O2 Resistance Test', fontsize = 14) 
#plt.grid() 
plt.show()


#####for dose response curve (motility response of N2 strains in ethanol test)
#####for dose response curve
Dose1 = pd.read_csv("Dose_Response_Eth.csv")
print(Dose1)

# force it to a datafra;e
ds1 = pd.DataFrame(Dose1)
print(ds1)

# lets make the plot
plt.figure(figsize=(10, 6))

plt.plot(ds1["EtOH"], ds1["10min"], label='10min', color = 'blue', marker = 'o')
plt.plot(ds1["EtOH"], ds1["20min"], label='20min', color = 'r', marker = 'o')
plt.plot(ds1["EtOH"], ds1["30min"], label='30min', color = 'y', marker = 'o')
plt.plot(ds1["EtOH"], ds1["40min"], label='40min', color = 'c', marker = 'o')
plt.plot(ds1["EtOH"], ds1["50min"], label='50min', color = 'k', marker = 'o')
plt.plot(ds1["EtOH"], ds1["60min"], label='60min', color = 'm', marker = 'o')
 
#plt.xlabel('Time(Mins)', fontsize = 14) 
#plt.ylabel('EC50(mM)', fontsize = 14) 
#plt.title('Plot of EC50 against Time for C. Elegans in Ethanol Resistance Test', fontsize = 14) 
plt.grid() 

# Display the legend
plt.legend()

#show the plot
plt.show()



#####for dose response curve (motility response of Daf-2 strains in ethanol test)
#####for dose response curve
Dose2 = pd.read_csv("Dose_Response_Peroxide.csv")
print(Dose2)

# force it to a datafra;e
ds2 = pd.DataFrame(Dose2)
print(ds2)

# lets make the plot
plt.figure(figsize=(10, 6))

plt.plot(ds2["EtOH"], ds2["10min"], label='10min', color = 'blue', marker = 'o')
plt.plot(ds2["EtOH"], ds2["20min"], label='20min', color = 'r', marker = 'o')
plt.plot(ds2["EtOH"], ds2["30min"], label='30min', color = 'y', marker = 'o')
plt.plot(ds2["EtOH"], ds2["40min"], label='40min', color = 'c', marker = 'o')
plt.plot(ds2["EtOH"], ds2["50min"], label='50min', color = 'k', marker = 'o')
plt.plot(ds2["EtOH"], ds2["60min"], label='60min', color = 'm', marker = 'o')
 
#plt.xlabel('Time(Mins)', fontsize = 14) 
#plt.ylabel('EC50(mM)', fontsize = 14) 
#plt.title('Plot of EC50 against Time for C. Elegans in Ethanol Resistance Test', fontsize = 14) 
plt.grid() 

# Display the legend
plt.legend()

#show the plot
plt.show()
