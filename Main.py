import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



Dataset1="Cp"
Dataset2="Ct"
x_as="lambda"

min_a=-24
max_a=24
interval=2





a_df=np.linspace(min_a,max_a,int((abs(min_a)+abs(max_a))/interval)+1)

def Dataverwerker(Dataset):

    handle=("Data\\{Dataset}.csv".format(Dataset=Dataset))
    data=np.array(pd.read_csv(handle,sep=';',skiprows=2))

    DelIndexArray=(np.linspace(1,(np.shape(data)[1]),(np.shape(data)[1]),endpoint=False)).astype(int)
    DelIndexArray=DelIndexArray[DelIndexArray%2==0]

    data=np.delete(data,DelIndexArray,1)
    data=np.rot90(data,1)


    data=np.delete(data,[0,1],0)
    print(data)
    print(np.shape(data)[0])
    data=data[data[:,-1].argsort()]

    print(data)
    df = pd.DataFrame(data)
    df.to_csv("Results\\{Dataset}_clean.csv".format(Dataset=Dataset), index=False)

    
    plt.figure()

    for i in range(0, (len(data)-1)):
        plt.plot(data[i], label= a_df[i])

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xlabel(x_as)
    plt.ylabel(Dataset)
    plt.title("{Dataset}/{x_as}".format(Dataset=Dataset,x_as=x_as))
    plt.grid()

    return data

df1=Dataverwerker(Dataset1)
df2=Dataverwerker(Dataset2)

df3=np.divide(df1,df2)



df = pd.DataFrame(df3)
df.to_csv("Results\\df3.csv")

plt.figure()

for i in range(0, (len(df3)-1)):
        plt.plot(df3[i], label= a_df[i])

print(df3)
plt.show()

