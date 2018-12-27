# linear search
def Lsearch(AR, ITEM) :
    i=0
    while i< len(AR)and(AR)[i] !=ITEM:
        i +=1
    if i< len(AR):
        return i
    else :
        return False

#----main----
N=int(input("ENTER desired linear-list size(max. 50)... "))
print ("\nEnter element for Linear List\n")
AR = [0] * N
for i in range(N) :
    AR[i] = int (input("ELEMENT" + str(i+1)+":"))

ITEM=int(input("'\n',Enter Element to be searched for ..."))
index = Lsearch(AR, ITEM)

if index :
    print("\Element found at index :", index, ", Position : ",(index + 1))
else :
    print ("\nSorry!! Given element could not be found.\n")
        
                           
