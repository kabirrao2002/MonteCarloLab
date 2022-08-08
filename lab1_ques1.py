import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame(columns = ['X0','a,b,m','Numbers','Distinct values before repitition'] )


for x0 in range(0,11):
    numbers = []
    x = (6*x0)%11
    
    t = x
    numbers.append(t)
    x = (6*x)%11
    while x!=t:
        numbers.append(x)
        x = (6*x)%11
    distinct = len(numbers)
    row = {'X0':x0,'a,b,m':'6,0,11','Numbers':tuple(numbers),'Distinct values before repitition':distinct}
    df = df.append(row,ignore_index=True)
    
for x0 in range(0,11):
    numbers = []
    x = (3*x0)%11
    
    t = x
    numbers.append(t)
    x = (3*x)%11
    while x!=t:
        numbers.append(x)
        x = (3*x)%11
    distinct = len(numbers)
    row = {'X0':x0,'a,b,m':'3,0,11','Numbers':tuple(numbers),'Distinct values before repitition':distinct}
    df = df.append(row,ignore_index=True)
print(df)