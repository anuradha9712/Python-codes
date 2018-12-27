class Applicant:
    grade=" "
    
    def __init__(self):
        self.Adno= 0
        self.Name=" "
        self.Agg=0.0
        self.Grade=" "
        
    def GRADEME(self):
        if self.Agg>=80:
            self.Grade="A"
        elif 65<=self.Agg<80:
            self.Grade="B"
        elif 50<=self.Agg<65:
            self.Grade="C"
        elif self.Agg<50:
            self.Grade="D"
            
    def ENTER(self):
        self.Adno=int(input("Accept the admission number:"))
        self.Name=str(input("Accept name:"))
        self.Agg=float(input("Accept aggregate:"))

    def RESULT(self):
        print("Name of student :",self.Name,"\n","Admission number:",self.Adno,"\n","aggregate Marks:",self.Agg,"\n","Grade:",self.Grade)

A=Applicant()
A.ENTER()
A.GRADEME()
A.RESULT()

    
             
   
        
