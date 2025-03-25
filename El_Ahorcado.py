import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import random
from Palabras import words_list
from Fases_Ahorcado import Fases_ahorcado

class Ahorcado_App(ttk.Window):
    def __init__(self, themename="cyborg"):

        # SET-UP DE SELF
        super().__init__(themename=themename)
        self.title("El Ahorcado")
        self.geometry("1280x720")
        self.minsize(960, 540)
        self.bind("<Escape>", lambda event: self.destroy())

        # PARTES DE LA APP
        self.widgets = Widgets(self)
        self.menu = Menu(self)
        # RUN
        self.mainloop()

class Widgets(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x= 0, y= 0, relwidth= 1, relheight= 1)

        # VARIABLES DE LA CLASE
        self.word = ""
        self.hidden_word = []
        self.chances = 5
        self.failed_letters = []
        self.guess_word = False
        self.guess = ""

        # FUNCIONES DE LA CLASE
        self.Choose_Word()
        self.Configure_Grid()
        self.Create_Widgets()
        self.Play()
    
    # LOGICA PARA ESCOGER LA PALABRA AL AZAR
    def Choose_Word(self):
        # ESCOGE LA PALABRA
        self.word = random.choice(words_list)
        self.hidden_word = ["_"] * len(self.word)
        self.chances = 5
        self.failed_letters = []
        self.guess_word = False

        # TEST DE LA FUNCIÓN PARA LA PALABRA OCULTA
        print(self.hidden_word, self.word)

    def Configure_Grid(self):
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

    
    # FUNCIÓN PARA LA SELECCIÓN DEL DIBUJO DEL AHORCADO
    def Elegir_Ahorcado(self):
        if self.chances == 5:
            return Fases_ahorcado[0]
        elif self.chances == 4:
            return Fases_ahorcado[1]
        elif self.chances == 3:
            return Fases_ahorcado[2]
        elif self.chances == 2:
            return Fases_ahorcado[3]
        elif self.chances == 1:
            return Fases_ahorcado[4]
        elif self.chances == 0:
            return Fases_ahorcado[5]
        #self.Fase_ahorcado = self.Elegir_Ahorcado 
        
    def Elegir_Background(self):
        if self.chances == 5:
            return "green"
        elif self.chances >= 3:
            return "gold"
        else:
            return "red"
    #color_bg = Elegir_Background()

        # FUNCION PARA OBTENER LA GUESS
            
    def Create_Widgets(self):    
        def Boton_Enviar():
            self.guess = self.Entry_Guess.get()
            self.update_game()
            self.Entry_Guess.delete(0, tk.END)
        
        # CREAR WIDGETS
        Label_Tittle = ttk.Label(self, font = "Cambria 25 bold", text= "EL AHORCADO", background= "silver", foreground= "black", anchor= "center")
        Label_Guess = ttk.Label(self, font= "Calibri 14", text= "Introduzca una letra o palabra para adivinar:", background= "blue", anchor= "center")
        self.Entry_Guess = ttk.Entry(self, font= "Calibri 20", foreground= "green", justify= "center")
        Button_Submit = ttk.Button(self, text= "Enviar", command= Boton_Enviar)
        Label_Failed_Guesses = ttk.Label(self, font= "Calibri 14", text= "Estas letras y palabras son incorrectas:", background= "red", anchor= "center")
        self.Label_Failed_Guesses_List = ttk.Label(self, font= "Calibri 14", text= self.failed_letters, background= "red", anchor= "center")
        Label_Chances = ttk.Label(self, font= "Calibri 14", text= "Intentos restantes", background= "purple", anchor= "center") #Fondo dinámico
        self.Label_Chances_Number = ttk.Label(self, font= "Calibri 36", text= self.chances, background= "purple", anchor= "center") #Fondo dinámico
        self.Label_Hangman = ttk.Label(self, font= "Calibri 14", text= self.Elegir_Ahorcado(), background= "purple", anchor= "center") #Fondo dinámico
        Label_Hidden_Word = ttk.Label(self, font= "Calibri 20", text = "Esta es la palabra oculta", anchor= "center")
        self.Label_Hidden_Word_Show = ttk.Label(self, font= "Calibri 36", text = self.hidden_word, anchor= "center")
        
        # PLACE
        Label_Tittle.grid(row= 1, column= 1, columnspan= 8, sticky= "nsew", padx= 5, pady= 5)
        Label_Guess.grid(row= 2, column= 2, sticky= "nsew", padx= 5, pady= 40)
        self.Entry_Guess.grid(row= 2 , column= 4, columnspan= 3, sticky= "nsew", padx= 10, pady= 40)
        Button_Submit.grid(row= 2, column= 7, sticky= "nsew", padx= 10, pady= 50)
        Label_Failed_Guesses.grid(row= 3, column= 2, sticky= "nsew", padx= 5, pady= 25)
        self.Label_Failed_Guesses_List.grid(row= 3, column= 4, columnspan= 4, sticky= "nsew", padx= 50, pady= 25)
        Label_Chances.grid(row= 4 , column= 2, columnspan= 1, sticky= "nsew", padx= 33, pady= 5)
        self.Label_Chances_Number.grid(row= 5 , column= 2, columnspan= 1, sticky= "nsew", padx= 33, pady= 5)
        self.Label_Hangman.grid(row= 4, column= 3, rowspan= 2, columnspan= 2, sticky= "nsew", padx= 20, pady= 10)
        Label_Hidden_Word.grid(row= 4, column= 6, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)
        self.Label_Hidden_Word_Show.grid(row= 5, column= 6, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)

    def Guess_Duplicada(self):
        window = tk.Toplevel(self.master)
        label = ttk.Label(window, text="Ya ha escogido esta letra antes o no ha introducido un valor válido")
        label.pack(fill='both', padx=25, pady=5)
        button_close = tk.Button(window, text="Close", command= window.destroy)
        button_close.pack(fill='x')
    
    # ACTUALIZAR EL ESTADO DEl JUEGO
    def update_game(self):
        # COMPRUEBA SI SE ADIVINÓ LA PALABRA COMPLETA
        if self.guess == self.word:
            self.guess_word = True
        # SI LA LETRA ESTA EN LA PALABRA A ADIVINAR
        elif self.guess in self.word:
            for i, letra in enumerate(self.word):
                if letra == self.guess:
                    self.hidden_word[i] = self.guess
        # SI LA LETRA NO ESTÁ EN LA PALABRA O LISTA DE FALLOS
        elif self.guess not in self.failed_letters:
            self.chances -= 1
            self.failed_letters.append(self.guess)
        else:
            self.Duplicada_PopUp()

        self.Label_Hidden_Word_Show.config(text=self.hidden_word)
        self.Label_Failed_Guesses_List.config(text=self.failed_letters)
        self.Label_Chances_Number.config(text=self.chances)
        self.Label_Hangman.config(text= self.Elegir_Ahorcado())

        if "_" not in self.hidden_word or self.guess_word == True:
            self.Win_PopUp()
        elif self.chances == 0:
            self.Lose_PopUp()
    
    # FUNCION PARA REINICIAR EL JUEGO
    def reiniciar_juego(self):
        # Vuelve a elegir la palabra
        self.Choose_Word() 
        # Actualiza los widgets
        self.Label_Hidden_Word_Show.config(text=self.hidden_word)
        self.Label_Failed_Guesses_List.config(text=self.failed_letters)
        self.Label_Chances_Number.config(text=self.chances)
        self.Label_Hangman.config(text=self.Elegir_Ahorcado())

    # POP UP DE VICTORIA
    def Win_PopUp(self):
        window = tk.Toplevel(self.master)
        window.geometry("550x150")
        window.resizable(0,0)
        window.title("🎉 🏆 ¡GANASTE! 🏆 🎉")
        Info_Win= f"Felicidades, acertaste la palabra '{self.word}' y ganaste el juego. \nAhora puedes salir del juego o intentar ganar de nuevo, ¿qué deseas hacer?"
        label = ttk.Label(window, text= Info_Win, wraplength= 510, justify= "center")
        label.pack(fill= "both", padx= 20, pady= 25)
        button_win_close = tk.Button(window, text="Salir del Ahorcado", command= lambda: self.master.destroy())
        button_win_close.pack(fill= "both", side= "bottom")
        button_win_reset = tk.Button(window, text="Volver a jugar", command= lambda: [self.reiniciar_juego(), window.destroy()])
        button_win_reset.pack(fill= "both", side= "bottom")

    # POP UP DE DERROTA
    def Lose_PopUp(self):
        window = tk.Toplevel(self.master)
        window.geometry("550x150")
        window.resizable(0,0)
        window.title("💀 😩 ¡PERDISTE! 😩 💀 ")
        Info_Lose= f"Una pena, no lograste acertar la palabra '{self.word}' y fuiste ahorcado. \nAhora puedes salir del juego o intentarlo de nuevo, ¿qué deseas hacer?"
        label = ttk.Label(window, text= Info_Lose, wraplength= 510, justify= "center")
        label.pack(fill= "both", padx= 20, pady= 25)
        button_lose_close = tk.Button(window, text="Salir del Ahorcado", command= lambda: self.master.destroy())
        button_lose_close.pack(fill= "both", side= "bottom")
        button_close_reset = tk.Button(window, text="Volver a jugar", command= lambda: [self.reiniciar_juego(), window.destroy()])
        button_close_reset.pack(fill= "both", side= "bottom")

    # POP UP DE DUPLICADOS
    def Duplicada_PopUp(self):
        window = tk.Toplevel(self.master)
        window.geometry("550x150")
        window.resizable(0,0)
        window.title("ERROR")
        Info_Lose= "Introdujiste una palabra o letra fallida ya dicha antes, ten más cuidado la próxima vez."
        label = ttk.Label(window, text= Info_Lose, wraplength= 510, justify= "center")
        label.pack(fill= "both", padx= 20, pady= 25)
        button_close_reset = tk.Button(window, text="Volver al juego", command= lambda: window.destroy())
        button_close_reset.pack(fill= "both", side= "bottom")

    def Play(self):
        self.update()

class Menu(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)
        self.Crear_Menu()
        parent.config(menu=self)

    def Crear_Menu(self):
        Ajustes = tk.Menu(self, tearoff = False)
        Ajustes.add_command(label= "Información", command= self.Info_PopUp)
        Ajustes.add_separator()
        Ajustes.add_command(label= "Reiniciar el Ahorcado", command= lambda: self.master.widgets.reiniciar_juego())
        Ajustes.add_separator()
        Ajustes.add_command(label= "Salir del Ahorcado", command= lambda: self.master.destroy())
        self.add_cascade(label= "Ajustes", menu= Ajustes)

    def Info_PopUp(self):
        window = tk.Toplevel(self.master)
        window.geometry("400x160")
        window.resizable(0,0)
        window.title("Información")
        Info="En este ahorcado puedes adivinar diciendo letras o palabras completas, de esta forma solo debes preocuparte por acertar la palabra antes de ser ahorcado 😉"
        label = ttk.Label(window, text= Info, wraplength= 360, justify= "center")
        label.pack(fill= "both", padx= 20, pady=20)
        button_close = tk.Button(window, text="Volver al juego", command= window.destroy)
        button_close.pack(fill= "both", side= "bottom")

Ahorcado_App()