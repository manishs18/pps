import csv

pathCSV = "D:\\Wipro\\24NAG4084\\pythonwork\\day05\\"
fileName = pathCSV+"sample2.csv"

content = []
with open(fileName,"r") as fp:
    r = csv.reader(fp)
    print(type(r))
    print(r)

    for row in r:
        print(row, type(row))
        if row[0] == "manish":
            row[0] = "singh"
        content.append(row)

    for row in content:
        print(row, type(row))


with open(fileName,"w",newline="") as fp:
    wc = csv.writer(fp)
    wc.writerows((content))
