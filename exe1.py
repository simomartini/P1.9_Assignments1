#FIRST ASSGNMENTS P1.9 MHPC

import sys
from numpy import *
from pylab import * 

#print("Give me a Number for the function as input:\n")
if len(sys.argv)==1:
    print("USAGE:\n 1: f(x)=x;\n 2: f(x)=x^2;\n 3: f(x)=x^3;\n 4: f(x)=sin(x);\n 5: f(x)=exp(x);\n 6: f(x)=tan(x);\n 7: f(x)=exp(x);\n 8: f(x)=sqrt(|x|)")
    sys.exit()
else:
    f=int(sys.argv[1])

start=-3.0
stop=3.0
step=0.1

xval=arange(start,stop,step)

if f==1:
    yval=xval
elif f==2:
    yval=xval**2
elif f==3:
    yval=xval**3
elif f==4:
    yval=sin(xval)
elif f==5:
    yval=exp(xval)
elif f==6:
    yval=tan(xval)
elif f==7:
    yval=exp(xval)
elif f==8:
    yval=sqrt(abs(xval))


plot(xval,yval)
show()
