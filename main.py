import numpy as np
import matplotlib.pyplot as plt
f = open("values.txt", "r") ## opens up and reads the file
f.readline()

r = []
v = []
dR = []
dV = []
m = []
predictedV = []
G = 4.3*(10**-6)

for line in f:
  r.append(float(line.split("\t")[0]))
  v.append(float(line.split("\t")[1]))
  dR.append(line.split("\t")[2])
  dV.append(float(line.split("\t")[3]))
  m.append(float(line.split("\t")[4]))
  predictedV.append(((float(G))*(float(line.split('\t')[4]))/(float(line.split('\t')[0])))**(1/2))

x = np.array(r)
y = np.array(v)
y1 = np.array(predictedV)


plt.plot(x,y)
plt.plot(x,y1)
plt.show()