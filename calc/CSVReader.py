import csv
# Read csv file and convert data into list format
class CSVReader:
    """Csv"""
    data = []

    def __init__(self, filepath):
        self.data = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass
