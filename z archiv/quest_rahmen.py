import tkinter as tk  # GUI framework für Fenster (Zeile 2-6)
from tkinter import ttk  # moderne Widgets für futuristisches Design (Zeile 2-6)

def create_window():  # erstellt das Hauptfenster (Zeile 8-14)
    root = tk.Tk()  # neues Fenster objekt (verwendet in Zeile 6,7)
    root.title("T-Quest")  # Fenstertitel setzen (sichtbar in Titelleiste)
    root.geometry("1200x800")  # Fenstergröße futuristisch (verwendet in Zeile 17)
    root.configure(bg="#0a0a0a")  # schwarzer Hintergrund für Zukunfts-Look (Zeile 17)
    return root  # Fenster zurückgeben für weitere Nutzung (Zeile 22)

def style_button():  # Button-Design futuristisch gestalten (Zeile 17-23)
    style = ttk.Style()  # Style-Objekt für moderne Optik (verwendet Zeile 2)
    style.theme_use("clam")  # minimalistisches Theme (für edles Design)
    style.configure("Future.TButton", foreground="#00ffff")  # cyan Text (Zeile 19)
    style.configure("Future.TButton", background="#1a1a1a")  # dunkler Button (Zeile 19) 
    style.configure("Future.TButton", font=("Arial", 16, "bold"))  # große Schrift (Zeile 19)
    return style  # Style zurückgeben (verwendet in Zeile 22)

def quest_click():  # Funktion für Button-Klick (verwendet in Zeile 22)
    print("How mutch Time you wanna offer?")  # Terminal-Ausgabe wie gewünscht

def create_quest_button(parent, style):  # Quest Button erstellen (Zeile 5,12,17)
    button = ttk.Button(parent, text="Quest", style="Future.TButton")  # Button mit Style (Zeile 12,17)
    button.configure(command=quest_click)  # Klick-Funktion verknüpfen (Zeile 18)
    button.place(relx=0.5, rely=0.5, anchor="center")  # Button mittig platzieren
    return button  # Button zurückgeben

def main():  # Hauptprogramm startet hier (alle anderen Funktionen)
    window = create_window()  # Fenster erstellen (Zeile 4)
    button_style = style_button()  # Button-Style laden (Zeile 10)
    quest_btn = create_quest_button(window, button_style)  # Button erstellen (Zeile 20)
    window.mainloop()  # GUI starten und auf Events warten

if __name__ == "__main__":  # Programm nur starten wenn direkt ausgeführt
    main()  # Hauptfunktion aufrufen (Zeile 25)