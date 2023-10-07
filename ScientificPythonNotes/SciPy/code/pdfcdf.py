import numpy as np
from scipy.stats import chi2

import matplotlib.pyplot as plt


def cdf():

 #full range
 chisqval=np.arange(0,1000,0.01)
 
 #choose some number of degrees of freedom
 dof=5
 cdf=chi2.cdf(chisqval,dof)
 
 #list of degrees of freedom
 dof=[5,10,20]
 
 #a subset of chisq values
 
 chisq=np.arange(0,50,0.1)
 
 #a for-loop plotting the CDF for different degrees of freedom
 for i in range(len(dof)):
  plt.plot(chisq,chi2.cdf(chisq,dof[i]),label=r'$\nu$ = {0:d}'.format(dof[i]))
  
 #making the plot look nicer
 plt.legend(loc='best')
 plt.xlabel('$\chi^{2}$',fontsize=14)
 plt.ylabel('$CDF(\chi^{2})$',fontsize=14)

 plt.show()

def pdf():


 #full range
 chisqval=np.arange(0,1000,0.01)
 
 #choose some number of degrees of freedom
 dof=5
 cdf=chi2.cdf(chisqval,dof)
 
 #list of degrees of freedom
 dof=[5,10,20]
 
 #a subset of chisq values
 
 chisq=np.arange(0,50,0.1)
 
 #a for-loop plotting the CDF for different degrees of freedom
 for i in range(len(dof)):
  plt.plot(chisq,1-chi2.cdf(chisq,dof[i]),label=r'$\nu$ = {0:d}'.format(dof[i]))
  
 #making the plot look nicer
 plt.legend(loc='best')
 plt.xlabel('$\chi^{2}$',fontsize=14)
 plt.ylabel('$p value(\chi^{2})$',fontsize=14)

 plt.show()


def norm_pdf():


 bins=np.arange(-40,40,0.01)
 PDF=norm.pdf(bins,loc=np.pi,scale=2*np.pi) #generates PDF in bins

 fig, ax  = plt.subplots()

 ax.plot(bins,PDF)
 ax.set_ylabel("PDF")

 #initialize some range of chisquared values
 chisqval=np.arange(0,1000,0.01) 

#dof 
# chispdf=chi2.pdf(chisqval,dof)

 dof=[5,10,20]

 chisq=np.arange(0,50,0.1)
 for i in range(len(dof)):
  plt.plot(chisq,chi2.pdf(chisq,dof[i]),label=r'$\nu$ = {0:d}'.format(dof[i]))

 plt.legend(loc='best')

 plt.xlabel('$\chi^{2}$',fontsize=14)
 #plt.ylabel(plt.ylabel('$PDF(\chi^{2})$',fontsize=14))
 plt.show()

def nsigmalim(nsig=3):

# derives the 68, 95, 99.7, etc rules --> false alarm probability for gaussian statistics

 import scipy.integrate as integrate

 result=integrate.quad(lambda x: np.e**(-0.5*x**2)/np.sqrt(2*np.pi),-nsig,nsig)

 return result[0]

 print(result[0])

def tdist():

 from scipy.stats import t
 from scipy.stats import norm


#t distribution PDF


 x=np.linspace(-5,5,100)

 dof=[2,5,10,1000]

#to apply some other normalization
 maxt=1;maxnorm=1

 for i in range(len(dof)):

   plt.plot(x,t.pdf(x,dof[i])/maxt,label=r't-dist, $\nu$ = {0:d}'.format(dof[i]))


#Now, plotting a Gaussian distribution
 plt.plot(x,norm.pdf(x)/maxnorm,ls='-.',label='Gaussian Distribution')

 plt.xlabel('x')
 plt.ylabel('PDF')
 plt.yscale('log')
 plt.title('t-distribution vs. Normal Distribution')

 plt.legend(loc='best')

 plt.ylim(1e-5,0.5)
 plt.show()


def tpenalty(sep=2,sigma=5,source=True):


 from scipy.stats import t
 from scipy.stats import norm 


 res_el=2*np.pi*sep

 #res_el=np.floor(res_el)


 if source:

  ss_corr=np.sqrt(1+1/(res_el))
  penalty = t.ppf(norm.cdf(sigma),res_el-2)*ss_corr/sigma

 else:
  
  ss_corr=np.sqrt(1+1/res_el)
  penalty = t.ppf(norm.cdf(sigma),res_el-1)*ss_corr/sigma

 print('penalty is ',penalty)
 return penalty
