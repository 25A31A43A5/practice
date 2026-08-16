import pytest
import numpy as np
import boolean_masking as bm

@pytest.fixture
def data()->np.ndarray:
    return  np.array([
                        [7, 2, 11],
                        [14, 5, 1],
                        [9, 13, 4],
                        [3, 15, 8],
                        [12, 6, 10]
                        ])

def test_filter_array(data):

    assert np.array_equal(np.array([7,6]),bm.filter_array(data))
    assert (2,)==bm.filter_array(data).shape

def test_replace_with_mask(data):
    array=bm.replace_with_mask(data)
    test_array=data.copy()
    test_array[(test_array>5)&((test_array<8))]=0

    assert np.array_equal(array,test_array)
    assert  not np.shares_memory(data,array)

def test_transpose_data(data):
    assert np.array_equal(data.T,bm.transpose_data(data))

def test_reshape_data(data):
    assert (3,5)==bm.reshape_data(data,(3,5)).shape

def test_reshape_data_failure(data):

    with pytest.raises(ValueError):
        bm.reshape_data(data,(20,44))

def test_split_data(data):
    test_data=bm.split_data(data)
    assert len(test_data["vsplit"])==5
    assert len(test_data["hsplit"])==3

    assert all(x.shape==(1,3) for x in test_data["vsplit"])
    assert all(x.shape==(5,1) for x in test_data["hsplit"])

def test_flatten_and_ravel(data):
    flatten_data=bm.flatten_data(data)
    ravel_data=bm.ravel_data(data)

    assert len(flatten_data)==15
    assert len(ravel_data)==15
    assert not np.shares_memory(flatten_data,data)
    assert np.shares_memory(ravel_data,data)

def test_combine_data():
    test_data1=np.array([[1, 7, 4],
                         [6 ,3, 2]])
    test_data2=np.array([[16, 11, 11], 
                          [16, 16, 18]])
    combined_data=bm.combine_data(test_data1,test_data2)

    assert (4,3) == combined_data["concatenate_axis_0"].shape
    assert (2,6) == combined_data["concatenate_axis_1"].shape
    assert (4,3) == combined_data["vstack"].shape
    assert (2,6) == combined_data["hstack"].shape
    assert (2,2,3) == combined_data["stack"].shape