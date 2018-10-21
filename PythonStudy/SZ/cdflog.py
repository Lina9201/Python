import csv
with open('Policy.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Message']=='GET: /api/healthcheck: 0ms: 200: OK':
            print(row['Time'],row['Message'])