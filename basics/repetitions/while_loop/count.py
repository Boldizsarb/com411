print("How many live cables must I avoid?")
avoid = int (input()) #answer
livecables_avoided = 0 #variable
print()

while livecables_avoided < avoid: #first then the second
    print("Avoiding....", end="") # by using end="" it will be displayed on the same line. 
    livecables_avoided = livecables_avoided +1
    print(f"Done! {livecables_avoided} cables avoided")
print()
print("All live cables have been avoided.")
print()


