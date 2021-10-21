import os #it goes above the function this way we do not need ot repeat that all over again
def cwd():
    path = os.getcwd()
    print(f"Current workning Directory: {path}")
    for file in os.listdir(path):
        print(file)
def run():
    print("Processing")
    cwd()


run()