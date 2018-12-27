def cls():
    print("\n"*1)
    
def isEmpty(Qu):
    if Qu==[]:
        return True
    else:
        return False

def Enqueue(Qu,item):
    Qu.append(item)
    if len(Qu)==1:
        front=rear=0
    else:
        rear=len(Qu)-1

def Dequeue(Qu):
    if isEmpty(Qu):
        return "Underflow"
    else:
        item=Qu.pop(0)
    if len(Qu)==0:
        front=rear=None
    return item

def Peek(Qu):
    if isEmpty (Qu):
        return "Underflow"
    else:
        front=0
    return Qu[front]

def Display(Qu):
    if isEmpty(Qu):
        print("Queue Empty!")
    elif len(Qu)==1:
        print( Qu[0],"<==front,rear")
    else:
        front=0
        rear=len(Qu)-1
        print(Qu[front],"<-front")
        for a in range(1,rear):
            print(Qu[a])
        print(Qu[rear],"<-rear")

queue=[]
front=None
while True:
    cls()
    print(""" QUEUE OPERATIONS
             1.Enqueue
             2.Dequeue
             3.Peek
             4.Display queue
             5.Exit     """)
    ch=int(input("Enter your choice(1-5):"))
    if ch==1:
        item=int(input("Enter item:"))
        Enqueue(queue,item)
        input("Press Enter to continue...")
    elif ch==2:
        item=Dequeue(queue)
        if item=="Underflow":
            print("Underflow! Queue is empty!")
        else:
            print("Dequeued item is",item)
        input("Press Enter to continue...")
    elif ch==3:
        item=Peek(queue)
        if item=="Underflow":
            print("Queue is empty!")
        else:
            print("Frontmost item is :",item)
        input("Press Enter to continue...")
    elif ch==4:
        Display(queue)
        input("Press Enter to continue...")
    elif ch==5:
        break
    else:
        print("Invalid choice!!!")
        input("Press Enter to continue...")
        
    
        
            
            
