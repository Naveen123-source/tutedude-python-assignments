number = int(input("Enter a number: "))
def factorial(num):
   if num == 1:
      return 1
   else:
      return num * factorial(num-1)
result = factorial(number)
print(f"Factorial of {number} is: {result}")