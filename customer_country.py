import csv

with open("customers.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile)

    with open("customer_country.csv", "w") as newfile:
        fieldnames = ["FirstName", "LastName", "City"]
        csv_writer = csv.DictWriter(newfile, fieldnames=fieldnames)
        csv_writer.writeheader()

        for line in csvreader:
            del line["\ufeffID"]
            del line["Country"]
            del line["Phone"]
            csv_writer.writerow(line)
