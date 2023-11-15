#uses IDL output of HGCA accelerators, queries Simbad to get the spectral type, queries Gaia-eDR3 to get photometry, saves to output
import astroquery
import numpy as np
from astroquery.simbad import Simbad
from astroquery.vizier import Vizier
from astropy.io import ascii
import astropy.units as u
import astropy.coordinates as coord
from astropy.table import QTable
#from astroquery.utils.tap.core import TapPlus
from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord,Angle

infile='astars_100pc'
Gaia.MAIN_GAIA_TABLE = "gaiaedr3.gaia_source"
radius=u.Quantity(1.5/3600.0,u.deg)

def add_gaia_data(infile):

    outfile=infile+'_plus_gaia_and_cahkv2'

    #formatted loading
    dtypes={'names': ('name1','name2','ra1','ra2','ra3','dec1','dec2','dec3','distance','spt','mass','chisq'),\
       'formats':('U20','U20',np.int,np.int,np.float64,np.int,np.int,np.float64,np.float64,'U20',np.float64,np.float64)}

    a= np.loadtxt(infile,usecols=range(12),dtype=dtypes)
   
    #combining the first two strings to get the target name
    names = np.array([ '{0} {1}'.format( x, y ) for x,y in zip( a['name1'], a['name2'] ) ])
    names =np.array(names,dtype=str)

    mass=a['mass']
    chisq=a['chisq']
    #determine ra and dec
    ra_deg=(a['ra1']+a['ra2']/60.+a['ra3']/3600.)*15
    dec_deg=(np.abs(a['dec1'])+np.abs(a['dec2']/60.)+np.abs(a['dec3']/3600.))

    pos = a['dec1'] >= 0
    neg = (a['dec1'] < 0) | (a['dec2'] < 0)
    print(len(neg))
    dec_deg[neg]=-1*dec_deg[neg]

    
    nstar=len(dec_deg)

    plx=np.zeros(nstar)
    gmag=np.zeros(nstar)
    bp_rp=np.zeros(nstar)
    ra=np.zeros(nstar)
    dec=np.zeros(nstar)
    bmv=np.zeros(nstar)
    hkact=np.zeros(nstar)

    Simbad.add_votable_fields('sptype')
    Simbad.timeout=60
    Vizier.timeout=60
 
    spt= ["" for i in range(nstar)]
    for i in range(nstar):
       print('processing star number ',i,' star name ',names[i])

       #simbad
       try:
        results=Simbad.query_object(names[i])
       except:
        print('!!!!!Error on ',names[i])
        continue
       spt[i]=results['SP_TYPE'][0]

       coord=SkyCoord(ra=ra_deg[i],dec=dec_deg[i],unit=(u.degree,u.degree),frame='icrs')
       r=Gaia.cone_search(coord,radius)
       j=r.get_results()
       try:
         ra[i]=j['ra'][0]
         dec[i]=j['dec'][0]
#         print('found star ',i,names[i],ra_deg[i],dec_deg[i],(a['dec1'])[i],(a['dec2'])[i],(a['dec3'])[i])
       except:
         print('missing star ',i,names[i],ra_deg[i],dec_deg[i],(a['dec1'])[i],(a['dec2'])[i],(a['dec3'])[i])
         continue
       plx[i]=j['parallax'][0]
       gmag[i]=j['phot_g_mean_mag'][0]
       bp_rp[i]=j['bp_rp'][0]

       #now, pull Tycho II catalog
       result=Vizier.query_region(SkyCoord.from_name(names[i]),radius=Angle(5/3600.,"deg"),catalog=['I/259/tyc2'])
       #print(result)
       #result=Vizier.query_object(names[i],radius=Angle(5/3600.,"deg"),catalog=['I/259/tyc2'])
       #print(result[0]['BTmag'][0])

       if len(result) >= 1:
         btmag=result[0]['BTmag'][0]
         vtmag=result[0]['VTmag'][0]
         bmag,vmag=tycho_convert(btmag,vtmag)
         #print(bmag,vmag,btmag,vtmag)
       else:
         bmag= -99
         vmag=-109

       caHK=99 #initializing to NaN

       #now, pull catalogs to find if the star has an activity measurement
       #Pace+2013
       result=Vizier.query_object(names[i],radius=Angle(5/3600.,"deg"),catalog=['J/A+A/551/L8'])
       try:
         caHK=0.5*(result[0]['logRmin'][0]+result[0]['logRmax'][0])      
       except:
         caHK=99

       #Gondoin+2020
       result=Vizier.query_object(names[i],radius=Angle(5/3600.,"deg"),catalog=['J/A+A/641/A110'])
       try:
          newHK=result[0]["logR'HK"][0]
          caHK=np.minimum(caHK,newHK)
       except:
          newHK=99

       #Hojjatpanah+2020 
       result=Vizier.query_object(names[i],radius=Angle(5/3600.,"deg"),catalog=['J/A+A/639/A35'])
       try:
          newHK=result[0]["logR'HK"][0]
          caHK=np.minimum(caHK,newHK)
       except:
          newHK=99

       #Hojjatpanah+2019
       result=Vizier.query_object(names[i],radius=Angle(5/3600.,"deg"),catalog=['J/A+A/629/A80'])
       try:
          newHK=result[0]["logR'HK"][0]
          caHK=np.minimum(caHK,newHK)
       except:
          newHK=99

       #Lick Planet Search 2010
       result=Vizier.query_object(names[i],radius=Angle(5/3600.,"deg"),catalog=['J/ApJ/725/875/table1'])
       try:
          newHK=result[0]['logRHK'][0]
          caHK=np.minimum(caHK,newHK)
       except:
          newHK=99

       #Gray/Nstars-south
        
       result=Vizier.query_object(names[i],radius=Angle(5/3600.,"deg"),catalog=['J/AJ/132/161'])
       try:
          newHK=result[0]['logR'][0]
          caHK=np.minimum(caHK,newHK)
       except:
          newHK=99

       #Gray/Nstars-north
        
       result=Vizier.query_object(names[i],radius=Angle(5/3600.,"deg"),catalog=['J/AJ/126/2048'])
       try:
          newHK=result[0]["logR'HK"][0]
          caHK=np.minimum(caHK,newHK)
       except:
          newHK=99

       #Boro Saikia+2018
       result=Vizier.query_object(names[i],radius=Angle(5/3600.,"deg"),catalog=['J/A+A/616/A108'])
       try:
          newHK=result[0]['logRpHK'][0]
          caHK=np.minimum(caHK,newHK)
       except:
          newHK=99

       #Hinkel+2017
       
       result=Vizier.query_object(names[i],radius=Angle(5/3600.,"deg"),catalog=['J/ApJ/848/34'])
       try:
          newHK=result[0]['logRpHK'][0]
          caHK=np.minimum(caHK,newHK)
       except:
          newHK=99

       #White and Hillenbrand 2007

       result=Vizier.query_object(names[i],radius=Angle(5/3600.,"deg"),catalog=['J/AJ/133/2524'])
       try:
          newHK=result[0]['logRHK'][0]
          caHK=np.minimum(caHK,newHK)
       except:
          newHK=99


       hkact[i]=caHK
       bmv[i]=bmag-vmag
       print('bmv and CaHK for ',names[i],' are ',bmv[i],hkact[i])

    gmag_abs=np.array(gmag-5*np.log10(1e2/plx))

    f=open(outfile,'w')
    for i in range(len(ra)):
       f.write("%s %.3s %f %f %f %f %f %f %f %f %f %f\n" % (names[i].replace(" ",""),spt[i],mass[i],chisq[i],ra[i],dec[i],plx[i],gmag_abs[i],gmag[i],bp_rp[i],bmv[i],hkact[i]))
       #f.write("%s %f %f %f %f %f %f\n" % (names[i].replace(" ",""),ra[i],dec[i],plx[i],gmag_abs[i],gmag[i],bp_rp[i]))

    f.close()

def tycho_convert(BT,VT):
      v=VT-0.09*(BT-VT)
      b=v+0.85*(BT-VT)
        
      return b, v
