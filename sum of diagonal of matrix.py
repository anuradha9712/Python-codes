from random import randint
d1 ,d2 =0,0
DA=[]
DB=[]
N=[[randint(10,99)for j in range(5)]for i in range (5)]
for i in range (0,5):
    for j in range (0,5):
        if i == j:
           DA. append (N[i][j])
           d1 +=N[i][j]
        if (i+j) ==4:
            DB. append (N[i][j])
            d2 += N[i][j]
    print(DA ,"sum1= ", d1)
    print(DB, "sum2= ",d2)
    
        
