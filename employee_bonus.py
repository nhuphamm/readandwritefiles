import csv

with open("EmployeePay.csv", "r") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        print(row)

    # pause = input("Press Enter to continue")
    # if pause == "Enter":
    #     break
