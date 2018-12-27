class Publication:
    def _init_(self):
        self.title=" "
        self.price=0.0

    def Getdata(self):
        self.title=input("Accept the title =")
        self.price=float(input("Accept the price="))

    def Putdata(self):
        print("The Title Is: ",self.title,'\n',"The Price Is: ",self.price)

class Book(Publication):
    b=Publication()
    def _init_(self):
        self.page_count=0
        Publication._init_(self)

    def Getdata(self):
        self.page_count=int(input("Accept the pagecount: "))

    def Putdata(self):
        print("The number of pages: ",self.page_count)

class Tape(Publication):
    d=Book()
    def _init_(self):
        self.playing_time=0.0
        Publication._init_(self)
        
    def Getdata(self):
        self.playing_time=float(input("Accept the playing time in minutes: "))

    def Putdata(self):
        print("The playing time: ",self.playing_time)

c=Tape()
c.d.b.Getdata()
c.d.Getdata()
c.Getdata()
c.d.b.Putdata()
c.d.Putdata()
c.Putdata()

        
