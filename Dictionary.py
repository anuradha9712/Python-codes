x=["Delhi","mumbai","bangalore"]
z=[0,0,0]
f=[0,0,0]
ans=input("y/n")
print(ans)
while ans=="y":
    p=input("code")
    income=int(input("income"))
    if p=="a":
        p=0
    if p=="b":
        p=1
    if p=="c":
        p=2
for i in range(0,3):
    if i==p:
        if income>100000:
            z[i]=z[i]+1
        else:
            f[i]=f[i]+1
ans=input("y/n")
print(ans)
    
for w in range(0,3):
    print("\n",x[i],"rich",z[i],"poor",f[i])
    
    
