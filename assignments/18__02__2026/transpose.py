#withfunction
import numpy as np
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(matrix.transpose())
#with out function
n=[[1,2,3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix = list(map(list, zip(*n)))
print(matrix)
