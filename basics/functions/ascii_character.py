#converting ASCII back to strings
print("Program started")
print("Please enter an ASCII code:")
asci_values = int(input())

if asci_values >= 32 and asci_values <= 126:
    print(f"The character represented by the value {asci_values} is: {chr(asci_values)}")
else:
    print("character can not be displayed!")
#The chr() method returns a string representing a 
# character whose Unicode code point is an integer. 
# The chr() method takes only one integer as argument.

