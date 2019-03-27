import csv


class Büchersuche():
    def get_index(self):
        name = 'bücherrei.csv'
        with open(name) as a:
            rows = []
            reader = csv.reader(a)
            for row in (list(reader)):
                try:
                    index = (row[0])
                except IndexError:
                    index = "index"
                else:
                    index = (row[0])
                rows.append(row)

            # rows.reverse()

            return index

