# _Python for Scientific Data Analysis_

## Homework - Week 11 (due November 15)


### 1. Project Update 

* Please give me a **short** update on the progress of your class project.  In particular, I would like to see ...

- A description of the current status of your project
- Items where you are getting stuck (if any)/questions you may have
- Any plots or graphics you have produced beyond those from last week's homework.


### 2. Reading in Fits Files

* read in 'keckimage.fits'
* save the image array as a variable, save the header as a variable
* from the header, return the keyword values for the altitude and azimuth of the telescope during this exposure
* use i) a NumPy function call to return a value for the dimensions of the image and ii) an astropy function call to return a value for the dimensions of the image


### 3. Reading in Fits Files

* read in the data cube `adi_oct172021.fits'
* return the keyword value for aperture radius in the third slice (here the first slice is indexed as 0)
* compute the pixel value of the cube at for the 10th slice (indexed from 0) at x=82, y=79.  
* What are the flux density units of the cube?


### 4. Writing Fits Files
* take the median of 'adi_oct172021.fits' across all wavelengths
* save as a new fits file called 'median_adi_oct172021.fits' with the previous fits header information retained.


### 5. (grad students only) Animations

Start with the animation ex1_6.gif. 

 Edit the source code to create a gif or a movie that prints a) a label at the top-left saying ``Exoplanet HIP 99770 b`` on the top line and ``SCExAO/CHARIS`` on teh second line and a counter at the bottom-left reading ``Wavelength Slice [Number]`` where the number increments by 1 with each slice.  See the attached file ``problem3.mp4`` for an example.
 
 Hints:
 
 * with each frame in the animation the original source code in my notes appends ``im`` which is an ``axes.imshow`` call (i.e. appends an image frame).   To get markups added, you also need to append them with each loop.
 
 * think carefully about _where_ you add the wavelength labeling in your source code.