largest = None
smallest = None

while True:
    try:
        n = input("Please enter an integer: ")
        if n == "done":
            break
        n = int(n)
        if( largest is None or largest < n):
            largest = n
        if(smallest is None or smallest > n):
            smallest = n
    except ValueError:
        print("Invalid input")


print("Maximum is", largest)
print("Minimum is", smallest)
