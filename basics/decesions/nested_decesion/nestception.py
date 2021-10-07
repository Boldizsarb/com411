print("Where should I look?")
answer = input()
if answer == "in the bedroom":
        print("Where should I look in the bedroom?")
        answer1 = input()
        if answer1 == "under the bed":
            print("Found some shoes but not battery")
        else:
            print("Found some mess but not battery")

elif answer == "in the bathroom":
    print("Where in the bathroom should I look?")
    answer2 = input()
    if answer2 == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery")

elif answer == 'in the lab':
    print("Where in the lab should I look?")
    answer3 = input()
    if answer3 == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but not battery")

else:
    print("I am not suer where that place is located")


