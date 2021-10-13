print("How many numbers should I sum up?")
response = int(input())
summed = 0 #control variable
print()
total = 0 # sum numbers

while summed < response:
    print(f"Please enter number {response} of {summed} :")
    number = int(input())
    total = total + number
    summed = summed +1 
print(f"The answer is {total}")
