import csv


class DataReader:
    @staticmethod
    def get_csv_data(filename):
        rows = []
        data_file = open(filename, "r")
        reader = csv.reader(data_file)
        next(reader, None)
        # Pomin pierwszy wiersz (naglowki)
        for row in reader:
            rows.append(row)
        return rows

