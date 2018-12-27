class calculator:
    def __init__(self):
        self.num1=0.0
        self.num2=0.0
    def Entry (self):
        self.num1=float(input("accept the first number:"))
        self.num2=float(input("accept the second number:"))
    def Add (self):
        self.a=self.num1+self.num2
        return self.a
    def Sub (self):
        self.s=self.num1-self.num2
        return self.s
    def Mul (self):
        self.m=self.num1*self.num2
        return self.m
    def Div (self):
        self.d=self.num1/self.num2
        return self.d
    def Result (self):
        print(" sum:",self.a,"\n","difference:",self.s,"\n","multiplication:",self.m,"\n","division:",self.d)

x=calculator()
x.Entry()
x.Add()
x.Sub()
x.Mul()
x.Div()
x.Result()


        
        
        
