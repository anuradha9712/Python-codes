from random import randint
h = [[randint (10 , 100) for j in range (5)] for i in range (5)]
for i in range (len(h)):
    for j in range (len(h[i])):
        print (h[i][j] ," ",end = " ")
    print("\n")
print("\n\n\n")

print("'''Transpose Of Matrix'''")
for i in range(len(h)):
    for j in range(len(h[i])):
        print (h[j][i] ," ", end = " ")
    print("\n")
      
'''da=[]
db=[]
d1=0
d2=0
n=[]
for i in range(0,5):
    for j in range(0,5):
        if i==j:
            da.append(n[i][j])
            d1+=n[i][j]
        if (i+j)==10:
            db.append(n[i][j])
            d2+=n[i][j]
print(da,'sum1=',d1)
print(db,'sum2=',d2)'''

s=0
p=0
y=[]
l=[]
for i in range(5):
    s+=h[i][j]
    l.append(h[i][j])
    print(l," ",end=" ")
    print("sum",s)
    for j in range(5):
        p+=h[j][len(h)-i-j]
        y.append(h[j][len(h)-i-j])
        print(y," ",end=" ")
        print("sum",p)
        
