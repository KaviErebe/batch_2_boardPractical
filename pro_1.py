'''Write a python program to implement searching methods based on user choice using a list
data-structure. (linear & binary)'''


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

def binary_search(arr,target):
    
    start = 0
    end = len(arr) -1
    
    while start<=end:
        
        mid = (start + end) //2
        
        if arr[mid] == target:
            i = mid
            return i
        if target > arr[mid] :
            start = mid + 1
            
        else:
            end = mid-1
            

    return -1

arr = [23, 7, 42, 13, 4, 18, 10, 29, 35, 2]

while True:
    print("\nChoose a searching method:\n1. Linear Search\n2. Binary Search\n3. break")
    choice = input("Enter your choice: ")

    if choice == '1':
        target = int(input("Enter the element to search: "))
        result = linear_search(arr, target)
        if result != -1:
            print(f"Element {target} found at index {result}.")
        else:
            print(f"Element {target} not found in the list.")

    elif choice == '2':
        target = int(input("Enter the element to search:"))
        arr.sort()
        result = binary_search(arr,target)
        if result != -1:
            print(f"Element {target} found at index {result}.")
        else:
            print(f"Element {target} not found in the list.")
    elif choice == "3":
        break

    else:
        print("Invalid choice.")

