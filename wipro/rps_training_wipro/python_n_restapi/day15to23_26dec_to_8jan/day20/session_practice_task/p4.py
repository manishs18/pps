import csv


content = [
    {"Name":"abcd1","Age":22,"City":"xyz1"},
    {"Name": "abcd2", "Age": 23, "City": "xyz2"}
]

with open("data\\sap3.csv", "w",newline="") as fp:
    fileName = ["Name","Age","City"]
    wContent = csv.DictWriter(fp,fieldnames=fileName)
    wContent.writeheader()
    wContent.writerows(content)
