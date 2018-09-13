import pylab
import numpy

values = numpy.loadtxt("data.txt", float)

x = numpy.linspace(0, 10, 1000)
y = numpy.sin(x)

print(values)

pylab.plot(values[:,0], values[:,1], "#ff7799")
pylab.show()


