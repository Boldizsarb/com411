print("Hey, what is your name?")
name = input()
print(f"Dear{name}, are you tiredt?")
answer2 = input()
if answer2 == ("yes") or ("little"):
    print("I know a cosy hotel nearby!")
    hotel_where = input()
    if hotel_where == ("where?"):
       print("It is just around the corner on your left. Do you need company?")
       company_answer = input()
        if company_answer == ("yes") or ("maybe"):
            print("Let us go then, I will show you the way.")
        else:
            print("somehting")
    else:
        print('In case you get lost just wistle 2 times and I will find you.')

elif answer2 == ("noo"):#why?? 
    print("Are you in the mood for football?")
    answer3 = input()
    if answer3 == ("yes"):
        for letsgo in "letsgo":
            print(letsgo)
else:
    print("Go and be misarable somwhere else.")