import time
import matplotlib.pyplot as plt
import findvalues as fv

ifcontinue = 'Y'
xpoints = []
ypoints = []


print('Hello, This is The Geometric SpiderWeb of The Web!!!!!!')
time.sleep(1.5)
while True:
    point = input('What point do you want on the graph? Say answer as a point (x,y) : ')
    xvalue = fv.findx(point)
    yvalue = fv.findy(point)
    xpoints.append(xvalue)
    ypoints.append(yvalue)
    ifcontinue = input('Is that all? Y/N : ')

    if ifcontinue == 'Y':
        ifstop = input('Do You want to run? Y/N : ')
        if ifstop == 'N':
            quit()
        else:
            break

plt.plot(xpoints, ypoints)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('The SpiderWeb of the Web!!!')
 
# function to show the plot
plt.show()