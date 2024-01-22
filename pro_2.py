'''2.Write a function that accepts an integer list as argument and shift all odd numbers to the left and even
numbers to the right of the list without changing the order'''


def shift(a,n):
    c=0
    for i in range(n):
        if a[i]%2!=0:
            x=a.pop(i)
            a.insert(c,x)
            c+=1
a=[ ]

n=int(input("How many values:"))

print("Enter",n,"values:") 

for i in range(n):
    a.append(int(input()))

print("List values before shifting:",a)
shift(a,n)
print("List values after shifting:",a)

