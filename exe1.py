#FIRST ASSGNMENTS P1.9 MHPC

import sys
from numpy import *
from pylab import * 

#print("Give me a Number for the function as input:\n")
f=int(sys.argv[1])

start=-5.0
stop=5.0
step=0.1

xval=arange(start,stop,step)

if f==1:
    yval=xval
elif f==2:
    yval=sin(xval)
elif f==3:
    yval=exp(xval)
elif f==4:
    yval=tan(xval)

plot(xval,yval)
show()
