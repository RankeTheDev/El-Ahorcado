import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

# setup
window = ttk.Window()
window.title("EL AHORCADO")
window.geometry("750x750")
window.minsize(600, 400)

# widgets
Label_Tittle = ttk.Label(window, text = "Label_Tittle", background= "red", font = "Arial 25 bold")
Label_Guess = ttk.Label(window, text = "Label_Guess", background= "green")
Entry_Guess = ttk.Entry(window, background= "green")
Label_Failed_Guesses = ttk.Label(window, text = "Label_Failed_Guesses", background= "orange")
Label_Failed_Guesses_List = ttk.Label(window, text = "Label_Failed_Guesses_List", background= "brown")
Label_Chances = ttk.Label(window, text = "Label_Chances", background= "pink")
Label_ChancesNumber = ttk.Label(window, text = "Label_ChancesNumber", background= "gray")
Label_Hangman = ttk.Label(window, text = "Label_Hangman", background= "gray")
Label_Hidden_Word = ttk.Label(window, text = "Label_Hidden_Word", background= "white")
Label_Hidden_Word_Show = ttk.Label(window, text = "Label_Hidden_Word_Show", background= "white")

# configuro las columnas y filas
    # COLUMN CONFIGURE
window.columnconfigure((0, 9), weight= 3)
window.columnconfigure((1), weight= 15)
window.columnconfigure((2), weight= 11)
window.columnconfigure((3), weight= 13)
window.columnconfigure((4), weight= 10)
window.columnconfigure((5), weight= 5)
window.columnconfigure((6), weight= 25)
window.columnconfigure((7), weight= 12)
window.columnconfigure((8), weight= 4)

    # ROW CONFIGURE
window.rowconfigure((0,6), weight= 4)
window.rowconfigure((1), weight= 21)
window.rowconfigure((2), weight= 13)
window.rowconfigure((3), weight= 20)
window.rowconfigure((4), weight= 19)
window.rowconfigure((5), weight= 19)

#place a widget
Label_Tittle.grid(row= 1, column= 2, columnspan=5, sticky= "nsew", padx= 5, pady= 5)
Label_Guess.grid(row= 2, column= 1, columnspan= 3, sticky= "nsew", padx= 5, pady= 40)
Entry_Guess.grid(row= 2 , column= 4, columnspan= 5, sticky= "nsew", padx= 20, pady= 40)
Label_Failed_Guesses.grid(row= 3, column= 1, columnspan= 3, sticky= "nsew", padx= 5, pady= 40)
Label_Failed_Guesses_List.grid(row= 3, column= 4, columnspan= 5, sticky= "nsew", padx= 5, pady= 40)
Label_Chances.grid(row= 4 , column= 1, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)
Label_ChancesNumber.grid(row= 5 , column= 1, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)
Label_Hangman.grid(row= 4, column= 3, rowspan= 2, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)
Label_Hidden_Word.grid(row= 4, column= 6, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)
Label_Hidden_Word_Show.grid(row= 5, column= 6, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)

# run
window.mainloop()