import csv

from büchersuche import Büchersuche


class BuchHinzufuegen():

    datei = 'bücherrei.csv'
    data = []
    with open(datei) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        count = 0
        for rows in reader:
            count += 1
        lineList = f.readlines()
        last_line = int(0)
        try:
            last_line = lineList[len(lineList) - 1]
        except IndexError:
            if count == 1:
                last_line = '0'
        else:
            last_line = lineList[len(lineList) - 1]

        for row in reader:
            list = []
            list.append(row[0]) #index
            list.append(row[1]) #name
            list.append(row[2]) #autor
            list.append(row[3]) #genre
            data.append(list)

    #neues Buch eingeben

    genres_list = []

    def enter_book(self, last_line, name, author, genre, datei):
        name2 = 'bücherrei.csv'
        data = []
        try:
            with open(datei, 'a', newline='') as a:
                writer = csv.writer(a)

                index = last_line
                index = int(index)
                index = index + 1
                index = str(index)

        except PermissionError:
            print("ERROR Bitte schließen sie Programme die eine .csv Datei offen haben und versuchen sie es nochmal")
        else:
            with open(datei, 'a', newline='') as a:
                writer = csv.writer(a)
                data.append(list)
                if len(data) == 0:
                    index = 0
                else:
                    index = last_line
                    index = int(index)
                    index = index + 1
                    index = str(index)
                print("\33[92m" + "Index = " + str(index) + '\33[0m')
                data.append(index)
                writerow = ([index, name, author, genre])
                print(index)
                return index











#Mach Funktion

