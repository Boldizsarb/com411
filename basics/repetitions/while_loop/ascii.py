print("How many bars should be charged?")
number_of_bars = int (input()) #answer
bars_charged = 0 #variable
print()
while bars_charged < number_of_bars:
    bars_charged = bars_charged +1 
    print(f"Charging: {'█' * bars_charged}") #the asci must be in single quote
print("Battery fully charged")
