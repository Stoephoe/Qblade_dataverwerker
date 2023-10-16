import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


cP_handle="Data/cP.csv"
cT_handle="Data/cT.csv"

min_a=-24
max_a=24
interval=2


a_df=np.linspace(min_a,max_a,int((abs(min_a)+abs(max_a))/interval)+1)
cP_data=np.array(pd.read_csv(cP_handle,sep=';',skiprows=2))

DelIndexArray=(np.linspace(1,(np.shape(cP_data)[1]),(np.shape(cP_data)[1]),endpoint=False)).astype(int)
DelIndexArray=DelIndexArray[DelIndexArray%2==0]

cP_data=np.delete(cP_data,DelIndexArray,1)
cP_data=np.rot90(cP_data,1)


cP_data=np.delete(cP_data,[0,1],0)
print(cP_data)
print(np.shape(cP_data)[0])
cP_data=cP_data[cP_data[:,-1].argsort()]

print(cP_data)
df_cP = pd.DataFrame(cP_data)
df_cP.to_csv("cP_done.csv", index=False)

for i in range(0, (len(cP_data)-1)):
    plt.plot(cP_data[i], label= a_df[i])

plt.title("cP/Lambda")
plt.xlabel("Lambda")
plt.ylabel("cP")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()