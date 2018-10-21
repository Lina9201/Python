import csv
with open("Policy.csv", encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    for line in reader:
        print(line[12])
        line[12]
    #print(line)


