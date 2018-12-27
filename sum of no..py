def sum(n):
    a=0
    if n>0:
        for i in range(n,(2*n)+1):
            a+=i
            print(a)
    else:
        for i in range(2*n,n+1):
            a+=i
            print(a)

x=int(input("accept a integer:"))
y=sum(x)
print(y)

      
