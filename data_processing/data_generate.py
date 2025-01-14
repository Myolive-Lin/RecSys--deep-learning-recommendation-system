import numpy as np

def generate_random_matrix(rows, cols,min_value,max_value,seed = None):
    """
    Generate random matrix
    Args:
        rows (int): number of rows
        cols (int): number of columns
        min_value (int): min value of matrix
        max_value (int): max value of matrix
        seed (int, optional): seed. Defaults to None.
    Returns:
        np.array: random matrix
    """
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(min_value,max_value + 1,size = (rows,cols))
