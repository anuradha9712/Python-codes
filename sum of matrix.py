from random import randint
n = [[randint (10 , 100) for j in range (5)] for i in range (5)]
for i in range (len(n)):
    for j in range (len(n[i])):
        print (n[i][j] ," ",end = " ")
    print("\n")
s=0
p=0
y=[]
l=[]
for i in range(5):
    s+=n[i][j]
    l.append(n[i][j])
    print(l," ",end=" ")
    print("sum:",s)
    for j in range(5):
        p+=n[j](len(n)-i-j)
        y.append(n[j](len(n)-1-j))
        print(y," ",end=" ")
        print("sum",p)
              
                 
