import numpy as np 
from collections.abc import Iterable

def zero_arr():
    return np.zeros((2, 4))

def positive_only(nums):
    filters = [True if x == int(x) and x > 0 else False for x in nums]
    nums_np = np.array(nums)
    return nums_np[filters]

def ind_of_max(nums):
    if not isinstance(nums, Iterable):
        return None
    return np.argmax(nums)

def combine_rooms(room_1, room_2):
    if not isinstance(room_1, Iterable)\
    or not isinstance(room_2, Iterable)\
    or type(room_1) is not list or len(room_1) != 7\
    or type(room_2) is not list or len(room_2) != 7:
        return None
    return [x if x > 0 else room_2[i] if room_2[i] > 0 else None for i, x in enumerate(room_1)]

def broadcast(vec, n):
    if not isinstance(vec, np.ndarray)\
    or str(vec.dtype) not in ['int32', 'float64']\
    or not isinstance(n, int)\
    or len(vec.shape) != 2 or vec.shape[1] != 1:
        return None
    return vec @ np.ones((1, n))

def transpose(nul):
    result = []
    result = nul.T
    return result    
if __name__ == "__main__":
    # Exercise 1
    print(zero_arr())

    # Exercise 2 
    print(positive_only([1, 3, 3.7, -4, 5.0]))

    # Exercise 3 
    print(ind_of_max([4, 1, 30, 7, 15]))

    # Exercise 4 
    room_1 = [1,2,-3,4,5,6,-7]
    room_2 = [8,9,10,11,12,-13,-14]
    res = combine_rooms(room_1, room_2)
    print(res)

    # Exercise 5 
    print(broadcast(np.array([[6], [7]]), 3))

    # Exercise 6
    print(transpose(7))
