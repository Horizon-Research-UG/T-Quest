import tkinter as tk  # GUI Framework (Zeile 4-10)
from tkinter import messagebox  # Dialoge (Zeile 4-10)

class EinfachesGeradenSpiel:  # Einfache Version ohne matplotlib (Zeile 16-22)
    def __init__(self):  # Konstruktor des einfachen Spiels (Zeile 4-10)
        self.root = tk.Tk()  # Hauptfenster erstellen (verwendet in Zeile 6-10)
        self.root.title("🎯 Einfaches Gerade-Ziehen (TEST)")  # Fenstertitel setzen
        self.root.geometry("800x600")  # Fenstergröße
        self.root.configure(bg="#2d2d2d")  # dunkler Hintergrund
        self.punkte = 0  # Spieler-Punkte (Zeile 22)
        self.setup_game()  # Spiel-GUI erstellen (Zeile 10)

    def setup_game(self):  # Einfaches Spiel aufbauen (Zeile 4)
        # Titel
        title_label = tk.Label(self.root, text="🎯 GERADEN-SPIEL TEST", fg="#00ff00", bg="#2d2d2d")  # Titel
        title_label.configure(font=("Arial", 24, "bold"))  # große Schrift
        title_label.pack(pady=30)  # Titel positionieren
        
        # Punkte
        self.punkte_label = tk.Label(self.root, text=f"🏆 Punkte: {self.punkte}", fg="#ffff00", bg="#2d2d2d")  # Punkte
        self.punkte_label.configure(font=("Arial", 16, "bold"))  # Punkte-Schrift (Zeile 6)
        self.punkte_label.pack(pady=10)  # Punkte positionieren
        
        # Eingabebereich
        eingabe_frame = tk.Frame(self.root, bg="#3d3d3d")  # Eingabe-Bereich
        eingabe_frame.pack(pady=20)  # Eingabe-Frame positionieren
        
        tk.Label(eingabe_frame, text="Gib eine Funktion ein: y = mx + b", fg="white", bg="#3d3d3d", font=("Arial", 14)).pack(pady=10)  # Anweisung
        
        # m-Eingabe
        tk.Label(eingabe_frame, text="Steigung (m):", fg="white", bg="#3d3d3d").pack()  # m-Label
        self.m_entry = tk.Entry(eingabe_frame, font=("Arial", 12), width=10)  # m-Eingabe
        self.m_entry.pack(pady=5)  # m-Eingabe positionieren
        
        # b-Eingabe  
        tk.Label(eingabe_frame, text="y-Achsenabschnitt (b):", fg="white", bg="#3d3d3d").pack()  # b-Label
        self.b_entry = tk.Entry(eingabe_frame, font=("Arial", 12), width=10)  # b-Eingabe
        self.b_entry.pack(pady=5)  # b-Eingabe positionieren
        
        # Test-Button
        tk.Button(eingabe_frame, text="✅ Funktion testen", command=self.funktion_testen, bg="#0066cc", fg="white", font=("Arial", 12, "bold")).pack(pady=15)  # Test-Button
        
        # Info-Text
        info_text = """📋 ANLEITUNG:
        
1. Gib Werte für m und b ein
2. Klicke auf 'Funktion testen'  
3. Du bekommst Punkte basierend auf deiner Eingabe!

Beispiel: m=2, b=3 ergibt y=2x+3"""  # Hilfe-Text
        
        info_label = tk.Label(self.root, text=info_text, fg="#cccccc", bg="#2d2d2d", font=("Arial", 11), justify=tk.LEFT)  # Info
        info_label.pack(pady=20)  # Info positionieren

    def funktion_testen(self):  # Funktion testen und Punkte geben (Zeile 28)
        try:  # Fehlerbehandlung für Eingabe
            m = float(self.m_entry.get())  # Steigung holen
            b = float(self.b_entry.get())  # y-Achsenabschnitt holen
            
            # Einfache Punktevergabe
            punkte_neu = abs(int(m * 10)) + abs(int(b * 5)) + 50  # Punkte basierend auf Eingabe
            self.punkte += punkte_neu  # Punkte hinzufügen (Zeile 6)
            
            # Punkte aktualisieren
            self.punkte_label.configure(text=f"🏆 Punkte: {self.punkte}")  # Punkte-Anzeige (Zeile 16)
            
            # Erfolgs-Nachricht
            messagebox.showinfo("Erfolg!", f"🎉 Funktion getestet!\n\ny = {m}x + {b}\n\n+{punkte_neu} Punkte erhalten!")  # Erfolg (Zeile 5)
            
            # Eingaben löschen
            self.m_entry.delete(0, tk.END)  # m-Feld leeren
            self.b_entry.delete(0, tk.END)  # b-Feld leeren
            
        except ValueError:  # bei ungültigen Eingaben
            messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben!")  # Fehler-Meldung (Zeile 5)

    def run(self):  # Spiel starten (Zeile 16)
        self.root.mainloop()  # GUI-Hauptschleife (verwendet Zeile 6)

if __name__ == "__main__":  # nur ausführen wenn direkt gestartet
    print("🎮 Starte einfaches Geraden-Spiel...")  # Start-Info
    spiel = EinfachesGeradenSpiel()  # Spiel erstellen (Zeile 4)
    spiel.run()  # Spiel starten (Zeile 28)