def display_ladder(steps):
    #displaying each step:
    for step in range(steps): #for each step it will display a ladder
        print("| |")
        print("***")
    print("| |")

def create_ladder():
    print("How many steps should I take?")
    steps = int(input()) # variable is the parameter 
    display_ladder(steps)

create_ladder()


