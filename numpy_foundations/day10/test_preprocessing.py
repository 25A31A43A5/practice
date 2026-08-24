import pytest
import preprocessing
import numpy as np

@pytest.fixture
def data():
    return np.array([
                        [37.1, 82,31],
                        [38.4, 110, 94],
                        [-5, 91, 97],
                        [40.2,13, 88],
                        [37.5, 200, 96]
                        ])

@pytest.fixture
def calculations(data:np.ndarray)->dict:
    return {"mean_values":np.nanmean(data,axis=0),
        "min_values":np.nanmin(data,axis=0),
        "max_values":np.nanmax(data,axis=0)}

def test_validate_data(data):
    test_data=preprocessing.validate_data(data)

    assert np.allclose(test_data,data)

def test_invalid_validate_data():
    data=np.array([1.3,1.5,3.1])

    with pytest.raises(ValueError):
        preprocessing.validate_data(data)

    with pytest.raises(ValueError):
        preprocessing.validate_data(np.array([]))

def test_clean_data(data):
    test_data=preprocessing.clean_data(data)
    temp_data=data.copy()
    temp_data[(data<0)|(data>200)]=np.nan

    assert np.allclose(test_data,temp_data,equal_nan=True)
    assert not np.shares_memory(data,test_data)

def test_calculate_statistics(data,calculations):
    test_data=preprocessing.calculate_statistics(data)
    assert test_data.keys()==calculations.keys()
    np.testing.assert_equal(test_data,calculations)

def test_calculate_impute_values(data,calculations):
    test_data=preprocessing.calculate_imputation_values(data)
    assert  np.allclose(calculations["mean_values"],test_data)

def test_impute_data(data,calculations):
    
    test_data=preprocessing.impute_data(data,calculations["mean_values"])
    data=data.copy()
    rows,columns=np.where(np.isnan(data))
    data[rows,columns]=calculations["mean_values"][columns]

    assert np.allclose(test_data,data)
    assert not np.isnan(test_data).any()

    array=np.array([[1.0,np.nan,2.0],
                    [1.0,3.0,np.nan]])
    statistic={"mean_values":np.array([1.0,3.0,2.0])}

    temp_data=preprocessing.impute_data(array,statistic["mean_values"])

    assert temp_data[0,1]==3.0 and temp_data[1,2]==2.0
    assert not np.shares_memory(temp_data,array)

def test_normalise_data():

    array=np.array([[1,30,60.0],
                    [3,56,33]])
    statistic={"min_values":np.array([1.0,30.0,33.0]),"max_values":np.array([3.0,56.0,60.0])}
    test_data=preprocessing.normalise_data(array,statistic)

    assert test_data.shape==(2,3)
    assert not np.isnan(test_data).any()
    assert np.allclose(np.min(test_data,axis=0),0)
    assert np.allclose(np.max(test_data,axis=0),1)


def test_pipeline(data):
    data=data.copy()

    test_data=preprocessing.validate_data(data)
    test_data=preprocessing.clean_data(test_data)
    values=preprocessing.calculate_imputation_values(test_data)
    test_data=preprocessing.impute_data(test_data,values)    
    statistic=preprocessing.calculate_statistics(test_data)
    test_data=preprocessing.normalise_data(test_data,statistic)

    assert test_data.shape==data.shape
    assert not np.isnan(test_data).any()
    assert np.allclose(np.min(test_data,axis=0),0)
    assert np.allclose(np.max(test_data, axis=0),1)
