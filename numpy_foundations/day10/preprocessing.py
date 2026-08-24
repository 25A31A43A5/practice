import numpy as np

def validate_data(data:np.ndarray)->np.ndarray:
    if data.size>0 and data.ndim==2:
        return data
    else:
        raise ValueError("Data does not meet the standards")

def clean_data(data:np.ndarray)->np.ndarray:
    data=data.copy()
    data[(data<0)|(data>200)]=np.nan
    return data

def calculate_statistics(data:np.ndarray)->dict[str,np.ndarray]:
    return {"mean_values":np.nanmean(data,axis=0),
    "min_values":np.nanmin(data,axis=0),
    "max_values":np.nanmax(data,axis=0)}

def calculate_imputation_values(data:np.ndarray)->np.ndarray:
    return np.nanmean(data,axis=0)

def impute_data(data:np.ndarray,values:np.ndarray)->np.ndarray:
    data=data.copy()
    rows_to_change,cols_to_change=np.where(np.isnan(data))
    data[rows_to_change,cols_to_change]=values[cols_to_change]
    return data

def normalise_data(data:np.ndarray,statistic:dict[str,np.ndarray])->np.ndarray:

    scaled_data=(data-statistic["min_values"])/(statistic["max_values"]-statistic["min_values"])

    return scaled_data