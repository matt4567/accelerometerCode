import numpy
import matplotlib.pyplot as plt
import math
import time


def openFile(fileName):
    return open(fileName)

def createDistBins(start, finish, resolution):
    bins = []
    n = start
    while (n <=finish):
        bins.append(round(n, 2))
        n+=resolution
    density = numpy.zeros(len(bins))
    return (bins, density)

def findBin(x, resolution):
    # todo - find nicer way of expression 2 - we want the number of decimal places.
    return round(math.floor(x/resolution) * resolution, 2)

def fillBins(file, bins, density, resolution, index):
    vals = []
    for i in file:
        x_val = float(i.split(" ")[index])
        #finding bin doesn't work for 9.79 as it rounds down after the multiplication. 
        x_bin = findBin(x_val, resolution)
        binIndex = findVal(bins, x_val)
        if (binIndex != None):
            density[binIndex] += 1
        vals.append(x_val)

    return (density, vals)

def findStandardDev(vals):
    a = numpy.array(vals)
    mean = numpy.mean(a, axis=0)
    standardDevString = "Standard deviation: " + str(numpy.std(a, axis=0))
    meanStr = "Mean is: " + str(mean)
    scaling = mean/9.81
    scalingStr = "Assuming gravity to be 9.81 the scaling is: " + str(scaling)
    
    print(meanStr)
    print(scalingStr)
    
    print(standardDevString)
    
def findVal(bins, pos):
    for index, value in enumerate(bins):
        if (value == pos):
            return index
    return None

def plotDist(fileName, start, finish, resolution, index):
    file = openFile(fileName)
    (bins, density) = createDistBins(start, finish, resolution)
    (density, vals) = fillBins(file, bins, density, resolution, index)
    findStandardDev(vals)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(bins, density)
    plt.title("Noise distribution of x axis if digital accelerometer")
    plt.xlabel("Noise value")
    plt.ylabel("Number of counts")
    ax.text(2, 9, "test", fontsize = 12)
    fig.savefig('scalingZ.png')
    plt.show()

