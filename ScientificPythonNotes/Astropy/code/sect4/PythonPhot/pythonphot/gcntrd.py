#!/usr/bin/python3


'''

Name:
	GCNTRD

PURPOSE:
	Compute the stellar centroid by Gaussian fits to marginal X, Y, sums

EXPLANATION:
	GCNTRD uses the DAOPHOT "FIND" centroid algorithm by fitting Gaussians 
	to the marginal X,Y distributions. User can specify bad pixels 
	(either by using the MAXGOOD keyword or setting them to NaN) to be 
	ignored in the fit. Pixel values are weighted toward the center to 
	avoid contamination by neighboring stars. 

CALLING SEQUENCE:
	gcntrd(img, x, y, fwhm)

INPUTS:
	img 		- 	two dimensional image array
	x,y 		- 	scalar or vector integers giving approximate stellar 
					center(s)
	fwhm 		- 	floating scalar; centroid is computed using a box of half 
					width equal to 1.5 sigma = 0.637* FWHM.
	maxgood 	-	Only pixels with values less than maxgood are used in 
					gaussian fits to determine the centroid. For non-integer 
					data, one can also flag using NaN values
	silent 		-	Normally gcntrd prints an error message if it is unable to 
					compute the centroid. Set silent = True to suppress this
	debug		- 	if debug = True, gcntrd will display the subarry it is 
					using to compute the centroid
	keepcenter	-	By default, gcntrd first convolves a small region around 
					the supplied position with a lowered gaussian filter, and
					then finds the maximum pixel in a box centered on the 
					input x,y coordinate(s). gcntrd then extracts a new box 
					about this maximum pixel. Set keepcenter = True to skip
					the convolution and finding the maximum pixel and only use
					a box centered on the input x,y coordinates. 


OUTPUTS: 
	XCEN - the computed X centroid position, same number of points as X
	YCEN - computed Y centroid position, same number of points as Y 

NOTES:
	Replication of the IDL code gcntrd.pro
	Written June 2004, W. Landsman  following algorithm used by P. Stetson 
        in DAOPHOT2.
    Modified centroid computation (as in IRAF/DAOFIND) to allow shifts of
    	more than 1 pixel from initial guess. March 2008
    First perform Gaussian convolution prior to finding maximum pixel 
    	to smooth out noise  W. Landsman  Jan 2009
    Wrote a python routine  Derek Hand  Dec 2020

'''		
import sys

import numpy as np	

from scipy import ndimage	


def gcntrd(img, x, y, FWHM, maxgood = False, keepcenter = False, silent = False, debug = False):
	
	if img.ndim != 2:
		sys.exit("Image array must be two dimensional")

	xsize = img.shape[1]
	ysize = img.shape[0]
	dtype = img.dtype
	if x is list:
		npts = len(x)
		xcen = [0*i - 1 for i in x] 
		ycen = [0*i - 1 for i in y]
		ix = [round(i) for i in x] #central x pixel
		iy = [round(i) for i in y] #central y pixel
	else:
		npts = 1
		xcen = [-1]
		ycen = [-1]
		ix = [round(x)]
		iy = [round(y)]
		x = [x]
		y = [y]

	maxbox = 13

	radius = 0.637*FWHM > 2.001			#radius is 1.5 sigma
	if radius == False:
		radius = 2.001
	else:
		radius = 0.637*FWHM

	radsq = radius**2.
	sigsq = (FWHM / 2.35482)**2.
	nhalf = int(radius) < (maxbox-1)//2
	if nhalf == False:
		nhalf = (maxbox-1)//2
	else:
		nhalf = int(radius)
	nbox = 2 * nhalf + 1				
	#number of pixels inside of convolution box

	# Create the gaussian convolution kernel in variable "g"
	mask = np.zeros((nbox, nbox))
	g = np.zeros((nbox, nbox))

	row2 = (np.arange(nbox) - nhalf)**2.
	
	for i in range(0,nhalf+1): 
	# +1 because python does not include the last number
		temp = row2 + i**2.
		g[nhalf - i, :] = temp
		g[nhalf + i, :] = temp
			
	mask = np.where( g >= radsq, mask, 1) #replaces everything that does not meet this condition with 1, if it meets it, uses 0

	good = (mask == 1.)

	g = np.exp(-0.5*g/sigsq) #make g into a gaussian kernal

	'''
	In fitting Gaussians to the marginal sums, pixels will arbitrarily be 
	assigned weights ranging from unity at the corners of the box to 
	NHALF^2 at the center (e.g. if NBOX = 5 or 7, the weights will be
	
	                              1   2   3   4   3   2   1
	   1   2   3   2   1          2   4   6   8   6   4   2
	   2   4   6   4   2          3   6   9  12   9   6   3
	   3   6   9   6   3          4   8  12  16  12   8   4
	   2   4   6   4   2          3   6   9  12   9   6   3
	   1   2   3   2   1          2   4   6   8   6   4   2
	
	respectively).  This is done to desensitize the derived parameters to 
	possible neighboring, brighter stars.
	'''

	x_wt = np.zeros((nbox,nbox))
	wt = nhalf - np.absolute(np.arange(nbox) - nhalf) + 1

	for i in range(0, nbox):
		x_wt[i,:] = wt

	y_wt = x_wt.T

	pixels = np.count_nonzero(good == 1)
	
	if keepcenter == False:
		c = g*mask #pre-compute convolution kernal
		sumc = np.sum(c)
		sumcsq = np.sum(np.square(c)) - (sumc**2.)/pixels
		sumc /= pixels
		c[good] = (c[good] -sumc)/sumcsq

	
	for i in range(npts):
		if keepcenter == False:
			if ((ix[i] < nhalf) or (ix[i] + nhalf > xsize -1) or (iy[i] < nhalf) or 
				(iy[i] + nhalf > ysize -1)):
				if silent == False:
					print("Position " + str(x[i]) + "," + str(y[i]) + " too near edge of image")
				continue

			x1 = ix[i] - nbox > 0
			if x1 == True:
				x1 = ix[i] - nbox
			else:
				x1 = 0

			x2 = ix[i] + nbox < xsize -1
			if x2 == True:
				x2 = ix[i] + nbox
			else:
				x2 = xsize - 1

			y1 = iy[i] - nbox > 0
			if y1 == True:
				y1 = iy[i] - nbox
			else:
				y1 = 0

			y2 = iy[i] + nbox < ysize -1
			if y2 == True:
				y2 = iy[i] + nbox
			else:
				y2 = ysize - 1

			h = img[int(y1):int(y2+1),int(x1):int(x2+1)].T
			h = ndimage.convolve(h, c, mode = 'constant',origin = 0, cval=0.0) 
			#not the same as the IDL routine. Might not be a good solution for all 
			#instances. Will have to check it more thoroughly in the future.
			h = h[nbox-nhalf: (nbox + nhalf)+1, nbox -nhalf: (nbox + nhalf)+1]

			d = img[int(iy[i]-nhalf): int((iy[i]+nhalf)+1), int(ix[i] - nhalf) 
				: int((ix[i] + nhalf)+1)].T


			if maxgood != False:
				ig = np.where(d < maxgood)
				ng = np.count_nonzero(d < maxgood)
				mx = np.amax(d[ig])
			else:	
				mx = np.amax(h) #max pixel value

			mx_pos = np.where(h == mx) #positions of max value

			#print(mx)
			#print(h[mx_pos[1],mx_pos[0]])

			Nmax = np.count_nonzero(h == mx) #number of pixels with max value

			if Nmax > 1: #more than 1 pixel at maximum?
				idx = round(np.sum(mx_pos[0])/Nmax)
				idy = round(np.sum(mx_pos[1])/Nmax)
			else:
				idx = mx_pos[0]
				idy = mx_pos[1]
			xmax = ix[i] - nhalf + idx #x coordinate in original image
			ymax = iy[i] - nhalf + idy #y coordinate in original image

		else:
			xmax = ix[i]
			ymax = iy[i]

			#check *new* center location for range
			#added by Hogg

		if ((xmax < nhalf) or (xmax + nhalf > xsize -1) or (ymax < nhalf) 
			or (ymax + nhalf > ysize -1)):
			if silent == False:
				print("Position ", x[i], y[i], "moved too near edge of image")
			xcen[i] = -1 
			ycen[i] = -1
			continue

		#Extract subimage centered on maximum pixel

		d = img[int(ymax-nhalf) : int((ymax+nhalf)+1), int(xmax - nhalf) : int((xmax+nhalf)+1)]


		if debug == True:
			print("Subarray used to compute centroid:")
			print()
			print(d)
			#print(int(xmax-nhalf), int((xmax+nhalf)+1), int(ymax - nhalf),int((ymax+nhalf)+1))
			print()

		if maxgood != False:
			mask = (d < maxgood)

		elif dtype == ">f4":
			mask = np.where(np.isfinite(d) == False, mask, 1.)
			mask = np.where(np.isfinite(d) == True, mask, 0.)
		else:
			mask = np.ones((nbox,nbox))

		maskx = np.sum(mask, axis = 0) > 0
		masky = np.sum(mask, axis = 1) > 0

		#at least 3 points are needed in the partial sum to compute the gaussian
		if (sum(maskx) < 3) or (sum(masky) < 3):
			if silent == False:
				print("Position ", x[i], y[i], "has insufficient good points")
			continue

		ywt = y_wt*mask
		xwt = x_wt*mask
		wt1 = wt*maskx
		wt2 = wt*masky

		'''
		Centroid computation:   The centroid computation was modified in 
		Mar 2008 and now differs from DAOPHOT which multiplies the 
		correction dx by 1/(1+abs(dx)). The DAOPHOT method is more robust 
		(e.g. two different sources will not merge) especially in a 
		package where the centroid will be subsequently be redetermined 
		using PSF fitting. However, it is less accurate, and introduces
		biases in the centroid histogram. The change here is the same made 
		in the IRAF DAOFIND routine (see http://iraf.net/article.php?story=7211&query=daofind )
		'''
		sd = np.sum(d.T*ywt, axis = 0)
		sg = np.sum(g*ywt, axis = 0)
		sumg = round(np.sum(wt1*sg),4)
		sumgsq = round(np.sum(wt1*sg*sg),4)

		sumgd = round(np.sum(wt1*sg*sd),3)
		sumgy = round(np.sum(wt1*sg),3)
		sumd = round(np.sum(wt1*sd),3)
		p = round(np.sum(wt1),3)

		yvec = nhalf - np.arange(nbox, dtype=float)
		dgdy = sg*yvec
		sdgdys = round(np.sum(wt1*(dgdy**2.)),4)
		sdgdy = round(np.sum(wt1*dgdy),4)

		sddgdy = round(np.sum(wt1*sd*dgdy),4)
		sgdgdy = np.sum(wt1*sg*dgdy)

		hy = (sumgd - sumg*sumd/p) / (sumgsq - (sumg**2.)/p)

		#hx is the height of the best-fitting marginal Gaussian. If this 
		#is not positive then the centroid does not make sense

		if hy < 0:
			if silent == False:
				print("Position", x, y, " cannot be fit by a gaussian")
			xcen[i] = -1
			ycen[i] = -1
			continue

		skylvl = (sumd - hy*sumg)/p
		

		dy = (sgdgdy - (sddgdy-sdgdy*(hy*sumg + skylvl*p))) / (hy*sdgdys/sigsq)

		if np.absolute(dy) > nhalf:
			if silent == False:
				print("Position", x, y, " is too far from initial guess")
			continue

		ycen[i] = ymax + dy

		#now repeat for y coord of centroid

		sd = np.sum(d.T*xwt, axis = 1)
		sg = np.sum(g*xwt, axis = 1)
		sumg = np.sum(wt2*sg)
		sumgsq = np.sum(wt2*sg*sg)

		sumgd = np.sum(wt2*sg*sd)
		sumd = np.sum(wt2*sd)
		p = np.sum(wt2)
		xvec = nhalf - np.arange(nbox, dtype = float)

		dgdx = sg*xvec
		sdgdxs = np.sum(wt2*dgdx**2.)
		sdgdx = np.sum(wt2*dgdx)
		sddgdx = np.sum(wt2*sd*dgdx)
	
		sgdgdx = np.sum(wt2*sg*dgdx)
		hx = (sumgd - sumg*sumd/p) / (sumgsq - (sumg**2.)/p)
		if hx < 0:
			if silent == False:
				print("Position", x, y, " cannot be fit by a gaussian")
			continue

		skylvl = (sumd - hx*sumg)/p
		dx = (sgdgdx - (sddgdx - sdgdx*(hx*sumg + skylvl*p))) / (hx*sdgdxs/sigsq)

		if np.absolute(dx) > nhalf:
			if silent == False:
				print("Position", x, y, " is too far from initial guess")
			continue

		xcen[i] = xmax + dx #y centroid in original array
    
	if npts==1:
			xcen, ycen = float(xcen[0]), float(ycen[0])

	return xcen, ycen
