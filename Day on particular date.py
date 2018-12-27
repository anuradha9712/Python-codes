z=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
x=int(input("number of days:"))
y=input("first day of year:")
for i in range (7):
    a=x%7
    if y==z[i]:
        b=i
        c=(a+b)-1
        i=c%7
print("the day on",x,"is",z[i])

   
