a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

print("The lagest integer is:", largest)
