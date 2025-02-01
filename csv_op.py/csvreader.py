import csv

with open('MOCK_DATA.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    fieldnames = csv_reader.fieldnames
    rows = list(csv_reader)
    with open('new_names.csv','w',newline='') as c:
        csv_writer = csv.DictWriter(c,fieldnames=fieldnames,delimiter=',');
        csv_writer.writeheader()
        for line in rows:
            del line['email'] # delete the field email from the entry
            csv_writer.writerow(line)
   