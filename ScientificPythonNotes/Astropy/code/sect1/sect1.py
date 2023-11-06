import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np

from astropy.io import fits
from astropy.wcs import WCS
from matplotlib import animation

def ex1_1():

 directory='./files/'
  
 hdu=fits.open(directory+'keckimage.fits')
 #or, hdu=fits.open('./files/n0023f.fits')


#info 
 hdu.info()

#data
 image=hdu[0].data
#print(image.shape)


 image_header=hdu[0].header
#print(image_header[0:10])

#read out some of the header
 print(image_header['LAT'])

#update the header 
# print(image_header['OBJECT'])
# image_header['OBJECT']='kappa And'
# print(image_header['OBJECT'])

 fig,axes=plt.subplots(figsize=(8,6))
 clims=np.nanpercentile(image,[0,99.5])

# axes.imshow(image) #default
 axes.imshow(image,origin='lower',cmap='viridis',clim=clims) #change the origin, note: viridis is the default

#do this if you want to later add a colorbar
# image1=axes.imshow(image,origin='lower',cmap='viridis',clim=clims) #change the origin, note: viridis is the default

#customize
 #center=np.array(imdim)//2
 center=np.array([173,252])
 windowsize=150
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)
 axes.set_xlabel('X Pixel Value',fontsize=14)
 axes.set_title('Keck/NIRC2 Image',fontsize=16)
 axes.set_ylabel('Y Pixel Value',fontsize=14) 
 
 #axes.set_xlabel()
 #axes.set_ylabel()
 #axes.xaxis.set_ticklabels([])
 #axes.yaxis.set_ticklabels([])
 axes.tick_params(which='both',width='1.75',labelsize=12)
 #axes.tick_params(which='major',length=7)
 #axes.tick_params(which='minor',length=3.5)
 #axes.xaxis.set_ticks_position('none')
 #axes.yaxis.set_ticks_position('none')
 #axes.xaxis.set_minor_locator(AutoMinorLocator(5))

#if you want to add a colorbar
#note: colorbar is a property of figure, not axes
# fig.colorbar(image1,ax=axes,orientation='vertical')

 plt.show()


def ex1_1b():

 directory='./files/'

 hdu=fits.open(directory+'keckimageext.fits')
 hdu.info()

#data
 image=hdu[1].data
 #or ...
 #image=fits.getdata(directory+'keckimageext.fits')

 primary_header=hdu[0].header
 ext_header=hdu[1].header


def ex1_2():
 directory='./files/'

#First Image
 hdu=fits.open(directory+'keckimage.fits')

#data
 image=hdu[0].data
#header
 image_header=hdu[0].header

#dimensions of the image

#Second Image

 hdu2=fits.open(directory+'secondkeckimage.fits')
 image2=hdu2[0].data

 meanval=np.nanmean(image)
 meanval2=np.nanmean(image2)

 psfsubimage=image-image2*(meanval/meanval2)
 #psfsubimage=image-image2

 #update the header
 image_header['OBJECT']='kappa And'

#write the new file
 fits.writeto(directory+'psfsubimage.fits',psfsubimage,image_header,overwrite=True)
 
#display the new file
 fig,axes=plt.subplots(figsize=(8,6))

 clims=np.nanpercentile(psfsubimage,[3,99])

 axes.imshow(psfsubimage,origin='lower',clim=clims) #change the origin

 axes.set_title('Simple PSF Subtraction',fontsize=18)
 axes.set_xlabel('X Pixel Value',fontsize=14)
 axes.set_ylabel('Y Pixel Value',fontsize=14)

 center=np.array([173,252])
 windowsize=150
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)

 axes.add_patch(plt.Circle([318,111],10,color='white',fill=False))

 #Other way ...
 #from matplotlib.patches import Circle
 #circle1=Circle([318,111],10,color='white',fill=False)
 #axes.add_patch(circle1)

 plt.show()
def ex1_2b():

 directory='./files/'

#First Image
 hdu=fits.open(directory+'keckimageext.fits')

#data
 image=hdu[1].data
#header
 image_header0=hdu[0].header
 image_header1=hdu[1].header

#dimensions of the image

#Second Image

 hdu2=fits.open(directory+'secondkeckimage.fits')
 image2=hdu2[0].data

 meanval=np.nanmean(image)
 meanval2=np.nanmean(image2)

 psfsubimage=image-image2*(meanval/meanval2)
 #psfsubimage=image-image2

 #update the header
 image_header0['OBJECT']='kappa And'

 fits.HDUList([fits.PrimaryHDU(header=image_header0),fits.ImageHDU(psfsubimage,header=image_header1)]).writeto('psfsubext.fits',overwrite=True)

#simple display
 fig,axes=plt.subplots(figsize=(8,6))

 clims=np.nanpercentile(psfsubimage,[3,99])

 axes.imshow(psfsubimage,origin='lower',clim=clims) #change the origin

 axes.set_title('Simple PSF Subtraction',fontsize=18)
 axes.set_xlabel('X Pixel Value',fontsize=14)
 axes.set_ylabel('Y Pixel Value',fontsize=14)

 center=np.array([173,252])
 windowsize=150
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)


 plt.show()
def ex1_3a():

 directory='./files/'

 hdu=fits.open(directory+'psfsubimage.fits')

#data
 image=hdu[0].data
 image_header=hdu[0].header

#dimensions of the image

 wcs=WCS(image_header)
#simple display
 fig,axes=plt.subplots(subplot_kw={'projection':wcs},figsize=(8,6))

 clims=np.nanpercentile(image,[3,99])

 axes.imshow(image,origin='lower',clim=clims) #change the origin

#customize
 center=np.array([173,252])
 windowsize=150
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)

 plt.show()
def ex1_3b():
 directory='./files/'

 hdu=fits.open(directory+'psfsubimage.fits')

#data
 image=hdu[0].data
 image_header=hdu[0].header

 wcs=WCS(image_header)
 fig,axes=plt.subplots(subplot_kw={'projection':wcs},figsize=(8,6))

 axes.coords[0].set_ticklabel_visible(False)
 axes.coords[1].set_ticklabel_visible(False)
 overlay=axes.get_coords_overlay('fk5')
 overlay[0].set_major_formatter('hh:mm:ss.s') #to move the formatting out of degrees for RA
 overlay.grid(color='white',ls='solid',alpha=0.5)

 overlay[0].set_axislabel('Right Ascension (J2000)',fontsize=16)
 overlay[1].set_axislabel('Declination (J2000)',fontsize=16)
 overlay[0].set_axislabel_position('b') #b=bottom,l=left,t=top,r=right
 overlay[1].set_axislabel_position('l')

 overlay[0].set_ticklabel_position('bt')
 overlay[1].set_ticklabel_position('lr')

 clims=np.nanpercentile(image,[3,99])

 axes.imshow(image,origin='lower',clim=clims) #change the origin
 #padding more than the default of 6 to make sure labels don't collide
 axes.set_title('With Overlays',fontsize=18,pad=30) 
#customize
 center=np.array([173,252])
 windowsize=150
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)

 plt.show()

def ex1_3c():

 directory='./files/'

 #doing this instead of image=(fits.open[filename])[0].data
 image=fits.getdata(directory+'psfsubimage_northup.fits')

 image_header=(fits.open('./files/psfsubimage_northup.fits'))[0].header

 wcs=WCS(image_header)
 fig,axes=plt.subplots(subplot_kw={'projection':wcs},figsize=(10,6))

 axes.coords[0].set_ticklabel_visible(False)
 axes.coords[1].set_ticklabel_visible(False)
 overlay=axes.get_coords_overlay('fk5')
 overlay[0].set_major_formatter('hh:mm:ss.s')
 overlay.grid(color='white',ls='solid',alpha=0.3)

 overlay[0].set_axislabel('Right Ascension (J2000)',size=14)
 overlay[1].set_axislabel('Declination (J2000)',size=14)
 overlay[0].set_axislabel_position('b')
 overlay[1].set_axislabel_position('l')


 overlay[0].set_ticklabel(size=12)
 overlay[1].set_ticklabel(size=12)
 overlay[0].set_ticklabel_position('bt')
 overlay[1].set_ticklabel_position('lr')

 clims=np.nanpercentile(image,[3,99])

 #axes.imshow(image,origin='lower',clim=clims,cmap='magma') #change the origin
#you need to do the below in order to display a colorbar
 image1=axes.imshow(image,origin='lower',clim=clims,cmap='magma') #change the origin

#customize
#it's different than before since the star was not at the center and the program I use to 'north-up' the image rotates from the image center
 center=np.array([340,250])
 windowsize=150
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)

 axes.tick_params(which='both',width='1.75')
 axes.tick_params(which='major',length=7)
 axes.tick_params(which='minor',length=3.5)
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.set_title("North-Up Image, With Colorbar",fontsize=18,pad=30)

 axes.add_patch(plt.Circle([182,397],10,color='white',fill=False))

 cbar=fig.colorbar(image1,orientation='vertical',pad=0.15,shrink=0.95)
 cbar.set_label(label='Counts (e/s)',size=14)


 plt.show()

def ex1_4():
#RGB images

 directory='./files/'
 jband=(fits.open(directory+'jband2.fits'))[0].data
 hband=(fits.open(directory+'hband2.fits'))[0].data
 kband=(fits.open(directory+'kband2.fits'))[0].data

 cmaps=['Blues','Greens','Reds']

 fig,axes=plt.subplots(figsize=(9,9))

 #import img_scale
 imagecomb=np.zeros((201,201,3),dtype=float)
 print(kband.shape)
 jnorm=0.04
 hnorm=0.03
 knorm=0.035

 jnorm=0.0375
 hnorm=0.0325
 knorm=0.0325
 imagecomb[:,:,0]=kband/knorm
 imagecomb[:,:,1]=hband/hnorm
 imagecomb[:,:,2]=jband/jnorm


 windowsize=60
 center=((jband.shape)[0]//2,(jband.shape)[0]//2)
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)

 import astropy.units as u

 #converting to arcsec
 print((jband.shape)[0])
 pixscale=0.01615*(u.arcsec/u.pixel)

 dim=(jband.shape)[0]
 distfromcenter=np.array([0,dim,0,dim])-100.5

 distfromcenter=distfromcenter << u.pixel
 pixscale = pixscale << u.arcsec/u.pixel
 distfromcenter_arcsec=(distfromcenter*pixscale).value

 #distfromcenter=(np.array([0,201,0,201])-100.5)
 #distfromcenter_arcsec=distfromcenter*0.01615
 #print(distfromcenter_arcsec)

 distfromcenter_arcsec[0]*=-1.0
 distfromcenter_arcsec[1]*=-1.0

 #print(distfromcenter_arcsec[0])
 #exit()

 rmax=0.9 #in units of arc-seconds
 extrange=[rmax,-1*rmax,-1*rmax,rmax]

 #extent goes 'left right bottom top'
 pixelscale=0.01615
 fullext_image=pixelscale*(jband.shape)[0]/2.0

 #axes.imshow(imagecomb,origin='lower',extent=distfromcenter_arcsec)
 #print(extrange)
 #exit()
 interpval='hanning'
 axes.imshow(imagecomb,origin='lower',extent=[fullext_image,-1*fullext_image,-1*fullext_image,fullext_image],interpolation=interpval)

 axes.set_xlim(rmax,-1*rmax)
 axes.set_ylim(-1*rmax,rmax)
 #axes.set_xlim(distfromcenter_arcsec[0],-1*distfromcenter_arcsec[0])
 #axes.set_ylim(distfromcenter_arcsec[1],-1*distfromcenter_arcsec[1])
 axes.tick_params(which='both',direction='out',labelsize=14)
 axes.tick_params(which='major',length=10,width=1.5)
 axes.tick_params(which='minor',length=5,width=1.5)
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.yaxis.set_minor_locator(AutoMinorLocator(5))

 axes.set_xlabel('$\Delta RA(^{\prime\prime})$',fontsize=16)
 axes.set_ylabel('$\Delta DEC(^{\prime\prime})$',fontsize=16)
 #axes.set_title('HIP 99770 b (JHK Composite Image)',fontsize=18,pad=25)

 axes.scatter(0,0,marker='*',c='yellow',edgecolor='black',s=500)
 axes.text(0.95*rmax,0.75*rmax,'Exoplanet HIP 99770 b\nSCExAO/CHARIS\nJHK Composite Image',fontsize=18,color='w')

 #axes.imshow(imagecomb,origin='lower',interpolation='hanning')

 plt.show()

def datacube():

 directory='./files/'
 data_cube=(fits.open(directory+'asdicomb_indiv.fits'))[0].data

 print(data_cube.shape)

def ex1_5():
 fig, ax = plt.subplots()


 directory='./files/'
 x = np.linspace(0, 2 * np.pi, 120)
 y = (np.linspace(0, 2 * np.pi, 100))[:,None]
 #y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1) #this also works ... basically, though, we need to create a 2D array from the combination of x and y either way

 def f(x,y):
  return np.sin(x) + np.cos(y)

 # ims is a list of lists, each row is a list of artists to draw in the
 # current frame; here we are just animating one artist, the image, in
 # each frame
 ims = []
 for i in range(60):
     x += np.pi / 45 #15
     y += np.pi / 30
     im = ax.imshow(f(x, y), animated=True,cmap='magma',origin='lower')
     if i == 0:
         ax.imshow(f(x, y),cmap='magma',origin='lower')  # show an initial one first
     ims.append([im])

 ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                 repeat_delay=1000)

 # To save the animation, use e.g.
 #
 # writer = animation.FFMpegWriter(fps=10,bitrate=1800)
 # ani.save("movie.mp4", writer=writer)

 #for a gif

 writergif = animation.PillowWriter(fps=10)
 ani.save(directory+'ex1_5.gif',writer=writergif)

 plt.show() #displays a quick-look animation, often useful

def ex1_6():

 import matplotlib as mpl
 R,G,B,A = mpl.cm.get_cmap('gist_heat')(np.linspace(0.0,1.0,256)).T
 color_vals = np.array([B,G,R,A]).T
 cmap1 = mpl.colors.ListedColormap(color_vals) # colormap for CHARIS image
 cmap1.set_bad('k')

 directory='./files/'
 data_cube=(fits.open(directory+'asdicomb_indiv.fits'))[0].data

 n_lambda=(data_cube.shape)[0]

#general formatting

 rmax=.9 #in units of arc-seconds
 pixelscale=0.01615
 extrange=[rmax,-1*rmax,-1*rmax,rmax]

 fullext_image=pixelscale*(data_cube.shape)[1]/2.0

 cmapval='plasma'
 cmapval=cmap1

 fig,axes=plt.subplots(figsize=(9,9))
 immovie=[]

 axes.set_xlim(rmax,-1*rmax)
 axes.set_ylim(-1*rmax,rmax)
 axes.tick_params(which='both',direction='out',labelsize=14)
 axes.tick_params(which='major',length=10,width=1.5)
 axes.tick_params(which='minor',length=5,width=1.5)
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.yaxis.set_minor_locator(AutoMinorLocator(5))
 axes.set_xlabel('$\Delta RA(^{\prime\prime})$',fontsize=16)
 axes.set_ylabel('$\Delta DEC(^{\prime\prime})$',fontsize=16)

 #axes.text(0.95*rmax,0.85*rmax,'Exoplanet HIP 99770 b\nSCExAO/CHARIS',fontsize=16,color='w')
 #axes.scatter(0,0,marker='*',c='yellow',edgecolor='black',s=500)

 for i in range(0,n_lambda):
  climsp=np.nanpercentile(data_cube[i,:,:],[0,99.9])
  clims=[-1.5*climsp[1],climsp[1]]
  interpval='hanning'

  im=axes.imshow(data_cube[i,:,:],animated=True,clim=clims,origin='lower',extent=[fullext_image,-1*fullext_image,-1*fullext_image,fullext_image],interpolation=interpval,cmap=cmapval)

  if i== 0:
   im=axes.imshow(data_cube[i,:,:],clim=clims,origin='lower',extent=[fullext_image,-1*fullext_image,-1*fullext_image,fullext_image],interpolation=interpval,cmap=cmapval)

  immovie.append([im])


 ani = animation.ArtistAnimation(fig,immovie,interval=50, blit=False,
                                 repeat_delay=50,repeat=True)

 #plt.rcParams['animation.ffmpeg_path'] = 'my/path/to/ffmpeg'
 # this is my path
 plt.rcParams['animation.ffmpeg_path'] = '/usr/local/bin/ffmpeg'
 writergif = animation.PillowWriter(fps=5)
 ani.save(directory+'ex1_6.gif',writer=writergif)
 mywriter=animation.FFMpegWriter(fps=5,extra_args=['-vcodec', 'libx264'])
 ani.save(directory+'ex1_6.mp4',writer=mywriter)

 plt.show()
