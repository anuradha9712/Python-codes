class date:
    def __init__(self,month,date):
        self.m=[1,2,3,4,5,6,7,8,9,10,11,12]
        self.d=[31,28,31,30,31,30,31,31,30,31,30,31]
        self.r=month
        self.p=date
        self.q=0
        self.i=0

    def read(self):
        for self.i in range(0,12):
            if self.r==self.m[self.i]:
                self.q=self.i
                print("Number of days:",self.d[self.i])

    def next_day(self):
        if self.p<self.d[self.i]:
            self.p+=1
        else:
            self.p=1
        print("the next day is:",self.p)
            
z=date(11,6)
z.read()
z.next_day()
