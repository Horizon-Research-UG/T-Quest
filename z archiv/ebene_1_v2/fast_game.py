import tkinter as tk  # GUI Framework (Zeile 4)
from tkinter import ttk  # moderne Widgets (Zeile 4)

def create_fast_game_window():  # futuristisches Fenster erstellen (Zeile 8)
    root = tk.Tk()  # Fenster erstellen (verwendet in Zeile 6,7)
    root.title("fast game")  # minimalistischer Titel (sichtbar oben)
    root.geometry("800x600")  # elegante Fenstergröße (verwendet in Zeile 8)
    root.configure(bg="#000000")  # tiefschwarzer Hintergrund (futuristisch)
    return root  # Fenster zurückgeben (verwendet in Zeile 14)

def create_center_button(window):  # Button mittig platzieren (Zeile 4,14)
    button = ttk.Button(window, text="fast game")  # minimalistischer Button (verwendet Zeile 2)
    button.configure(command=lambda: print("FAST GAME ACTIVATED"))  # Klick-Aktion (Terminal-Output)
    button.place(relx=0.5, rely=0.5, anchor="center")  # perfekt mittig (mathematisch zentral)
    return button  # Button zurückgeben

def style_fast_game_design():  # futuristisches Design anwenden (Zeile 14)
    style = ttk.Style()  # Style-Objekt (verwendet Zeile 2)
    style.theme_use("clam")  # minimalistisches Theme (edel & clean)
    style.configure("TButton", foreground="#00FFFF")  # cyan Text (Zukunfts-Farbe)
    style.configure("TButton", background="#111111")  # dunkler Button (edel)
    style.configure("TButton", font=("Arial", 16, "bold"))  # klare, große Schrift
    return style  # Style zurückgeben

def main():  # Hauptprogramm - super einfach (alle Funktionen verwenden)
    window = create_fast_game_window()  # Fenster erstellen (Zeile 4)
    style_fast_game_design()  # Design anwenden (Zeile 11)
    create_center_button(window)  # Button hinzufügen (Zeile 8)
    window.mainloop()  # Fenster starten und warten

if __name__ == "__main__":  # nur ausführen wenn direkt gestartet
    main()  # Programm starten (Zeile 18)