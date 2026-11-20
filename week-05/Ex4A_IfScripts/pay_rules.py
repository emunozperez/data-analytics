pay_rate = float(input("Enter pay rate: "))
hours_worked = float(input("Enter hours worked: "))

if hours_worked <= 40:
    overtime_pay = (hours_worked - 40) * (pay_rate * 1.5)
    total_pay = (pay_rate * hours_worked) + overtime_pay
else:
    total_pay = pay_rate * hours_worked

print(f"Total pay is: ${total_pay:.2f}")