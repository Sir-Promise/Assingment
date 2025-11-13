number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))

if number1 <= number2 and number1 <= number3:
   if number2 <= number3:
      print(number1, number2, number3)
   else:
      print(number1, number3, number2)
elif number2 <= number1 and number2 <= number3:
   if number1 <= number3:
      print(number2, number3, number1)
else:
   if number1 <= number2:
      print(number3, number1, number2)
   else:
      print(number3, number2, number1)
