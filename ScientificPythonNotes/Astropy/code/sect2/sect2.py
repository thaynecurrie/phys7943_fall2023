import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib import ticker
import numpy as np

from astropy.io import fits
from astropy.wcs import WCS
from astropy.visualization import quantity_support
from matplotlib import animation

import astropy.units as u

def ex2_1():
 R_eff=29*u.pc
 #R_eff=u.Quantity(29,unit=u.pc) # does the same thing

 print("""Half light radius
 value: {0}
 unit: {1}""".format(R_eff.value, R_eff.unit))

 #print("The Half light radius value is {0:.1f} and unit is {1:s}".format(R_eff.value,R_eff.unit))

 print("{0:.3g}".format(R_eff.to(u.m))) # meters
#8.95e+17 m
 print("{0:.3g}".format(R_eff.to(u.lyr))) # light-years
#94.6 lyr
 print("{0:.3g}".format(R_eff.to(u.um))) # microns
#8.95e+23 um

 vmean = 206
 sigin = 4.3
 v = np.random.normal(vmean, sigin, 500)*u.km/u.s

 import matplotlib.pyplot as plt
 fig,axes=plt.subplots()
 axes.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
 axes.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
 axes.tick_params(which='both', axis='x',direction='in')
 axes.tick_params(which='major',length=6)
 axes.tick_params(which='minor',length=3)
 axes.set_xlabel('Velocity in {0:s}'.format(v.unit),fontsize=14)
 axes.set_ylabel('Relative Number',fontsize=14)

 axes.hist(v.value,bins=50,density=True,color='tab:green')
 plt.show()

def ex2_2():
 R_eff=29*u.pc
 #R_eff=u.Quantity(29,unit=u.pc) # does the same thing

 print("""Half light radius
 value: {0}
 unit: {1}""".format(R_eff.value, R_eff.unit))

 #print("The Half light radius value is {0:.1f} and unit is {1:s}".format(R_eff.value,R_eff.unit))

 print("{0:.3g}".format(R_eff.to(u.m))) # meters
#8.95e+17 m
 print("{0:.3g}".format(R_eff.to(u.lyr))) # light-years
#94.6 lyr
 print("{0:.3g}".format(R_eff.to(u.um))) # microns
#8.95e+23 um

 vmean = 206
 sigin = 4.3
 v = np.random.normal(vmean, sigin, 500)*u.km/u.s

 import matplotlib.pyplot as plt

 fig,axes=plt.subplots()
 quantity_support()

 axes.tick_params(which='both', axis='x',direction='in')
 axes.tick_params(which='major',length=6)
 axes.tick_params(which='minor',length=3)
 axes.set_ylabel('Relative Number',fontsize=14)
 axes.hist(v,bins='auto',histtype='step')

 plt.show()

def ex2_3():
 from astropy.constants import G, h, k_B

 R_eff=29*u.pc
 #R_eff=u.Quantity(29,unit=u.pc) # does the same thing

 print("""Half light radius
 value: {0}
 unit: {1}""".format(R_eff.value, R_eff.unit))

 #print("The Half light radius value is {0:.1f} and unit is {1:s}".format(R_eff.value,R_eff.unit))

 print("{0:.3g}".format(R_eff.to(u.m))) # meters
#8.95e+17 m
 print("{0:.3g}".format(R_eff.to(u.lyr))) # light-years
#94.6 lyr
 print("{0:.3g}".format(R_eff.to(u.um))) # microns
#8.95e+23 um

 vmean = 206
 sigin = 4.3
 v = np.random.normal(vmean, sigin, 500)*u.km/u.s

 sigma = np.sqrt(np.sum((v - np.mean(v))**2) / np.size(v))
 print("Velocity dispersion: {0:.2f}".format(sigma))

 sigma_scalar = np.sqrt(np.sum((v - np.mean(v))**2) / len(v))

 M = 4*sigma**2*R_eff/G
 M
 M.decompose()
 print(M)
 print(M.decompose())

 print("""Galaxy mass
 in solar units: {0:.3g}
 SI units: {1:.3g}
 CGS units: {2:.3g}""".format(M.to(u.Msun), M.si, M.cgs))
 print(np.log10(M.to_value(u.Msun)))
 print(np.log10(M.value))

def ex2_4():

 c1 = SkyCoord('00h42m30s', '+41d12m00s', frame='icrs')
 c2 = SkyCoord(ra=10.625*u.degree, dec=41.2*u.degree, frame='icrs')

 print(c1)
 print(c2)

 c = SkyCoord(ra=[10, 11, 12, 13]*u.degree, dec=[41, -5, 42, 0]*u.degree)

 print(c)
#<SkyCoord (ICRS): (ra, dec) in deg
#    [(10., 41.), (11., -5.), (12., 42.), (13.,  0.)]>

 print(c[1])
#<SkyCoord (ICRS): (ra, dec) in deg
#    (11., -5.)>

 print(c.reshape(2, 2))
#<SkyCoord (ICRS): (ra, dec) in deg
#    [[(10., 41.), (11., -5.)],
#     [(12., 42.), (13.,  0.)]]>

 print(np.roll(c, 1))
#<SkyCoord (ICRS): (ra, dec) in deg
#    [(13.,  0.), (10., 41.), (11., -5.), (12., 42.)]>

 c = SkyCoord(ra=10.68458*u.degree, dec=41.26917*u.degree)

 print(c.to_string('decimal'))
 #'10.6846 41.2692'
 print(c.to_string('dms'))
 #'10d41m04.488s 41d16m09.012s'

 print(c.to_string('hmsdms'))
 #00h42m44.2992s +41d16m09.012s

 c_icrs = SkyCoord(ra=10.68458*u.degree, dec=41.26917*u.degree, frame='icrs')
 print(c_icrs.galactic  )
#<SkyCoord (Galactic): (l, b) in deg
#   (121.17424181, -21.57288557)>

 from astropy.coordinates import FK5
 c_fk5 = c_icrs.transform_to('fk5')
 #<SkyCoord (FK5: equinox=J2000.000): (ra, dec) in deg
#    (10.68459154, 41.26917146)>

 c_fk5.transform_to(FK5(equinox='J1975'))
 print(c_fk5)
#<SkyCoord (FK5: equinox=J1975.000): (ra, dec) in deg
#    (10.34209135, 41.13232112)>

