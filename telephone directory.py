
def pn(num):
    print("Telephone Numbers:")
    for n, i in num.items():
        print("Name:", n, "\tNumber:", i)
    print()
 
def add(num, N, u):
    num[N] = u
 
def find(num, N):
    if N in num:
        return "The number is " + num[N]
    else:
        return N + " was not found"
 
def remove(num, N):
    if N in num:
        del num[N]
    else:
        print(N," was not found")
 
def load(num, fname):
    f1 = open(fname, "rt")
    while True:
        l = f1.readline()
        if not l:
            break
        l = l[:-1]
        N, u = l.split(",")
        num[N] = u
    f1.close()
 
def save(num, fname):
    f2 = open(fname, "wt")
    for n, i in num.items():
        f2.write(n + "," + i + "\n")
    f2.close()
 
def menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Load numbers')
    print('6. Save numbers')
    print('7. Quit')
    print()
 
p = {}
c = 0
menu()
while True:
    c = int(input("Type in a number (1-7): "))
    if c == 1:
        pn(p)
    elif c == 2:
        print("Add Name and Number")
        N = input("Name: ")
        ph = input("Number: ")
        add(p, N, ph)
    elif c == 3:
        print("Remove Name and Number")
        N = input("Name: ")
        remove(p, N)
    elif c == 4:
        print("Locate Number")
        N= input("Name: ")
        print(find(p, N))
    elif c == 5:
        fname = input("Filename to load: ")
        load(p, fname)
    elif c == 6:
        fname = input("Filename to save: ")
        save(p, fname)
    elif c == 7:
        break
    else:
        menu()
 
print("Goodbye")
