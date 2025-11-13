number = int(input("Enter a five-digit integer: "))
digit1 = number // 10000
number = number % 10000
print(digit1, end=' ')

digit2 = number // 1000
number = number % 1000
print(digit2, end=' ')

digit3 = number // 100
number = number % 100
print(digit3, end=' ')

digit4 = number // 10
number = number % 10
print(digit4, end=' ')

digit5 = number
print(digit5)
