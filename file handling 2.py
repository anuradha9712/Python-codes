pcs=open("ABC","w+")
for i in range(0,2):
    n=input("Name:")
    m=int(input("Marks:"))
    s=''
    if m>=45:
        s="Pass"
    else:
        s="Fail"
    r=(n+" "+str(m)+" "+s+" "+"\n")
    pcs.write(r)
pcs.seek(0)
k=pcs.readlines()
l=[]
for i in range(2):
    p=k[i].split()
    l.append(p)
print(l)
for i in range(2):
    print("Name:",l[i][0],"\n","Marks:",l[i][1],"\n","Status:",l[i][2],"\n")
    

