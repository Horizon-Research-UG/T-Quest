import tkinter as tk  # GUI framework für Fenster (Zeile 2-6)
from tkinter import ttk  # moderne Widgets für futuristisches Design (Zeile 2-6)
import random  # für Zufallswerte beim Flimmern (Zeile 8-14, 16-22)

def create_window():  # erstellt das Hauptfenster (Zeile 24-30)
    root = tk.Tk()  # neues Fenster objekt (verwendet in Zeile 6,7)
    root.title("T-Quest v2")  # Fenstertitel setzen (sichtbar in Titelleiste)
    root.geometry("600x400")  # Fenstergröße futuristisch (verwendet in Zeile 24)
    root.configure(bg="#0a0a0a")  # start schwarzer Hintergrund (Zeile 8)
    return root  # Fenster zurückgeben für weitere Nutzung (Zeile 32)

def flicker_background(root):  # Hintergrund flimmern lassen (Zeile 3,32)
    colors = ["#0a0a0a", "#1a1a1a", "#2a2a2a", "#0f0f0f", "#050505"]  # grau-schwarz Palette
    bg_color = random.choice(colors)  # zufällige Farbe auswählen (Zeile 3)
    root.configure(bg=bg_color)  # Hintergrund ändern (verwendet in Zeile 7)
    flicker_time = random.randint(100, 500)  # zufällige Flimmer-Geschwindigkeit (Zeile 3)
    root.after(flicker_time, lambda: flicker_background(root))  # rekursiver Aufruf (Zeile 8)

def style_button():  # Button-Design futuristisch gestalten (Zeile 24-30)
    style = ttk.Style()  # Style-Objekt für moderne Optik (verwendet Zeile 2)
    style.theme_use("clam")  # minimalistisches Theme (für edles Design)
    style.configure("Future.TButton", foreground="#00ffff")  # cyan Text (Zeile 26)
    style.configure("Future.TButton", background="#1a1a1a")  # dunkler Button (Zeile 26) 
    style.configure("Future.TButton", font=("Arial", 16, "bold"))  # große Schrift (Zeile 26)
    return style  # Style zurückgeben (verwendet in Zeile 32)

def flicker_button_text(button):  # Button Text flackern wie kaputte Lampe (Zeile 3,32)
    flicker_texts = ["Quest", "Qu st", "Q est", "Que t", "Quest", ""]  # kaputte Lampen-Effekte
    text = random.choice(flicker_texts)  # zufälligen Text wählen (Zeile 3)
    button.configure(text=text)  # Button Text ändern
    flicker_delay = random.randint(50, 300)  # kurze zufällige Verzögerung (Zeile 3)
    button.after(flicker_delay, lambda: flicker_button_text(button))  # rekursiver Aufruf

def quest_click():  # Funktion für Button-Klick (verwendet in Zeile 32)
    print("How mutch Time you wanna offer?")  # Terminal-Ausgabe wie gewünscht
    import thanks
    thanks.main()
    import mission_control
    mission_control.main()

def create_quest_button(parent, style):  # Quest Button erstellen (Zeile 5,18,23)
    button = ttk.Button(parent, text="Quest", style="Future.TButton")  # Button mit Style (Zeile 18,23)
    button.configure(command=quest_click)  # Klick-Funktion verknüpfen (Zeile 28)
    button.place(relx=0.5, rely=0.5, anchor="center")  # Button mittig platzieren
    flicker_button_text(button)  # Button Flackern starten (Zeile 24)
    return button  # Button zurückgeben

def main():  # Hauptprogramm startet hier (alle anderen Funktionen)
    window = create_window()  # Fenster erstellen (Zeile 4)
    button_style = style_button()  # Button-Style laden (Zeile 16)
    quest_btn = create_quest_button(window, button_style)  # Button erstellen (Zeile 30)
    flicker_background(window)  # Hintergrund Flimmern starten (Zeile 8)
    window.mainloop()  # GUI starten und auf Events warten

if __name__ == "__main__":  # Programm nur starten wenn direkt ausgeführt
    main()  # Hauptfunktion aufrufen (Zeile 35)