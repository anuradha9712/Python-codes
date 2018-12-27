for i in range(2):
    class account():
        def __init__ (self):
            self.name=" "
            self.account_no=0
            self.opening_balance=0.0

        def entry (self):
            self.name=input("accept the name ")
            self.account_no=int(input("accept the account no. "))
            self.opening_balance=float(input("accept the opening balance"))

        def output (self):
            print ("customer name:",self.name,'\n',"account number:",self.account_no,'\n',"opening balance",self.opening_balance)

    class saving (account):
        b=account()
        def __init__(self):
            self.rate=12
            account.__init__(self)

        def ci(self):
            self.time=float(input("accept the time"))
            self.compound_interest=self.opening_balance*((1+(self.rate/100))**self.time)
            print("compoundaed interest",self.compound_interest)

        def wf(self):
            withdrawal_amount=float(input("withdrawal amount:"))
            self.balance=self.opening_balance-withdrawal_amount
            print ("balance left",self.balance)

    class current(saving):
        d=saving()
        def __init__(self):
            self.min_balance=1000
            saving.__init__(self)

        def cheque (self):
            print ("congrats!! ",self.name," you are provided with cheque book")

        def service_charge (self):
            if self.balance<self.min_balance:
                self.service_charge=self.balance*0.04
                self.balance=self.balance-self.service_charge
                print ("Oooops your left balance is ",self.balance)
            
        
    c=current()
    fileout=open("bankdata","a+")
    c.entry()
    fileout.write()
    fileout.close()

        
        
        

    








        
        
        

    






        

    













