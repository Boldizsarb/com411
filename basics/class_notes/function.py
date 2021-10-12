def get_name(): #this is only defining the function not execution
    print("Please enter your name")
    name = input()
    print(f"your name is {name}")
    print("please enter weight")
    weight = float (input())
    print("please enter your height")
    height = float (input())
    bmi = weight / (height ** 2)
    print(f"{name} your bmi is {bmi}")

#return
def get_name2():
    print("please enter your name")
    name = input()
    return name #it returns the value in this case the name
get_name2() 


#call to a function execution
get_name()


def display_name():
    print(f"*** {get_name} ***") #we did not want to ask for name again
#call for the function again
display_name() #by using this the get_name and display_name is tied together


#parameter
def diplay_name(name):
    print(f" *** {name} ***")

#call to a function
name = get_name()
display_name(name)