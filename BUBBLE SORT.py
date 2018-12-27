def swapElements(aList):
    i = 0
    while(i <((len(aList))-1)):
        if(aList[i]>aList[i+1]):
            temp = aList[i]
            aList[i] = aList[i+1]
            aList[i+1] = temp
        i = (i+1)
        print ("List after pass", (i), ":", aList)

def bubblesort(aList):
    for num in range(len(aList) - 1):
        print("_ _ _ _ _ _Iteration",num, "_ _ _ _ _")
        swapElements(aList)

#_ _ _ _main_ _ _ _
list1 = [15, 6, 13, 22,3]
print ("Original list is :", list1)
bubblesort(list1)
print ("List after sorting :", list1)
