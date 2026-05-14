import numpy as np
a = np.array([[1,2,4,6], [5,6,7,8], [9,0,1,2]] )
print("Printing the entire matrix:\n", a)
print("first row", a[0])
print("Second row", a[1])
print("third row", a[2])
print("geting value [1][2]", a[2][0])

#col wise print 
row, col = a.shape
for i in range(col):
    for j in range(row):
        print(a[j][i])
#creating array 
arr = np.zeros((3,2), dtype = int) # ROW, COL
print(a)
print(a.size) #check the size of an array
print(a.shape) #shape of a array


#row wise print
for i in range(row):
    for j in range(col):
        print(a[i][j])

#col wise print
for i in range(col):
    for j in range(row):
        print(a[j][i])

sum = 0
for i in range(col):
    for j in range(row):
        sum += a[j][i]
print(sum)

#sum of every row 
def row_sum(x):
    row, col = x.shape
    new_m = np.zeros((row,1), dtype=int)
    for i in range(row):
        for j in range(col):
            new_m[i][0] += x[i][j]

    print(new_m)
row_sum(a)
def col_sum(y):
    row,col = y.shape
    new_col= np.zeros((1,col), dtype = int)
    for i in range(col):
        for j in range(row):
            new_col[0][i] += a[j][i]
    
    print(new_col)
col_sum(a)

def get_primary_digonal(x):
    row,col = x.shape
    if row != col:
        print("Not possible")
    
    new_mat = np.zeros((col,1), dtype=int)
    for i in range(row):
        for j in range(col):
            new_mat[i][0] += x[i][i]

    print(new_mat)
get_primary_digonal(a)

def secondary_digonal(y):
    rows, cols = y.shape
    if rows != cols:
        print("Not possible")
    new_m = np.zeros((rows,1), dtype = int)

    for i in range(rows):
        for j in range(cols):
            new_m[i][0] += y[i][cols-j-1]

    print(new_m)
secondary_digonal(a)