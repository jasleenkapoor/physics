import numpy as np
import math
import matplotlib.pyplot as plt

i = open('values.txt', 'r')
i.readline()
r = []
Dm = []
Vm = []
combinedM = []

firstsum = 4*(math.pi)*(1*(10**8))*((1.87)**2) 

for line in i:
  r.append(float(line.split('\t')[0]))
  Vm.append(float(line.split('\t')[4]))
  trig = math.atan((float(line.split('\t')[0])/(1.87)))
  secondsum = ((float(line.split('\t')[0])) - ((1.87)*(trig)))
  wholesum = (4*(math.pi)*(1*(10**8))*((1.87)**2)*(((float(line.split('\t')[0])) - ((1.87)*(trig)))))
  #wholesum = (firstsum)*(secondsum)
  Dm.append((4*(math.pi)*(1*(10**8))*((1.87)**2)*(((float(line.split('\t')[0])) - ((1.87)*(trig))))))
  combinedM.append((float(line.split('\t')[4]))+((4*(math.pi)*(1*(10**8))*((1.87)**2)*(((float(line.split('\t')[0])) - ((1.87)*(trig)))))))
  #combinedM.append(((4*(math.pi)*(1*(10**8))*((1.87)**2) )*(((float(line.split('\t')[0]))-((1.87)*(trig))))))


x= np.array(r)
y= np.array(Vm)
y1= np.array(Dm)
combinedM = np.array(combinedM)

plt.plot(x,combinedM)
plt.plot(x,y)
plt.plot(x,y1)
plt.show()