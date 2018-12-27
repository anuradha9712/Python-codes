count=int(input("HOW MANY STUDENTS IN THE CASS:?"))
fileout=open("Marks.det","w")
for i in range (count):
    print("Enter details for student",(i+1),"below:")
    rollno=int(input("Rollno:"))
    name=input("Enter name:")
    marks=float(input("Enter marks:"))
    rec=str(rollno)+","+name+","+str(marks)+'\n'
    fileout.write(rec)
fileout.close()

# To add new student record in existing file

import os
infile=open("Marks.det","r")
outfile=open("temp.det","w")
nrollno=int(input("Enter roll no:"))
nname=input("Enter name:")
nmarks=float(input("Enter marks:"))
nrec=str(nrollno)+","+nname+","+str(nmarks)+'\n'
count=0
rec=" "
while rec:
    rec=infile.readline()
    count=count+1
    if count==5:
        outfile.write(nrec)
        outfile.write(rec)
    else:
        outfile.write(rec)

infile.close()
outfile.close()
os.remove("Marksdet")
os.rename("temp.det","Marksdet")

print("New record successfully added.")
