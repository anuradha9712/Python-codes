import pickle
numerals={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C"}
file1=open("roman.log","wb")
pickle.dump(numerals,file1)

file1.close()

file2=open("roman.log","rb")
num=pickle.load(file2)
file2.close()

n=0
while n!=-1:
    print("Enter 1 / 4 / 5 / 9 / 10 / 40 / 50 / 90 / 100")
    print("...Enter-1 to exit...")
    n=int(input("Enter the number:"))
    if n!=-1:
        print("Equivalent roman number of this numeral is:",num[n])
    else:
        print("Thank You!!!!")
        
