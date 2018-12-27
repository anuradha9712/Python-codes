m=int(input("Enter number of rows :"))
n=int(input("Enter number of columns :"))
mat1=[[0 for j in range(n)]for i in range(m)]
mat2=[[0 for j in range(m)]for i in range(n)]
print("INPUT MATRIX BELOW:")
for i in range(m):
    for j in range(n):
        mat1[i][j]=int(input(str(i)+","+str(j)+":"))

    for i in range(n):
        for j in range(m):
            mat2[i][j]=mat1[j][i]
            
print("Given Matrix:")
for i in range(m):
    for j in range(n):
        print(mat1[i][j],)
    print
    
print("Transpose Matrix:")
for i in range(n):
    for j in range(m):
        print(mat2[i][j],)
    print

            
