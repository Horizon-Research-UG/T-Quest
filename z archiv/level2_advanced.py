import tkinter as tk  # GUI Framework
from tkinter import ttk  # moderne Widgets
import os
import sys

def create_advanced_interface(window):  # Erweiterte Benutzeroberfläche
    """Erstellt eine erweiterte Benutzeroberfläche für Level 2"""
    
    # Titel-Label
    title_label = tk.Label(window, text="🚀 ADVANCED LEVEL 2", 
                          bg="#000000", fg="#00FFFF", 
                          font=("Arial", 24, "bold"))
    title_label.place(relx=0.5, rely=0.2, anchor="center")
    
    # Haupt-Button für Level 2 Funktionen
    main_button = ttk.Button(window, text="Erweiterte Funktionen")
    main_button.configure(command=lambda: print("LEVEL 2 AKTIVIERT"))
    main_button.place(relx=0.5, rely=0.5, anchor="center")
    
    # Sub-Menu Buttons
    sub_buttons = [
        ("📊 Statistiken", lambda: print("Statistiken geöffnet")),
        ("⚙️ Einstellungen", lambda: print("Einstellungen geöffnet")),
        ("🎯 Missionen", lambda: print("Missionen gestartet"))
    ]
    
    for i, (text, command) in enumerate(sub_buttons):
        btn = ttk.Button(window, text=text)
        btn.configure(command=command)
        btn.place(relx=0.3 + i*0.2, rely=0.7, anchor="center")

def load_into_window(window, back_callback=None):  # In bestehendes Fenster laden
    """Lädt Level 2 Inhalte in ein bestehendes Fenster"""
    
    # Erweiterte Benutzeroberfläche erstellen
    create_advanced_interface(window)
    
    # TICKET-KONFORME Navigation hinzufügen
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
    
    # Weiter zu Level 3 Button
    next_button = ttk.Button(window, text="Level 3 →")
    next_button.configure(command=lambda: load_next_level(window, back_callback))
    next_button.place(relx=0.5, rely=0.85, anchor="center")  # Unten mittig positioniert

def load_next_level(window, back_callback):  # Nächstes Level laden
    """Lädt das nächste Level"""
    try:
        print("🔄 load_next_level() aufgerufen")
        
        # Navigation-Stack aktualisieren
        import wake_up
        wake_up.NavigationManager.push_level("Level 3 Expert", lambda w: load_level3_direct(w, back_callback))
        
        # Level 3 direkt laden
        load_level3_direct(window, back_callback)
        
    except Exception as e:
        print(f"Level 3 noch nicht verfügbar: {e}")

def load_level3_direct(window, back_callback):  # Direkter Level 3 Load
    """Lädt Level 3 Interface direkt"""
    print("🔄 load_level3_direct() aufgerufen")
    
    # Beispiel-Level 3 Interface
    for widget in window.winfo_children():
        widget.destroy()
    
    # Level 3 Placeholder
    title_label = tk.Label(window, text="🌟 LEVEL 3 EXPERT", 
                          bg="#000000", fg="#FFD700", 
                          font=("Arial", 28, "bold"))
    title_label.place(relx=0.5, rely=0.3, anchor="center")
    
    info_label = tk.Label(window, text="Coming Soon...\nDies wird das Experten-Level!", 
                         bg="#000000", fg="#00FFFF", 
                         font=("Arial", 16))
    info_label.place(relx=0.5, rely=0.5, anchor="center")
    
    # TICKET-KONFORME Navigation hinzufügen
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
    
    window.title("FUTURE - Level 3 Expert")

def main():  # Hauptprogramm für direkten Start
    """Startet Level 2 als eigenständiges Programm"""
    root = tk.Tk()
    root.title("FUTURE - Level 2 Advanced")
    root.geometry("800x600")
    root.configure(bg="#000000")
    
    # Style setzen
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", foreground="#00FFFF")
    style.configure("TButton", background="#111111")
    style.configure("TButton", font=("Arial", 12, "bold"))
    
    # Interface laden
    load_into_window(root)
    root.mainloop()

if __name__ == "__main__":
    main()