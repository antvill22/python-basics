import sys
import csv
from tabulate import tabulate

if len(sys.argv)==2:
    f=sys.argv[1]
    if f.endswith(".csv"):
        try:
            with open(f,newline='') as file:
                reader = csv.DictReader(file)
                table = tabulate(reader, headers="keys", tablefmt="grid")
                print(table)

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")
elif len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments ")
