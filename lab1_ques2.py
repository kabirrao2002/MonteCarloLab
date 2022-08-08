import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame()
values_of_x0 = [10,21,3,8,51]

def count(list1, l, r):
    c = 0
    # traverse in the list1
    for x in list1:
        # condition check
        if x>= l and x< r:
            c+= 1
    return c

list_of_list = []
list_of_list1 = []
for xx in values_of_x0:
    ui = []
    ui1 = []
    x0 = xx
    

    x = (1597*x0)%244944
    u = x/244944
    ui.append(u)
    w =u
    x = (1597*x)%244944
    u = x/244944
    ui.append(u)

    x1 = (51749*x0)%244944
    u1 = x1/244944
    ui1.append(u1)
    w1 =u1
    x1 = (51749*x1)%244944
    u1 = x1/244944
    ui1.append(u1)

    i = 3
    while i<10001:
        x = (1597*x)%244944
        u = x/244944
        ui.append(u)
        i=i+1

    i = 3
    while i<10001:
        x1 = (51749*x1)%244944
        u1 = x1/244944
        ui1.append(u1)
        i=i+1

    f = []
    g = []
    f1 = []
    g1 = []
    i =0.00
    while i<1:
        k = count(ui,i,i+0.05)
        f.append(k)
        e = str(round(i,2))+'-'+str(round(i+0.05,2))
        g.append(e)

        k1 = count(ui1,i,i+0.05)
        f1.append(k1)
        e1 = str(round(i,2))+'-'+str(round(i+0.05,2))
        g1.append(e1)

        i = i+0.05

    list_of_list.append(f)
    list_of_list1.append(f1)

    if x0 ==10:
        df['Range'] = g
    
    fig, ax=plt.subplots(figsize=(18,5))

    x_axis = np.arange(len(g))
    x_axis1 = np.arange(len(g1))

    ax.bar(x_axis -0.2,f,width=0.4,label='For a = 1597',color = 'grey')
    ax.bar(x_axis1 +0.2,f1,width=0.4,label='For a = 51749',color='blue')
    ax.set_title('For x0 = '+str(xx))
    ax.set_xticks(x_axis)
    ax.set_xticklabels(g,rotation = 'vertical')
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Ranges')
    ax.legend()
    #plt.show()

i =0
for it in values_of_x0:
    df['FOR x0 = '+ str(it)] = list_of_list[i]
    i = i+1

i =0
for it in values_of_x0:
    df['For x0 = '+ str(it)] = list_of_list1[i]
    i = i+1

df.to_csv('table_ques2_1.csv')

print(df)








