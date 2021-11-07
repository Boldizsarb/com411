
LINE_WIDTH = 85
def started(msg=""):
    output = f"Operatin started: {msg}..."
    dashes = "-" * LINE_WIDTH
    print(f"{dashes}\n {output}\n")

def completed():
    dashes = "-" * LINE_WIDTH
    print(f"\nOperation completed.\n{dashes}\n")

def error(msg):
    print(f"Error!{msg}\n Invalid section!")

def menu():
    print(f"""Please select one of the following options:
       {"[years]":<10} List unique years
       {"[tally]":<10} Tally up medals
       {"[team]":<10} Tally up medals for each team
       {"[exit]":<10} Exit the program
       """)
    selection = input("Your selection: ")
    return selection.strip().lower()
