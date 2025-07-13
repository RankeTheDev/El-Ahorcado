import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import sys
import os
import random
from WordsPool import words_en
from WordsPool import words_es
from Fails import fases_ahorcado

# FUNCION PARA OBTENER LA RUTA ABSOLUTA AL PUTO ICONO
def resource_path(relative_path):
    #Obtiene la ruta absoluta al recurso, funciona para dev y para PyInstaller
    try:
        base_path = sys._MEIPASS  # PyInstaller crea esta variable
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

labels = {
    "es": {
        # WIDGETS AREA
        "titulo": "EL AHORCADO",
        "label_guess": "Introduzca una letra o palabra para adivinar:",
        "boton_enviar": "Enviar",
        "boton_pista": "Pista",
        "label_failed_guesses": "Estas letras y palabras son incorrectas:",
        "label_chances": "Intentos restantes",
        "label_hidden_word": "Esta es la palabra oculta",
        # POP UP COMMON ASSETS
        "button_exit": "Salir del juego",
        "button_replay": "Volver a jugar",
        "button_return": "Volver al juego",
        # POP-UP WIN 
        "popup_win_tittle": "🎉 🏆 ¡GANASTE! 🏆 🎉",
        "popup_win_text": "Felicidades, acertaste la palabra '{}' y ganaste el juego. \nAhora puedes salir del juego o intentar ganar de nuevo, ¿qué deseas hacer?",
        # POP-UP LOSE
        "popup_lose_tittle": "💀 😩 ¡PERDISTE! 💀 😩",
        "popup_lose_text": "Una pena, no lograste acertar la palabra '{}' y fuiste ahorcado. \nAhora puedes salir del juego o intentarlo de nuevo, ¿qué deseas hacer?",
        # POP-UP DUPLICATES
        "popup_duplicates_text": "Introdujiste una palabra o letra fallida ya dicha antes, ten más cuidado la próxima vez.",
        # POP-UP HINT
        "popup_hint_text": "No puedes pedir una pista si solo te queda una vida o si la palabra ya está completa.",

        # MENU AREA
        "settings": "Ajustes",
        "change_language": "Cambiar idioma",
        "change_theme": "Cambiar tema",
        "popup_info_text": "En este ahorcado puedes adivinar diciendo letras o palabras completas, de esta forma solo debes preocuparte por acertar la palabra antes de ser ahorcado 😉. Ten en cuenta que ninguna de las palabras ocultas lleva tilde aún si realmente deberían, asi que no introduzcas tales letras pues serán consideradas erróneas. \n\nPD: Usa el botón 'volver al juego' para cerrar este pop-up o no podrás verlo de nuevo."

    },
    "en": {
        # WIDGETS AREA
        "titulo": "THE HANGMAN",
        "label_guess": "Enter a letter or word to guess:",
        "boton_enviar": "Submit",
        "boton_pista": "Hint",
        "label_failed_guesses": "These letters and words are incorrect:",
        "label_chances": "Remaining attempts",
        "label_hidden_word": "This is the hidden word",
        # POP UP COMMON ASSETS
        "button_exit": "Exit the game",
        "button_replay": "Play again",
        "button_return": "Return to the game",
        # POP-UP WIN
        "popup_win_tittle": "🎉 🏆 YOU WON! 🏆 🎉",
        "popup_win_text": "Congratulations, you guessed the word '{}' and won the game. \nNow you can exit the game or try to win again, what would you like to do?",
        # POP-UP LOSE
        "popup_lose_tittle": "💀 😩 YOU LOST! 💀 😩",
        "popup_lose_text": "Unfortunately, you didn't guess the word '{}' and were hanged. \nNow you can exit the game or try again, what would you like to do?",
        # POP-UP DUPLICATES
        "popup_duplicates_text": "You entered a word or failed letter that has already been mentioned, be more careful next time.",
        # POP-UP HINT
        "popup_hint_text": "You cannot request a hint if you only have one life left or if the word is already complete.",

        # MENU AREA
        "settings": "Settings",
        "change_language": "Change language",
        "change_theme": "Change theme",
        "popup_info_text": "In this hangman game, you can guess by saying letters or complete words, so you only need to worry about guessing the word before being hanged 😉. Keep in mind that none of the hidden words have accents even if they should, so don't enter such letters as they will be considered wrong. \n\nPS: Use the 'return to game' button to close this pop-up or you won't be able to see it again."

    }
}

# APP
class Ahorcado_App(ttk.Window):
    def __init__(self, themename= "cosmo"):

        # SET-UP DE SELF
        super().__init__(themename=themename)
        self.title("The Hangman")
        self.geometry("1280x720")
        self.minsize(960, 540)
        # ICONO DE LA VENTANA
        self.iconbitmap(resource_path("Ahorcado.ico"))
        self.theme = themename  # Tema actual de la ventana
        
        # PARTES DE LA APP
        self.widgets = Widgets(self)
        self.menu = Menu(self)
        # RUN
        self.mainloop()

    def cambiar_tema(self, nuevo_tema):
        """Cambia el tema de la app y actualiza widgets si es necesario"""
        self.style.theme_use(nuevo_tema)
        self.theme = nuevo_tema
        # Si necesitas refrescar widgets, llama a métodos de actualización aquí

# CLASE CON LOS WIDGETS Y FUNCIONES PRINCIPALES
class Widgets(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x= 0, y= 0, relwidth= 1, relheight= 1)

        # VARIABLES DE LA CLASE
        self.language_pool = words_en
        self.selected_language = "en"
        self.word = ""
        self.hidden_word = []
        self.chances = 5
        self.failed_letters = []
        self.guess_word = False
        self.guess = ""
        self.hint_requested = False  # Variable para controlar si se ha solicitado una pista
        self.win_pop_up_is_open = False
        self.lose_pop_up_is_open = False

        # FUNCIONES DE LA CLASE
        self.choose_word()
        self.grid_config()
        self.create_widgets()
        self.play()
    
    # LOGICA PARA ESCOGER LA PALABRA AL AZAR
    def choose_word(self):
        # ESCOGE LA PALABRA
        self.word = random.choice(self.language_pool)
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

    # FUNCIÓN PARA LA SELECCIÓN DEL COLOR DE LA ZONA DE INTENTOS    
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
            print(self.word)

        def boton_pista():
            # Este botón revela una letra de la palabra oculta al hacer clic a cambio de una vida
            if self.chances > 0 and "_" in self.hidden_word:
               # Encuentra un guion bajo y lo reemplaza con la letra correspondiente de la palabra
                self.hint_requested = True 
                self.update_game()
        
        # CREAR WIDGETS
        self.label_tittle = ttk.Label(self, font = "Cambria 25 bold", text= labels[self.selected_language]["titulo"], background= "silver", foreground= "black", anchor= "center")
        self.label_guess = ttk.Label(self, font= "Calibri 14", text= labels[self.selected_language]["label_guess"], background= "cyan",  foreground= "black", anchor= "center")
        self.entry_guess = ttk.Entry(self, font= "Calibri 20", foreground= "orange", justify= "center")
        
        self.button_submit = ttk.Button(self, text= labels[self.selected_language]["boton_enviar"], command= boton_enviar)
        # Vincular la tecla Enter al campo de entrada
        self.entry_guess.bind("<Return>", boton_enviar)
        
        self.button_hint = ttk.Button(self, text= labels[self.selected_language]["boton_pista"], command= boton_pista) # Botón de pista que revela la palabra oculta
        
        self.label_failed_guesses = ttk.Label(self, font= "Calibri 14", text= labels[self.selected_language]["label_failed_guesses"], background= "red", foreground= "black", anchor= "center")
        self.label_failed_guesses_list = ttk.Label(self, font= "Calibri 14", text= self.failed_letters, background= "red", foreground= "black", anchor= "center")
        self.label_chances = ttk.Label(self, font= "Calibri 14", text= labels[self.selected_language]["label_chances"], background= self.elegir_color_background(), foreground= "black", anchor= "center") #Fondo dinámico
        self.label_chances_number = ttk.Label(self, font= "Calibri 36", text= self.chances, background= self.elegir_color_background(), foreground= "black", anchor= "center") #Fondo dinámico
        self.label_hangman = ttk.Label(self, font= "Calibri 14", text= self.elegir_dibujo_ahorcado(), background= self.elegir_color_background(), foreground= "black", anchor= "center") #Fondo dinámico
        self.label_hidden_word = ttk.Label(self, font= "Calibri 20", text = labels[self.selected_language]["label_hidden_word"], anchor= "center")
        self.label_hidden_word_show = ttk.Label(self, font= "Calibri 36", text = self.hidden_word, anchor= "center")
        label_version = ttk.Label(self, font= "Calibri 7", text= "v 1.3", foreground= "grey", anchor= "center")
        
        # PLACE WIDGETS
        self.label_tittle.grid(row= 1, column= 1, columnspan= 8, sticky= "nsew", padx= 5, pady= 5)
        self.label_guess.grid(row= 2, column= 2, sticky= "nsew", padx= 5, pady= 40)
        self.entry_guess.grid(row= 2 , column= 4, columnspan= 3, sticky= "nsew", padx= 10, pady= 40)
        self.button_submit.grid(row= 2, column= 7, sticky= "nsew", padx= 10, pady= 50)
        self.button_hint.grid(row= 2, column= 8, sticky= "nsew", padx= 10, pady= 50)
        self.label_failed_guesses.grid(row= 3, column= 2, sticky= "nsew", padx= 5, pady= 25)
        self.label_failed_guesses_list.grid(row= 3, column= 4, columnspan= 4, sticky= "nsew", padx= 50, pady= 25)
        self.label_chances.grid(row= 4 , column= 2, columnspan= 1, sticky= "nsew", padx= 33, pady= 5)
        self.label_chances_number.grid(row= 5 , column= 2, columnspan= 1, sticky= "nsew", padx= 33, pady= 5)
        self.label_hangman.grid(row= 4, column= 3, rowspan= 2, columnspan= 2, sticky= "nsew", padx= 20, pady= 10)
        self.label_hidden_word.grid(row= 4, column= 6, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)
        self.label_hidden_word_show.grid(row= 5, column= 6, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)
        label_version.grid(row= 6, column= 9, sticky= "sw", padx= 5, pady= 5)
    
    # ACTUALIZAR EL ESTADO DEl JUEGO
    def update_game(self):
        # Si se pidió pista, procesar primero
        if self.hint_requested:
            if self.chances > 1 and "_" in self.hidden_word:
                index = self.hidden_word.index("_")
                self.hidden_word[index] = self.word[index]
                self.chances -= 1
            else:
                self.hint_pop_up()
            self.hint_requested = False
        # Lógica normal de adivinanza
        elif self.guess == self.word:
            self.guess_word = True
        elif self.guess in self.word:
            for i, letra in enumerate(self.word):
                if letra == self.guess:
                    self.hidden_word[i] = self.guess
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

        if "_" not in self.hidden_word or self.guess_word == True and self.win_pop_up_is_open == False:
            self.win_pop_up()
        elif self.chances == 0 and self.lose_pop_up_is_open == False:
            self.lose_pop_up()
    
    # ACTUALIZA LOS TEXTOS DE LOS WIDGETS SEGÚN EL IDIOMA SELECCIONADO
    def update_language(self):
        # Actualiza los textos de los widgets según el idioma seleccionado
        self.label_tittle.config(text= labels[self.selected_language]["titulo"])
        self.label_guess.config(text= labels[self.selected_language]["label_guess"])
        self.button_submit.config(text= labels[self.selected_language]["boton_enviar"])
        self.button_hint.config(text= labels[self.selected_language]["boton_pista"])
        self.label_failed_guesses.config(text= labels[self.selected_language]["label_failed_guesses"])
        self.label_chances.config(text= labels[self.selected_language]["label_chances"])
        self.label_hidden_word.config(text= labels[self.selected_language]["label_hidden_word"])
        # Actualiza el texto de los ajustes del menú
        self.master.menu.update_menu_language()
        

    # FUNCION PARA REINICIAR EL JUEGO
    def reiniciar_juego(self):
        # Vuelve a elegir la palabra
        self.choose_word() 
        # Actualiza los textos de los widgets
        self.update_language()
        # Actualiza los widgets
        self.label_hidden_word_show.config(text=self.hidden_word)
        self.label_failed_guesses_list.config(text=self.failed_letters)
        self.label_chances.config(background= self.elegir_color_background())
        self.label_chances_number.config(text=self.chances, background= self.elegir_color_background())
        self.label_hangman.config(text= self.elegir_dibujo_ahorcado(), background= self.elegir_color_background())
        # Resetea la variable para prevenir bugs de repeticion infinita en los pop ups
        self.win_pop_up_is_open = False
        self.lose_pop_up_is_open = False
        self.info_pop_up_is_open = False
        
    # POP UP DE VICTORIA
    def win_pop_up(self):
        # SET-UP POP-UP WIN
        window = tk.Toplevel(self.master)
        window.geometry("590x250")
        window.resizable(0,0)
        window.iconbitmap(resource_path("Ahorcado.ico"))
        window.title(labels[self.selected_language]["popup_win_tittle"])
        self.win_pop_up_is_open = True

        # CONTENIDO WIN
        label = ttk.Label(window, text= labels[self.selected_language]["popup_win_text"].format(self.word), wraplength= 550, justify= "center")
        label.pack(fill= "both", padx= 25, pady= 25)
        button_win_close = tk.Button(window, text= labels[self.selected_language]["button_exit"], command= lambda: self.master.destroy())
        button_win_close.pack(fill= "both", side= "bottom")
        button_win_reset = tk.Button(window, text= labels[self.selected_language]["button_replay"], command= lambda: [self.reiniciar_juego(), window.destroy()])
        button_win_reset.pack(fill= "both", side= "bottom")

    # POP UP DE DERROTA
    def lose_pop_up(self):
        # SET-UP POP-UP LOSE
        window = tk.Toplevel(self.master)
        window.geometry("590x250")
        window.resizable(0,0)
        window.iconbitmap(resource_path("Ahorcado.ico"))
        window.title(labels[self.selected_language]["popup_lose_tittle"])
        self.lose_pop_up_is_open = True

        # CONTENIDO LOSE
        label = ttk.Label(window, text= labels[self.selected_language]["popup_lose_text"].format(self.word), wraplength= 550, justify= "center")
        label.pack(fill= "both", padx= 25, pady= 25)
        button_lose_close = tk.Button(window, text= labels[self.selected_language]["button_exit"], command= lambda: self.master.destroy())
        button_lose_close.pack(fill= "both", side= "bottom")
        button_close_reset = tk.Button(window, text= labels[self.selected_language]["button_replay"], command= lambda: [self.reiniciar_juego(), window.destroy()])
        button_close_reset.pack(fill= "both", side= "bottom")

    # POP UP DE DUPLICADOS
    def duplicados_pop_up(self):
        # SET-UP POP-UP DUPLICADOS
        window = tk.Toplevel(self.master)
        window.geometry("750x150")
        window.resizable(0,0)
        window.iconbitmap(resource_path("Ahorcado.ico"))
        window.title("🚫 ERROR 🚫")
        
        # CONTENIDO DUPLICADOS
        info_duplicados_txt= "Introdujiste una palabra o letra fallida ya dicha antes, ten más cuidado la próxima vez."
        label = ttk.Label(window, text= labels[self.selected_language]["popup_duplicates_text"], wraplength= 750, justify= "center")
        label.pack(fill= "both", padx= 25, pady= 25)
        button_close_reset = tk.Button(window, text= labels[self.selected_language]["button_return"] , command= lambda: window.destroy())
        button_close_reset.pack(fill= "both", side= "bottom")

    # POP UP DE PISTA INNECESARIA O NO DISPONIBLE
    def hint_pop_up(self):
        # SET-UP POP-UP PISTA
        window = tk.Toplevel(self.master)
        window.geometry("750x150")
        window.resizable(0,0)
        window.iconbitmap(resource_path("Ahorcado.ico"))
        window.title(" 🚫 ERROR 🚫")

        # CONTENIDO PISTA
        label = ttk.Label(window, text= labels[self.selected_language]["popup_hint_text"], wraplength= 750, justify= "center")
        label.pack(fill= "both", padx= 25, pady= 25)
        button_close_reset = tk.Button(window, text= labels[self.selected_language]["button_return"], command= lambda: window.destroy())
        button_close_reset.pack(fill= "both", side= "bottom")

    def play(self):
        self.update()

# CLASE DEL MENÚ
class Menu(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)
        self.crear_menu()
        self.info_pop_up_is_open = False
        parent.config(menu=self)
        self.master.widgets.language_pool = words_en  # Establece el idioma por defecto al español

    # FUNCIONES PARA CAMBIAR EL IDIOMA
    def set_language_esp(self):
        self.master.widgets.language_pool = words_es
        self.master.widgets.selected_language = "es"  # Actualiza el idioma seleccionado
        self.master.widgets.reiniciar_juego()  # Reinicia el juego con el nuevo idioma

    def set_language_eng(self):
        self.master.widgets.language_pool = words_en
        self.master.widgets.selected_language = "en"  # Actualiza el idioma seleccionado
        self.master.widgets.reiniciar_juego() # Reinicia el juego con el nuevo idioma

    def update_menu_language(self):
        self.delete(0, "end")  # Borra el menú anterior
        self.crear_menu()      # Crea el menú con los textos actualizados
    
    # FUNCIONES PARA CAMBIAR EL TEMA
    # LIGHT THEMES
    def set_theme_cosmo(self):
        self.master.cambiar_tema("cosmo")

    def set_theme_united(self):
        self.master.cambiar_tema("united")

    def set_theme_morph(self):
        self.master.cambiar_tema("morph")

    def set_theme_simplex(self):
        self.master.cambiar_tema("simplex")

    def set_theme_cerculean(self):
        self.master.cambiar_tema("cerculean")

    # DARK THEMES
    def set_theme_cyborg(self):
        self.master.cambiar_tema("cyborg")

    def set_theme_darkly(self):
        self.master.cambiar_tema("darkly")

    def set_theme_superhero(self):
        self.master.cambiar_tema("superhero")

    def set_theme_solar(self):
        self.master.cambiar_tema("solar")
    
    def set_theme_vapor(self):
        self.master.cambiar_tema("vapor")

    # CREO EL MENÚ 
    def crear_menu(self):
        # SUBMENU LANGUAGES
        submenu_language = tk.Menu(self, tearoff = False)
        submenu_language.add_command(label= "Español", command= self.set_language_esp)
        submenu_language.add_command(label= "English", command= self.set_language_eng)

        # SUBMENU THEMES LIGHT
        submenu_theme_light = tk.Menu(self, tearoff = False)
        submenu_theme_light.add_command(label= "Cosmo", command= self.set_theme_cosmo)
        submenu_theme_light.add_command(label= "United", command= self.set_theme_united)
        submenu_theme_light.add_command(label= "Morph", command= self.set_theme_morph)
        submenu_theme_light.add_command(label= "Simplex", command= self.set_theme_simplex)
        submenu_theme_light.add_command(label= "Cerculean", command= self.set_theme_cerculean)

        # SUBMENU THEMES DARK      
        submenu_theme_dark = tk.Menu(self, tearoff = False)
        submenu_theme_dark.add_command(label= "Cyborg", command= self.set_theme_cyborg)
        submenu_theme_dark.add_command(label= "Darkly", command= self.set_theme_darkly)
        submenu_theme_dark.add_command(label= "Superhero", command= self.set_theme_superhero)
        submenu_theme_dark.add_command(label= "Solar", command= self.set_theme_solar)
        submenu_theme_dark.add_command(label= "Vapor", command= self.set_theme_vapor)

        # SUBMENU THEMES
        submenu_theme = tk.Menu(self, tearoff = False)
        submenu_theme.add_cascade(label= "Dark Themes (🌛)", menu= submenu_theme_dark)
        submenu_theme.add_cascade(label= "Light Themes (🌞)", menu= submenu_theme_light)

        ajustes = tk.Menu(self, tearoff = False)
        ajustes.add_command(label= "Info", command= lambda: self.info_pop_up() if not self.info_pop_up_is_open else None)
        ajustes.add_separator()
        ajustes.add_cascade(label= labels[self.master.widgets.selected_language]["change_language"], menu= submenu_language)  # Aquí se enlaza el submenú
        ajustes.add_separator()
        ajustes.add_cascade(label= labels[self.master.widgets.selected_language]["change_theme"], menu= submenu_theme)  # Aquí se enlaza el submenú
        ajustes.add_separator()
        ajustes.add_command(label= labels[self.master.widgets.selected_language]["button_replay"], command= lambda: self.master.widgets.reiniciar_juego())
        ajustes.add_separator()
        ajustes.add_command(label= labels[self.master.widgets.selected_language]["button_exit"], command= lambda: self.master.destroy())
        self.add_cascade(label= labels[self.master.widgets.selected_language]["settings"], menu= ajustes)

        
    # POP UP DE INFORMACIÓN
    def info_pop_up(self):
        # SET-UP POP-UP INFO
        window = tk.Toplevel(self.master)
        window.geometry("500x230")
        window.resizable(0,0)
        window.iconbitmap(resource_path("Ahorcado.ico"))
        window.title("Info")
        self.info_pop_up_is_open = True

        # CONTENIDO INFO
        label = ttk.Label(window, text= labels[self.master.widgets.selected_language]["popup_info_text"], wraplength= 460, justify= "center")
        label.pack(fill= "both", padx= 20, pady=20)
        
        # BOTÓN PARA CERRAR EL POP-UP Y RESETEAR LA VARIABLE
        def close_info_pop_up():
            window.destroy()
            self.info_pop_up_is_open = False

        button_close = tk.Button(window, text="Volver al juego", command=close_info_pop_up)
        button_close.pack(fill= "both", side= "bottom")

    # CHECK SI YA ESTÁ ABIERTO EL POP UP DE INFO
    

# LLAMO A LA APP
Ahorcado_App()