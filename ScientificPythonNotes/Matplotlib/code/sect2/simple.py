import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator,AutoMinorLocator

def run():


 CO2concentration=np.array([289,288,291,295,294,298,297,299,310,317,325,338,354,370,390.1,401,420]) #roughly estimated from NOAA

 CO2years=np.array([1700,1750,1800,1850,1875,1900,1925,1950,1960,1970,1980,1990,2000,2005,2010,2015,2020])

 sval=0.25 #add some noise
 pirate_attacks=5000*np.exp(-1*(CO2years-CO2years[0])/150)*(1+sval*0.25*np.random.randn(len(CO2years)))

 fig,axes=plt.subplots(figsize=(9,9))

 #now fit an exponential to the pirate attacks

 piratefit=np.polyfit(CO2years,np.log(pirate_attacks),1)

 atest=np.exp(piratefit[1])
 btest=piratefit[0]
 #print(atest,btest,result[1])
 #exit()

 axes.scatter(CO2years,CO2concentration,marker='o',s=250,color='darkblue',edgecolor='black',alpha=0.9,label='CO2')
 axes.set_xlabel('Year',fontsize=14)
 axes.set_ylabel(r'CO$_{\rm 2}$ Concentration (PPM)',fontsize=16,color='darkblue')

 axes.set_ylim(275,425)

 axes.tick_params(labelbottom=True,labeltop=False,top=False,bottom=True,left=True,right=False)
 axes.tick_params(which='both',width=1.5,direction='in',labelsize='large')
 axes.tick_params(which='major',length=6)
 axes.tick_params(which='minor',length=3)
 #axes.tick_params(labeltop=True,top=True)
 axes.yaxis.set_ticks_position('both')
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.yaxis.set_minor_locator(AutoMinorLocator(5))

 for axl in ['top','bottom','left','right']:
   axes.spines[axl].set_linewidth(2)
 plt.show()
