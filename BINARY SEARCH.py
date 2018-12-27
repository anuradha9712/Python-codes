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
print("\n"+"Enter elements for Linear List in ASCENDING ORDER"+"\n")
AR=[0] * N
for i in range(N) :
    AR[i] = int (input("Element" + str(i)+" :"))

ITEM = int(input("\nEnter element to be searched for ..."))
index = Bsearch(AR, ITEM)

if index :
    print("\nElement found at index : ", index, ", position : ", (index + 1))
else :
    print ("\nsorry!! Given element could not be found,\n")
    
