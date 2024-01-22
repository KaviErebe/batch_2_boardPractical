'''Write a program to create a CSV file and also display the contents of the file'''

import csv

    #Create Header First
f = open("students.csv","w",newline='\n')
dt = csv.writer(f)
dt.writerow(['Student_ID','StudentName','Score'])
    #Insert Data
while True:
    st_id= int(input("Enter Student ID:"))
    st_name = input("Enter Student name:")
    st_score = input("Enter score:")
    dt.writerow([st_id,st_name,st_score])
    print("Record has been added.")
    ch=int(input("Want to insert More records?(enter 1 to exit this program):"))
    if ch == 1:
        break
    
f.close()

f = open("students.csv")
data = csv.DictReader(f)
for row in data:
    print(row)

