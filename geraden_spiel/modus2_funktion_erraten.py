import tkinter as tk  # GUI Framework (Zeile 10-16)
from tkinter import ttk, messagebox  # moderne Widgets und Dialoge (Zeile 10-16)
import matplotlib.pyplot as plt  # für Geraden-Plots (Zeile 40-46)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Plot in GUI (Zeile 40-46)
import random  # für zufällige Geraden (Zeile 22-28)

class FunktionErratenSpiel:  # Modus 2: Funktion aus Gerade erraten (Zeile 52-58)
    def __init__(self):  # Konstruktor des Errate-Spiels (Zeile 10-16)
        self.root = tk.Tk()  # Hauptfenster erstellen (verwendet in Zeile 12-16)
        self.root.title("🔍 MODUS 2: Funktion erraten")  # Fenstertitel setzen
        self.root.geometry("1200x800")  # Fenstergröße für Spiel
        self.root.configure(bg="#2d2d2d")  # dunkler Spiel-Hintergrund
        self.level = 1  # aktuelles Schwierigkeits-Level (1-4)
        self.punkte = 0  # Spieler-Punkte (Zeile 28)
        self.aktuelle_gerade = None  # aktuell angezeigte Gerade (Zeile 34)
        self.setup_game()  # Spiel-GUI erstellen (Zeile 16)

    def generiere_gerade(self):  # Gerade für Level generieren (Zeile 14,34)
        # Je nach Level verschiedene Schwierigkeiten
        if self.level == 1:  # Level 1: einfache Zahlen
            m = random.choice([-3, -2, -1, 0, 1, 2, 3])  # ganze Zahlen (Zeile 5)
            b = random.choice([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])  # ganze Zahlen (Zeile 5)
        elif self.level == 2:  # Level 2: halbe Zahlen
            m = random.choice([-2.5, -1.5, -0.5, 0.5, 1.5, 2.5])  # halbe Zahlen (Zeile 5)
            b = random.randint(-5, 5)  # ganze b-Werte (Zeile 5)
        elif self.level == 3:  # Level 3: viertel Zahlen
            m = random.uniform(-2, 2)  # beliebige Zahlen (Zeile 5)
            m = round(m * 4) / 4  # auf Viertel runden
            b = random.randint(-8, 8)  # größerer b-Bereich (Zeile 5)
        else:  # Level 4: schwierige Zahlen
            m = random.uniform(-3, 3)  # beliebige Steigung (Zeile 5)
            b = random.uniform(-10, 10)  # beliebiger y-Achsenabschnitt (Zeile 5)
            m = round(m, 2)  # auf 2 Dezimalstellen
            b = round(b, 2)  # auf 2 Dezimalstellen
        
        return {"m": m, "b": b}  # Gerade zurückgeben

    def setup_game(self):  # Spiel-GUI aufbauen (Zeile 10)
        # Punkte und Level Frame (oben)
        info_frame = tk.Frame(self.root, bg="#2d2d2d")  # Info-Bereich
        info_frame.pack(fill=tk.X, padx=20, pady=10)  # Info-Frame positionieren
        
        self.punkte_label = tk.Label(info_frame, text=f"🏆 Punkte: {self.punkte}", fg="#ffff00", bg="#2d2d2d")  # Punkte-Anzeige
        self.punkte_label.configure(font=("Arial", 16, "bold"))  # Punkte-Schrift (Zeile 14)
        self.punkte_label.pack(side=tk.LEFT)  # links positionieren
        
        self.level_label = tk.Label(info_frame, text=f"📊 Level: {self.level}", fg="#00ff00", bg="#2d2d2d")  # Level-Anzeige
        self.level_label.configure(font=("Arial", 16, "bold"))  # Level-Schrift (Zeile 14)
        self.level_label.pack(side=tk.RIGHT)  # rechts positionieren
        
        # Steuerung Frame (links)
        steuerung_frame = tk.LabelFrame(self.root, text="🔍 Rate die Funktion", bg="#3d3d3d", fg="white")  # Steuerung
        steuerung_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=10)  # links positionieren
        
        # Eingabefelder für geratene Funktion
        tk.Label(steuerung_frame, text="Welche Funktion siehst du?", fg="white", bg="#3d3d3d", font=("Arial", 14, "bold")).pack(pady=10)  # Titel
        
        tk.Label(steuerung_frame, text="Steigung (m):", fg="white", bg="#3d3d3d").pack(pady=5)  # m-Label
        self.m_entry = tk.Entry(steuerung_frame, font=("Arial", 12), width=15)  # m-Eingabe
        self.m_entry.pack(pady=5)  # m-Eingabe positionieren
        
        tk.Label(steuerung_frame, text="y-Achsenabschnitt (b):", fg="white", bg="#3d3d3d").pack(pady=5)  # b-Label
        self.b_entry = tk.Entry(steuerung_frame, font=("Arial", 12), width=15)  # b-Eingabe
        self.b_entry.pack(pady=5)  # b-Eingabe positionieren
        
        # Buttons
        tk.Button(steuerung_frame, text="✅ Funktion prüfen", command=self.funktion_pruefen, bg="#0066cc", fg="white", font=("Arial", 12, "bold")).pack(pady=15)  # Prüf-Button
        tk.Button(steuerung_frame, text="🎲 Neue Gerade", command=self.neue_gerade, bg="#cc6600", fg="white", font=("Arial", 12, "bold")).pack(pady=5)  # Neue-Gerade-Button
        tk.Button(steuerung_frame, text="⬆️ Level +", command=self.level_erhoehen, bg="#009900", fg="white", font=("Arial", 12, "bold")).pack(pady=5)  # Level+-Button
        tk.Button(steuerung_frame, text="⬇️ Level -", command=self.level_senken, bg="#990000", fg="white", font=("Arial", 12, "bold")).pack(pady=5)  # Level--Button
        
        # Multiple-Choice Buttons (für einfachere Bedienung)
        tk.Label(steuerung_frame, text="--- ODER ---", fg="#ffff00", bg="#3d3d3d", font=("Arial", 12, "bold")).pack(pady=10)  # Trenner
        tk.Label(steuerung_frame, text="Schnell-Auswahl:", fg="white", bg="#3d3d3d", font=("Arial", 12, "bold")).pack(pady=5)  # Multiple-Choice Titel
        
        # Frame für Multiple-Choice Buttons
        self.choice_frame = tk.Frame(steuerung_frame, bg="#3d3d3d")  # Frame für Auswahl-Buttons
        self.choice_frame.pack(pady=10)  # Choice-Frame positionieren
        
        # Plot Frame (rechts)
        plot_frame = tk.LabelFrame(self.root, text="📈 Rate diese Funktion!", bg="#3d3d3d", fg="white")  # Plot-Bereich
        plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=10)  # rechts positionieren
        
        # Matplotlib Figure
        self.fig, self.ax = plt.subplots(figsize=(8, 6), facecolor='#2d2d2d')  # dunkler Plot (Zeile 3,4)
        self.ax.set_facecolor('#1a1a1a')  # dunkler Plot-Hintergrund
        self.canvas = FigureCanvasTkAgg(self.fig, plot_frame)  # Canvas für Plot (Zeile 4)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Canvas positionieren
        
        # Aufgaben-Info
        self.aufgabe_label = tk.Label(steuerung_frame, text="", fg="#ffff00", bg="#3d3d3d", font=("Arial", 11), wraplength=200, justify=tk.LEFT)  # Aufgaben-Text
        self.aufgabe_label.pack(pady=20)  # Aufgaben-Text positionieren
        
        self.neue_gerade()  # erste Gerade anzeigen (Zeile 85)

    def level_erhoehen(self):  # Level erhöhen (bis Level 4) (Zeile 64)
        if self.level < 4:  # Maximum Level 4
            self.level += 1  # Level um 1 erhöhen (Zeile 14)
            self.level_label.configure(text=f"📊 Level: {self.level}")  # Level-Anzeige aktualisieren (Zeile 48)
            self.neue_gerade()  # neue Gerade für neues Level (Zeile 85)

    def level_senken(self):  # Level senken (bis Level 1) (Zeile 64)
        if self.level > 1:  # Minimum Level 1
            self.level -= 1  # Level um 1 senken (Zeile 14)
            self.level_label.configure(text=f"📊 Level: {self.level}")  # Level-Anzeige aktualisieren (Zeile 48)
            self.neue_gerade()  # neue Gerade für neues Level (Zeile 85)

    def erstelle_multiple_choice(self):  # Multiple-Choice Optionen generieren (Zeile 85)
        # Alte Buttons entfernen
        for widget in self.choice_frame.winfo_children():  # durch alle Choice-Buttons
            widget.destroy()  # Button löschen
        
        # Richtige Antwort und 3 falsche generieren
        richtige = f"y = {self.aktuelle_gerade['m']}x + {self.aktuelle_gerade['b']}"  # richtige Funktion
        optionen = [richtige]  # Liste mit richtiger Antwort
        
        # 3 falsche Antworten generieren
        for i in range(3):  # 3 falsche Optionen
            falsche_gerade = self.generiere_gerade()  # falsche Gerade generieren (Zeile 18)
            while falsche_gerade == self.aktuelle_gerade:  # nicht die gleiche wie richtige
                falsche_gerade = self.generiere_gerade()  # neue falsche Gerade (Zeile 18)
            falsch = f"y = {falsche_gerade['m']}x + {falsche_gerade['b']}"  # falsche Funktion
            optionen.append(falsch)  # zur Optionen-Liste hinzufügen
        
        # Optionen mischen
        random.shuffle(optionen)  # Reihenfolge zufällig machen (Zeile 5)
        
        # Buttons für jede Option erstellen
        for i, option in enumerate(optionen):  # durch alle Optionen
            btn = tk.Button(self.choice_frame, text=f"{chr(65+i)}) {option}", command=lambda opt=option: self.choice_gewaehlt(opt))  # A,B,C,D Buttons
            btn.configure(bg="#666666", fg="white", font=("Arial", 10), width=25)  # Button-Style
            btn.pack(pady=2)  # Button positionieren

    def choice_gewaehlt(self, gewaehlte_option):  # Multiple-Choice Option gewählt (Zeile 94)
        richtige = f"y = {self.aktuelle_gerade['m']}x + {self.aktuelle_gerade['b']}"  # richtige Antwort (Zeile 88)
        
        if gewaehlte_option == richtige:  # wenn richtig gewählt
            # Punkte für richtige Antwort
            basis_punkte = 50  # Grundpunkte für richtige Antwort
            level_bonus = (self.level - 1) * 25  # Level-Bonus
            gesamt_punkte = basis_punkte + level_bonus  # Gesamt-Punkte
            
            self.punkte += gesamt_punkte  # Punkte hinzufügen (Zeile 14)
            self.punkte_label.configure(text=f"🏆 Punkte: {self.punkte}")  # Punkte aktualisieren (Zeile 44)
            
            messagebox.showinfo("Richtig!", f"🎉 KORREKT!\n\n+{gesamt_punkte} Punkte (inkl. {level_bonus} Level-Bonus)\n\nRichtige Funktion: {richtige}")  # Erfolg-Meldung
        else:  # wenn falsch gewählt
            messagebox.showerror("Falsch!", f"❌ Leider falsch!\n\nDeine Wahl: {gewaehlte_option}\nRichtig wäre: {richtige}")  # Fehler-Meldung

    def neue_gerade(self):  # neue Gerade zum Erraten generieren (Zeile 70,76,82)
        self.aktuelle_gerade = self.generiere_gerade()  # neue Gerade generieren (Zeile 18)
        aufgabe_text = f"🔍 AUFGABE:\nWelche Funktion siehst du?\n\nLevel {self.level} Schwierigkeit"  # Aufgaben-Text
        self.aufgabe_label.configure(text=aufgabe_text)  # Aufgaben-Text setzen (Zeile 72)
        self.plot_aktualisieren()  # Plot aktualisieren (Zeile 131)
        self.erstelle_multiple_choice()  # Multiple-Choice Buttons erstellen (Zeile 82)

    def plot_aktualisieren(self):  # Plot mit aktueller Gerade und Level-Anpassungen (Zeile 113,119)
        self.ax.clear()  # alten Plot löschen
        
        # Achsen je nach Level anzeigen oder verstecken
        if self.level >= 2:  # Level 2+: Y-Achse verstecken
            self.ax.set_yticklabels([])  # Y-Achsen-Labels entfernen
        if self.level >= 3:  # Level 3+: X-Achse verstecken  
            self.ax.set_xticklabels([])  # X-Achsen-Labels entfernen
        if self.level == 4:  # Level 4: beide Achsen verstecken
            self.ax.set_xticks([])  # X-Ticks entfernen
            self.ax.set_yticks([])  # Y-Ticks entfernen
        
        # Grundlegende Plot-Einstellungen
        self.ax.grid(True, alpha=0.3, color='white')  # weißes Gitter
        self.ax.set_xlim(-10, 10)  # X-Bereich
        self.ax.set_ylim(-10, 10)  # Y-Bereich
        self.ax.axhline(y=0, color='white', linewidth=1)  # X-Achse weiß
        self.ax.axvline(x=0, color='white', linewidth=1)  # Y-Achse weiß
        
        # Aktuelle Gerade zeichnen
        x_werte = range(-10, 11)  # X-Werte für Gerade
        y_werte = [self.aktuelle_gerade["m"] * x + self.aktuelle_gerade["b"] for x in x_werte]  # Y-Werte berechnen
        self.ax.plot(x_werte, y_werte, color='cyan', linewidth=4, label='Rate diese Funktion!')  # cyan Gerade
        
        # Einige Punkte auf der Gerade hervorheben
        highlight_x = [-6, -2, 2, 6]  # X-Werte für Highlight-Punkte
        highlight_y = [self.aktuelle_gerade["m"] * x + self.aktuelle_gerade["b"] for x in highlight_x]  # Y-Werte berechnen
        self.ax.scatter(highlight_x, highlight_y, color='yellow', s=120, marker='o', zorder=5)  # gelbe Punkte
        
        # Titel je nach Level
        if self.level == 1:  # Level 1: alle Infos
            self.ax.set_title(f"Level {self.level}: Alle Achsen sichtbar", color='white', fontsize=14)
        elif self.level == 2:  # Level 2: ohne Y-Labels
            self.ax.set_title(f"Level {self.level}: Ohne Y-Achsen-Beschriftung", color='white', fontsize=14)
        elif self.level == 3:  # Level 3: ohne X-Labels
            self.ax.set_title(f"Level {self.level}: Ohne X-Achsen-Beschriftung", color='white', fontsize=14)
        else:  # Level 4: ohne beide Labels
            self.ax.set_title(f"Level {self.level}: Ohne X- und Y-Achsen-Beschriftung", color='white', fontsize=14)
        
        self.ax.legend()  # Legende anzeigen
        self.canvas.draw()  # Plot neu zeichnen (Zeile 68)

    def funktion_pruefen(self):  # manuell eingegebene Funktion prüfen (Zeile 58)
        try:  # Fehlerbehandlung für Eingabe
            m_user = float(self.m_entry.get())  # Benutzer-Steigung holen
            b_user = float(self.b_entry.get())  # Benutzer-y-Achsenabschnitt holen
            
            # Genauigkeit prüfen
            m_richtig = self.aktuelle_gerade["m"]  # richtige Steigung (Zeile 14)
            b_richtig = self.aktuelle_gerade["b"]  # richtiger y-Achsenabschnitt (Zeile 14)
            
            if m_user == m_richtig and b_user == b_richtig:  # wenn exakt richtig
                # Punkte für perfekte Antwort
                basis_punkte = 100  # mehr Punkte für manuelle Eingabe
                level_bonus = (self.level - 1) * 25  # Level-Bonus
                gesamt_punkte = basis_punkte + level_bonus  # Gesamt-Punkte
                
                self.punkte += gesamt_punkte  # Punkte hinzufügen (Zeile 14)
                self.punkte_label.configure(text=f"🏆 Punkte: {self.punkte}")  # Punkte aktualisieren (Zeile 44)
                
                messagebox.showinfo("Perfekt!", f"🏆 EXAKT RICHTIG!\n\n+{gesamt_punkte} Punkte (inkl. {level_bonus} Level-Bonus)\n\nFunktion: y = {m_richtig}x + {b_richtig}")  # Erfolg-Meldung
            else:  # wenn falsch
                messagebox.showerror("Falsch!", f"❌ Leider nicht korrekt!\n\nDeine Eingabe: y = {m_user}x + {b_user}\nRichtig: y = {m_richtig}x + {b_richtig}")  # Fehler-Meldung
            
            # Eingabefelder leeren
            self.m_entry.delete(0, tk.END)  # m-Feld leeren
            self.b_entry.delete(0, tk.END)  # b-Feld leeren
            
        except ValueError:  # bei ungültigen Eingaben
            messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben!")

    def run(self):  # Spiel starten (Zeile 119)
        self.root.mainloop()  # GUI-Hauptschleife (verwendet Zeile 12)

if __name__ == "__main__":  # nur ausführen wenn direkt gestartet
    spiel = FunktionErratenSpiel()  # Spiel erstellen (Zeile 10)
    spiel.run()  # Spiel starten (Zeile 170)