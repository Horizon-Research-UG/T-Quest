import tkinter as tk  # GUI framework für Fenster (Zeile 2-6)
from tkinter import ttk  # moderne Widgets für futuristisches Design (Zeile 2-6)
import random  # für Zufallswerte beim Flimmern (Zeile 8-14, 16-22)

# Globale Variable für aktuellen Screen (Zeile 48-54)
current_screen = "start"

def create_window():  # erstellt das Hauptfenster (Zeile 48-54)
    root = tk.Tk()  # neues Fenster objekt (verwendet in Zeile 6,7)
    root.title("T-Quest v3 - Hauptmenü")  # Fenstertitel setzen (sichtbar in Titelleiste)
    root.geometry("1200x800")  # Fenstergröße futuristisch (verwendet in Zeile 48)
    root.configure(bg="#0a0a0a")  # start schwarzer Hintergrund (Zeile 12)
    return root  # Fenster zurückgeben für weitere Nutzung (Zeile 56)

def flicker_background(root):  # Hintergrund flimmern lassen (Zeile 3,56)
    colors = ["#0a0a0a", "#1a1a1a", "#2a2a2a", "#0f0f0f", "#050505"]  # grau-schwarz Palette
    bg_color = random.choice(colors)  # zufällige Farbe auswählen (Zeile 3)
    root.configure(bg=bg_color)  # Hintergrund ändern (verwendet in Zeile 11)
    flicker_time = random.randint(100, 300)  # zufällige Flimmer-Geschwindigkeit (Zeile 3)
    root.after(flicker_time, lambda: flicker_background(root))  # rekursiver Aufruf (Zeile 12)

def style_button():  # Button-Design futuristisch gestalten (Zeile 48-54)
    style = ttk.Style()  # Style-Objekt für moderne Optik (verwendet Zeile 2)
    style.theme_use("clam")  # minimalistisches Theme (für edles Design)
    style.configure("Future.TButton", foreground="#00ffff")  # cyan Text (Zeile 30)
    style.configure("Future.TButton", background="#1a1a1a")  # dunkler Button (Zeile 30) 
    style.configure("Future.TButton", font=("Arial", 14, "bold"))  # Schrift für Menü (Zeile 30)
    return style  # Style zurückgeben (verwendet in Zeile 56)

def clear_screen(window):  # alle Widgets entfernen für Screen-Wechsel (Zeile 42,46)
    for widget in window.winfo_children():  # durch alle Widgets iterieren
        if widget.winfo_class() != 'Toplevel':  # Toplevel Fenster nicht löschen
            widget.destroy()  # Widget entfernen

def quest_click(window, style):  # Quest Button Klick - zeigt Hauptmenü (Zeile 56)
    global current_screen  # globale Variable verwenden (Zeile 5)
    current_screen = "main_menu"  # Screen zu Hauptmenü wechseln (Zeile 5)
    clear_screen(window)  # Start-Screen löschen (Zeile 27)
    show_main_menu(window, style)  # Hauptmenü anzeigen (Zeile 42)

def schnelles_spiel_click():  # Schnelles Spiel Button Klick (leer wie gewünscht)
    print("Schnelles Spiel - noch nicht implementiert")  # Platzhalter

def skill_forest_click():  # SkillForest Button Klick (leer wie gewünscht)
    print("Skill - Forest - noch nicht implementiert")  # Platzhalter

def show_main_menu(window, style):  # Hauptmenü anzeigen (Zeile 32,56)
    # Titel
    title = tk.Label(window, text="HAUPTMENÜ", fg="#00ffff", bg="#0a0a0a")  # cyan Titel
    title.configure(font=("Arial", 24, "bold"))  # große Schrift für Titel
    title.pack(pady=50)  # Titel mit Abstand platzieren

    # Schnelles Spiel Button
    btn1 = ttk.Button(window, text="Schnelles Spiel", style="Future.TButton")  # erster Menüpunkt
    btn1.configure(command=schnelles_spiel_click)  # Klick-Funktion verknüpfen (Zeile 36)
    btn1.pack(pady=20)  # Button mit Abstand platzieren

    # Skill - Forest Button
    btn2 = ttk.Button(window, text="Skill - Forest", style="Future.TButton")  # zweiter Menüpunkt
    btn2.configure(command=skill_forest_click)  # Klick-Funktion verknüpfen (Zeile 39)
    btn2.pack(pady=20)  # Button mit Abstand platzieren

def show_start_screen(window, style):  # Start-Screen mit Quest Button (Zeile 56)
    button = ttk.Button(window, text="Quest", style="Future.TButton")  # Quest Button erstellen
    button.configure(command=lambda: quest_click(window, style))  # Klick-Funktion (Zeile 32)
    button.place(relx=0.5, rely=0.5, anchor="center")  # Button mittig platzieren
    flicker_button_text(button)  # Button Flackern starten (Zeile 60)

def flicker_button_text(button):  # Button Text flackern wie kaputte Lampe (Zeile 57)
    if button.winfo_exists():  # prüfen ob Button noch existiert
        flicker_texts = ["Quest", "Qu st", "Q est", "Que t", "Quest", ""]  # kaputte Lampen-Effekte
        text = random.choice(flicker_texts)  # zufälligen Text wählen (Zeile 3)
        button.configure(text=text)  # Button Text ändern
        flicker_delay = random.randint(50, 300)  # kurze zufällige Verzögerung (Zeile 3)
        button.after(flicker_delay, lambda: flicker_button_text(button))  # rekursiver Aufruf

def main():  # Hauptprogramm startet hier (alle anderen Funktionen)
    window = create_window()  # Fenster erstellen (Zeile 8)
    button_style = style_button()  # Button-Style laden (Zeile 20)
    show_start_screen(window, button_style)  # Start-Screen anzeigen (Zeile 54)
    flicker_background(window)  # Hintergrund Flimmern starten (Zeile 12)
    window.mainloop()  # GUI starten und auf Events warten

if __name__ == "__main__":  # Programm nur starten wenn direkt ausgeführt
    main()  # Hauptfunktion aufrufen (Zeile 68)