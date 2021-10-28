
def read(file_path):
    with open(file_path) as file: #The function should start by opening the specified file for reading.
        csv_reader = csv.reader(file) #differ from the txt
        #The function should then read in and display the headings in the format 
        # "Headings:\n{headings}" where {headings} is the headings that have been retrieved from the CSV file.
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")
        #The function should then display the message "Values:".
        print("Values:")
#For each line remaining in the file, the function should do the following:
#The function should display the values for that line.
        for values in csv_reader:
            print(values)

def run():
    read("bots.csv")

if __name__ == "__main__":
    run() 
    #still cant find the directory for some reason
    #[Errno 2] No such file or directory: 'bots.csv