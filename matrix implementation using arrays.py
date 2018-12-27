m=int(input("Enter number of rows: "))
n=int(input("Enter number of columns:"))
#create matrices of size m x n
Mat1 = [ [0 for j in range(n)]for i in range (m)]
Mat2 = [ [0 for j in range(n)]for i in range (m)]
Mat3 = [ [0 for j in range(n)]for i in range (m)]

print("Input matrix 1 below:")
for i in range(m):
    for j in range(n):
        Mat1[i][j] = int(input(str(i)+", "+str(j) +" : "))

print("Input matrix 2 below:")
for i in range(m):
    for j in range(n):
        Mat2[i][j] = int(input(str(i)+", "+ str(j) + " :"))

#calculate sum of two matrices
        for i in range( m ):
            for j in range( n ):
                Mat3[i][j] = Mat1[i][j] + Mat2[i][j]

#print sum of two matrices
print ("Matrix1:")
for i in range( m ):
    for j in range ( n ):
        print (Mat1[i][j],)
    print

print ("Matrix2:")
for i in range( m ):
    for j in range ( n ):
        print (Mat2[i][j],)
    print

print ("Sum of these matrices:")
for i in range( m ):
    for j in range( n ):
        print (Mat3[i][j],)
    print
