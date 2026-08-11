import numpy as np

def get_data()->np.ndarray:
    return  np.array([
                [7, 2, 11],
                [14, 5, 1],
                [9, 13, 4],
                [3, 15, 8],
                [12, 6, 10]
                ])

def inspect_data(data:np.ndarray)->dict:
    return {"shape":data.shape,"ndim":data.ndim,"dtype":data.dtype,"size":data.size}

def calculate_statistics(data:np.ndarray)->dict:
    return {"mean":np.mean(data,axis=0),"sum":np.sum(data,axis=0),"max":np.max(data,axis=0),"min":np.min(data,axis=0),"std":np.std(data,axis=0)}

def transform_data(data:np.ndarray,statistics:dict)->dict:
    scaled_data=(data-statistics["min"])/(statistics["max"]-statistics["min"])
    centered_data=data-statistics["mean"]

    return {"scaled":scaled_data,"centered":centered_data}