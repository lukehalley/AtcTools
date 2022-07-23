import csv

def loadCSVAsDict(csvPath):
    with open(csvPath) as f:
        file_data = csv.reader(f)
        headers = next(file_data)
        return [dict(zip(headers, i)) for i in file_data]