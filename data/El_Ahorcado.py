import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import sys
import os
import random
from WordsPool import words_en
from WordsPool import words_es
from Fails import phases_hangman

# OBTAIN THE PATH TO THE ICON
def resource_path(relative_path):
    #   Get the absolute path to the resource, works for both development and PyInstaller
    try:
        base_path = sys._MEIPASS  # PyInstaller creates this variable
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# DICTIONARY FOR THE LABELS IN MULTIPLE LANGUAGES
labels = {
    "es": {
        # WIDGETS AREA
        "titulo": "EL AHORCADO",
        "label_guess": "Introduzca una letra o palabra para adivinar:",
        "button_send": "Enviar",
        "button_hint": "Pista",
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
        "popup_hint_text": "No puedes pedir una pista si tan solo te queda una vida.",

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
        "button_send": "Submit",
        "button_hint": "Hint",
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
        "popup_hint_text": "You cannot request a hint if you only have one life left.",

        # MENU AREA
        "settings": "Settings",
        "change_language": "Change language",
        "change_theme": "Change theme",
        "popup_info_text": "In this hangman game, you can guess by saying letters or complete words, so you only need to worry about guessing the word before being hanged 😉. Keep in mind that none of the hidden words have accents even if they should, so don't enter such letters as they will be considered wrong. \n\nPS: Use the 'return to game' button to close this pop-up or you won't be able to see it again."

    }
}

# APP
class Hangman_App(ttk.Window):
    def __init__(self, themename= "cosmo"):

        # SELF SETUP
        super().__init__(themename=themename)
        self.title("The Hangman")
        self.geometry("1280x720")
        self.minsize(960, 540)
        # WINDOW ICON
        self.iconbitmap(resource_path("Ahorcado.ico"))
        self.theme = themename  # Saves the current theme name
        
        # APP PARTS
        self.widgets = Widgets(self)
        self.menu = Menu(self)
        # RUN THE APP
        self.mainloop()

    def change_theme(self, new_theme):
        # Changes the theme of the application and updates the widgets
        self.style.theme_use(new_theme)
        self.theme = new_theme

# CLASS WITH THE MAIN FUCNTIONS OF THE GAME AND WIDGETS
class Widgets(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x= 0, y= 0, relwidth= 1, relheight= 1)

        # VARIABLES OF THE CLASS
        self.language_pool = words_en
        self.selected_language = "en"
        self.word = ""
        self.hidden_word = []
        self.chances = 5
        self.failed_letters = []
        self.guess_word = False
        self.guess = ""
        self.hint_requested = False 
        self.win_pop_up_is_open = False
        self.lose_pop_up_is_open = False
        self.hint_pop_up_is_open = False

        # FUNCTIONS OF THE CLASS
        self.choose_word()
        self.grid_config()
        self.create_widgets()
        self.play()
    
    # LOGIC TO CHOOSE A WORD FROM THE POOL
    def choose_word(self):
        self.word = random.choice(self.language_pool)
        self.hidden_word = ["_"] * len(self.word)
        self.chances = 5
        self.failed_letters = []
        self.guess_word = False

        # TEST OF THE CHOOSEN_WORD FUNCTION
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

    
    # FUNCTION TO CHOOSE THE HANGMAN DRAWING BASED ON THE CHANCES LEFT
    def choose_hangman_drawing(self):
        if self.chances == 5:
            return phases_hangman[0]
        elif self.chances == 4:
            return phases_hangman[1]
        elif self.chances == 3:
            return phases_hangman[2]
        elif self.chances == 2:
            return phases_hangman[3]
        elif self.chances == 1:
            return phases_hangman[4]
        elif self.chances == 0:
            return phases_hangman[5]

    # FUNCTION TO CHOOSE THE BACKGROUND COLOR OF THE "CHANCES LEFT" ZONE BASED ON THE CHANCES LEFT    
    def choose_chances_background_color(self):
        if self.chances == 5:
            return "green"
        elif self.chances >= 3:
            return "gold"
        else:
            return "red"

    def create_widgets(self):    
        # FUNCTION TO OBTAIN THE GUESS FROM THE ENTRY AND UPDATE THE GAME
        def button_send(event= None):
            self.guess = self.entry_guess.get().lower() # Using lower() to avoid case sensitivity
            self.update_game()
            self.entry_guess.delete(0, tk.END)
            print(self.word) # For tests

        def button_hint():
            # This button reveals a letter of the hidden word when clicked in exchange for a life
            self.hint_requested = True 
            self.update_game()
        
        # CREATE WIDGETS
        self.label_tittle = ttk.Label(self, font = "Cambria 25 bold", text= labels[self.selected_language]["titulo"], background= "silver", foreground= "black", anchor= "center")
        self.label_guess = ttk.Label(self, font= "Calibri 14", text= labels[self.selected_language]["label_guess"], background= "cyan",  foreground= "black", anchor= "center")
        self.entry_guess = ttk.Entry(self, font= "Calibri 20", foreground= "orange", justify= "center")
        
        self.button_submit = ttk.Button(self, text= labels[self.selected_language]["button_send"], command= button_send)
        self.entry_guess.bind("<Return>", button_send) # Links the Enter key to the entry field
        
        self.button_hint = ttk.Button(self, text= labels[self.selected_language]["button_hint"], command= button_hint) # Hint button that reveals the hidden word
        
        self.label_failed_guesses = ttk.Label(self, font= "Calibri 14", text= labels[self.selected_language]["label_failed_guesses"], background= "red", foreground= "black", anchor= "center")
        self.label_failed_guesses_list = ttk.Label(self, font= "Calibri 14", text= self.failed_letters, background= "red", foreground= "black", anchor= "center")
        self.label_chances = ttk.Label(self, font= "Calibri 14", text= labels[self.selected_language]["label_chances"], background= self.choose_chances_background_color(), foreground= "black", anchor= "center") # Dinamic background
        self.label_chances_number = ttk.Label(self, font= "Calibri 36", text= self.chances, background= self.choose_chances_background_color(), foreground= "black", anchor= "center") # Dinamic background
        self.label_hangman = ttk.Label(self, font= "Calibri 14", text= self.choose_hangman_drawing(), background= self.choose_chances_background_color(), foreground= "black", anchor= "center") # Dinamic background
        self.label_hidden_word = ttk.Label(self, font= "Calibri 20", text = labels[self.selected_language]["label_hidden_word"], anchor= "center")
        self.label_hidden_word_show = ttk.Label(self, font= "Calibri 36", text = self.hidden_word, anchor= "center")
        label_version = ttk.Label(self, font= "Calibri 7", text= "v1.4", foreground= "grey", anchor= "center")
        
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
    
    # UPDATE THE GAME STATE
    def update_game(self):
        # Logic to handle a hint request
        if self.hint_requested == True:
            if self.chances > 1 and "_" in self.hidden_word:
                index = self.hidden_word.index("_")
                self.hidden_word[index] = self.word[index]
                self.chances -= 1
                self.hint_requested = False
            else:
                if self.hint_pop_up_is_open == False:
                    self.hint_pop_up()
                    self.hint_requested = False
                    
            self.hint_requested = False
        # Logic for the guess
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
            self.duplicates_pop_up()

        self.label_hidden_word_show.config(text=self.hidden_word)
        self.label_failed_guesses_list.config(text=self.failed_letters)
        self.label_chances.config(background= self.choose_chances_background_color())
        self.label_chances_number.config(text=self.chances, background= self.choose_chances_background_color())
        self.label_hangman.config(text= self.choose_hangman_drawing(), background= self.choose_chances_background_color())

        if "_" not in self.hidden_word or self.guess_word == True and self.win_pop_up_is_open == False:
            self.win_pop_up()
        elif self.chances == 0 and self.lose_pop_up_is_open == False:
            self.lose_pop_up()
    
    # UPDATE THE LANGUAGE OF THE WIDGETS
    def update_language(self):
        self.label_tittle.config(text= labels[self.selected_language]["titulo"])
        self.label_guess.config(text= labels[self.selected_language]["label_guess"])
        self.button_submit.config(text= labels[self.selected_language]["button_send"])
        self.button_hint.config(text= labels[self.selected_language]["button_hint"])
        self.label_failed_guesses.config(text= labels[self.selected_language]["label_failed_guesses"])
        self.label_chances.config(text= labels[self.selected_language]["label_chances"])
        self.label_hidden_word.config(text= labels[self.selected_language]["label_hidden_word"])
        self.master.menu.update_menu_language() # Updates the menu language
        

    # FUNCTION TO RESTART THE GAME
    def restart_game(self):  
        self.choose_word() # Chooses a new word
        self.update_language() # Updates the language of the widgets
        
        # Updates the widgets
        self.label_hidden_word_show.config(text=self.hidden_word)
        self.label_failed_guesses_list.config(text=self.failed_letters)
        self.label_chances.config(background= self.choose_chances_background_color())
        self.label_chances_number.config(text=self.chances, background= self.choose_chances_background_color())
        self.label_hangman.config(text= self.choose_hangman_drawing(), background= self.choose_chances_background_color())
        
        # Resets the variables to prevent infinite pop-up repetition
        self.win_pop_up_is_open = False
        self.lose_pop_up_is_open = False
        self.info_pop_up_is_open = False
        self.hint_pop_up_is_open = False
        
    # WIN POP UP
    def win_pop_up(self):
        # SET-UP POP-UP WIN
        window = tk.Toplevel(self.master)
        window.geometry("610x200")
        window.resizable(0,0)
        window.iconbitmap(resource_path("Ahorcado.ico"))
        window.title(labels[self.selected_language]["popup_win_tittle"])
        self.win_pop_up_is_open = True

        # WIN POP UP CONTENT
        label = ttk.Label(window, text= labels[self.selected_language]["popup_win_text"].format(self.word), wraplength= 550, justify= "center")
        label.pack(fill= "both", padx= 53, pady= 45)
        button_win_close = tk.Button(window, text= labels[self.selected_language]["button_exit"], command= lambda: self.master.destroy())
        button_win_close.pack(fill= "both", side= "bottom")
        button_win_reset = tk.Button(window, text= labels[self.selected_language]["button_replay"], command= lambda: [self.restart_game(), window.destroy()])
        button_win_reset.pack(fill= "both", side= "bottom")

    # LOSE POP UP
    def lose_pop_up(self):
        # SET-UP POP-UP LOSE
        window = tk.Toplevel(self.master)
        window.geometry("580x175")
        window.resizable(0,0)
        window.iconbitmap(resource_path("Ahorcado.ico"))
        window.title(labels[self.selected_language]["popup_lose_tittle"])
        self.lose_pop_up_is_open = True

        # LOSE POP UP CONTENT
        label = ttk.Label(window, text= labels[self.selected_language]["popup_lose_text"].format(self.word), wraplength= 500, justify= "center")
        label.pack(fill= "both", padx= 50, pady= 30)
        button_lose_close = tk.Button(window, text= labels[self.selected_language]["button_exit"], command= lambda: self.master.destroy())
        button_lose_close.pack(fill= "both", side= "bottom")
        button_close_reset = tk.Button(window, text= labels[self.selected_language]["button_replay"], command= lambda: [self.restart_game(), window.destroy()])
        button_close_reset.pack(fill= "both", side= "bottom")

    # DUPLICATES POP UP
    def duplicates_pop_up(self):
        # SET-UP POP-UP DUPLICATES
        window = tk.Toplevel(self.master)
        window.geometry("700x160")
        window.resizable(0,0)
        window.iconbitmap(resource_path("Ahorcado.ico"))
        window.title("🚫 ERROR 🚫")
        
        # DUPLICATES POP UP CONTENT
        label = ttk.Label(window, text= labels[self.selected_language]["popup_duplicates_text"], wraplength= 640, justify= "center")
        label.pack(fill= "both", padx= 30, pady= 50)
        button_close_reset = tk.Button(window, text= labels[self.selected_language]["button_return"] , command= lambda: window.destroy())
        button_close_reset.pack(fill= "both", side= "bottom")

    # POP UP DE PISTA INNECESARIA O NO DISPONIBLE
    def hint_pop_up(self):
        # SET-UP POP-UP HINTS
        window = tk.Toplevel(self.master)
        window.geometry("500x150")
        window.resizable(0,0)
        window.iconbitmap(resource_path("Ahorcado.ico"))
        window.title(" 🚫 ERROR 🚫")
        self.hint_pop_up_is_open = True
        
        # HINT POP UP CONTENT
        label = ttk.Label(window, text= labels[self.selected_language]["popup_hint_text"], wraplength= 450, justify= "center")
        label.pack(fill= "both", padx= 50, pady= 40)
        
        # BUTTON TO CLOSE THE POP-UP & RESET THE VARIABLE
        def close_hint_pop_up():
            window.destroy()
            self.hint_pop_up_is_open = False
        
        button_close_reset = tk.Button(window, text= labels[self.selected_language]["button_return"], command= close_hint_pop_up)
        button_close_reset.pack(fill= "both", side= "bottom")

    def play(self):
        self.update()

# MENU CLASS
class Menu(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_menu()
        self.info_pop_up_is_open = False
        parent.config(menu=self)
        self.master.widgets.language_pool = words_en  # Sets the default language pool

    # FUNCTIONS FOR THE CHANGE LANGUAGE LOGIC
    def set_language_esp(self):
        self.master.widgets.language_pool = words_es
        self.master.widgets.selected_language = "es"  # Updates the selected language
        self.master.widgets.restart_game()  # Restarts the game with the new language

    def set_language_eng(self):
        self.master.widgets.language_pool = words_en
        self.master.widgets.selected_language = "en"  # Updates the selected language
        self.master.widgets.restart_game() # Restarts the game with the new language

    def update_menu_language(self):
        self.delete(0, "end")  # Deletes all current menu items
        self.create_menu()      # Creates the menu again with the updated language
    
    # FUNCTIONS FOR THE CHANGE THEME LOGIC
    # LIGHT THEMES
    def set_theme_cosmo(self):
        self.master.change_theme("cosmo")

    def set_theme_united(self):
        self.master.change_theme("united")

    def set_theme_morph(self):
        self.master.change_theme("morph")

    def set_theme_simplex(self):
        self.master.change_theme("simplex")

    def set_theme_cerculean(self):
        self.master.change_theme("cerculean")

    # DARK THEMES
    def set_theme_cyborg(self):
        self.master.change_theme("cyborg")

    def set_theme_darkly(self):
        self.master.change_theme("darkly")

    def set_theme_superhero(self):
        self.master.change_theme("superhero")

    def set_theme_solar(self):
        self.master.change_theme("solar")
    
    def set_theme_vapor(self):
        self.master.change_theme("vapor")

    # CREATING THE MENU 
    def create_menu(self):
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

        settings = tk.Menu(self, tearoff = False)
        settings.add_command(label= "Info", command= lambda: self.info_pop_up() if not self.info_pop_up_is_open else None)
        settings.add_separator()
        settings.add_cascade(label= labels[self.master.widgets.selected_language]["change_language"], menu= submenu_language)  # Linking the language submenu
        settings.add_separator()
        settings.add_cascade(label= labels[self.master.widgets.selected_language]["change_theme"], menu= submenu_theme)  # Linking the theme submenu
        settings.add_separator()
        settings.add_command(label= labels[self.master.widgets.selected_language]["button_replay"], command= lambda: self.master.widgets.restart_game())
        settings.add_separator()
        settings.add_command(label= labels[self.master.widgets.selected_language]["button_exit"], command= lambda: self.master.destroy())
        self.add_cascade(label= labels[self.master.widgets.selected_language]["settings"], menu= settings)

        
    # INFO POP-UP
    def info_pop_up(self):
        # SET-UP POP-UP INFO
        window = tk.Toplevel(self.master)
        window.geometry("500x250")
        window.resizable(0,0)
        window.iconbitmap(resource_path("Ahorcado.ico"))
        window.title("Info")
        self.info_pop_up_is_open = True

        # INFO POP UP CONTENT
        label = ttk.Label(window, text= labels[self.master.widgets.selected_language]["popup_info_text"], wraplength= 460, justify= "center")
        label.pack(fill= "both", padx= 20, pady=20)
        
        # BUTTON TO CLOSE THE POP-UP & RESET THE VARIABLE
        def close_info_pop_up():
            window.destroy()
            self.info_pop_up_is_open = False

        button_close = tk.Button(window, text="Volver al juego", command=close_info_pop_up)
        button_close.pack(fill= "both", side= "bottom")
    
# CALLING THE APP FUNCTION
Hangman_App()