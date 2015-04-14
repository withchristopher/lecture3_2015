import numpy
from matplotlib import pyplot as plt
#we can import functions we just wrote!
import func_example

x=numpy.arange(-1,1,0.002)
#functions are referenced by the file they're in
y=func_example.mygauss(x,cent=0.5,sig=0.05)
#we can assign the function to a variable
gg=func_example.mygauss
y2=gg(x,cent=0.5,sig=0.05)
delt=numpy.abs(y2-y)
print 'error is ' + repr(delt.sum())
#will output:
#error is 0.0
plt.plot(x,y,'r')
plt.show()
