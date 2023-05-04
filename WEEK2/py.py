import numpy as np 
def transpose(mat):
    if type(mat) != np.ndarray or not np.isreal(mat).all():
        return None
    elif not np.issubdtype(mat.dtype, np.number):
        return None
    results = []
    results = mat.T
    return results
def product(mat_a,mat_b):
    if type(mat_a) != np.ndarray or type(mat_b) != np.ndarray:
        return None
    elif not np.issubdtype(mat_a.dtype, np.number) or not np.issubdtype(mat_b.dtype, np.number):
        return None
    else:
        if mat_a.shape[1] == mat_b.shape[0]:
            result1= np.dot(mat_a,mat_b) 
        else:
            result1 = 'Khong co tich ma tran'
        if mat_a.shape == mat_b.shape:
            result2 = mat_a * mat_b
        else:
            result2 = 'Khong co tich Hadamard'
    return result1 , result2
def replace_col(mat,col_ind):
    if type(mat) != np.ndarray or not np.isreal(mat).all():
        return None
    elif not np.issubdtype(mat.dtype, np.number):
        return None
    mat[:,col_ind] = 1
    return mat
if __name__ =="__main__":
    print(transpose(np.array([[1, 2], [3, 4], [5, 6]])))
    print(product(np.array([[1,2,3],[4,5,6]]),np.array([[1,2],[3,4],[5,6]])))
    print(replace_col(np.array([[1, 3, 4], [-2, 6, 0], [-5, 7, 2]]),1))


