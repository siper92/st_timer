import csv

# indexes
FUNCTION_LEVEL = 1
FUNCTION_NUMENR = 2

with open("./trace.89137710.xt") as tsv:
    count = 0
    for line in csv.reader(tsv, dialect="excel-tab"):
        if len(line) < 3:
            continue
        # print(line)
        if count < 10 and (len(line) > 3):
            print(line[2])
        count += 1

    print(count)

print("end")
