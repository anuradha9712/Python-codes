class Result:

    def __init__(self):
        self.Rollno= 0
        self.Name=" "
        self.Marks=0.0
        self.Grade=" "
        
    def getdata(self):
        self.Rollno=int(input("Accept the Roll_number:"))
        self.Name=str(input("Accept Name:"))
        self.Marks=float(input("Accept Marks:"))

    def calgrade(self):
        if 90<=self.Marks<=100:
            self.Grade="A"
        elif 70<=self.Marks<90:
            self.Grade="B"
        elif 50<=self.Marks<70:
            self.Grade="C"
        elif 40<=self.Marks<50:
            self.Grade="D"
        else:
            self.Grade="E"

    def display(self):
        print("Name of student :",self.Name,"\n","Roll number:",self.Rollno,"\n"," Marks:",self.Marks,"\n","Grade:",self.Grade)

A=Result()
A.getdata()
A.calgrade()
A.display()
