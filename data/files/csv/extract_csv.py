import csv 
def extract(file_path):
    print("Extracting...", end="") 
    with open(file_path) as file: #open the specified file for reading.
        csv_reader = csv.reader(file) #read in and ignore the headings.
        headings = next(csv_reader) #read in and ignore the headings.
        names = "" #create a variable named names which is set to an empty string i.e. ""
        # For each remaining line in the file:
        # read in the values and extract the name of the robot.
        #add the extracted name with a new line character to the variable names.
        for values in csv_reader:
            names += f"{values[1]}\n"
    print("Done!")
    #After all the lines have been processed, the function should display the message "Done! The extracted names are as follows:".
    print(f"The extracted names are:\n{names}")
def run():
    extract("C:\\Users\\Boyszy\\Visual studio reposatory\\com411\\data\\files\\csv\\bots.csv")

if __name__ == "__main__":
    run()

