import csv
import pandas as pd

# with open("customers.csv", "r") as csvfile:
#     csvreader = csv.DictReader(csvfile)

#     with open("customer_country.csv", "w") as newfile:
#         fieldnames = ["FirstName", "LastName", "City"]
#         csv_writer = csv.DictWriter(newfile, fieldnames=fieldnames)
#         csv_writer.writeheader()

#         for line in csvreader:
#             del line["\ufeffID"]
#             del line["Country"]
#             del line["Phone"]
#             csv_writer.writerow(line)

csv_input = pd.read_csv("customers.csv", delimiter=",")
csv_input["FullName"] = csv_input["FirstName"].astype(str) + " " + csv_input["LastName"]

print(f"Total number of customer: {len(csv_input)} customers")

output = csv_input[["FullName", "Country"]]

output.to_csv("customer_country.csv", index=False)
