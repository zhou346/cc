import numpy as np
data = np.genfromtxt('dataset_uci\\final_X_train.txt',delimiter=',',dtype=float)
# data = np.expand_dims(data, axis=2)
# data = np.expand_dims(data, axis=1)\
data = data[:,0:16]
data_tmp = []
for i in range(len(data)):
    data_tmp.append(np.array_split(data[i], 4))
# data = np.array_split()

data = np.array(data_tmp)
np.save("filename.npy",data_tmp)
print(data)