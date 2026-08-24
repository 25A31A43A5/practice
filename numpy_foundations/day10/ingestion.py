import csv 
import numpy as np
from pathlib import Path

def import_data(PATH=Path("sensor_data.csv"))->np.ndarray:
    data=[]
    try:
        with open(PATH,newline="") as file:
            reader=csv.reader(file)
            next(reader,None)
            for row in reader:
                data.append([float(x) if x.strip() else np.nan for x in row])

    except FileNotFoundError:
        return np.array([])
    
    return np.array(data)