import numpy as np 
import matplotlib.pyplot as plt 

f = open('values.txt', 'r') 
f.readline()
x =  []
y=   []

for line in f:
  x.append(float(line.split('\t')[0]))
  y.append(float(line.split('\t')[1]))

plt.plot(x,y)
plt.title('A graph of velocity(km/h) against radius(kpc)')
plt.xlabel('radius(kpc)')
plt.ylabel('velocity(km/h)')
plt.show()