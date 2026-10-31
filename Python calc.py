print("==simple_calculator==")
num1=float(input("Enter the first Number: "))
operator=input("Enter operator(+,-,*,/): ")
num2=float(input("Enter the second Number: "))
if operator== "+":
  result= num1 + num2
elif operator=="-":
  result= num1 - num2
elif operator=="*":
  result= num1 * num2
elif operator=="/":
  result= num1 / num2
else:
  result="Invalid operator"
print("Result:", result)