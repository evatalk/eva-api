import csv


class CSVFileReader(object):

    def __init__(self, file_name):
        self.csv_file_name = file_name

    def check_if_email_exists(self, email_address):
        with open(self.csv_file_name, encoding='utf-16-le', newline='') as f:
            reader = csv.reader(f.readlines(), delimiter='|', quotechar='|')
            count = 0
            for row in reader:
                a = row
                print(a)
                print("\n")
                print("Tamanho", len(a))
                print("\n")
                count += 1
                if count == 2:
                    break

    def close(self):
        pass


if __name__ == "__main__":

    test = CSVFileReader("csv_utf16.csv")
    test.check_if_email_exists("cu")