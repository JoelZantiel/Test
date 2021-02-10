# determinant of 2x2 matrix
def det2x2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

matrix = [
    [ 6, 1, 1 ],
    [ 4, -2, 5 ],
    [ 2, 8, 7 ]
]

print("Matrix:")
for array in matrix: print(array)

print()

#a = matrix[0][0]
#b = matrix[0][1]
#c = matrix[0][2]
# or just...
a,b,c = matrix[0]

# extract sub matrix
efhi = [x[1:] for x in matrix[1:]]

# x[::2] - from col idx 0 to idx 2 with step of 2
dfgi = [x[::2] for x in matrix[1:]]

degh = [x[0:2] for x in matrix[1:]]

det = (
    a * det2x2(efhi)
    - b * det2x2(dfgi)
    + c * det2x2(degh)
)

print(f"Determinant of matrix is: {det}")