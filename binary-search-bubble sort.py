from random import randint
# BUBBLE SORT
def swapElements(aList):
    i = 0
    while(i <((len(aList))-1)):
        if(aList[i]>aList[i+1]):
            temp = aList[i]
            aList[i] = aList[i+1]
            aList[i+1] = temp
        i = (i+1)
        '''print ("List after pass", (i), ":", aList)'''

def bubblesort(aList):
    for num in range(len(aList) - 1):
         '''print("_ _ _ _ _ _Iteration",num, "_ _ _ _ _")'''
         swapElements(aList)
       
        

# BINARY SEARCH
def Bsearch(AR, ITEM):
    beg=0
    last=len(AR)-1
    while(beg<=last):
        mid=int((beg+last)/2)
        if(ITEM==AR[mid]):
            return mid
        elif(ITEM>AR[mid]):
            beg=mid+1
        else:
            last=mid-1
    else:
        return False
#----main----
     
N=int(input("Enter desired linear-list size (max. 50)..."))
AR=[randint(100,999) for i in range(N)]
print ("Original list is :", AR)
bubblesort(AR)
print ("List after sorting :", AR)
ITEM = int(input("\nEnter element to be searched for ..."))
index = Bsearch(AR, ITEM)

if index :
    print("\nElement found at index : ", index, ", position : ", (index + 1))
else :
    print ("\nsorry!! Given element could not be found,\n")
    
