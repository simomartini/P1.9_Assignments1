#FIRST ASSGNMENTS P1.9 MHPC

import sys
from numpy import *
from pylab import * 

#print("Give me a Number for the function as input:\n")
if len(sys.argv)==1:
    print("USAGE:\n 1: f(x)=x;\n 2: f(x)=sin(x);\n 3: f(x)=exp(x);\n 4: f(x)=tan(x);")
    sys.exit()
else:
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
