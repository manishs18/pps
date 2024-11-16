#Exercise 6: Write all content of a given file into a new file by skipping line number 5

with open("C:/Users/mkuma/OneDrive/Desktop/New folder/pps/pps/piaoe/e6.txt", "r") as fr:
    c = fr.readlines()

with open("C:/Users/mkuma/OneDrive/Desktop/New folder/pps/pps/piaoe/n6.txt", "w") as fw:
    count = 0
    for line in c:
        if count == 4:
            count = count + 1
            continue
        else:
            fw.write(line)

        count = count + 1
