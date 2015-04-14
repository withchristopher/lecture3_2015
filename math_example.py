import math
from math import sin

#you *can* do this.  But don't!
from math import sin as cos
for x in range(0,10):
    print [x,math.sin(x),sin(x),cos(x)]

