import tkinter as tk  # GUI Framework (Zeile 4)
from tkinter import ttk  # moderne Widgets (Zeile 4)
import os
import sys

def create_future_window():  # futuristisches Fenster erstellen (Zeile 8)
    root = tk.Tk()  # Fenster erstellen (verwendet in Zeile 6,7)
    root.title("FUTURE")  # minimalistischer Titel (sichtbar oben)
    root.geometry("800x600")  # elegante Fenstergröße (verwendet in Zeile 8)
    root.configure(bg="#000000")  # tiefschwarzer Hintergrund (futuristisch)
    return root  # Fenster zurückgeben (verwendet in Zeile 14)

def create_center_button(window, command=None):  # Button mittig platzieren (Zeile 4,14)
    if command is None:
        command = lambda: print("FUTURE ACTIVATED")  # Standard-Kommando
    button = ttk.Button(window, text="TimeQuest")  # minimalistischer Button (verwendet Zeile 2)
    button.configure(command=command)  # Klick-Aktion (anpassbar)
    button.place(relx=0.5, rely=0.5, anchor="center")  # perfekt mittig (mathematisch zentral)
    return button  # Button zurückgeben

def load_into_window(window, back_callback=None):  # In bestehendes Fenster laden
    """Lädt Plugin-Inhalte in ein bestehendes Fenster"""
    
    # Titel für Plugin-Bereich
    title_label = tk.Label(window, text="🔌 PLUGINS LOADED", 
                          bg="#000000", fg="#00FFFF", 
                          font=("Arial", 20, "bold"))
    title_label.place(relx=0.5, rely=0.2, anchor="center")
    
    # Level-Navigation Buttons (verschiedene Programme!)
    level_buttons = [
        ("📊 Level 2 - Advanced", lambda: load_level2(window, back_callback)),
        ("🎮 Geraden-Spiel", lambda: load_game_module(window, back_callback)),
        ("🚀 Level 3 - Expert", lambda: print("Level 3 kommt bald...")),
        ("⚡ Schnellstart", lambda: print("Schnellstart aktiviert"))
    ]
    
    # Buttons in 2x2 Grid anordnen
    for i, (text, command) in enumerate(level_buttons):
        row = i // 2
        col = i % 2
        x = 0.3 + col * 0.4  # 0.3 oder 0.7
        y = 0.45 + row * 0.15  # 0.45 oder 0.6
        
        btn = ttk.Button(window, text=text)
        btn.configure(command=command)
        btn.place(relx=x, rely=y, anchor="center")
    
    # TICKET-KONFORME Navigation-Buttons hinzufügen
    try:
        import wake_up
        wake_up.NavigationManager.add_navigation_buttons(window)
    except Exception as e:
        print(f"Navigation-Buttons nicht verfügbar: {e}")
        # Fallback: manueller Back-Button
        if back_callback:
            back_button = ttk.Button(window, text="← Zurück")
            back_button.configure(command=back_callback)
            back_button.place(relx=0.05, rely=0.05, anchor="nw")

def load_level2(window, back_callback):  # Level 2 in gleichem Fenster laden
    """Lädt Level 2 Advanced im gleichen Fenster"""
    try:
        print("🔄 load_level2() aufgerufen")
        
        # Navigation-Stack von wake_up importieren und aktualisieren  
        import wake_up
        wake_up.NavigationManager.push_level("Level 2 Advanced", lambda w: load_level2_direct(w, back_callback))
        
        # Level 2 direkt laden
        load_level2_direct(window, back_callback)
        
    except Exception as e:
        print(f"Fehler beim Laden von Level 2: {e}")
        # Fallback: zurück zu Plugins
        if back_callback:
            back_callback()

def load_level2_direct(window, back_callback):  # Direkter Level 2 Load ohne Stack-Update
    print("🔄 load_level2_direct() aufgerufen")
    
    # Fenster leeren
    for widget in window.winfo_children():
        widget.destroy()
    
    # Level 2 Modul importieren und laden
    import level2_advanced
    level2_advanced.load_into_window(window, back_callback)
    
    # Titel aktualisieren
    window.title("FUTURE - Level 2 Advanced")

def load_game_module(window, back_callback):  # Geraden-Spiel laden
    """Lädt das Geraden-Spiel Modul"""
    try:
        import subprocess
        import sys
        # Geraden-Spiel in separatem Prozess starten (modulare Struktur)
        script_path = os.path.join(os.path.dirname(__file__), 'geraden_spiel', 'untermain.py')
        subprocess.Popen([sys.executable, script_path])
    except Exception as e:
        print(f"Fehler beim Laden des Spiels: {e}")

def style_future_design():  # futuristisches Design anwenden (Zeile 14)
    style = ttk.Style()  # Style-Objekt (verwendet Zeile 2)
    style.theme_use("clam")  # minimalistisches Theme (edel & clean)
    style.configure("TButton", foreground="#00FFFF")  # cyan Text (Zukunfts-Farbe)
    style.configure("TButton", background="#111111")  # dunkler Button (edel)
    style.configure("TButton", font=("Arial", 16, "bold"))  # klare, große Schrift
    return style  # Style zurückgeben

def main(preserve_style=False):  # Hauptprogramm mit Style-Option
    window = create_future_window()  # Fenster erstellen (Zeile 4)
    if not preserve_style:  # nur Style anwenden wenn nicht von wake_up aufgerufen
        style_future_design()  # Design anwenden (Zeile 11)
    create_center_button(window)  # Button hinzufügen (Zeile 8)
    window.mainloop()  # Fenster starten und warten

if __name__ == "__main__":  # nur ausführen wenn direkt gestartet
    main()  # Programm starten (Zeile 18)