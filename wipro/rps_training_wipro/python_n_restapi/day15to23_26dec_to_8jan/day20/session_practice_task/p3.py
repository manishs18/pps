import os
import csv

# os.mkdir("data")
#os.rmdir("data")


with open("data\\sap1.csv","r") as file:
    rContent = csv.DictReader(file)

    for row in rContent:
        print(type(row), row)
        print(row['Name'],row['Age'],row['City'])


