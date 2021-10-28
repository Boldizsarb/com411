def search(file_path):
    print("Searching...")
    with open(file_path) as file:
        for location in file:
            print(f"Looked in {location.strip()}")
    print("Done!")


def run():
    search("library.txt")


if __name__ == "__main__":
 run()
 #mine
 import os 
def search(file_name):
    print("Searching...")
    with open(file_name) as file:
        for line in file:
           # line = file.readline().strip()
            print(f"Looked in {location.strip()}")
def run():
    search("library.txt")

if __name__ == "__main__":
    run()
#ModuleNotFoundError: No module named 'txt'