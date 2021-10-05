# ask the user if it is suny
print("Is it sunny")
is_sunny = input().lower()

print("Is ther a breeze?")
is_breeze = input().lower()

if is_sunny == "yes" and is_breeze == "yes": #why two equal == sign
    if is_breeze == "yes":
        print("Clothes are dry")
    else:
        print("clothes are drying slowly")
else:
    print("clothes are not dry")
