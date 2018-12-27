from random import randint
def Schk(s):
    if s==[]:
        return True
    else:
        return False

def Push(s,i):
    s.append(i)
    l=len(s)-1
    return l

def Pop(s):
    if Schk(s):
        return "Empty Stack"
    else:
        i=s.pop()
        if (len(s)==0):
            t=None
        else:
            t=len(s)-1
        return i

def Peek(s):
    if Schk(s):
        return "Underflow"
    else:
        t=len(s)-1
        return s[t]

def Display(s):
    if Schk(s):
        print("Stack Empty")
    else:
        t=len(s)-1
        print(s[t],"<-t")
    for a in range(t-1,-1,-1):
        print(s[a])

s=[randint(50,500)for i in range(10)]
t=None

while True:
    print(""" Stack Operations
           1. Push
           2. Pop
           3. Peek
           4. Display Stack
           5. Exit """)
    ch=int(input("Enter your choice(1-5): "))
    if ch==1:
        item=int(input("Enter Item:"))
        Push(s,item)
    elif ch==2:
        item=Pop(s)
        if item=="Underflow":
            print("Underflow Empty Stack")
        else:
            print("Poped Item",item)
    elif ch==3:
        item=Peek(s)
        if item=="Underflow":
            print("Underflow,Stack Empty")
        else:
            print("Top Most Item",item)
    elif ch==4:
        Display(s)
    elif ch==5:
        break
    else:
        print("Invalid")


