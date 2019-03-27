import tkinter as tk
from tkinter import PhotoImage, Label, Text, END
import csv
from PIL import Image, ImageTk
from bücher_leser import BuchHinzufuegen as bh
from büchersuche import Büchersuche
import sys


suche1 = bh
datei = 'bücherrei.csv'
window = tk.Tk()
window.title("Bibliothek")
window.geometry("400x400")



#  image
load = Image.open("Bibliothek_icon.gif")
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
img.place(x=100, y=150)


bh = Büchersuche()
#---Funktionen----

ib = tk.Button(text="Indexsuche")


def search_author(author_name, *args):
    with open(datei) as d:
        reader = csv.reader(d)
        number = 0
        for item in args:
            item.delete(0, tk.END)
            for row in reader:
                try:
                    if row[2].lower() == author_name.lower():
                        found1 = tk.Tk()
                        found1.title("Bookinfos")
                        found1.geometry("200x200")
                        name1 = tk.Label(found1, text="Name:   " + row[1])
                        name1.grid(row=1, column=2)
                        author1 = tk.Label(found1, text="Author:   " + row[2])
                        author1.grid(row=2, column=2)
                        genre1 = tk.Label(found1, text="Genre:   " + row[3])
                        genre1.grid(row=3, column=2)
                        index1 = tk.Label(found1, text="Index:   " + row[0])
                        index1.grid(row=4, column=2)
                        btn2 = tk.Button(found1, text="Exit", command=lambda: sys.exit())
                        btn2.grid(row=5, column=3)
                        btn3 = tk.Button(found1, text="neue Suchen", command=lambda : suchen())
                        btn3.grid(row=6, column=3)
                        number +=1
                except IndexError:
                    break

        if number == 0:
            not_found1 = tk.Tk()
            not_found1.title("Book not found")
            not_found1.geometry("200x200")
            not_found = tk.Label(not_found1,
                                 text="Kein Buch von\n diesem Autor gefunen.\nBitte versuchen sie"
                                                  " es nochmal.")
            not_found.grid(row=3, column=5)

            btn2 = tk.Button(not_found1, text="Exit", command=lambda: sys.exit())
            btn2.grid(row=6, column=5)
            btn3 = tk.Button(not_found1, text="neue Suchen", command=lambda: suchen(not_found1))
            btn3.grid(row=7, column=5)


def search_buchname(name, *args):
    with open(datei) as d:
        reader = csv.reader(d)
        number = 0
        for item in args:
            item.delete(0, tk.END)
        for row in reader:
            try:
                if row[1].lower() == name.lower():
                    found1 = tk.Tk()
                    found1.title("Bookinfos")
                    found1.geometry("200x200")
                    name1 = tk.Label(found1, text="Name:   " + row[1])
                    name1.grid(row=1, column=2)
                    author1 = tk.Label(found1, text="Author:   " + row[2])
                    author1.grid(row=2, column=2)
                    genre1 = tk.Label(found1, text="Genre:   " + row[3])
                    genre1.grid(row=3, column=2)
                    index1 = tk.Label(found1, text="Index:   " + row[0])
                    index1.grid(row=4, column=2)
                    btn2 = tk.Button(found1, text="Exit", command=lambda: sys.exit())
                    btn2.grid(row=5, column=3)
                    number +=1
                    btn3 = tk.Button(found1, text="neue Suchen", command=lambda: suchen(not_found1))
                    btn3.grid(row=6, column=3)
            except IndexError:
                break

        if number == 0:
            not_found1 = tk.Tk()
            not_found1.title("Book not found")
            not_found1.geometry("200x200")
            not_found = tk.Label(not_found1,
                                 text="Kein Buch unter\n diesem Namen gefunen.\nBitte versuchen sie"
                                                  " es nochmal.")
            not_found.grid(row=3, column=5)

            btn2 = tk.Button(not_found1, text="Exit", command=lambda: sys.exit())
            btn2.grid(row=6, column=5)
            btn3 = tk.Button(not_found1, text="neue Suchen", command=lambda: suchen(not_found1))
            btn3.grid(row=7, column=5)


def search_index(index, *args):

    with open(datei) as d:
        reader = csv.reader(d)
        number = 0

        for item in args:
            item.delete(0, tk.END)
        for row in reader:
            try:
                if row[0] == str(index):

                    found1 = tk.Tk()
                    found1.title("Bookinfos")
                    found1.geometry("200x200")
                    name1 = tk.Label(found1, text="Name:   " + row[1])
                    name1.grid(row=1, column=2)
                    author1 = tk.Label(found1, text="Author:   " + row[2])
                    author1.grid(row=2, column=2)
                    genre1 = tk.Label(found1, text="Genre:   " + row[3])
                    genre1.grid(row=3, column=2)
                    btn2 = tk.Button(found1, text="Exit", command=lambda: sys.exit())
                    btn2.grid(row=5, column=2)
                    number += 1
                    btn3 = tk.Button(found1, text="neue Suchen", command=lambda: suchen(found1))
                    btn3.grid(row=6, column=2)
            except IndexError:
                break

        if number == 0:
            # else:
            not_found1 = tk.Tk()
            not_found1.title("Book not found")
            not_found1.geometry("200x200")
            not_found = tk.Label(not_found1, text="Kein Buch unter\n diesem Index gefunen.\nBitte versuchen sie"
                                                  " es nochmal.")
            not_found.grid(row=3, column=5)

            btn2 = tk.Button(not_found1, text="Exit", command=lambda: sys.exit())
            btn2.grid(row=6, column=5)
            btn3 = tk.Button(not_found1, text="neue Suchen", command=lambda: suchen(not_found1))
            btn3.grid(row=7, column=5)


def hinzufuegen(*args, add_button, search_button):
    search_button.destroy()
    add_button.destroy()
    with open(datei, 'a', newline='') as a:
        index1 = Büchersuche.get_index(bh)
        if args == True:
            index1 = index1 + 1

        for item in args:
            if isinstance(item, tk.Button):
                item.destroy()

        #---LABEL---
        l1 = tk.Label(text="Bitte füllen sie die folgenden Felder aus:")
        l1.grid(row=0, column=2, )

        l2 = tk.Label(text="Name des Buches")
        l2.grid(row=1, column=2)

        l3 = tk.Label(text="Name des Autors")
        l3.grid(row=2, column=2)

        l4 = tk.Label(text="Name des Genres")
        l4.grid(row=3, column=2)

        #---Entries---

        e1 = tk.Entry()
        e1.grid(row=1, column=3)

        e2 = tk.Entry()
        e2.grid(row=2, column=3)

        e3 = tk.Entry()
        e3.grid(row=3, column=3)

        try:
            int(index1) + 1
        except ValueError:
            index2 = 0
        else:
            index2 = int(index1) + 1

        def speichere_bücher():
            datei = 'bücherrei.csv'
            with open(datei, 'a', newline='') as a:
                writer1 = csv.writer(a)

                name = str(e1.get())
                author = str(e2.get())
                genre = str(e3.get())
                index = index2
                writer1.writerow([index, name, author, genre])
                gespeichert = tk.Label(text="Das Buche wurde gespeichert, \n unter dem Index " + str(index))
                gespeichert.grid(row=6, column=2)

                btn2 = tk.Button(text="Exit", command=lambda: sys.exit())
                btn2.grid(row=8, column=2)
                btn3 = tk.Button(text="weiteres Buch hinzufügen", command=lambda: hinzufuegen(1, add_button=add_button, search_button=search_button))
                btn3.grid(row=9, column=2)

        # ---BUTTONS---
        b1 = tk.Button(text="Buch hinzufügen", command=speichere_bücher)
        b1.grid(row=5, column=3)
        window.mainloop()


def entry_athor():

    entr3 = tk.Entry()
    entr3.grid(row=4, column=1)

    btn3 = tk.Button(text="Lock", command=lambda: search_author(entr3.get(), entr3))
    btn3.grid(row=4, column=2)


def entry_index():
    entr1 = tk.Entry()
    entr1.grid(row=2, column=1)

    btn2 = tk.Button(text="Lock", command=lambda: search_index(entr1.get(), entr1))
    btn2.grid(row=2, column=2)


def entry_name():

    name2 = tk.Entry()
    name2.grid(row=3, column=1)

    btn2 = tk.Button(text="Lock", command=lambda: search_buchname(name2.get(), name2))
    btn2.grid(row=3, column=2)


def suchen(*args):
    l1.destroy()
    b1.destroy()
    b2.destroy()

    for item in args:
        item.destroy()

    if args == 0:
        suche_window = tk.Tk()
        suche_window.title("Suche")
        suche_window.geometry("400x400")
    window.geometry("300x150")
    btn1 = tk.Button(text="Indexsuche", command=lambda: entry_index())
    btn1.grid(row=2, column=0)

    btn3 = tk.Button(text="Buchnamensuche", command=lambda: entry_name())
    btn3.grid(row=3, column=0)

    btn3 = tk.Button(text="Autorname", command=lambda: entry_athor())
    btn3.grid(row=4, column=0)


l1 = tk.Label(text="Wollen sie ein Buch hinzufügen oder suchen?")
l1.grid(row=1, column=2)

# ---BUTTONS----
b1 = tk.Button(text="Hinzufügen", command=lambda: remove_text and hinzufuegen(l1, add_button=b1, search_button=b2,))
b1.grid(row=4, column=2)


b2 = tk.Button(window, text="Suchen", command=suchen)
b2.grid(row=4, column=3)


def remove_text():
    print("removing text")
    l1.destroy()


window.mainloop()
