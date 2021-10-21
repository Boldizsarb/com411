import os
def display_chars(file_path, numer_characters):
    with open(file_path) as file: # the file path not specified just yet
        data = file.read(numer_characters) # variable with the parameter
        print(data)

def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print(data)

def display_text():
    with open(file_path) as file:
        data = file.read()
        print(data)

def run():
    display_chars(library.txt, 5) #the parameter is the variable the filepath
    display_line(library.txt)
    display_text(library.txt)

if __name__ == "__main__":
    run()

