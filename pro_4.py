'''Write a program to create a binary file and display the records whose marks are > 95.'''

import pickle

def search_95plus():
    f = open("marks.dat","rb")
    try:
        while True:
            data = pickle.load(f)
            for s in data:
                if s[2]>95:
                    print("RollNO:",s[0])
                    print("Name:",s[1])
                    print("Marks:",s[2])
            
    except EOFError:
        f.close()

f = open("marks.dat","ab")
rec=[]
while True:
    rn=int(input("Enter the rollno:"))
    sname=input("Enter the name:")
    marks=int(input("Enter the marks:"))
    rec.append([rn,sname,marks])
    ch=input("Want more records?:")
    if ch in "nN":
        pickle.dump(rec,f)
        f.close()
        break


search_95plus()