import csv

with open("EmployeePay.csv", "r") as file:
    csv_reader = csv.DictReader(file, delimiter=",")

    for record in csv_reader:

        record2 = record["EmpFName"]
        record3 = record["EmpLName"]
        record4 = float(record["Salary"])
        record5 = float(record["Bonus"])

        total = (record4 * record5) + record4

        print("EmpFName: ", record2)
        print("EmpLName: ", record3)
        print("Salary: ", record4)
        print("Bonus: ", record5)
        print("Total: ", total)
        input("Press Enter to continue")
