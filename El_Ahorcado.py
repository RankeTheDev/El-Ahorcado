import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import random
from Palabras import words_list
from Fases_Ahorcado import fases_ahorcado

# APP
class Ahorcado_App(ttk.Window):
    def __init__(self, themename="cyborg"):

        # SET-UP DE SELF
        super().__init__(themename=themename)
        self.title("El Ahorcado")
        self.geometry("1280x720")
        self.iconbitmap("Ahorcado.ico")
        self.minsize(960, 540)

        # PARTES DE LA APP
        self.widgets = Widgets(self)
        self.menu = Menu(self)
        # RUN
        self.mainloop()

# CLASE CON LOS WIDGETS Y FUNCIONES PRINCIPALES
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
        self.choose_word()
        self.grid_config()
        self.create_widgets()
        self.play()
    
    # LOGICA PARA ESCOGER LA PALABRA AL AZAR
    def choose_word(self):
        # ESCOGE LA PALABRA
        self.word = random.choice(words_list)
        self.hidden_word = ["_"] * len(self.word)
        self.chances = 5
        self.failed_letters = []
        self.guess_word = False

        # TEST DE LA FUNCIÓN PARA LA PALABRA OCULTA
        #print(self.hidden_word, self.word)

    def grid_config(self):
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
    def elegir_dibujo_ahorcado(self):
        if self.chances == 5:
            return fases_ahorcado[0]
        elif self.chances == 4:
            return fases_ahorcado[1]
        elif self.chances == 3:
            return fases_ahorcado[2]
        elif self.chances == 2:
            return fases_ahorcado[3]
        elif self.chances == 1:
            return fases_ahorcado[4]
        elif self.chances == 0:
            return fases_ahorcado[5]
        
    def elegir_color_background(self):
        if self.chances == 5:
            return "green"
        elif self.chances >= 3:
            return "gold"
        else:
            return "red"

    def create_widgets(self):    
        # FUNCION PARA OBTENER LA GUESS
        def boton_enviar(event= None):
            # CON EL LOWER LA GUESS SIEMPRE PASARÁ EN MINÚSCULAS, EVITANDO ERRORES AL COMPARAR LAS LETRAS 
            self.guess = self.entry_guess.get().lower() 
            self.update_game()
            self.entry_guess.delete(0, tk.END)
        
        # CREAR WIDGETS
        label_tittle = ttk.Label(self, font = "Cambria 25 bold", text= "EL AHORCADO", background= "silver", foreground= "black", anchor= "center")
        label_guess = ttk.Label(self, font= "Calibri 14", text= "Introduzca una letra o palabra para adivinar:", background= "cyan",  foreground= "black", anchor= "center")
        self.entry_guess = ttk.Entry(self, font= "Calibri 20", foreground= "purple", justify= "center")
        
        button_submit = ttk.Button(self, text= "Enviar", command= boton_enviar)
        # Vincular la tecla Enter al campo de entrada
        self.entry_guess.bind("<Return>", boton_enviar)
        
        label_failed_guesses = ttk.Label(self, font= "Calibri 14", text= "Estas letras y palabras son incorrectas:", background= "brown", foreground= "black", anchor= "center")
        self.label_failed_guesses_list = ttk.Label(self, font= "Calibri 14", text= self.failed_letters, background= "brown", foreground= "black", anchor= "center")
        self.label_chances = ttk.Label(self, font= "Calibri 14", text= "Intentos restantes", background= self.elegir_color_background(), foreground= "black", anchor= "center") #Fondo dinámico
        self.label_chances_number = ttk.Label(self, font= "Calibri 36", text= self.chances, background= self.elegir_color_background(), foreground= "black", anchor= "center") #Fondo dinámico
        self.label_hangman = ttk.Label(self, font= "Calibri 14", text= self.elegir_dibujo_ahorcado(), background= self.elegir_color_background(), foreground= "black", anchor= "center") #Fondo dinámico
        label_hidden_word = ttk.Label(self, font= "Calibri 20", text = "Esta es la palabra oculta", anchor= "center")
        self.label_hidden_word_show = ttk.Label(self, font= "Calibri 36", text = self.hidden_word, anchor= "center")
        
        # PLACE WIDGETS
        label_tittle.grid(row= 1, column= 1, columnspan= 8, sticky= "nsew", padx= 5, pady= 5)
        label_guess.grid(row= 2, column= 2, sticky= "nsew", padx= 5, pady= 40)
        self.entry_guess.grid(row= 2 , column= 4, columnspan= 3, sticky= "nsew", padx= 10, pady= 40)
        button_submit.grid(row= 2, column= 7, sticky= "nsew", padx= 10, pady= 50)
        label_failed_guesses.grid(row= 3, column= 2, sticky= "nsew", padx= 5, pady= 25)
        self.label_failed_guesses_list.grid(row= 3, column= 4, columnspan= 4, sticky= "nsew", padx= 50, pady= 25)
        self.label_chances.grid(row= 4 , column= 2, columnspan= 1, sticky= "nsew", padx= 33, pady= 5)
        self.label_chances_number.grid(row= 5 , column= 2, columnspan= 1, sticky= "nsew", padx= 33, pady= 5)
        self.label_hangman.grid(row= 4, column= 3, rowspan= 2, columnspan= 2, sticky= "nsew", padx= 20, pady= 10)
        label_hidden_word.grid(row= 4, column= 6, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)
        self.label_hidden_word_show.grid(row= 5, column= 6, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)
    
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
            self.duplicados_pop_up()

        self.label_hidden_word_show.config(text=self.hidden_word)
        self.label_failed_guesses_list.config(text=self.failed_letters)
        self.label_chances.config(background= self.elegir_color_background())
        self.label_chances_number.config(text=self.chances, background= self.elegir_color_background())
        self.label_hangman.config(text= self.elegir_dibujo_ahorcado(), background= self.elegir_color_background())

        if "_" not in self.hidden_word or self.guess_word == True:
            self.win_pop_up()
        elif self.chances == 0:
            self.lose_pop_up()
    
    # FUNCION PARA REINICIAR EL JUEGO
    def reiniciar_juego(self):
        # Vuelve a elegir la palabra
        self.choose_word() 
        # Actualiza los widgets
        self.label_hidden_word_show.config(text=self.hidden_word)
        self.label_failed_guesses_list.config(text=self.failed_letters)
        self.label_chances.config(background= self.elegir_color_background())
        self.label_chances_number.config(text=self.chances, background= self.elegir_color_background())
        self.label_hangman.config(text= self.elegir_dibujo_ahorcado(), background= self.elegir_color_background())

    # POP UP DE VICTORIA
    def win_pop_up(self):
        # SET-UP POP-UP WIN
        window = tk.Toplevel(self.master)
        window.geometry("590x250")
        window.resizable(0,0)
        window.iconbitmap("Ahorcado.ico")
        window.title("🎉 🏆 ¡GANASTE! 🏆 🎉")

        # CONTENIDO WIN
        info_win_txt= f"Felicidades, acertaste la palabra '{self.word}' y ganaste el juego. \nAhora puedes salir del juego o intentar ganar de nuevo, ¿qué deseas hacer?"
        label = ttk.Label(window, text= info_win_txt, wraplength= 550, justify= "center")
        label.pack(fill= "both", padx= 25, pady= 25)
        button_win_close = tk.Button(window, text="Salir del Ahorcado", command= lambda: self.master.destroy())
        button_win_close.pack(fill= "both", side= "bottom")
        button_win_reset = tk.Button(window, text="Volver a jugar", command= lambda: [self.reiniciar_juego(), window.destroy()])
        button_win_reset.pack(fill= "both", side= "bottom")

    # POP UP DE DERROTA
    def lose_pop_up(self):
        # SET-UP POP-UP LOSE
        window = tk.Toplevel(self.master)
        window.geometry("590x250")
        window.resizable(0,0)
        window.iconbitmap("Ahorcado.ico")
        window.title("💀 😩 ¡PERDISTE! 😩 💀 ")

        # CONTENIDO LOSE
        info_lose_txt= f"Una pena, no lograste acertar la palabra '{self.word}' y fuiste ahorcado. \nAhora puedes salir del juego o intentarlo de nuevo, ¿qué deseas hacer?"
        label = ttk.Label(window, text= info_lose_txt, wraplength= 550, justify= "center")
        label.pack(fill= "both", padx= 25, pady= 25)
        button_lose_close = tk.Button(window, text="Salir del Ahorcado", command= lambda: self.master.destroy())
        button_lose_close.pack(fill= "both", side= "bottom")
        button_close_reset = tk.Button(window, text="Volver a jugar", command= lambda: [self.reiniciar_juego(), window.destroy()])
        button_close_reset.pack(fill= "both", side= "bottom")

    # POP UP DE DUPLICADOS
    def duplicados_pop_up(self):
        # SET-UP POP-UP DUPLICADOS
        window = tk.Toplevel(self.master)
        window.geometry("750x150")
        window.resizable(0,0)
        window.iconbitmap("Ahorcado.ico")
        window.title("ERROR")
        
        # CONTENIDO DUPLICADOS
        info_duplicados_txt= "Introdujiste una palabra o letra fallida ya dicha antes, ten más cuidado la próxima vez."
        label = ttk.Label(window, text= info_duplicados_txt, wraplength= 750, justify= "center")
        label.pack(fill= "both", padx= 25, pady= 25)
        button_close_reset = tk.Button(window, text="Volver al juego", command= lambda: window.destroy())
        button_close_reset.pack(fill= "both", side= "bottom")

    def play(self):
        self.update()

# CLASE DEL MENÚ
class Menu(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)
        self.crear_menu()
        parent.config(menu=self)

    # CREO EL MENÚ 
    def crear_menu(self):
        ajustes = tk.Menu(self, tearoff = False)
        ajustes.add_command(label= "Información", command= self.info_pop_up)
        ajustes.add_separator()
        ajustes.add_command(label= "Reiniciar el Ahorcado", command= lambda: self.master.widgets.reiniciar_juego())
        ajustes.add_separator()
        ajustes.add_command(label= "Salir del Ahorcado", command= lambda: self.master.destroy())
        self.add_cascade(label= "Ajustes", menu= ajustes)

    # POP UP DE INFORMACIÓN
    def info_pop_up(self):
        # SET-UP POP-UP INFO
        window = tk.Toplevel(self.master)
        window.geometry("400x200")
        window.resizable(0,0)
        window.iconbitmap("Ahorcado.ico")
        window.title("Información")

        # CONTENIDO INFO
        info_txt ="En este ahorcado puedes adivinar diciendo letras o palabras completas, de esta forma solo debes preocuparte por acertar la palabra antes de ser ahorcado 😉"
        label = ttk.Label(window, text= info_txt, wraplength= 360, justify= "center")
        label.pack(fill= "both", padx= 20, pady=20)
        button_close = tk.Button(window, text="Volver al juego", command= window.destroy)
        button_close.pack(fill= "both", side= "bottom")

# LLAMO A LA APP
Ahorcado_App()