total_bill = float(input("Enter the total bill: "))
is_member = input("Are you a member? (yes/no: ").lower()

if total_bill >= 1000 and is_member == "yes":
    discount = total_bill * 0.1
    print(f"Discount: 10% off")
elif total_bill >= 1000 and is_member == "no":
    discount = total_bill * 0.05
    print(f"Discount: 5% off")
else:
    discount = 0
final_amount = total_bill - discount
print(f"final amount: = {final_amount:.2f}")
