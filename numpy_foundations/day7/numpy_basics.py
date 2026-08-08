import numpy as np

def multiplication_list(lst:list[int])->list[int]:
    result=[]
    for i in lst:
        result.append(i*2)
    return result

def multiplication_array(lst:list[int])->np.ndarray:
    array=np.array(lst)
    result=array*2
    return result

def ndim(lst:list[int])->int:
    # ndim returns the number of dimensions a given ndarray or simply array
    # dimension is the number of layers present in an array
    array=np.array(lst)
    return array.ndim

def shape(lst:list[int])->tuple:
    # shape returns the shape of the array, i.e., the number of layers and elements in each layer
    array=np.array(lst)
    return array.shape

def size(lst: list[int])->int:
    # size returns an interger which corelates to the numeber of elements present in a ndarray
    
    array=np.array(lst)
    return array.size

def dtype(lst: list)->str:
    # dtype tells us what type of data is stored in an array
    # arrays are homogeneous, i.e., all elements should be of the same data type

    array=np.array(lst)
    return array.dtype.name

def dtype_promotion(lst:list)->np.ndarray:
    # dtype promotion is a phenomenon that happens when converting a list into an array when all the elements are not of same type

    array=np.array(lst)
    return array

def indexing(lst:list[int])->np.ndarray:
    #indexing is the method of accessing elements in an array it is almost similar to a python lists and more closely related to cpp/c arrarys
    
    array=np.array(lst)
    return array[0]

def  slicing(lst:list[int])->np.ndarray:
    # slicing is the technique to extract data efficiently and it is fairly customizable
    # syntax is  array_name[start:end:skips]
    # remember that slicing returns a view not a copy

    array=np.array(lst)
    return array[0::1]

def view(lst:list[int])->np.ndarray:
    # view is the name of the method that is used to create an object to the data without copying it
    # if you change a view of an array the original array also changes and it is similar to pointers in c and cpp
    # for optimisation reasons slicing indexing and almost every operation returns a view instead of a copy

    array=np.array(lst)
    temp_array=array[0::1]
    temp_array*=2

    return array

def copy(lst:list[int])->np.ndarray:
    # copy is the name of the function that makes it possible to duplicate an array without making a view

    array=np.array(lst)
    temp_array=array.copy()
    temp_array*=2

    return array

def array_to_scalar_vectorization(lst:list[int])->np.ndarray:
    # we can perform mathematical operations to ndarray and a constant as if they were basic data types like int, double,etc

    array=np.array(lst)

    return array*2

def array_to_array_vectorization(lst1:list[int],lst2:list[int])->np.ndarray:
    # we can perform mathematical operations to ndarray and another ndarray as if they were basic data types like int,double,etc

    array1=np.array(lst1)
    array2=np.array(lst2)

    return array1+array2

