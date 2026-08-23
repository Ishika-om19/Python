#2nd Example of List using numpy
import numpy
templist=[35.7,40.2,37.1,38.3,30.5,36.4,39.5]
maxtemp= max(templist)
mintemp= min(templist)
#average = sum(templist)/len(templist)
print("Maximum Temp = %.2f" %maxtemp)
print("Minimum Temp = %.2f" %mintemp)
print("average Temp = %.2f" %numpy.mean(templist))
