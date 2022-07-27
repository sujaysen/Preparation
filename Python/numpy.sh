Numpy is the general purpose of multi dimentional array packagage.
Create an array from tuple and list
arr1 = np.array(list,dtype="float")
arr2 = np.array(tuple,dtype=np.float64)
sum = np.add(arr1,arr2) # adition of two array
sumOfAllElement = np.sum(arr1) # sum of all array elements
sqrt = np.sqrt(arr1)  # square root of array
transpose = arr1.T   # transpose of a matrix
dimension = arr1.ndim
size = arr1.size
shape = arr1.shape
arr = np.zeros((m,n)) # create a zero matrix of order mxn
arr = np.full((m,n),fixedValue, dtype = "complex")
arr = np.ones((m,n))
addBy1 = arr + 1  # add 1 with each element in array
subBy2 = arr -2   # substract 2 from each element in array
mulBy10 = arr*10
square = arr**2   # square each element of the array
largestEle = arr.max()
matrixMul = arr1.dot(arr2) # matrix multiplication
getsine = np.sin(arr1)
getExp = np.exp(arr1)
# rank of matrix
rank = np.linalg.matrix_rank(matrix)
# trace of a matrix
trace = np.trace(matrix)
# determinant of a matrix
det = np.linalg.det(matrix)
# inverse of a matrix
inv = np.linalg.inv(matrix)
# power of a matrix
power = np.linalg.matrix_power(matrix)
# calculate eigen value
eigenValue = np.linalg.eigvals(matrix)
# dot product of two vector 
dotProd = np.dot(vec1,vec2)
# inner product
innerProd = np.inner(arr1,arr2)
# solve system of linear eq
solve = np.linalg.solve(A,b)  # system of eq Ax = b
# matrix vector norm
norm = np.linalg.norm(matrix)
# condition number of a matrix
cnd = np.linalge.cond(matrix)
# Cholesky decomposition.
chl = np.linalg.cholesky(matrix)
# Compute the qr factorization of a matrix
qr = np.linalg.qr(matrix)
# Singular Value Decomposition.
svd = np.linalg.svd(matrix)	
# pseudo-inverse of a matrix
pinv = np.linalg.pinv(matrix)
# Solve the tensor equation a x = b for x.
tnsolve = np.linalg.tensorsolve(matrix)
# least-squares solution to a linear matrix equation Ax = b
lstsol = np.linalg.lstsq(A.T,y)[0]  
# Kronecker product of two arrays.
knprod = kron(arr1,arr2)
# Compute the outer product of two vectors.
outProd = outer(vec1,vec2)
matMultiplication = matmul(matrix1,matrix2)
# bitwise and 
bitwiseAnd = np.bitwise_and(b_num1,b_num2)
# bitwise or
bitwiseOr = np.bitwise_or(b_num1,b_num2)
# bitwise xor
bitwiseXor = np.bitwise_xor(arr1,arr2)
# left shift
leftshift = np.left_shift(number,no_bit_shift)
# right shift
rightshift = np.right_shift(number,no_bit_shift) # number may be array or exact number
# binary representation
brep = np.binary_repr(numberi,width=None)
# multiply two array element wise
arr = arr1*arr2
# sort in numpy
arr = np.sort(arr,axis=None)  # sort whole 
arr = np.sort(arr,axis=0)     # sort along first axis
arr = np.sort(arr,axis=-1)    # sort along last axis
# returns the indices that would sort an array.
indices = np.argsort(arr)
# partition in numpy








