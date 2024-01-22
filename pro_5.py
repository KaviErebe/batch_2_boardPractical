'''Write a program to implement stack operations in Python.'''
def push(l,v):
    a = int(input("enter a value to push"))
    if len(l)== v:
        print("overflow")
    else:
        l.append(a)

def pop(l):
    if l == []:
        print("underflow")
    else:
        f = l.pop()
        print(f,"this values have been poped")




l=[]

v = int(input("enter number of value::"))

for i in range(v):
    l.append(int(input(":")))

while True:
    ch = int(input("enter choice\n1.push\n2.pop\n3.peek\n4.display\n5.exit"))
    
    if ch == 1:
        push(l,v)
    elif ch == 2:
        pop(l)
    elif ch == 3:
        print("the peek value :",l[-1])
    elif ch== 4:  
        if l == []:
            print("stack empty")
        for i in range(len(l)):
            print(l[i])
    elif ch == 5:
        break
    else:
        print("invalid")
        
    