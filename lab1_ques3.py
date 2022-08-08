import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

xaxis = []
yaxis = []
x0 = 100
x = (1229*x0+1)%2048
u = x/2048
xaxis.append(u)
for i in range (1,10001):
    x = (1229*x+1)%2048
    u = x/2048
    xaxis.append(u)
    yaxis.append(u)
xaxis.pop()
plt.scatter(xaxis,yaxis)
plt.title('Question 3: Two Dimensional Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()