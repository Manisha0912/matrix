# 1. Diagonal elements sum (Level 1 is any one diagonal and level 2 is )
# O(n*n)
list1=[[1,2,3],
       [4,5,6],
       [7,8,9]]
    
def diagonal(mat,n):
    first=0
    second=0

    for i in range(0,n):
        for j in range(0,n):
            if i==j:
               first += mat[i][j]
            if i+j==n-1:
               second += mat[i][j]
    print("first diagonal elements:",first)    
    print("secondary diagonal elements:",second)    
diagonal(list1,3)         


# O(n)

list2=[[2,2,3],
       [4,5,6],
       [7,8,5]]
    
def diagonalsum(mat,n):
    primary=0
    secondary=0

    for i in range(0,n):
               primary += mat[i][i]
               secondary += mat[i][n-i-1]
    print("first diagonal elements:",primary)    
    print("secondary diagonal elements:",secondary)    
diagonalsum(list2,3) 



# 2. Add 2 matrixes

X=[[1,2,3],
       [4,5,6],
         [7,8,9]]
Y=[[1,2,3],
       [4,5,6],
         [7,8,9]] 
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]           

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)
