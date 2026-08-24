import pytest
import ingestion
from pathlib import Path
import csv
import numpy as np

@pytest.fixture
def path(tmp_path)->Path:
    return Path(tmp_path)/("day10.csv")

@pytest.fixture
def data()->dict:
    return {"header":["temperature","heart_rate","oxygen"],"array":[
                        [37.1, 82,""],
                        [38.4, 110, 94],
                        [-5, 91, 97],
                        [40.2,"", 88],
                        [37.5, 90, 96]
                        ]}

    
def test_valid_input(path,data):
    with open(path,"w",newline="") as temp_file:
        writer=csv.writer(temp_file)
        writer.writerow(data["header"])
        writer.writerows(data["array"])

    imported_data=ingestion.import_data(path)
    test_array=np.array([[float(x) if x!="" else np.nan for x in row ]for row in data["array"]])

    assert np.allclose(test_array,imported_data,equal_nan=True)
    assert imported_data.size==15
    assert imported_data.shape==(5,3)

def test_invalid_file():
    imported_data=ingestion.import_data("non_exisistant.csv")
    assert np.allclose(imported_data,np.array([]))

def test_empty_file(path):
    path.touch()
    imported_data=ingestion.import_data(path)
    assert np.allclose(imported_data,np.array([]))