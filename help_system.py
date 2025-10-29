import tkinter as tk  # GUI Framework (verwendet Zeile 23, 45)
from tkinter import ttk  # moderne Widgets (verwendet Zeile 16, 28)

help_window = None  # globales Hilfe-Fenster (verwendet Zeile 34, 47)

def create_help_button(parent):  # Hilfe-Button (verwendet überall)
    btn = ttk.Button(parent, text="?")  # Fragezeichen-Symbol (Universal)
    btn.configure(command=toggle_help)  # Hilfe ein/aus (Zeile 22)
    btn.place(relx=0.95, rely=0.95, anchor="se")  # rechts unten (immer sichtbar)
    return btn  # Button-Objekt (Referenz)

def create_draggable_help(parent):  # verschiebbarer Hilfe-Button (Anforderung)
    btn = tk.Button(parent, text="💡", bg="#FFD700", fg="#000000")  # Gold-Button (Highlight)
    btn.configure(command=toggle_help, font=("Arial", 12, "bold"))  # Hilfe-Toggle (Zeile 22)
    btn.place(relx=0.9, rely=0.1, anchor="center")  # Start-Position (rechts oben)
    make_draggable(btn)  # verschiebbar machen (Zeile 27)
    return btn  # Button-Objekt (Referenz)

def make_draggable(widget):  # Widget verschiebbar (verwendet Zeile 13)
    widget.bind("<Button-1>", start_drag)  # Maus-Click (Start-Event)
    widget.bind("<B1-Motion>", drag_motion)  # Maus-Bewegung (Drag-Event)
    widget.bind("<ButtonRelease-1>", stop_drag)  # Maus-Release (Stop-Event)

def start_drag(event):  # Drag-Start (verwendet Zeile 18)
    widget = event.widget  # Widget-Referenz (Event-Source)
    widget.start_x = event.x  # Start-X-Position (Drag-Anfang)
    widget.start_y = event.y  # Start-Y-Position (Drag-Anfang)

def drag_motion(event):  # Drag-Bewegung (verwendet Zeile 18)
    widget = event.widget  # Widget-Referenz (Event-Source)
    x = widget.winfo_x() + event.x - widget.start_x  # neue X-Position (Berechnung)
    y = widget.winfo_y() + event.y - widget.start_y  # neue Y-Position (Berechnung)
    widget.place(x=x, y=y)  # Position setzen (Update)

def stop_drag(event):  # Drag-Ende (verwendet Zeile 18)
    pass  # keine Aktion (Event-Handler)

def toggle_help():  # Hilfe ein/ausblenden (verwendet Zeile 8, 13)
    global help_window  # globaler Zugriff (State-Management)
    if help_window and help_window.winfo_exists():  # Fenster existiert (Check)
        help_window.destroy()  # Fenster schließen (Cleanup)
        help_window = None  # Referenz löschen (Reset)
    else:  # Fenster nicht vorhanden (Create)
        create_help_window()  # Hilfe-Fenster erstellen (Zeile 42)

def create_help_window():  # Hilfe-Fenster (verwendet Zeile 37)
    global help_window  # globaler Zugriff (State-Management)
    help_window = tk.Toplevel()  # neues Fenster (Popup)
    help_window.title("TimeQuest - Hilfe")  # Fenster-Titel (Branding)
    help_window.geometry("400x300")  # Kompakte Größe (Usability)
    help_window.configure(bg="#000000")  # schwarz (Design-Konsistenz)
    add_help_content(help_window)  # Inhalt hinzufügen (Zeile 47)

def add_help_content(window):  # Hilfe-Inhalt (verwendet Zeile 42)
    title = tk.Label(window, text="🎮 TimeQuest Hilfe")  # Hilfe-Titel (Header)
    title.configure(bg="#000000", fg="#00FFFF", font=("Arial", 16, "bold"))  # Style (Design)
    title.pack(pady=10)  # Position mit Abstand (Layout)
    
    help_text = get_help_text()  # Hilfe-Text holen (Zeile 52)
    content = tk.Label(window, text=help_text, justify="left")  # Hilfe-Inhalt (Content)
    content.configure(bg="#000000", fg="#FFFFFF", font=("Arial", 11))  # lesbar (Usability)
    content.pack(padx=20, pady=10, anchor="w")  # Position (Layout)

def get_help_text():  # Hilfe-Text-Inhalt (verwendet Zeile 50)
    return """🎯 TimeQuest - Gamifizierte Zeitverwaltung
    
📍 Navigation:
- Quest: Startet das Haupt-System
- Zurück: Eine Ebene zurück
- 🏠 Wake up: Zurück zum Start
    
🔄 Funktionen:
- Plugins: Verschiedene Module
- Level 2: Erweiterte Funktionen  
- Geraden-Spiel: Mathematik-Training"""  # Hilfe-Inhalt (Information)

def add_help_to_window(parent):  # Hilfe zu Fenster hinzufügen (Universal)
    return create_draggable_help(parent)  # verschiebbarer Button (Anforderung)