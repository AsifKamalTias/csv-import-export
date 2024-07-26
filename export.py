import csv

def exportCSV(data):
    try:
        f = open("export.csv", "w", newline="")

        # writer = csv.writer(f)
        fields = ['name', 'age']
        writer = csv.DictWriter(f, fields)
        writer.writeheader()

        for row in data:
            writer.writerow(row)

        f.close()

        print("Data exported successfully.")
    except:
        print("Something went wrong.")
    finally:
        print("Program terminated.")

exportCSV([{'name': 'Anik', 'age': '26'},
        {'name': 'Asif', 'age': '22'},
        {'name': 'Jalil', 'age': '28'}])
