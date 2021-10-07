# out of 3 numbers how many even and odd. 
print("Please neter the first number")
first_number = int (input())
print("Please enter the second number")
second_number = int (input())
print("Please enter ther third number")
third_number = int (input())

# we are looking for the number of even and odd numbers
even_numbers = 0    #declaring variables
odd_numbers = 0
# determining which numbers are even and odd
if first_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if second_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers + 1

if third_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

print(f"There were {even_numbers} even number(s) and {odd_numbers} odd number(s)")
