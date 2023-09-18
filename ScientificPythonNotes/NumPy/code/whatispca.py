import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


def draw_vector(v0, v1, ax=None):
    ax = ax or plt.gca()
    arrowprops=dict(arrowstyle='->',
                    linewidth=2,
                    shrinkA=0, shrinkB=0)
    ax.annotate('', v1, v0, arrowprops=arrowprops)

def run():
#pca = PCA(n_components=2)
#pca.fit(X)
 rng = np.random.RandomState(1)
 X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T
 pca = PCA(n_components=2, whiten=True)
 pca.fit(X)
 
 fig, ax = plt.subplots(1, 2, figsize=(16, 6))
 fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)
 
 # plot data
 ax[0].scatter(X[:, 0], X[:, 1], alpha=0.2)
 for length, vector in zip(pca.explained_variance_, pca.components_):
     v = vector * 3 * np.sqrt(length)
     draw_vector(pca.mean_, pca.mean_ + v, ax=ax[0])
 ax[0].axis('equal');
 ax[0].set(xlabel='x', ylabel='y', title='input')
 
 # plot principal components
 X_pca = pca.transform(X)
 ax[1].scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.2)
 draw_vector([0, 0], [0, 3], ax=ax[1])
 draw_vector([0, 0], [3, 0], ax=ax[1])
 ax[1].axis('equal')
 ax[1].set(xlabel='component 1', ylabel='component 2',
           title='principal components',
           xlim=(-5, 5), ylim=(-3, 3.1))
 
 plt.show()



def run2():

 rng = np.random.RandomState(1)
 X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T
# rng = np.random.RandomState(1)
 #X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T
 #pca = PCA(n_components=2, whiten=True)
 #pca.fit(X)

 pca = PCA(n_components=1)
 pca.fit(X)
 X_pca = pca.transform(X)
 


 X_new = pca.inverse_transform(X_pca)
 plt.scatter(X[:, 0], X[:, 1], alpha=0.2)
 plt.scatter(X_new[:, 0], X_new[:, 1], alpha=0.8)
 plt.axis('equal')
 plt.show()

 
