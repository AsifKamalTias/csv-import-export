import csv


def importCSV(file_path):
    try:
        f = open(file_path, 'r')

        # reader = csv.reader(file_path)
        reader = csv.DictReader(f)

        for row in reader:
            print(row)

        f.close()

        print("Data imported successfully.")
    except:
        print("Something went wrong.")
    finally:
        print("Program terminated.")

importCSV('import.csv')