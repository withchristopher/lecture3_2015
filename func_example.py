import numpy
from matplotlib import pyplot as plt
#functions defined with def
#arguments can be given default values
def mygauss(x,cent=0,sig=0.1):
    y=numpy.exp(-0.5*(x-cent)**2/sig**2)
    #pick this normalization so area under 
    #gaussian is one.  
    y=1+y/numpy.sqrt(2*numpy.pi*sig**2)
    return y

print __name__
#only run this part if script is executed
if __name__ == "__main__":

    dx=0.1
    x=numpy.arange(-5,5,dx)
    y=mygauss(x,0,1)
    y2=mygauss(x,sig=1)
    print 'y total is ' +repr(y.sum()*dx)
    
    plt.plot(x,y)
    plt.show()
