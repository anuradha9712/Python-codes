from random import randint
def ins (x,k):
    x[0]=0
    for i in range (1,k):
        t=x[i]
        j=i-1
        while t<x[j]:
              x[j+1]=x[j]
              j-=1
        x[j+1]=t

        for j in range (0,(k-1)-i):
            if x[j]> x[j+1]:
               t=x[j]
               x[j]=x[j+1]
               x[j+1]= t
        print (" list after ",i," pass:", end=" " )
        for z in range (1,k):
            print (x[z], " ", end= ' ')
        print ("/n")

print (" list of 10 random integer values between 10 and 100", "/n")
       
A=[ ]
for i in range (0,10):
    A. append (randint(10,100))
print(" /n Original list ", A, "/n")
B=[ ]
B.append(0)
for i in range (0,10):
        B.append (randint (10,100))
ins(B,11)
B.remove(0)
print(B)
