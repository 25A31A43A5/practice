import numpy as np

def get_data()->np.ndarray:
    return  np.array([
                    [7, 2, 11],
                    [14, 5, 1],
                    [9, 13, 4],
                    [3, 15, 8],
                    [12, 6, 10]
                    ])

def filter_array(data:np.ndarray)->np.ndarray:

    return data[(data>5)&(data<8)]

def replace_with_mask(data:np.ndarray)->np.ndarray:
    data=data.copy()
    data[(data>5)&(data<8)]=0
    return data

def reshape_data(data:np.ndarray,shape:tuple)->np.ndarray:
    return data.reshape(shape)

def transpose_data(data:np.ndarray)->np.ndarray:
    return np.transpose(data,(1,0))

def split_data(data:np.ndarray)->dict:
    return {"vsplit":np.vsplit(data,5),"hsplit":np.hsplit(data,3)}

def ravel_data(data:np.ndarray)->np.ndarray:
    return data.ravel()

def flatten_data(data:np.ndarray)->np.ndarray:
    return data.flatten()

def combine_data(data1:np.ndarray,data2:np.ndarray)->dict:
    return {"concatenate_axis_0":np.concatenate((data1,data2),axis=0),"concatenate_axis_1":np.concatenate((data1,data2),axis=1),"vstack":np.vstack((data1,data2)),"hstack":np.hstack((data1,data2)),"stack":np.stack((data1,data2),axis=0)}