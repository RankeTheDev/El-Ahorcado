import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import random
from Palabras import words_list
from Fases_Ahorcado import Fases_ahorcado

class Ahorcado_App(ttk.Window):
    def __init__(self, themename="cyborg"):

        # SET-UP DE LA self
        super().__init__(themename=themename)
        self.title("El Ahorcado")
        self.geometry("1280x720")
        self.bind("<Escape>", lambda event: self.destroy())

        # PARTES DE LA APP
        self.widgets = Widgets(self)


        # RUN
        self.mainloop()

class Widgets(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x= 0, y= 0, relwidth= 1, relheight= 1)

        self.Choose_Word()
        self.Widgets_Grid()
        self.Create_Widgets()
    
    # LOGICA PARA ESCOGER LA PALABRA AL AZAR
    def Choose_Word(self):
        # ACCESIBLE GLOBAL
        global word
        global hidden_word
        global chances
        global failed_letters
        global guess_word
        
        # ESCOGE LA PALABRA
        word = random.choice(words_list)
        hidden_word = ["_"] * len(word)
        chances = 5
        failed_letters = list(("Test","Test","Test","Test","Test"))
        guess_word = False

        # TEST DE LA FUNCIÓN PARA LA PALABRA OCULTA
        print(hidden_word, word)

    def Widgets_Grid(self):
        # COLUMN CONFIGURE
        self.columnconfigure((0, 9), weight= 3)
        self.columnconfigure((1), weight= 15)
        self.columnconfigure((2), weight= 11)
        self.columnconfigure((3), weight= 13)
        self.columnconfigure((4), weight= 10)
        self.columnconfigure((5), weight= 5)
        self.columnconfigure((6), weight= 27)
        self.columnconfigure((7), weight= 10)
        self.columnconfigure((8), weight= 4)

         # ROW CONFIGURE
        self.rowconfigure((0,6), weight= 4)
        self.rowconfigure((1), weight= 21)
        self.rowconfigure((2), weight= 15)
        self.rowconfigure((3), weight= 18)
        self.rowconfigure((4), weight= 19)
        self.rowconfigure((5), weight= 19)

    def Create_Widgets(self):
        # FUNCIÓN PARA LA SELECCIÓN DEL DIBUJO DEL AHORCADO
        def Elegir_Ahorcado():
            if chances == 5:
                return Fases_ahorcado[0]
            elif chances == 4:
                return Fases_ahorcado[1]
            elif chances == 3:
                return Fases_ahorcado[2]
            elif chances == 2:
                return Fases_ahorcado[3]
            elif chances == 1:
                return Fases_ahorcado[4]
            elif chances == 0:
                return Fases_ahorcado[5]
        Fase_ahorcado = Elegir_Ahorcado() 
        print(Fase_ahorcado)
        
        Colores_Background=("green","gold","red")
        def Elegir_Background():
            if chances == 5:
                return Colores_Background[0]
            elif chances >= 3:
                return Colores_Background[1]
            else:
                return Colores_Background[2]
        color_bg = Elegir_Background()

        # FUNCION PARA OBTENER LA GUESS
        def Boton_Enviar():
            global guess
            guess = Entry_Guess.get()

        # CREAR WIDGETS
        Label_Tittle = ttk.Label(self, font = "Cambria 25 bold", text= "EL AHORCADO", background= "silver", foreground= "black", anchor= "center")
        Label_Guess = ttk.Label(self, font= "Calibri 14", text= "Introduzca una letra o palabra para adivinar:", background= "blue", anchor= "center")
        Entry_Guess = ttk.Entry(self, font= "Calibri 20", foreground= "green", justify= "center")
        Button_Submit = ttk.Button(self, text= "Enviar", command= Boton_Enviar)
        Label_Failed_Guesses = ttk.Label(self, font= "Calibri 14", text= "Estas letras y palabras son incorrectas:", background= "purple", anchor= "center")
        Label_Failed_Guesses_List = ttk.Label(self, font= "Calibri 14", text= failed_letters, background= "purple", anchor= "center")
        Label_Chances = ttk.Label(self, font= "Calibri 14", text= "Intentos restantes", background= color_bg, anchor= "center") #Fondo dinámico
        Label_ChancesNumber = ttk.Label(self, font= "Calibri 36", text= chances, background= color_bg, anchor= "center") #Fondo dinámico
        Label_Hangman = ttk.Label(self, font= "Calibri 14", text= Fase_ahorcado, background= color_bg, anchor= "center") #Fondo dinámico
        Label_Hidden_Word = ttk.Label(self, font= "Calibri 20", text = "Esta es la palabra oculta", anchor= "center")
        Label_Hidden_Word_Show = ttk.Label(self, font= "Calibri 36", text = hidden_word, anchor= "center")
        
        # PLACE
        Label_Tittle.grid(row= 1, column= 1, columnspan= 8, sticky= "nsew", padx= 5, pady= 5)
        Label_Guess.grid(row= 2, column= 2, sticky= "nsew", padx= 5, pady= 40)
        Entry_Guess.grid(row= 2 , column= 4, columnspan= 3, sticky= "nsew", padx= 10, pady= 40)
        Button_Submit.grid(row= 2, column= 7, sticky= "nsew", padx= 10, pady= 50)
        Label_Failed_Guesses.grid(row= 3, column= 2, sticky= "nsew", padx= 5, pady= 25)
        Label_Failed_Guesses_List.grid(row= 3, column= 4, columnspan= 4, sticky= "nsew", padx= 50, pady= 25)
        Label_Chances.grid(row= 4 , column= 2, columnspan= 1, sticky= "nsew", padx= 33, pady= 5)
        Label_ChancesNumber.grid(row= 5 , column= 2, columnspan= 1, sticky= "nsew", padx= 33, pady= 5)
        Label_Hangman.grid(row= 4, column= 3, rowspan= 2, columnspan= 2, sticky= "nsew", padx= 20, pady= 10)
        Label_Hidden_Word.grid(row= 4, column= 6, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)
        Label_Hidden_Word_Show.grid(row= 5, column= 6, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)
        
Ahorcado_App()