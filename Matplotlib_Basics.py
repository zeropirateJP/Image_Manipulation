
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use("fivethirtyeight")
'''
x1 = [2,4,5]
x2 = [4,7,2]
y1 = [4,5,6]
y2 = [3,4,7]

plt.plot(x1,y1,label="First line",color='r')
plt.plot(x2,y2, label="Seconf Line",color='b')
plt.legend()
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()
'''

def create_plots():
    x=[]
    y=[]
    for i in range(10):
        x.append(i)
        y.append(random.randrange(10))
    return x, y

#create figure
fig = plt.figure()
#create subplots (height,width,plot)
axis1 = fig.add_subplot(211)
axis2 = fig.add_subplot(212)
x,y =create_plots()
axis1.plot(x,y,label='Line1',color='r')
axis1.legend()
x,y =create_plots()
axis2.plot(x,y,label='Line2',color='b')
axis2.legend()
plt.show()
