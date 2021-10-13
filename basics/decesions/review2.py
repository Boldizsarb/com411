
print("What type of cover does the book have?")
cover_type = input()
if cover_type == "soft":
    print("Is the book perfect bound?")
    bound = input() 
    if bound == "yes":
            print("Soft cover, perfect bound books are very popular")
            something_answer = input()
            if something_answer == ("whyy"):
                print("why do you work now?")
            elif something_answer == ("soemthing"):
                print("fuck you")

    else:
            print("Soft covers with coils or stitches are great for short books")
elif cover_type == "hard":
        print("Books with hard covers can be more expensive!")
else: 
    print("why would not you work?")