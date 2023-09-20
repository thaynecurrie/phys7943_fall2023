import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

from sklearn.datasets import load_digits
from sklearn.decomposition import PCA


def run(numpca=2):

 digits=load_digits()
 digits.data.shape

#plot stuff

 # set up the figure
 fig = plt.figure(figsize=(6, 6))  # figure size in inches
 fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# plot the digits: each image is 8x8 pixels
 for i in range(64):
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
    
    # label the image with the target value
    ax.text(0, 7, str(digits.target[i]))

 plt.show()
 
 pca = PCA(n_components=numpca)  # project from 64 to 2 dimensions
 projected = pca.fit_transform(digits.data)
 #print(digits.data.shape)
 #print(projected.shape)
 
 plt.scatter(projected[:, 0], projected[:, 1],
             c=digits.target, edgecolor='none', alpha=0.5,
             cmap=plt.cm.get_cmap('nipy_spectral', 10))
 plt.xlabel('component 1')
 plt.ylabel('component 2')
 plt.colorbar()
 
 plt.show()
 pca = PCA(n_components=18)
 Xproj = pca.fit_transform(digits.data)
 sns.set_style('white')

 print(Xproj[10].shape)
 fig = plot_pca_components(digits.data[10], Xproj[10],
                           pca.mean_, pca.components_)
 
 
 plt.show()
 #exit()
 
 pca = PCA().fit(digits.data)
 plt.plot(np.cumsum(pca.explained_variance_ratio_))
 plt.xlabel('number of components')
 plt.ylabel('cumulative explained variance')


def plot_pca_components(x, coefficients=None, mean=0, components=None,
                        imshape=(8, 8), n_components=8, fontsize=10,
                        show_mean=True):
    if coefficients is None:
        coefficients = x
        
    if components is None:
        components = np.eye(len(coefficients), len(x))
        
    mean = np.zeros_like(x) + mean
        

    fig = plt.figure(figsize=(1.2 * (5 + n_components), 1.2 * 2))
    g = plt.GridSpec(2, 4 + bool(show_mean) + n_components, hspace=0.3)

    def show(i, j, x, title=None):
        ax = fig.add_subplot(g[i, j], xticks=[], yticks=[])
        ax.imshow(x.reshape(imshape), interpolation='nearest')
        if title:
            ax.set_title(title, fontsize=fontsize)

    show(slice(2), slice(2), x, "True")
    
    approx = mean.copy()
    
    counter = 2
    if show_mean:
        show(0, 2, np.zeros_like(x) + mean, r'$\mu$')
        show(1, 2, approx, r'$1 \cdot \mu$')
        counter += 1

    for i in range(n_components):
        approx = approx + coefficients[i] * components[i]
        show(0, i + counter, components[i], r'$c_{0}$'.format(i + 1))
        show(1, i + counter, approx,
             r"${0:.2f} \cdot c_{1}$".format(coefficients[i], i + 1))
        if show_mean or i > 0:
            plt.gca().text(0, 1.05, '$+$', ha='right', va='bottom',
                           transform=plt.gca().transAxes, fontsize=fontsize)

    show(slice(2), slice(-2, None), approx, "Approx")
    return fig

