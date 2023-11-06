# _Python for Scientific Data Analysis_

## Homework - Week 11 (due November 8)


### 1. Project Update 

* Please give me a **short** update on the progress of your class project.  In particular, I would like to see ...

- A description of the current status of your project
- Items where you are getting stuck (if any)/questions you may have
- Any plots or graphics you have produced beyond those from last week's homework.


### 2. Shadings/Fill-Between Plots

* read in files for spectra for HIP 99770 b and HD 33632 Ab.  The columns are: Wavelength (microns), Flux Density (mJy), uncertainty in Flux Density (mJy), Signal-to-noise Ratio

* scale the HD 33632 Ab spectrum so that the mean value of its spectrum and HIP 99770 b's spectrum are the same (using np.mean).

You will produce two side-by-side panels:

Panel 1

* Use the plt.plot to produce a line plot _with_ symbols corresponding to individual data points
* Use the fill-between function to shade in regions +/- the uncertainties
* Add a legend and adjust the axes formatting to thicken the spines, add labels, and add 5 minor tick marks in between major ticks

Panel 2

* Same as panel 1 except you are doing simple error bar plots, not fill-between.

The resulting figure should look as follows:

![](./prob2.png)