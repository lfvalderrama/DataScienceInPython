import math

## Linear Algebra

#Vectors

def vector_add(v,w):
    return [v_i + w_i
            for v_i, w_i in zip (v,w)]

def vector_substract(v, w):
    return [v_i - w_i 
            for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    """ result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result """
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot_multiply(v, w):
    return sum (v_i * w_i
                for v_i, w_i in zip(v,w))

def sum_of_squares(v):
     return dot_multiply(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def distance(v, w):
    return magnitude(vector_substract(v,w))


#Matrix

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j]
            for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i,j)
             for j in range(num_cols)]
             for i in range(num_rows)]

def is_diagonal(i,j):
    return 1 if i==j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)

print identity_matrix
