import sys,csv

if len(sys.argv)==3:
    before=sys.argv[1]
    after=sys.argv[2]
    if before.endswith(".csv"):
        try:
            students = []
            with open(before) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append({"name": row["name"], "house": row["house"]})

            if after.endswith(".csv"):
                with open(after, "w") as file:
                    writer = csv.DictWriter(file, delimiter=',', fieldnames=["first", "last", "house"])
                    writer.writeheader()

                    for student in students:
                        full_name = student['name'].strip('""')
                        last, first = map(str.strip, full_name.split(","))
                        house = student['house']
                        writer.writerow({"first": first, "last": last, "house": house})
            else:
                sys.exit(f"{after}is not a csv")





        except :
            sys.exit(f"Could not read {before}")
    else:
        sys.exit("Not a CSV file")
elif len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments ")
