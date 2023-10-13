import matplotlib.pyplot as plt
import numpy as np

#simple vertically stacked panels
def ex2_1():
 xarray=np.arange(20)   #an array of numbers from 0 to 19
 yarray=np.arange(20)+3*np.random.randn(20)
 #y is same as x EXCEPT now we vary the value +/- some random number about x
 
 a,b=np.polyfit(xarray,yarray,1)
 #a polynomial fit of degree one look up the documentation if you are curious
 
 yarray2=(np.arange(20))**2.+20*np.random.randn(20)
 
 #polynomial of degree two
 a2,b2,c2=np.polyfit(xarray,yarray2,2)

 poly=np.poly1d(np.polyfit(xarray,yarray2,2))
 #a convenience class to write the polynomial fit

 fig,axes=plt.subplots(2,1)
 axes[0].plot(xarray,xarray*a+b,label='Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a,b))
 axes[0].scatter(xarray,yarray,marker='o',s=150,alpha=0.7,label=r'$Random_{num}$')
 axes[0].legend(loc='best')

 axes[1].plot(xarray,poly(xarray),c='tab:green',label=r'Quadratic fit with y = {0:.2f}*$x^2$+{1:.2f}*$x$+{2:.2f}'.format(a2,b2,c2))

 axes[1].scatter(xarray,yarray2,marker='s',c='orange',s=50, label=r'$Random_{num}$, quadratic')
 axes[1].legend(loc='best',fontsize='xx-small')
 
 plt.show()

#vertically stacked panels
def ex2_2a():
 xarray=np.arange(20)   #an array of numbers from 0 to 19
 yarray=np.arange(20)+3*np.random.randn(20)
 #y is same as x EXCEPT now we vary the value +/- some random number about x
 
 a,b=np.polyfit(xarray,yarray,1)
 #a polynomial fit of degree one look up the documentation if you are curious
 
 yarray2=(np.arange(20))**2.+20*np.random.randn(20)
 
 #polynomial of degree two
 a2,b2,c2=np.polyfit(xarray,yarray2,2)

 poly=np.poly1d(np.polyfit(xarray,yarray2,2))
 #a convenience class to write the polynomial fit

 fig,axes=plt.subplots(2,1)

 fig.subplots_adjust(hspace=0.5)
 axes[0].plot(xarray,xarray*a+b,label='Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a,b))
 axes[0].scatter(xarray,yarray,marker='o',s=150,alpha=0.7,label=r'$Random_{num}$')
 axes[0].legend(loc='best')

 axes[1].plot(xarray,poly(xarray),c='tab:green',label=r'Quadratic fit with y = {0:.2f}*$x^2$+{1:.2f}*$x$+{2:.2f}'.format(a2,b2,c2))

 axes[1].scatter(xarray,yarray2,marker='s',c='orange',s=50, label=r'$Random_{num}$, quadratic')
 axes[1].legend(loc='best',fontsize='small')

 for i in range(len(axes)):
 
  axes[i].set_xlabel('Initial $X_{Array}$',font='Verdana',size=14,color='black',weight='bold')
  axes[i].set_ylabel(r'Output,$Y_{Array, random}$',font='Verdana',size=14,color='black',weight='bold')
 
 plt.show()

#side-by-side panels
def ex2_2b():
 xarray=np.arange(20)   #an array of numbers from 0 to 19
 yarray=np.arange(20)+3*np.random.randn(20)
 #y is same as x EXCEPT now we vary the value +/- some random number about x
 
 a,b=np.polyfit(xarray,yarray,1)
 #a polynomial fit of degree one look up the documentation if you are curious
 
 yarray2=(np.arange(20))**2.+20*np.random.randn(20)
 
 #polynomial of degree two
 a2,b2,c2=np.polyfit(xarray,yarray2,2)

 poly=np.poly1d(np.polyfit(xarray,yarray2,2))
 #a convenience class to write the polynomial fit

 fig,axes=plt.subplots(1,2,figsize=(9.6,4.8)) 
#the default width is 6.4 inches by 4.8 inches, here increase width by 50%

 fig.subplots_adjust(wspace=0.325)
 axes[0].plot(xarray,xarray*a+b,label='Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a,b))
 axes[0].scatter(xarray,yarray,marker='o',s=150,alpha=0.7,label=r'$Random_{num}$')
 axes[0].legend(loc='upper left',fontsize='x-small',handlelength=1,markerscale=0.85)

 axes[1].plot(xarray,poly(xarray),c='tab:green',label=r'Quadratic fit with y = {0:.2f}*$x^2$+{1:.2f}*$x$+{2:.2f}'.format(a2,b2,c2))

 axes[1].scatter(xarray,yarray2,marker='s',c='orange',s=50, label=r'$Random_{num}$, quadratic')
 axes[1].legend(loc='upper left',fontsize='x-small',handlelength=1)

 for i in range(len(axes)):
 
  axes[i].set_xlabel('Initial $X_{Array}$',font='Verdana',size=14,color='black',weight='bold')
  axes[i].set_ylabel(r'Output,$Y_{Array, random}$',font='Verdana',size=14,color='black',weight='bold')
 
 plt.show()

def ex2_2c():

 #from matplotlib.ticker import FormatStrFormatter
 from matplotlib import ticker

 xarray=np.arange(20)   #an array of numbers from 0 to 19
 yarray=np.arange(20)+3*np.random.randn(20)
 #y is same as x EXCEPT now we vary the value +/- some random number about x
 
 a,b=np.polyfit(xarray,yarray,1)
 #a polynomial fit of degree one look up the documentation if you are curious
 
 yarray2=(np.arange(20))**2.+20*np.random.randn(20)
 
 #polynomial of degree two
 a2,b2,c2=np.polyfit(xarray,yarray2,2)

 poly=np.poly1d(np.polyfit(xarray,yarray2,2))
 #a convenience class to write the polynomial fit
 
 standardsize=np.array((6.4,4.8))
 scaleval=1.25
 newsize=list(scaleval*standardsize)

 fig,axes=plt.subplots(2,1,figsize=newsize) 
#the default width is 6.4 inches by 4.8 inches, here increase width by 25% using variables

 axes[0].yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
 axes[1].yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

 fig.subplots_adjust(hspace=0)
 axes[0].plot(xarray,xarray*a+b,label='Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a,b))
 axes[0].scatter(xarray,yarray,marker='o',s=150,alpha=0.7,label=r'$Random_{num}$')
 axes[0].legend(loc='upper left',fontsize='x-small',handlelength=1,markerscale=0.85)

 axes[1].plot(xarray,poly(xarray),c='tab:green',label=r'Quadratic fit with y = {0:.2f}*$x^2$+{1:.2f}*$x$+{2:.2f}'.format(a2,b2,c2))

 axes[1].scatter(xarray,yarray2,marker='s',c='orange',s=50, label=r'$Random_{num}$, quadratic')
 axes[1].legend(loc='upper left',fontsize='x-small',handlelength=1)

 for i in range(len(axes)):

  if i > 1: 
   axes[i].set_xlabel('Initial $X_{Array}$',font='Verdana',size=14,color='black',weight='bold')
  axes[i].set_ylabel(r'Output,$Y_{Array, random}$',font='Verdana',size=14,color='black',weight='bold')
 
 plt.show()

#making 4 panels
def ex2_2dbk():

 #from matplotlib.ticker import FormatStrFormatter
 from matplotlib import ticker

 xarray=np.arange(20)   #an array of numbers from 0 to 19

#Panel 1 determination
 yarray=np.arange(20)+3*np.random.randn(20)
 #y is same as x EXCEPT now we vary the value +/- some random number about x
 
 a,b=np.polyfit(xarray,yarray,1)
 #a polynomial fit of degree one look up the documentation if you are curious

#Panel 2 determination 
 yarray2=(np.arange(20))**2.+20*np.random.randn(20)
 
 #polynomial of degree two
 a2,b2,c2=np.polyfit(xarray,yarray2,2)

 poly=np.poly1d(np.polyfit(xarray,yarray2,2))
 #a convenience class to write the polynomial fit


#Panel 3 determination

 yarray3=(np.arange(20))**2.+40*np.random.randn(20)
 
 #polynomial of degree two
 a3,b3,c3=np.polyfit(xarray,yarray3,2)

 poly2=np.poly1d(np.polyfit(xarray,yarray3,2))
 #a convenience class to write the polynomial fit


#Panel 1 determination
 yarray4=np.arange(20)+1.5*np.random.randn(20)
 #y is same as x EXCEPT now we vary the value +/- some random number about x
 
 a4,b4=np.polyfit(xarray,yarray4,1)
 #a polynomial fit of degree one look up the documentation if you are curious

 
 
 standardsize=np.array((6.4,4.8))
 scaleval=2
 newsize=list(scaleval*standardsize)

 fig,axes=plt.subplots(2,2,figsize=newsize,sharex=True)
#,sharey=True) 
 fig.subplots_adjust(hspace=0,wspace=0)

#the default width is 6.4 inches by 4.8 inches, here increase width by 25% using variables
 labels_fits = ['Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a,b),r'Quadratic fit with y = {0:.2f}*$x^2$+{1:.2f}*$x$+{2:.2f}'.format(a2,b2,c2),
             r'Second Quadratic fit with y = {0:.2f}*$x^2$+{1:.2f}*$x$+{2:.2f}'.format(a3,b3,c3), 'Second Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a4,b4)]

 labels_data=[r'$Random_{num}$',r'$Random_{num}$, quadratic',r'$Random_{num}$, quadratic (v2)',r'$Random_{num}$ (v2)']

 colors_data=['tab:blue','orange','lime','cyan']
 colors_fit=['tab:blue','tab:green','tab:brown','tab:gray']

 sizes_data=[150,50,100,75]
 marker_data=['o','s','^','X']
 alphas_data=[0.7,1,0.6,0.5]


 #ylabelpos=["left","right","left","right"] 

 axes[0,0].plot(xarray,xarray*a+b,label=labels_fits[0],c=colors_fit[0])
 axes[0,0].scatter(xarray,yarray,marker=marker_data[0],c=colors_data[0],s=sizes_data[0],alpha=alphas_data[0],label=labels_data[0])
 axes[0,0].legend(loc='upper left',fontsize='x-small',handlelength=1,markerscale=0.85)
 #axes[0,0].yaxis_tick_left()
 #axes[0,0].yaxis_set_label_position("left")


 axes[0,1].plot(xarray,xarray*a4+b4,c=colors_fit[3],label=labels_fits[3])
 axes[0,1].scatter(xarray,yarray4,marker=marker_data[3],c=colors_data[3],s=sizes_data[3], alpha=alphas_data[3],label=r'$Random_{num}$, quadratic')
 axes[0,1].legend(loc='upper left',fontsize='x-small',handlelength=1)
 #axes[0,1].yaxis_tick_right()
 #axes[0,1].yaxis_set_label_position("right")

 #axes[1,1].plot(xarray,xarray*a+b,label=labels_fits[0],c=colors_fit[0])
 #axes[1,1].scatter(xarray,yarray,marker=marker_data[0],c=colors_data[0],s=sizes_data[0],alpha=alphas_data[0],label=labels_data[0])
 #axes[1,1].legend(loc='upper left',fontsize='x-small',handlelength=1,markerscale=0.85)

 axes[1,0].plot(xarray,poly(xarray),label=labels_fits[1],c=colors_fit[1])
 axes[1,0].scatter(xarray,yarray2,marker=marker_data[1],c=colors_data[1],s=sizes_data[1],alpha=alphas_data[1],label=labels_data[1])
 axes[1,0].legend(loc='upper left',fontsize='x-small',handlelength=1,markerscale=0.85)
 #axes[1,0].yaxis_tick_left()
 #axes[1,0].yaxis_set_label_position("left")

 axes[1,1].plot(xarray,poly2(xarray),c=colors_fit[2],label=labels_fits[2])
 axes[1,1].scatter(xarray,yarray3,marker=marker_data[2],c=colors_data[2],s=sizes_data[2], label=labels_data[2],alpha=alphas_data[2])
 axes[1,1].legend(loc='upper left',fontsize='x-small',handlelength=1)
 #axes[1,1].yaxis_tick_right()
 #axes[1,1].yaxis_set_label_position("right")

#continue after here ... 5:26pm 6/12

 for ax in [axes[0,1],axes[1,1]]:
#  ax.set_yticks([])
 #for ax in [axes[0,1],axes[1,1]]:
  ax.yaxis.tick_right()
  ax.yaxis.set_tick_params(labelright='on',labelleft=False)
 #for i in range(len(axes)):
# for ax in axes.flat:
#  ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
 
# axes[0].yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
# axes[1].yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))


# for i in range(len(axes)):
#
#  if i > 1: 
#   axes[i].set_xlabel('Initial $X_{Array}$',font='Verdana',size=14,color='black',weight='bold')
#   axes[i].set_ylabel(r'Output,$Y_{Array, random}$',font='Verdana',size=14,color='black',weight='bold')
  
# for ax in fig.get_axes():
 for i in range(len(axes)):
#   axes.yaxis.set_label_position(ylabelpos[i])
  ax.label_outer()
 plt.show()


#making 4 panels
def ex2_2d():

 #from matplotlib.ticker import FormatStrFormatter
 from matplotlib import ticker

 xarray=np.arange(20)   #an array of numbers from 0 to 19

#Panel 1 determination
 yarray=np.arange(20)+3*np.random.randn(20)
 #y is same as x EXCEPT now we vary the value +/- some random number about x
 
 a,b=np.polyfit(xarray,yarray,1)
 #a polynomial fit of degree one look up the documentation if you are curious

#Panel 2 determination 
 yarray2=(np.arange(20))**2.+20*np.random.randn(20)
 
 #polynomial of degree two
 a2,b2,c2=np.polyfit(xarray,yarray2,2)

 poly=np.poly1d(np.polyfit(xarray,yarray2,2))
 #a convenience class to write the polynomial fit


#Panel 3 determination

 yarray3=(np.arange(20))**2.+40*np.random.randn(20)
 
 #polynomial of degree two
 a3,b3,c3=np.polyfit(xarray,yarray3,2)

 poly2=np.poly1d(np.polyfit(xarray,yarray3,2))
 #a convenience class to write the polynomial fit


#Panel 4 determination
 yarray4=np.arange(20)+1.5*np.random.randn(20)
 #y is same as x EXCEPT now we vary the value +/- some random number about x
 
 a4,b4=np.polyfit(xarray,yarray4,1)
 #a polynomial fit of degree one look up the documentation if you are curious

 
 
 standardsize=np.array((6.4,4.8))
 scaleval=2
 newsize=list(scaleval*standardsize)

#the default width is 6.4 inches by 4.8 inches, here increase width by 25% using variables
 fig,axes=plt.subplots(2,2,figsize=newsize,sharex=True)
#,sharey=True) 
 fig.subplots_adjust(hspace=0,wspace=0)

# turn the fit labels, fit data points, fit colors, data point colors, data point sizes, ...
## data markers (symbols), data alphas ... all to lists

 labels_fits = ['Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a,b),'Second Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a4,b4),
             r'Quadratic fit with y = {0:.2f}*$x^2$+{1:.2f}*$x$+{2:.2f}'.format(a2,b2,c2), r'Second Quadratic fit with y = {0:.2f}*$x^2$+{1:.2f}*$x$+{2:.2f}'.format(a3,b3,c3)]

 labels_data=[r'$Random_{num}$',r'$Random_{num}$ (v2)',r'$Random_{num}$, quadratic',r'$Random_{num}$, quadratic (v2)']

 colors_fit=['tab:blue','tab:brown','tab:green','tab:gray']

 colors_data=['tab:blue','lime','orange','cyan']

 sizes_data=[150,50,100,75]
 marker_data=['o','^','s','X']
 alphas_data=[0.7,1,0.6,0.5]

#turn the functional fits into a list

 eq=[xarray*a+b,xarray*a4+b4,poly(xarray),poly2(xarray)]

#turn the generated data arrays into a list
 dataarr=[yarray,yarray4,yarray2,yarray3]

#use python enumerate over axes; flatten axes ... columns first, then rows
# ax represents each iteration of axes (i.e. axes.flat([0]), axes.flat([1]), etc etc
# you advance i as well
 for i,ax in enumerate(axes.flat):
  ax.plot(xarray,eq[i],label=labels_fits[i],c=colors_fit[i])
  ax.scatter(xarray,dataarr[i],marker=marker_data[i],c=colors_data[i],s=sizes_data[i],alpha=alphas_data[i],label=labels_data[i])
  ax.legend(loc='upper left',fontsize='small',handlelength=1,markerscale=0.85)
  ax.set_xlabel('Initial $X_{Array}$',font='Verdana',size=14,color='black',weight='bold')
  ax.set_ylabel(r'Output,$Y_{Array, random}$',font='Verdana',size=14,color='black',weight='bold')

#now, iterate over the subplots on the righthand side only
 for ax in [axes[0,1],axes[1,1]]:
  ax.yaxis.tick_right()
  #ax.yaxis.set_tick_params(labelright='on',labelleft=False) #not needed
  ax.yaxis.set_label_position("right")

#set tick marks to the right for these ,set the labels to the right for these

 plt.show()

#tickmark extravaganzas
def ex2_3a():

 #from matplotlib.ticker import FormatStrFormatter
 from matplotlib import ticker
 from matplotlib.ticker import AutoMinorLocator

 xarray=np.arange(20)   #an array of numbers from 0 to 19

#Panel 1 determination
 yarray=np.arange(20)+3*np.random.randn(20)
 #y is same as x EXCEPT now we vary the value +/- some random number about x
 
 a,b=np.polyfit(xarray,yarray,1)
 #a polynomial fit of degree one look up the documentation if you are curious

#Panel 2 determination 
 yarray2=(np.arange(20))**2.+20*np.random.randn(20)
 
 #polynomial of degree two
 a2,b2,c2=np.polyfit(xarray,yarray2,2)

 poly=np.poly1d(np.polyfit(xarray,yarray2,2))
 #a convenience class to write the polynomial fit


#Panel 3 determination

 yarray3=(np.arange(20))**2.+40*np.random.randn(20)
 
 #polynomial of degree two
 a3,b3,c3=np.polyfit(xarray,yarray3,2)

 poly2=np.poly1d(np.polyfit(xarray,yarray3,2))
 #a convenience class to write the polynomial fit


#Panel 4 determination
 yarray4=np.arange(20)+1.5*np.random.randn(20)
 #y is same as x EXCEPT now we vary the value +/- some random number about x
 
 a4,b4=np.polyfit(xarray,yarray4,1)
 #a polynomial fit of degree one look up the documentation if you are curious

 
 
 standardsize=np.array((6.4,4.8))
 scaleval=2
 newsize=list(scaleval*standardsize)

#the default width is 6.4 inches by 4.8 inches, here increase width by 25% using variables
 fig,axes=plt.subplots(2,2,figsize=newsize,sharex=True)
#,sharey=True) 
 fig.subplots_adjust(hspace=0,wspace=0)

# turn the fit labels, fit data points, fit colors, data point colors, data point sizes, ...
## data markers (symbols), data alphas ... all to lists

 labels_fits = ['Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a,b),'Second Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a4,b4),
             r'Quadratic fit with y = {0:.2f}*$x^2$+{1:.2f}*$x$+{2:.2f}'.format(a2,b2,c2), r'Second Quadratic fit with y = {0:.2f}*$x^2$+{1:.2f}*$x$+{2:.2f}'.format(a3,b3,c3)]

 labels_data=[r'$Random_{num}$',r'$Random_{num}$ (v2)',r'$Random_{num}$, quadratic',r'$Random_{num}$, quadratic (v2)']

 colors_fit=['tab:blue','tab:brown','tab:green','tab:gray']

 colors_data=['tab:blue','lime','orange','cyan']

 sizes_data=[150,50,100,75]
 marker_data=['o','^','s','X']
 alphas_data=[0.7,1,0.6,0.5]

#turn the functional fits into a list

 eq=[xarray*a+b,xarray*a4+b4,poly(xarray),poly2(xarray)]

#turn the generated data arrays into a list
 dataarr=[yarray,yarray4,yarray2,yarray3]

#use python enumerate over axes; flatten axes ... columns first, then rows
# ax represents each iteration of axes (i.e. axes.flat([0]), axes.flat([1]), etc etc
# you advance i as well
 for i,ax in enumerate(axes.flat):
  ax.plot(xarray,eq[i],label=labels_fits[i],c=colors_fit[i])
  ax.scatter(xarray,dataarr[i],marker=marker_data[i],c=colors_data[i],s=sizes_data[i],alpha=alphas_data[i],label=labels_data[i])
  ax.legend(loc='upper left',fontsize='small',handlelength=1,markerscale=0.85)
  ax.set_xlabel('Initial $X_{Array}$',font='Verdana',size=14,color='black',weight='bold')
  ax.set_ylabel(r'Output,$Y_{Array, random}$',font='Verdana',size=14,color='black',weight='bold')

  ax.xaxis.set_minor_locator(AutoMinorLocator(5))
  ax.yaxis.set_minor_locator(AutoMinorLocator(5))
  ax.tick_params(which='both',width=1.5,direction='in',labelsize='large')
  ax.tick_params(which='major',length=6)
  ax.tick_params(which='minor',length=3)

#now, iterate over the subplots on the righthand side only
 for i,ax in enumerate([axes[0,1],axes[1,1]]):
  ax.yaxis.tick_right()
  #ax.yaxis.set_tick_params(labelright='on',labelleft=False) #not needed
  ax.yaxis.set_label_position("right")
  #if i == 0:
  # ax.set_ylabel(r'Output,$Y_{Array, random}$',font='Verdana',color='black',weight='bold',size=16)
  #else:
  # ax.grid(True,linestyle='dotted',color='tab:blue')
  #ax.tick_params(which='major',color='magenta',labelsize='x-large',labelrotation=45,width=3,length=9)

#set tick marks to the right for these ,set the labels to the right for these

 plt.show()

#other formatting + tickmark extravaganzas
def ex2_3b():

 #from matplotlib.ticker import FormatStrFormatter
 from matplotlib import ticker
 from matplotlib.ticker import MultipleLocator,AutoMinorLocator

 xarray=np.arange(20)   #an array of numbers from 0 to 19

#Panel 1 determination
 yarray=np.arange(20)+3*np.random.randn(20)
 #y is same as x EXCEPT now we vary the value +/- some random number about x
 
 a,b=np.polyfit(xarray,yarray,1)
 #a polynomial fit of degree one look up the documentation if you are curious

#Panel 2 determination 
 yarray2=(np.arange(20))**2.+20*np.random.randn(20)
 
 #polynomial of degree two
 a2,b2,c2=np.polyfit(xarray,yarray2,2)

 poly=np.poly1d(np.polyfit(xarray,yarray2,2))
 #a convenience class to write the polynomial fit


#Panel 3 determination

 yarray3=(np.arange(20))**2.+40*np.random.randn(20)
 
 #polynomial of degree two
 a3,b3,c3=np.polyfit(xarray,yarray3,2)

 poly2=np.poly1d(np.polyfit(xarray,yarray3,2))
 #a convenience class to write the polynomial fit


#Panel 4 determination
 yarray4=np.arange(20)+1.5*np.random.randn(20)
 #y is same as x EXCEPT now we vary the value +/- some random number about x
 
 a4,b4=np.polyfit(xarray,yarray4,1)
 #a polynomial fit of degree one look up the documentation if you are curious

 
 
 standardsize=np.array((6.4,4.8))
 scaleval=2
 newsize=list(scaleval*standardsize)

#the default width is 6.4 inches by 4.8 inches, here increase width by 25% using variables
 fig,axes=plt.subplots(2,2,figsize=newsize,sharex=True)
#,sharey=True) 
 fig.subplots_adjust(hspace=0,wspace=0)

# turn the fit labels, fit data points, fit colors, data point colors, data point sizes, ...
## data markers (symbols), data alphas ... all to lists

 labels_fits = ['Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a,b),'Second Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a4,b4),
             r'Quadratic fit with y = {0:.2f}*$x^2$+{1:.2f}*$x$+{2:.2f}'.format(a2,b2,c2), r'Second Quadratic fit with y = {0:.2f}*$x^2$+{1:.2f}*$x$+{2:.2f}'.format(a3,b3,c3)]

 labels_data=[r'$Random_{num}$',r'$Random_{num}$ (v2)',r'$Random_{num}$, quadratic',r'$Random_{num}$, quadratic (v2)']

 colors_fit=['tab:blue','tab:brown','tab:green','tab:gray']

 colors_data=['tab:blue','lime','orange','cyan']

 sizes_data=[150,50,100,75]
 marker_data=['o','^','s','X']
 alphas_data=[0.7,1,0.6,0.5]

#turn the functional fits into a list

 eq=[xarray*a+b,xarray*a4+b4,poly(xarray),poly2(xarray)]

#turn the generated data arrays into a list
 dataarr=[yarray,yarray4,yarray2,yarray3]

#use python enumerate over axes; flatten axes ... columns first, then rows
# ax represents each iteration of axes (i.e. axes.flat([0]), axes.flat([1]), etc etc
# you advance i as well
 for i,ax in enumerate(axes.flat):
  ax.plot(xarray,eq[i],label=labels_fits[i],c=colors_fit[i])
  ax.scatter(xarray,dataarr[i],marker=marker_data[i],c=colors_data[i],s=sizes_data[i],alpha=alphas_data[i],label=labels_data[i])
  ax.legend(loc='upper left',fontsize='small',handlelength=1,markerscale=0.85)
  ax.set_xlabel('Initial $X_{Array}$',font='Verdana',size=14,color='black',weight='bold')
  ax.set_ylabel(r'Output,$Y_{Array, random}$',font='Verdana',size=14,color='black',weight='bold')

  ax.xaxis.set_minor_locator(AutoMinorLocator(5))
  ax.yaxis.set_minor_locator(AutoMinorLocator(5))
  ax.tick_params(which='both',width=1.5,direction='in',labelsize='large')
  ax.tick_params(which='major',length=6)
  ax.tick_params(which='minor',length=3)

#now, iterate over the subplots on the righthand side only
 for i,ax in enumerate([axes[0,1],axes[1,1]]):
  ax.yaxis.tick_right()
  #ax.yaxis.set_tick_params(labelright=True,labelleft=False) #not needed
  ax.yaxis.set_label_position("right")
  if i == 0:
   ax.set_ylabel(r'Output,$Y_{Array, random}$',font='Verdana',color='black',weight='bold',size=16)
  else:
   ax.grid(True,linestyle='dotted',color='tab:blue')
  ax.tick_params(which='major',color='magenta',labelsize='x-large',labelrotation=45,width=3,length=9)

#set tick marks to the right for these ,set the labels to the right for these

 plt.show()


def ex2_4():

 from matplotlib import ticker
 from matplotlib.ticker import MultipleLocator,AutoMinorLocator

 xarray=np.arange(20)   #an array of numbers from 0 to 19

# in this example, we are just going to do one linear plot and one quadratic plot
#Panel 1 determination
 yarray=np.arange(20)+3*np.random.randn(20)

 #y is same as x EXCEPT now we vary the value +/- some random number about x
 
 a,b=np.polyfit(xarray,yarray,1)
 #a polynomial fit of degree one look up the documentation if you are curious

#Panel 2 determination 
 yarray2=(np.arange(20))**2.+20*np.random.randn(20)

#this is equivalent to yarray2[where(yarray2 le 0)] > 0.01 in IDL 
  #it basically sets to 0.01 any value from the random number generator that is less than 0
 (yarray2 > 0.0).choose(yarray2,0.01)

 #polynomial of degree two
 a2,b2,c2=np.polyfit(xarray,yarray2,2)

 poly=np.poly1d(np.polyfit(xarray,yarray2,2))
 #a convenience class to write the polynomial fit


 standardsize=np.array((6.4,4.8))
 scaleval=2
 newsize=list(scaleval*standardsize)

#the default width is 6.4 inches by 4.8 inches, here increase width by 25% using variables
 fig,axes=plt.subplots(1,2,figsize=newsize)
 fig.subplots_adjust(hspace=0.25,wspace=0.25)

# turn the fit labels, fit data points, fit colors, data point colors, data point sizes, ...
## data markers (symbols), data alphas ... all to lists

 labels_fits = ['Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a,b),
             r'Quadratic fit with y = {0:.2f}*$x^2$+{1:.2f}*$x$+{2:.2f}'.format(a2,b2,c2)]

 labels_data=[r'$Random_{num}$',r'$Random_{num}$, quadratic']

 colors_fit=['tab:blue','tab:green','tab:gray']

 colors_data=['tab:blue','orange']

 sizes_data=[150,100]
 marker_data=['o','s']
 alphas_data=[0.7,0.6]

#turn the functional fits into a list

 eq=[xarray*a+b,poly(xarray)]

#turn the generated data arrays into a list
 dataarr=[yarray,yarray2]

#use python enumerate over axes; flatten axes ... columns first, then rows
# ax represents each iteration of axes (i.e. axes.flat([0]), axes.flat([1]), etc etc
# you advance i as well
 for i,ax in enumerate(axes.flat):
  ax.plot(xarray,eq[i],label=labels_fits[i],c=colors_fit[i])
  ax.scatter(xarray,dataarr[i],marker=marker_data[i],c=colors_data[i],s=sizes_data[i],alpha=alphas_data[i],label=labels_data[i])
  ax.legend(loc='upper left',fontsize='small',handlelength=1,markerscale=0.85)
  ax.set_xlabel('Initial $X_{Array}$',font='Verdana',size=14,color='black',weight='bold')
  ax.set_ylabel(r'Output,$Y_{Array, random}$',font='Verdana',size=14,color='black',weight='bold')

  ax.tick_params(which='both',direction='in',labelsize=16)
#'small')
  ax.tick_params(which='major',length=7,width=3)
  ax.tick_params(which='minor',length=3.5,width=1.5)
  ax.xaxis.set_minor_locator(AutoMinorLocator(5))

 
  if i == 0:
   ax.set_ylabel(r'Output,$Y_{Array, random}$',font='Verdana',color='black',weight='bold',size=14)
   ax.set_ylim(-7,27)
   ax.set_yscale('linear')
   ax.yaxis.set_minor_locator(AutoMinorLocator(5))
  else:
   ax.set_ylim(0.5,500)
   ax.set_yscale('log')
   ax.yaxis.set_minor_locator(ticker.LogLocator(base=10,subs=np.arange(1,10)*.1))

  ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

# one way to thicken spines of the plot
  for axl in ['top','bottom','left','right']:
   ax.spines[axl].set_linewidth(2)
#other way 
  #plt.setp(ax.spines.values(),linewidth=2)
  #plt.setp(ax.spines.values(),visible=False)
  #plt.getp(ax.spines.values())

  #ax.xaxis.label.set_fontsize(18)
  #ax.yaxis.label.set_fontsize(18)
 plt.show()

def ex2_5():

 from matplotlib.ticker import MultipleLocator,AutoMinorLocator

 CO2concentration=np.array([289,288,291,295,294,298,297,299,310,317,325,338,354,370,390.1,401,420]) #roughly estimated from NOAA
 CO2years=np.array([1700,1750,1800,1850,1875,1900,1925,1950,1960,1970,1980,1990,2000,2005,2010,2015,2020])

 sval=0.25 #add some noise to the number of pirate attacks/year
 pirate_attacks=5000*np.exp(-1*(CO2years-CO2years[0])/150)*(1+sval*0.25*np.random.randn(len(CO2years)))

 fig,axes=plt.subplots(figsize=(8,7))

 #now fit an exponential to the pirate attacks

 piratefit=np.polyfit(CO2years,np.log(pirate_attacks),1)

 atest=np.exp(piratefit[1])
 btest=piratefit[0]

 axes.scatter(CO2years,CO2concentration,marker='o',s=250,color='darkblue',edgecolor='black',alpha=0.9,label='CO2')
 axes.set_xlabel('Year',fontsize=14)
 axes.set_ylabel(r'CO$_{\rm 2}$ Concentration (PPM)',fontsize=16,color='darkblue')

 axes.set_ylim(275,425)

 axes.tick_params(which='both',width=1.5,direction='in',labelsize=14)
 axes.tick_params(which='major',length=7,width=3)
 axes.tick_params(which='minor',length=3.5,width=1.5)

#this makes the labels appear at top and bottom
 axes.tick_params(labeltop=False,labelbottom=True,bottom=True,top=True,labelright=True)

 axes.xaxis.set_ticks_position('both')
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.yaxis.set_ticks_position('both')
 axes.yaxis.set_minor_locator(AutoMinorLocator(5))

#thicken the spines
 for axl in ['top','bottom','left','right']:
   axes.spines[axl].set_linewidth(2)

####THIS IS THE KEY LINE

 axes2=axes.twinx()

 axes2.tick_params(which='both',direction='in',labelsize=14)
 axes2.set_ylim(0,5100)

 axes2.scatter(CO2years,pirate_attacks,marker='s',s=150,color='tab:green',edgecolor='black',alpha=0.9)

 axes2.plot(CO2years,atest*np.exp(btest*CO2years),ls='-',label='Exponential Fit to Pirate Attacks/Year',color='tab:green',)
 axes2.set_ylabel(r'Pirate Attacks Per Year (Source: The Pirate News Network)',fontsize=14,color='darkgreen',alpha=0.9)

 axes2.legend(loc=[0.25,0.9],fontsize='large',markerscale=0.85)


 axes2.tick_params(which='both',width=1.5,direction='in',labelsize=14)

 axes2.tick_params(which='major',length=7,width=3)
 axes2.tick_params(which='minor',length=3.5,width=1.5)
 axes2.xaxis.set_ticks_position('both')
 axes2.xaxis.set_minor_locator(AutoMinorLocator(5))

 axes2.yaxis.set_ticks_position('right')
 axes2.yaxis.set_minor_locator(AutoMinorLocator(5))

 axes2.tick_params(labeltop=True)

 #fig.tight_layout() #note: see what this does
 plt.show()

def ex2_6():

 from matplotlib.ticker import MultipleLocator,AutoMinorLocator
 from scipy import interpolate
 
 #array of angular separations

 file_in='./files/broadband_contrast.txt'

 dstar=40 #assume a distance of 40 pc
 dtypes={'names':('angsep','contrast'), 'formats':(np.float64,np.float64)}

 a = np.loadtxt(file_in,usecols=range(2),dtype=dtypes)
 #a=np.loadtxt(file_in)

 ang_sep=a['angsep']
 contrast_5sig=a['contrast']

 nhour=2
 scalefact=(nhour*3600/1800.)**(0.5)

 fscexao=interpolate.interp1d(ang_sep,contrast_5sig/scalefact)

 ang_sep_new=np.arange(0.15,0.9,0.05)
 contrast_5sig_twohours=fscexao(ang_sep_new)


 #approximate performance for Keck/NIRC2

 ang_sep_keck=np.array([0.15,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
 contrast_keck=np.array([1e-2,1e-3,3e-4,1e-4,3e-5,1.5e-5,1.25e-5,1e-5,8e-6])

 fkeck=interpolate.interp1d(ang_sep_keck,contrast_keck)
 #print(fkeck)
 #exit()
 contrast_5sig_keck=fkeck(ang_sep_new)
 #estimate for new performance, SCExAO

 improve_fact=4
 contrast_5sig_twohours_new=contrast_5sig_twohours/improve_fact
 igood=np.where(ang_sep_new < 0.25)
 contrast_5sig_twohours_new[igood]/=(3-ang_sep_new[igood]*8.)
 ibad=np.where(ang_sep_new > 0.7)
 contrast_5sig_twohours_new[ibad]*=(1+1.75*ang_sep_new[ibad]-.7)

 print(ang_sep)

 fig,axes=plt.subplots(figsize=(9,5))

 axes.plot(ang_sep_new,contrast_5sig_keck,linewidth=4,markersize=np.sqrt(50),color='tab:blue',label='Keck/NIRC2')
 axes.plot(ang_sep_new,contrast_5sig_twohours,linewidth=5,color='magenta',label='SCExAO/CHARIS (Early 2023 Performance)')
 axes.plot(ang_sep_new,contrast_5sig_twohours_new,linewidth=4,ls='-.',color='tab:green',label='SCExAO/CHARIS (2024 Performance, predicted)')

 axes.set_yscale('log')
 axes.set_ylim(1e-7,1e-3)
 axes.set_xlim(0.1,0.9)

#note: setting to 'both' instead of 'bottom' would draw tick marks at top of plot:
   #would mismatch with secondary axis tick marks
 axes.xaxis.set_ticks_position('bottom')

 axes.tick_params(labeltop=False,labelbottom=True,labelright=True,labelleft=True)
 axes.tick_params(which='both',direction='in',labelsize=14)
 axes.tick_params(which='major',length=10,width=1.5)
 axes.tick_params(which='minor',length=5,width=1.5)
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 #log scale automatically sets minor tick marks to be reasonable here

#note: setting this to 'both' would make contrast numbers appear on left and right side of plot
 axes.yaxis.set_ticks_position('left')

 axes.set_ylabel(r'5$\sigma$ Contrast (Bright Mid-A Star)',fontsize=16)
 axes.set_xlabel('Angular Separation(\u2033)',fontsize=16)

###IMPORTANT LINES
 secondaxis=axes.secondary_xaxis('top',functions=(lambda x: dstar*x, lambda x: x/dstar))

 secondaxis.set_xlabel('Projected Separation (au) for d = 40 pc',fontsize=16)
 secondaxis.tick_params(which='both',direction='in',labelsize=14)
 secondaxis.tick_params(which='major',length=10,width=1.5)
 secondaxis.tick_params(which='minor',length=5,width=1.5)
 secondaxis.xaxis.set_minor_locator(AutoMinorLocator(5))

 #thicken the spines
 for axl in ['top','bottom','left','right']:
   axes.spines[axl].set_linewidth(2)
 axes.legend(loc=[0.4,0.75])

 plt.show()

def ex2_7():
 from scipy import interpolate
 from matplotlib.ticker import MultipleLocator,AutoMinorLocator,LogLocator

 file_in='./files/broadband_contrast.txt'

 dstar=40 #assume a distance of 40 pc
 dtypes={'names':('angsep','contrast'), 'formats':(np.float64,np.float64)}

 a = np.loadtxt(file_in,usecols=range(2),dtype=dtypes)
 #a=np.loadtxt(file_in)

 ang_sep=a['angsep']
 contrast_5sig=a['contrast']

 nhour=2
 scalefact=(nhour*3600/1800.)**(0.5)

 fscexao=interpolate.interp1d(ang_sep,contrast_5sig/scalefact)

 ang_sep_new=np.arange(0.15,0.9,0.05)
 contrast_5sig_twohours=fscexao(ang_sep_new)


 #approximate performance for Keck/NIRC2

 ang_sep_keck=np.array([0.15,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
 contrast_keck=np.array([1e-2,1e-3,3e-4,1e-4,3e-5,1.5e-5,1.25e-5,1e-5,8e-6])

 fkeck=interpolate.interp1d(ang_sep_keck,contrast_keck)
 #print(fkeck)
 #exit()
 contrast_5sig_keck=fkeck(ang_sep_new)
 #estimate for new performance, SCExAO

 improve_fact=4
 contrast_5sig_twohours_new=contrast_5sig_twohours/improve_fact
 igood=np.where(ang_sep_new < 0.25)
 contrast_5sig_twohours_new[igood]/=(3-ang_sep_new[igood]*8.)
 ibad=np.where(ang_sep_new > 0.7)
 contrast_5sig_twohours_new[ibad]*=(1+1.75*ang_sep_new[ibad]-.7)

 print(ang_sep)

 fig,axes=plt.subplots(figsize=(9,5))
 axes.plot(ang_sep_new,contrast_5sig_keck,linewidth=4,markersize=np.sqrt(50),color='tab:blue',label='Keck/NIRC2')
 axes.plot(ang_sep_new,contrast_5sig_twohours,linewidth=5,color='magenta',label='SCExAO/CHARIS (Early 2023 Performance)')
 axes.plot(ang_sep_new,contrast_5sig_twohours_new,linewidth=4,ls='-.',color='tab:green',label='SCExAO/CHARIS (2024 Performance, predicted)')

 axes.set_yscale('log')
 axes.set_ylim(5e-8,2e-3)
 axes.set_xlim(0.1,1.01)

#note: setting to 'both' instead of 'bottom' would draw tick marks at top of plot:
   #would mismatch with secondary axis tick marks
 axes.xaxis.set_ticks_position('bottom')

 axes.tick_params(labeltop=False,labelbottom=True,labelright=False,labelleft=True)
 axes.tick_params(which='both',direction='in',labelsize=14)
 axes.tick_params(which='major',length=10,width=1.5)
 axes.tick_params(which='minor',length=5,width=1.5)
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 #log scale automatically sets minor tick marks to be reasonable here
 axes.yaxis.set_ticks_position('both')

 axes.set_ylabel(r'5$\sigma$ Contrast (Bright Mid-A Star)',fontsize=16)
 axes.set_xlabel('Angular Separation(\u2033)',fontsize=16)
 axes.set_title('SCExAO Contrast Plot With An Inset',fontsize=18)

###IMPORTANT LINES

 left,bottom,width,height=[0.5,0.6,0.33,0.25]
 secondaxis=fig.add_axes([left,bottom,width,height])
 #secondaxis=axes.secondary_xaxis('top',functions=(lambda x: dstar*x, lambda x: x/dstar))

 secondaxis.plot(dstar*ang_sep_new,-2.5*np.log10(contrast_5sig_keck),linewidth=4,markersize=np.sqrt(50),color='tab:blue')
 secondaxis.plot(dstar*ang_sep_new,-2.5*np.log10(contrast_5sig_twohours),linewidth=5,color='magenta')
 secondaxis.plot(dstar*ang_sep_new,-2.5*np.log10(contrast_5sig_twohours_new),ls='-.',linewidth=5,color='tab:green')
 secondaxis.set_xlabel('Projected Separation (au) for d = 40 pc',fontsize=8)
 secondaxis.set_ylabel('$\Delta$m',fontsize=8)
 secondaxis.set_xlim(3,15)
 secondaxis.set_ylim(17.5,8.5)
 secondaxis.tick_params(which='both',direction='in',labelsize=8)
 secondaxis.tick_params(which='major',length=10,width=1.5)
 secondaxis.tick_params(which='minor',length=5,width=1.5)
 secondaxis.xaxis.set_minor_locator(AutoMinorLocator(5))
 secondaxis.yaxis.set_minor_locator(AutoMinorLocator(5))

 #thicken the spines
 for axl in ['top','bottom','left','right']:
   axes.spines[axl].set_linewidth(2)

 #axes.legend(loc=[0.4,0.75])
 axes.legend(loc=[0.025,0.05],fontsize=8)

 plt.show()

def ex2_8():
 from scipy import interpolate
 from mpl_toolkits.axes_grid.inset_locator import inset_axes
 from matplotlib.ticker import AutoMinorLocator

 file_in='./files/broadband_contrast.txt'

 dstar=40 #assume a distance of 40 pc
 dtypes={'names':('angsep','contrast'), 'formats':(np.float64,np.float64)}

 a = np.loadtxt(file_in,usecols=range(2),dtype=dtypes)
 #a=np.loadtxt(file_in)

 ang_sep=a['angsep']
 contrast_5sig=a['contrast']

 nhour=2
 scalefact=(nhour*3600/1800.)**(0.5)

 fscexao=interpolate.interp1d(ang_sep,contrast_5sig/scalefact)

 ang_sep_new=np.arange(0.15,0.9,0.05)
 contrast_5sig_twohours=fscexao(ang_sep_new)


 #approximate performance for Keck/NIRC2

 ang_sep_keck=np.array([0.15,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
 contrast_keck=np.array([1e-2,1e-3,3e-4,1e-4,3e-5,1.5e-5,1.25e-5,1e-5,8e-6])

 fkeck=interpolate.interp1d(ang_sep_keck,contrast_keck)
 #print(fkeck)
 #exit()
 contrast_5sig_keck=fkeck(ang_sep_new)
 #estimate for new performance, SCExAO

 improve_fact=4
 contrast_5sig_twohours_new=contrast_5sig_twohours/improve_fact
 igood=np.where(ang_sep_new < 0.25)
 contrast_5sig_twohours_new[igood]/=(3-ang_sep_new[igood]*8.)
 ibad=np.where(ang_sep_new > 0.7)
 contrast_5sig_twohours_new[ibad]*=(1+1.75*ang_sep_new[ibad]-.7)

 print(ang_sep)

 fig,axes=plt.subplots(figsize=(9,5))
 axes.plot(ang_sep_new,contrast_5sig_keck,linewidth=4,markersize=np.sqrt(50),color='tab:blue',label='Keck/NIRC2')
 axes.plot(ang_sep_new,contrast_5sig_twohours,linewidth=5,color='magenta',label='SCExAO/CHARIS (Early 2023 Performance)')
 axes.plot(ang_sep_new,contrast_5sig_twohours_new,linewidth=4,ls='-.',color='tab:green',label='SCExAO/CHARIS (2024 Performance, predicted)')

 axes.set_yscale('log')
 axes.set_ylim(5e-8,2e-3)
 axes.set_xlim(0.1,1.01)

#note: setting to 'both' instead of 'bottom' would draw tick marks at top of plot:
   #would mismatch with secondary axis tick marks
 axes.xaxis.set_ticks_position('bottom')

 axes.tick_params(labeltop=False,labelbottom=True,labelright=False,labelleft=True)
 axes.tick_params(which='both',direction='in',labelsize=14)
 axes.tick_params(which='major',length=10,width=1.5)
 axes.tick_params(which='minor',length=5,width=1.5)
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 #log scale automatically sets minor tick marks to be reasonable here
 axes.yaxis.set_ticks_position('both')

 axes.set_ylabel(r'5$\sigma$ Contrast (Bright Mid-A Star)',fontsize=16)
 axes.set_xlabel('Angular Separation(\u2033)',fontsize=16)
 axes.set_title('SCExAO Contrast Plot With An Inset and Zoom-In',fontsize=18)

###IMPORTANT LINES

 #secondaxis=inset_axes(axes,width=1.3,height=0.9,[0.5,0.6])
 secondaxis=axes.inset_axes([0.625, 0.65, 0.33, 0.25])
#,width=1.3,height=0.9)
 #left,bottom,width,height=[0.5,0.6,0.33,0.25]
 #secondaxis=fig.add_axes([left,bottom,width,height])
 #secondaxis=axes.secondary_xaxis('top',functions=(lambda x: dstar*x, lambda x: x/dstar))

 secondaxis.plot(ang_sep_new,contrast_5sig_twohours,linewidth=5,color='magenta')
 secondaxis.plot(ang_sep_new,contrast_5sig_twohours_new,ls='-.',linewidth=5,color='tab:green')
 secondaxis.set_ylabel(r'5$\sigma$ Contrast (Bright Mid-A Star)',fontsize=7)
 secondaxis.set_xlabel('Angular Separation(\u2033)',fontsize=7)
 secondaxis.set_xlim(0.15,0.4)
 secondaxis.set_ylim(5e-7,1e-4)
 #secondaxis.set_ylim(5e-8,2e-3)
 secondaxis.tick_params(which='both',direction='in',labelsize=8)
 secondaxis.tick_params(which='major',length=10,width=1.5)
 secondaxis.tick_params(which='minor',length=5,width=1.5)
 secondaxis.xaxis.set_minor_locator(AutoMinorLocator(5))
 #secondaxis.yaxis.set_minor_locator(AutoMinorLocator(5))
 secondaxis.set_yscale('log')

 secondary_axis2=secondaxis.secondary_xaxis('top',functions=(lambda x: dstar*x, lambda x: x/dstar))
 secondary_axis2.set_xlabel('Projected Separation (au) for d = 40 pc',fontsize=7)
 secondary_axis2.tick_params(which='both',direction='in',labelsize=7)
 secondary_axis2.tick_params(which='major',length=10,width=1.5)
 secondary_axis2.tick_params(which='minor',length=5,width=1.5)
 secondary_axis2.xaxis.set_minor_locator(AutoMinorLocator(5))


 axes.indicate_inset_zoom(secondaxis)

 #thicken the spines
 for axl in ['top','bottom','left','right']:
   axes.spines[axl].set_linewidth(2)

#move the legend location b/c otherwise it clashes with the inset
 #axes.legend(loc=[0.4,0.75])
 axes.legend(loc=[0.025,0.05],fontsize=8)

 plt.show()

def ex2_9():

 #from matplotlib import patches
 from scipy import interpolate
 from matplotlib.ticker import MultipleLocator,AutoMinorLocator,LogLocator

 file_in='./files/broadband_contrast.txt'

 dstar=40 #assume a distance of 40 pc
 dtypes={'names':('angsep','contrast'), 'formats':(np.float64,np.float64)}

 a = np.loadtxt(file_in,usecols=range(2),dtype=dtypes)
 #a=np.loadtxt(file_in)

 ang_sep=a['angsep']
 contrast_5sig=a['contrast']

 nhour=2
 scalefact=(nhour*3600/1800.)**(0.5)

 fscexao=interpolate.interp1d(ang_sep,contrast_5sig/scalefact)

 ang_sep_new=np.arange(0.15,0.9,0.05)
 contrast_5sig_twohours=fscexao(ang_sep_new)


 #approximate performance for Keck/NIRC2

 ang_sep_keck=np.array([0.15,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
 contrast_keck=np.array([1e-2,1e-3,3e-4,1e-4,3e-5,1.5e-5,1.25e-5,1e-5,8e-6])

 fkeck=interpolate.interp1d(ang_sep_keck,contrast_keck)
 #print(fkeck)
 #exit()
 contrast_5sig_keck=fkeck(ang_sep_new)
 #estimate for new performance, SCExAO

 improve_fact=4
 contrast_5sig_twohours_new=contrast_5sig_twohours/improve_fact
 igood=np.where(ang_sep_new < 0.25)
 contrast_5sig_twohours_new[igood]/=(3-ang_sep_new[igood]*8.)
 ibad=np.where(ang_sep_new > 0.7)
 contrast_5sig_twohours_new[ibad]*=(1+1.75*ang_sep_new[ibad]-.7)

 print(ang_sep)

 fig,axes=plt.subplots(figsize=(9,5))
 axes.plot(ang_sep_new,contrast_5sig_keck,linewidth=4,markersize=np.sqrt(50),color='tab:blue',label='Keck/NIRC2')
 axes.plot(ang_sep_new,contrast_5sig_twohours,linewidth=5,color='magenta',label='SCExAO/CHARIS (Early 2023 Performance)')
 axes.plot(ang_sep_new,contrast_5sig_twohours_new,linewidth=4,ls='-.',color='tab:green',label='SCExAO/CHARIS (2024 Performance, predicted)')

 axes.set_yscale('log')
 axes.set_ylim(5e-8,2e-3)
 axes.set_xlim(0.1,1.01)

#note: setting to 'both' instead of 'bottom' would draw tick marks at top of plot:
   #would mismatch with secondary axis tick marks
 axes.xaxis.set_ticks_position('bottom')

 axes.tick_params(labeltop=False,labelbottom=True,labelright=False,labelleft=True)
 axes.tick_params(which='both',direction='in',labelsize=14)
 axes.tick_params(which='major',length=10,width=1.5)
 axes.tick_params(which='minor',length=5,width=1.5)
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 #log scale automatically sets minor tick marks to be reasonable here
 axes.yaxis.set_ticks_position('both')

 axes.set_ylabel(r'5$\sigma$ Contrast (Bright Mid-A Star)',fontsize=16)
 axes.set_xlabel('Angular Separation(\u2033)',fontsize=16)

###IMPORTANT LINES
###IMPORTANT LINES
# secondaxis=axes.secondary_xaxis('top',functions=(lambda x: dstar*x, lambda x: x/dstar))

# secondaxis.set_xlabel('Projected Separation (au) for d = 40 pc',fontsize=16)
#secondaxis.tick_params(which='both',direction='in',labelsize=14)
# secondaxis.tick_params(which='major',length=10,width=1.5)
# secondaxis.tick_params(which='minor',length=5,width=1.5)
# secondaxis.xaxis.set_minor_locator(AutoMinorLocator(5))

 #thicken the spines
 for axl in ['top','bottom','left','right']:
   axes.spines[axl].set_linewidth(2)

 axes.legend(loc=[0.4,0.75])

 planetnames=['HR 8799 e','HR 8799 d','HR 8799 c','51 Eri b','HIP 99770 b']
 planetcontrast=10**(-0.4*(np.array([11.56,11.64,11.65,14.09,12.05])))
 planetseps=np.array([0.39,0.68,0.93,0.45,0.41])
 planetmass=np.array([9.2,9,8,3,16])

 labeloffsetsx=np.array([0.01,0.0025,-0.01,-0.01,0.01])
 labeloffsetsy=np.array([1.1,1.25,1.1,1.1,1.1])


 axes.scatter(planetseps,planetcontrast,color='darkgoldenrod',edgecolor='black',s=100*planetmass/10,zorder=15)

# HR 8799 bcd labeling
 axes.text(0.7,7.5e-5,'HR 8799 bcd')

 for i in range(0,3):
  axes.annotate("",xy=(planetseps[i]+labeloffsetsx[i],labeloffsetsy[i]*planetcontrast[i]),xytext=(0.75,7.e-5),textcoords='data',arrowprops=dict(arrowstyle='-',facecolor='black'))

#HIP 99770 b labeling

#note: we had to use transform=axes.transAxes because the y axis is a log plot.
 axes.arrow(0.425,0.475,-0.07,0.05,width=0.005,transform=axes.transAxes,length_includes_head=True,color='black',fill=True)
#in data coordinates
 axes.text(0.55,7e-6,'HIP 99770 b',transform=axes.transData,ha='center',va='center')

#51 Eri b
 axes.annotate("51 Eri b",xy=(planetseps[-2]+labeloffsetsx[-2],labeloffsetsy[-2]*planetcontrast[-2]),xytext=(0.3,7e-6),textcoords='data',arrowprops=dict(arrowstyle='->',facecolor='black',connectionstyle="angle3,angleA=90,angleB=0"))

 plt.show()

