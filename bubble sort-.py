from random import randint
s=p=0
def sel(x,k):
    for i in range (0,k):
        s=x[i]
        for j in range (i+1,k):
              if s>x[j]:
                  s=x[j]
                  p=j
        t=x[i]
        x[i]=x[p]
        x[p]=t
        print(" list after", (i+1),"pass:",end=" ")
        for z in range (0,k):
              print(x[z], " ", end= ' ')
        print("/n")

def bub (x,k):
    for i in range(0,k):
        for j in range (0,(k-1)-i):
            if x[j]> x[j+1]:
                 t=x[j]
                 x[j]=x[j+1]
                 x[j+1]=t
        print(" list after", (i+1)," pass:", end=" ")
        for z in range (0,k):
            print( x[z], " ", end=' ')
        print("/n")

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
print (''' Sorting Menu
           1. Selection sort
           2. Bubble sort
           3. Insertion sort''')
c= int(input(" your choice"))
if c==1:
       bub(A,10)
       print(A)
elif c==2:
       sel(A,10)
       print(A)
elif c==3:
       B=[ ]
       B.append(0)
       for i in range (0,10):
            B.append (randint (10,100))
       ins(B,11)
       B.remove(0)
       print(B)
else:
       print(" wrong choice selection") 
