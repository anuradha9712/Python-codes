s=["a","b","c","d"]
r=["Delhi","Mumbai","Hyderabad","Bangalore"]
q={"Delhi poor":0,"Mumbai poor":0,"Hyderabad poor":0,"Bangalore poor":0}
t={"Delhi rich":0,"Mumbai rich":0,"Hyderabad rich":0,"Bangalore rich":0}
u=q.keys()
v=t.keys()
x=int(input("code:"))
y=int(input("salary:"))
for i in range(0,4):
    if[s[i]==x]:
        print("City is:",r[i])
    if (y>=1000000):
        t[v[i]]+=1
    else:
        q[u[i]]+=1
    print(q,t)
       
   
