import tkinter as tk  # GUI framework für Fenster (Zeile 2-6)
from tkinter import ttk  # moderne Widgets für futuristisches Design (Zeile 2-6)
import random  # für Zufallswerte beim Flimmern (Zeile 8-14)

def create_window():  # erstellt das Edit-Menü Fenster (Zeile 27-33)
    root = tk.Tk()  # neues Fenster objekt (verwendet in Zeile 6,7)
    root.title("T-Quest Edit-Menü")  # Fenstertitel setzen (sichtbar in Titelleiste)
    root.geometry("1200x800")  # Fenstergröße futuristisch (verwendet in Zeile 27)
    root.configure(bg="#0a0a0a")  # schwarzer Hintergrund (Zeile 8)
    return root  # Fenster zurückgeben für weitere Nutzung (Zeile 35)

def flicker_background(root):  # Hintergrund flimmern lassen (Zeile 3,35)
    colors = ["#0a0a0a", "#1a1a1a", "#2a2a2a", "#0f0f0f", "#050505"]  # grau-schwarz Palette
    bg_color = random.choice(colors)  # zufällige Farbe auswählen (Zeile 3)
    root.configure(bg=bg_color)  # Hintergrund ändern (verwendet in Zeile 7)
    flicker_time = random.randint(100, 300)  # zufällige Flimmer-Geschwindigkeit (Zeile 3)
    root.after(flicker_time, lambda: flicker_background(root))  # rekursiver Aufruf (Zeile 8)

def style_button():  # Button-Design futuristisch gestalten (Zeile 27-33)
    style = ttk.Style()  # Style-Objekt für moderne Optik (verwendet Zeile 2)
    style.theme_use("clam")  # minimalistisches Theme (für edles Design)
    style.configure("Future.TButton", foreground="#00ffff")  # cyan Text (Zeile 20)
    style.configure("Future.TButton", background="#1a1a1a")  # dunkler Button (Zeile 20) 
    style.configure("Future.TButton", font=("Arial", 14, "bold"))  # Schrift für Menü (Zeile 20)
    return style  # Style zurückgeben (verwendet in Zeile 35)

def skill_forest_click():  # SkillForest Button Klick (leer wie gewünscht)
    print("Skill-Forest - Edit-Modus gestartet")  # Platzhalter für Implementierung

def close_edit_menu():  # Edit-Menü schließen und zurück zum Hauptmenü (einfache Verknüpfung)
    import program_linker  # einfaches Verknüpfungsmodul (Zeile 26)
    program_linker.start_main_menu()  # zurück zum Hauptmenü (Zeile 26)

def show_edit_menu(window, style):  # Edit-Menü anzeigen (Zeile 5,35)
    # Titel
    title = tk.Label(window, text="EDIT MENÜ", fg="#00ffff", bg="#0a0a0a")  # cyan Titel
    title.configure(font=("Arial", 24, "bold"))  # große Schrift für Titel
    title.pack(pady=50)  # Titel mit Abstand platzieren

    # Skill-Forest Button
    btn1 = ttk.Button(window, text="Skill-Forest", style="Future.TButton")  # Skill-Forest Option
    btn1.configure(command=skill_forest_click)  # Klick-Funktion (Zeile 23)
    btn1.pack(pady=20)  # Button mit Abstand platzieren

    # Zurück Button
    btn_back = ttk.Button(window, text="← Zurück zum Hauptmenü", style="Future.TButton")  # Zurück
    btn_back.configure(command=close_edit_menu)  # Klick-Funktion (Zeile 26)
    btn_back.pack(pady=30)  # Button mit mehr Abstand platzieren

def main():  # Hauptprogramm startet hier (alle anderen Funktionen)
    window = create_window()  # Fenster erstellen (Zeile 5)
    button_style = style_button()  # Button-Style laden (Zeile 16)
    show_edit_menu(window, button_style)  # Edit-Menü anzeigen (Zeile 32)
    flicker_background(window)  # Hintergrund Flimmern starten (Zeile 8)
    window.mainloop()  # GUI starten und auf Events warten

if __name__ == "__main__":  # Programm nur starten wenn direkt ausgeführt
    main()  # Hauptfunktion aufrufen (Zeile 43)