import tkinter as tk  # GUI Framework (Zeile 8-14)
from tkinter import ttk, messagebox  # moderne Widgets und Dialoge (Zeile 8-14)
import subprocess  # für Modul-Start (Zeile 20-26)
import sys  # für Pfad-Operationen (Zeile 20-26)

class GeradenSpielMenu:  # Hauptmenü für das Geraden-Spiel (Zeile 32-38)
    def __init__(self):  # Konstruktor des Spiel-Menüs (Zeile 8-14)
        self.root = tk.Tk()  # Hauptfenster erstellen (verwendet in Zeile 10-14)
        self.root.title("🎮 GERADEN-SPIEL - Hauptmenü")  # Fenstertitel setzen
        self.root.geometry("800x600")  # Fenstergröße für Spiel-Menü
        self.root.configure(bg="#1e1e1e")  # dunkler Gaming-Hintergrund
        self.setup_menu()  # Menü erstellen (Zeile 14)

    def setup_menu(self):  # Spiel-Menü aufbauen (Zeile 8)
        # Titel-Frame
        titel_frame = tk.Frame(self.root, bg="#1e1e1e")  # Rahmen für Titel
        titel_frame.pack(pady=50)  # Titel-Bereich positionieren
        
        # Spiel-Titel
        title_label = tk.Label(titel_frame, text="🎯 GERADEN-SPIEL", fg="#00ff00", bg="#1e1e1e")  # Gaming-Titel
        title_label.configure(font=("Arial", 28, "bold"))  # große Gaming-Schrift
        title_label.pack()  # Titel positionieren
        
        subtitle_label = tk.Label(titel_frame, text="Teste dein Mathematik-Wissen!", fg="#ffff00", bg="#1e1e1e")  # Untertitel
        subtitle_label.configure(font=("Arial", 16))  # mittlere Schrift für Untertitel
        subtitle_label.pack(pady=10)  # Untertitel positionieren
        
        # Spiel-Modi Frame
        modi_frame = tk.Frame(self.root, bg="#1e1e1e")  # Rahmen für Spiel-Modi
        modi_frame.pack(pady=30)  # Modi-Bereich positionieren
        
        # Modus 1: Gerade-Ziehen
        btn1 = tk.Button(modi_frame, text="🎯 MODUS 1: Gerade ziehen", command=self.start_modus1)  # Modus1-Button
        btn1.configure(font=("Arial", 14, "bold"), bg="#0066cc", fg="white", width=25, height=2)  # Button-Style
        btn1.pack(pady=15)  # Button positionieren
        
        # Modus 2: Funktion erraten
        btn2 = tk.Button(modi_frame, text="🔍 MODUS 2: Funktion erraten", command=self.start_modus2)  # Modus2-Button
        btn2.configure(font=("Arial", 14, "bold"), bg="#cc6600", fg="white", width=25, height=2)  # Button-Style
        btn2.pack(pady=15)  # Button positionieren
        
        # Level-Auswahl Frame
        level_frame = tk.Frame(self.root, bg="#1e1e1e")  # Rahmen für Level-Info
        level_frame.pack(pady=20)  # Level-Bereich positionieren
        
        level_info = tk.Label(level_frame, text="📊 SCHWIERIGKEITS-LEVEL:", fg="#ffffff", bg="#1e1e1e")  # Level-Info
        level_info.configure(font=("Arial", 14, "bold"))  # Info-Schrift
        level_info.pack()  # Info positionieren
        
        # Level-Beschreibungen
        level_text = """🟢 Level 1: Alle Achsen beschriftet (Einfach)
🟡 Level 2: Ohne Y-Achsen-Beschriftung (Mittel)  
🟠 Level 3: Ohne X-Achsen-Beschriftung (Schwer)
🔴 Level 4: Ohne X- und Y-Achsen (Extrem)"""  # Level-Details
        
        level_desc = tk.Label(level_frame, text=level_text, fg="#cccccc", bg="#1e1e1e", justify=tk.LEFT)  # Level-Details
        level_desc.configure(font=("Arial", 11))  # Details-Schrift
        level_desc.pack(pady=10)  # Details positionieren

    def start_modus1(self):  # Modus 1 starten: Gerade ziehen (Zeile 26)
        print("🎯 Starte Modus 1: Gerade ziehen...")  # Debug-Info
        try:  # Fehlerbehandlung
            import os  # für Pfad-Operationen
            current_dir = os.path.dirname(os.path.abspath(__file__))  # aktueller Ordner
            modus1_path = os.path.join(current_dir, "modus1_gerade_ziehen.py")  # vollständiger Pfad
            subprocess.Popen([sys.executable, modus1_path])  # Modus1-Programm mit Pfad starten
        except Exception as e:  # alle Fehler abfangen
            messagebox.showerror("Fehler", f"Modus 1 konnte nicht gestartet werden:\n{str(e)}")  # Fehlermeldung

    def start_modus2(self):  # Modus 2 starten: Funktion erraten (Zeile 26)
        print("🔍 Starte Modus 2: Funktion erraten...")  # Debug-Info
        try:  # Fehlerbehandlung
            import os  # für Pfad-Operationen
            current_dir = os.path.dirname(os.path.abspath(__file__))  # aktueller Ordner
            modus2_path = os.path.join(current_dir, "modus2_funktion_erraten.py")  # vollständiger Pfad
            subprocess.Popen([sys.executable, modus2_path])  # Modus2-Programm mit Pfad starten
        except Exception as e:  # alle Fehler abfangen
            messagebox.showerror("Fehler", f"Modus 2 konnte nicht gestartet werden:\n{str(e)}")  # Fehlermeldung

    def run(self):  # Spiel-Menü starten (Zeile 38)
        self.root.mainloop()  # GUI-Hauptschleife (verwendet Zeile 10)

def main():  # Haupt-Start-Funktion für das Spiel (alle Module verwenden)
    print("🎮 Geraden-Spiel wird gestartet...")  # Start-Info
    spiel_menu = GeradenSpielMenu()  # Spiel-Menü erstellen (Zeile 8)
    spiel_menu.run()  # Spiel-Menü starten (Zeile 32)

if __name__ == "__main__":  # nur ausführen wenn direkt gestartet
    main()  # Spiel starten (Zeile 58)