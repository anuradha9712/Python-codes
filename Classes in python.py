file=open("people","a")
class PEOPLE:

    def _init_(self):
        self.R_no=0
        self.name=" "
        self.city=" "

    def putdata(self):
        for i in range(3):
            self.R_no=int(input("accept the registration number:"))
            self.name=input("accept name:")
            self.city=input("accept city:")
            file.write(str(self.R_no)+"  ")
            file.write(str(self.name)+"  ")
            file.write(str(self.city)+"  "+"\n")
        

a=PEOPLE()
a.putdata()

# to display the content of file
file=open("people","r")
while str:
    str=file.readline()
    print(str,)
file.close()

#to delete the record
import os
file=open("people","r")
file1=open("temp","w")
count=0
rec=" "
while rec:
    rec=file.readline()
    count=count+1
    if count==1:
        pass
    else:
        file1.write(rec)
file.close()
file1.close()
os.remove("people")
os.rename("temp","people")


#to modify a record for a person
import os
file=open("people","r")
file1=open("temp","a")
r_no=int(input("ACCEPT THE REG_NO. TO MODIFY RECORD:"))
R_no="r_no"
rec=" "
while rec:
    rec=file.readline()
    if rec.find(R_no,0,10)!=-1:
        #Record=rec.split(',')
        print("record right now contains this information :",rec)
        print("enter new information below:")
        name=input("Enter name:")
        city=input("Enter city:")
        nrec=R_no+" "+name+" "+city+"\n"
        file1.write(nrec)
    else:
        file1.write(rec)
file.close()
file1.close()
os.remove("people")
os.rename("temp","people")


    



