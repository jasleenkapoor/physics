import numpy as numpy
import math

i = open('values.txt', 'r')
i.readline()
r = []
mass = []

for line in i:
  r.append(float(line.split('\t')[0]))



firstsum = 4*(math.pi)*(1*(10**8))*((1.87)**2)

for f in r:
  trig = math.atan(f/(1.87))
  secondsum = f-((1.87)*(trig))
  wholesum = (firstsum)*(secondsum)
  mass.append(wholesum)


print(mass)