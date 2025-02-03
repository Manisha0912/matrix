mat1=[
    [1,5,67],
    [2.2,3,-2],
    [4,9,10],
    [5,3,-3],
]
sum=0
for i in mat1:
    for j in i:
        sum += j
print(sum)