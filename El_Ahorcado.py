import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import random
from Palabras import words_list
from Fases_Ahorcado import Fases_ahorcado

# LOGICA PARA LA PALABRA AL AZAR
    # BASE 
word = random.choice(words_list)
hidden_word = ["_"] * len(word)
chances = 5
failed_letters = list()
guess_word = False
print(hidden_word, word)

# SET-UP DE LA VENTANA
window = ttk.Window(themename="cyborg")
window.title("EL AHORCADO")
window.attributes("-fullscreen", True)
window.bind("<Escape>", lambda event: window.destroy())

# WIDGETS
Label_Tittle = ttk.Label(window, text = "EL AHORCADO", background= "blue", font = "Cambria 25 bold", anchor= "center")
Label_Guess = ttk.Label(window, font= "Calibri 14", text = "Introduzca una letra o palabra para adivinar:", background= "green", anchor= "center")
Entry_Guess = ttk.Entry(window, font= "Calibri 20", foreground= "green", justify="center")
Button_Submit = ttk.Button(window, text="Enviar", command= lambda: print(chances))
Label_Failed_Guesses = ttk.Label(window, font= "Calibri 14", text = "Estas letras y palabras son incorrectas:", background= "red", anchor= "center")
Label_Failed_Guesses_List = ttk.Label(window, font= "Calibri 14", text = failed_letters, background= "red", anchor= "center")
Label_Chances = ttk.Label(window, font= "Calibri 14", text = "Intentos restantes", background= "brown", anchor= "center") #Fondo dinámico
Label_ChancesNumber = ttk.Label(window, font= "Calibri 36", text = chances, background= "brown", anchor= "center") #Fondo dinámico
Label_Hangman = ttk.Label(window, font= "Calibri 14", text = Fases_ahorcado[3], background= "brown", anchor= "center") #Fondo dinámico
Label_Hidden_Word = ttk.Label(window, font= "Calibri 20", text = "Esta es la palabra oculta", anchor= "center")
Label_Hidden_Word_Show = ttk.Label(window, font= "Calibri 36", text = hidden_word, anchor= "center")


# CONFIGURO ROWS Y COLUMNS
    # COLUMN CONFIGURE
window.columnconfigure((0, 9), weight= 3)
window.columnconfigure((1), weight= 15)
window.columnconfigure((2), weight= 11)
window.columnconfigure((3), weight= 13)
window.columnconfigure((4), weight= 10)
window.columnconfigure((5), weight= 5)
window.columnconfigure((6), weight= 27)
window.columnconfigure((7), weight= 10)
window.columnconfigure((8), weight= 4)

    # ROW CONFIGURE
window.rowconfigure((0,6), weight= 4)
window.rowconfigure((1), weight= 21)
window.rowconfigure((2), weight= 15)
window.rowconfigure((3), weight= 18)
window.rowconfigure((4), weight= 19)
window.rowconfigure((5), weight= 19)

# PONGO LOS ELEMNTOS EN EL GRID

Label_Tittle.grid(row= 1, column= 1, columnspan= 8, sticky= "nsew", padx= 5, pady= 5)
Label_Guess.grid(row= 2, column= 2, sticky= "nsew", padx= 5, pady= 40)
Entry_Guess.grid(row= 2 , column= 4, columnspan= 3, sticky= "nsew", padx= 10, pady= 40)
Button_Submit.grid(row= 2, column= 7, sticky= "nsew", padx= 10, pady= 50)
Label_Failed_Guesses.grid(row= 3, column= 2, sticky= "nsew", padx= 5, pady= 50)
Label_Failed_Guesses_List.grid(row= 3, column= 4, columnspan= 4, sticky= "nsew", padx= 50, pady= 50)
Label_Chances.grid(row= 4 , column= 2, columnspan= 1, sticky= "nsew", padx= 33, pady= 5)
Label_ChancesNumber.grid(row= 5 , column= 2, columnspan= 1, sticky= "nsew", padx= 33, pady= 5)
Label_Hangman.grid(row= 4, column= 3, rowspan= 2, columnspan= 2, sticky= "nsew", padx= 5, pady= 50)
Label_Hidden_Word.grid(row= 4, column= 6, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)
Label_Hidden_Word_Show.grid(row= 5, column= 6, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)


# RUN
window.mainloop()