
import csv
def read_data():
    data = {
        "survived": [], "sex": [], "age": [], "fare": []
    }
    with open("titanic.csv") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader) # header ingore
