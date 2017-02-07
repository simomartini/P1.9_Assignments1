#FIRST ASSGNMENTS P1.9 MHPC

import sys
from numpy import *
from pylab import * 

#print("Give me a Number for the function as input:\n")
if len(sys.argv)==1:
    print("USAGE:\n 1: f(x)=x;\n 2: f(x)=x^2;\n 3: f(x)=x^3;")
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
    yval=xval**2
elif f==3:
    yval=xval**3

plot(xval,yval)
show()
