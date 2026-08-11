import data_trans as dt
import pytest
import numpy as np

@pytest.fixture
def array()->np.ndarray:
    return dt.get_data()

def test_inspect_data(array):
    inspect=dt.inspect_data(array)
    assert array.ndim==inspect["ndim"]
    assert array.dtype==inspect["dtype"]
    assert array.shape==inspect["shape"]
    assert array.size==inspect["size"]

def test_calculate_stats(array):
    statistics=dt.calculate_statistics(array)

    assert np.array_equal(np.mean(array,axis=0),statistics["mean"])
    assert np.array_equal(np.sum(array,axis=0),statistics["sum"])
    assert np.array_equal(np.max(array,axis=0),statistics["max"])
    assert np.array_equal(np.min(array,axis=0),statistics["min"])
    assert np.array_equal(np.std(array,axis=0),statistics["std"])


def test_transformed_data(array):
    
    statistics=dt.calculate_statistics(array)
    transformed=dt.transform_data(array,statistics)

    test_scaled=(array-statistics["min"])/(statistics["max"]-statistics["min"])

    assert np.array_equal(test_scaled,transformed["scaled"])

    test_centered=array-dt.calculate_statistics(array)["mean"]

    assert np.allclose(test_centered,transformed["centered"])

