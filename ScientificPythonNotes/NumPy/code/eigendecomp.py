import numpy as np
import matplotlib.pyplot as plt

def ex1():
 # some matrix
 M  = np.array([ [2,3],[2,1] ])
 x  = np.array([ [1,1.5] ]).T # transposed into a column vector!
 Mx = M.dot(x)
 
 
 plt.figure(figsize=(6,6))
 
 plt.plot([0,x[0,0]],[0,x[1,0]],'k',linewidth=4,label='x')
 plt.plot([0,Mx[0,0]],[0,Mx[1,0]],'--',linewidth=3,color=[.7,.7,.7],label='Mx')
 plt.xlim([-7,7])
 plt.ylim([-7,7])
 plt.legend()
 plt.grid()
 plt.savefig('Figure_05_05a.png',dpi=300)
 plt.show()
 
 
 M  = np.array([ [2,3],[2,1] ])
 v  = np.array([ [1.5,1] ]).T # transposed into a column vector!
 Mv = M.dot(v)
 
 
 plt.figure(figsize=(6,6))
 
 plt.plot([0,v[0,0]],[0,v[1,0]],'k',linewidth=4,label='v')
 plt.plot([0,Mv[0,0]],[0,Mv[1,0]],'--',linewidth=3,color=[.7,.7,.7],label='Mv')
 plt.xlim([-7,7])
 plt.ylim([-7,7])
 plt.legend()
 plt.grid()
 plt.savefig('Figure_05_05b.png',dpi=300)
 plt.show()     

def ex2():
 


 # in 2D of course, for visualization
 
 # the matrix
 M = np.array([ [-1,1],
                [-1,2] ])
 
 # its eigenvalues and eigenvectors
 eigenvalues,eigenvectors = np.linalg.eig(M)
 print(eigenvalues)
 
 # some random vectors
 notEigenvectors = np.random.randn(2,2)
 
 # multipy to create new vectors
 Mv = M.dot(eigenvectors)
 Mw = M.dot(notEigenvectors)
 
 
 
 ## and now plot
 _,axs = plt.subplots(1,2,figsize=(10,6))
 
 # the two eigenvectors
 axs[0].plot([0,eigenvectors[0,0]],[0,eigenvectors[1,0]],'k',linewidth=2,label='v1')
 axs[0].plot([0,Mv[0,0]],[0,Mv[1,0]],'k--',linewidth=2,label='Mv1')
 
 axs[0].plot([0,eigenvectors[0,1]],[0,eigenvectors[1,1]],'r',linewidth=2,label='v2')
 axs[0].plot([0,Mv[0,1]],[0,Mv[1,1]],'r--',linewidth=2,label='Mv2')
 
 # the two non-eigenvectors
 axs[1].plot([0,notEigenvectors[0,0]],[0,notEigenvectors[1,0]],'k',linewidth=2,label='w1')
 axs[1].plot([0,Mw[0,0]],[0,Mw[1,0]],'k--',linewidth=2,label='Mw1')
 
 axs[1].plot([0,notEigenvectors[0,1]],[0,notEigenvectors[1,1]],'r',linewidth=2,label='w2')
 axs[1].plot([0,Mw[0,1]],[0,Mw[1,1]],'r--',linewidth=2,label='Mw2')
 
 
 # adjust the graphs a bit
 for i in range(2):
   axs[i].axis('square')
   axs[i].set_xlim([-1.5,1.5])
   axs[i].set_ylim([-1.5,1.5])
   axs[i].grid()
   axs[i].legend()
 
 #plt.savefig('Figure_13_01.png',dpi=300)
 plt.show()

def ex3():
 import numpy as np
 import matplotlib.pyplot as plt
 
 plt.style.use('seaborn-poster')
 
 import matplotlib.pyplot as plt
 
 A = np.array([[2, 0],[0, 1]])
 
 x = np.array([[1],[1]])
 b = np.dot(A, x)
 plot_vect(x,b,(0,3),(0,2))

#different version
 x = np.array([[1], [0]])
 b = np.dot(A, x)

 plot_vect(x,b,(0,3),(-0.5,0.5))

def plot_vect(x, b, xlim, ylim):
    '''
    function to plot two vectors, 
    x - the original vector
    b - the transformed vector
    xlim - the limit for x
    ylim - the limit for y
    '''
    plt.figure(figsize = (10, 6))
    plt.quiver(0,0,x[0],x[1],\
        color='k',angles='xy',\
        scale_units='xy',scale=1,\
        label='Original vector')
    plt.quiver(0,0,b[0],b[1],\
        color='g',angles='xy',\
        scale_units='xy',scale=1,\
        label ='Transformed vector')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()
