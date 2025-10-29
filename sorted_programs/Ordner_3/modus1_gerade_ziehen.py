import tkinter as tk  # GUI Framework (Zeile 10-16)
from tkinter import ttk, messagebox  # moderne Widgets und Dialoge (Zeile 10-16)
import matplotlib.pyplot as plt  # für Geraden-Plots (Zeile 43-49)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Plot in GUI (Zeile 43-49)
import random  # für zufällige Geraden (Zeile 22-28)
import math  # für Mathematik-Berechnungen (Zeile 22-28)

class GeradenZiehenSpiel:  # Modus 1: Gerade ziehen und Punkte sammeln (Zeile 55-61)
    def __init__(self):  # Konstruktor des Zieh-Spiels (Zeile 10-16)
        self.root = tk.Tk()  # Hauptfenster erstellen (verwendet in Zeile 12-16)
        self.root.title("🎯 MODUS 1: Gerade ziehen")  # Fenstertitel setzen
        self.root.geometry("1200x800")  # Fenstergröße für Spiel
        self.root.configure(bg="#2d2d2d")  # dunkler Spiel-Hintergrund
        self.level = 1  # aktuelles Schwierigkeits-Level (1-4)
        self.punkte = 0  # Spieler-Punkte (Zeile 28)
        self.ziel_gerade = self.generiere_zufalls_gerade()  # Ziel-Gerade generieren (Zeile 22)
        self.setup_game()  # Spiel-GUI erstellen (Zeile 16)

    def generiere_zufalls_gerade(self):  # zufällige Ziel-Gerade erstellen (Zeile 14)
        m = random.uniform(-3, 3)  # zufällige Steigung zwischen -3 und 3 (Zeile 5)
        b = random.uniform(-5, 5)  # zufälliger y-Achsenabschnitt (Zeile 5)
        return {"m": round(m, 1), "b": round(b, 1)}  # gerundete Werte zurückgeben

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
        steuerung_frame = tk.LabelFrame(self.root, text="🎮 Steuerung", bg="#3d3d3d", fg="white")  # Steuerung
        steuerung_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=10)  # links positionieren
        
        # Eingabefelder für Gerade
        tk.Label(steuerung_frame, text="Deine Gerade:", fg="white", bg="#3d3d3d", font=("Arial", 14, "bold")).pack(pady=10)  # Titel
        
        tk.Label(steuerung_frame, text="Steigung (m):", fg="white", bg="#3d3d3d").pack(pady=5)  # m-Label
        self.m_entry = tk.Entry(steuerung_frame, font=("Arial", 12), width=15)  # m-Eingabe
        self.m_entry.pack(pady=5)  # m-Eingabe positionieren
        
        tk.Label(steuerung_frame, text="y-Achsenabschnitt (b):", fg="white", bg="#3d3d3d").pack(pady=5)  # b-Label
        self.b_entry = tk.Entry(steuerung_frame, font=("Arial", 12), width=15)  # b-Eingabe
        self.b_entry.pack(pady=5)  # b-Eingabe positionieren
        
        # Buttons
        tk.Button(steuerung_frame, text="✅ Gerade zeichnen", command=self.gerade_pruefen, bg="#0066cc", fg="white", font=("Arial", 12, "bold")).pack(pady=15)  # Prüf-Button
        tk.Button(steuerung_frame, text="🎲 Neue Aufgabe", command=self.neue_aufgabe, bg="#cc6600", fg="white", font=("Arial", 12, "bold")).pack(pady=5)  # Neue-Aufgabe-Button
        tk.Button(steuerung_frame, text="⬆️ Level +", command=self.level_erhoehen, bg="#009900", fg="white", font=("Arial", 12, "bold")).pack(pady=5)  # Level+-Button
        tk.Button(steuerung_frame, text="⬇️ Level -", command=self.level_senken, bg="#990000", fg="white", font=("Arial", 12, "bold")).pack(pady=5)  # Level--Button
        
        # Plot Frame (rechts)
        plot_frame = tk.LabelFrame(self.root, text="📈 Geraden-Spiel", bg="#3d3d3d", fg="white")  # Plot-Bereich
        plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=10)  # rechts positionieren
        
        # Matplotlib Figure
        self.fig, self.ax = plt.subplots(figsize=(8, 6), facecolor='#2d2d2d')  # dunkler Plot (Zeile 3,4)
        self.ax.set_facecolor('#1a1a1a')  # dunkler Plot-Hintergrund
        self.canvas = FigureCanvasTkAgg(self.fig, plot_frame)  # Canvas für Plot (Zeile 4)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Canvas positionieren
        
        # Aufgaben-Info
        self.aufgabe_label = tk.Label(steuerung_frame, text="", fg="#ffff00", bg="#3d3d3d", font=("Arial", 11), wraplength=200, justify=tk.LEFT)  # Aufgaben-Text
        self.aufgabe_label.pack(pady=20)  # Aufgaben-Text positionieren
        
        self.neue_aufgabe()  # erste Aufgabe generieren (Zeile 67)

    def level_erhoehen(self):  # Level erhöhen (bis Level 4) (Zeile 43)
        if self.level < 4:  # Maximum Level 4
            self.level += 1  # Level um 1 erhöhen (Zeile 14)
            self.level_label.configure(text=f"📊 Level: {self.level}")  # Level-Anzeige aktualisieren (Zeile 30)
            self.neue_aufgabe()  # neue Aufgabe für neues Level (Zeile 67)

    def level_senken(self):  # Level senken (bis Level 1) (Zeile 43)
        if self.level > 1:  # Minimum Level 1
            self.level -= 1  # Level um 1 senken (Zeile 14)
            self.level_label.configure(text=f"📊 Level: {self.level}")  # Level-Anzeige aktualisieren (Zeile 30)
            self.neue_aufgabe()  # neue Aufgabe für neues Level (Zeile 67)

    def neue_aufgabe(self):  # neue Ziel-Gerade generieren (Zeile 49,55)
        self.ziel_gerade = self.generiere_zufalls_gerade()  # neue Ziel-Gerade (Zeile 18)
        aufgabe_text = f"🎯 AUFGABE:\nZeichne eine Gerade, die durch die grünen Punkte geht!\n\nLevel {self.level} Schwierigkeit"  # Aufgaben-Text
        self.aufgabe_label.configure(text=aufgabe_text)  # Aufgaben-Text setzen (Zeile 54)
        self.plot_aktualisieren()  # Plot aktualisieren (Zeile 73)

    def plot_aktualisieren(self):  # Plot mit Ziel-Gerade und Level-Anpassungen (Zeile 61,67)
        self.ax.clear()  # alten Plot löschen
        
        # Grundlegende Plot-Einstellungen ERST setzen
        self.ax.grid(True, alpha=0.3, color='white')  # weißes Gitter
        self.ax.set_xlim(-10, 10)  # X-Bereich
        self.ax.set_ylim(-10, 10)  # Y-Bereich
        self.ax.axhline(y=0, color='white', linewidth=2)  # X-Achse weiß (dicker)
        self.ax.axvline(x=0, color='white', linewidth=2)  # Y-Achse weiß (dicker)
        
        # Achsen-BESCHRIFTUNG je nach Level anzeigen oder verstecken
        if self.level == 1:  # Level 1: ALLE Achsen beschriftet (FIX!)
            self.ax.set_xlabel("X-Achse", color='white', fontsize=12)  # X-Achse beschriften
            self.ax.set_ylabel("Y-Achse", color='white', fontsize=12)  # Y-Achse beschriften
            # Achsen-Zahlen sichtbar lassen (Standard)
        elif self.level == 2:  # Level 2: nur X-Achse beschriftet
            self.ax.set_xlabel("X-Achse", color='white', fontsize=12)  # X-Achse beschriften
            self.ax.set_yticklabels([])  # Y-Achsen-Zahlen entfernen
        elif self.level == 3:  # Level 3: nur Y-Achse beschriftet
            self.ax.set_ylabel("Y-Achse", color='white', fontsize=12)  # Y-Achse beschriften  
            self.ax.set_xticklabels([])  # X-Achsen-Zahlen entfernen
        elif self.level == 4:  # Level 4: keine Achsen beschriftet
            self.ax.set_xticklabels([])  # X-Achsen-Zahlen entfernen
            self.ax.set_yticklabels([])  # Y-Achsen-Zahlen entfernen
        
        # Ziel-Punkte auf der Gerade anzeigen
        x_punkte = [-8, -4, 0, 4, 8]  # X-Werte für Zielpunkte
        y_punkte = [self.ziel_gerade["m"] * x + self.ziel_gerade["b"] for x in x_punkte]  # Y-Werte berechnen
        self.ax.scatter(x_punkte, y_punkte, color='lime', s=100, marker='o', label='Zielpunkte', zorder=5)  # grüne Zielpunkte
        
        # Titel je nach Level
        if self.level == 1:  # Level 1: alle Infos
            self.ax.set_title(f"Level {self.level}: Alle Achsen sichtbar", color='white', fontsize=14)
        elif self.level == 2:  # Level 2: ohne Y-Labels
            self.ax.set_title(f"Level {self.level}: Ohne Y-Achsen-Beschriftung", color='white', fontsize=14)
        elif self.level == 3:  # Level 3: ohne X-Labels
            self.ax.set_title(f"Level {self.level}: Ohne X-Achsen-Beschriftung", color='white', fontsize=14)
        else:  # Level 4: ohne beide Labels
            self.ax.set_title(f"Level {self.level}: Ohne X- und Y-Achsen-Beschriftung", color='white', fontsize=14)
        
        self.canvas.draw()  # Plot neu zeichnen (Zeile 46)

    def gerade_pruefen(self):  # eingegebene Gerade prüfen und bewerten (Zeile 37,43)
        try:  # Fehlerbehandlung für Eingabe
            m_user = float(self.m_entry.get())  # Benutzer-Steigung holen
            b_user = float(self.b_entry.get())  # Benutzer-y-Achsenabschnitt holen
            
            # Benutzer-Gerade zeichnen
            x_werte = range(-10, 11)  # X-Werte für Gerade
            y_werte = [m_user * x + b_user for x in x_werte]  # Y-Werte berechnen
            self.ax.plot(x_werte, y_werte, color='red', linewidth=3, label=f'Deine Gerade: y={m_user}x+{b_user}')  # rote Benutzer-Gerade
            
            # Genauigkeit berechnen
            m_diff = abs(self.ziel_gerade["m"] - m_user)  # Steigung-Unterschied
            b_diff = abs(self.ziel_gerade["b"] - b_user)  # Y-Achsenabschnitt-Unterschied
            gesamt_diff = m_diff + b_diff  # Gesamt-Abweichung
            
            # Punkte berechnen (je näher, desto mehr Punkte)
            if gesamt_diff < 0.5:  # sehr genau
                neue_punkte = 100
                feedback = "🏆 PERFEKT! Exzellente Gerade!"
            elif gesamt_diff < 1.0:  # genau
                neue_punkte = 75
                feedback = "🎉 SEHR GUT! Fast perfekt!"
            elif gesamt_diff < 2.0:  # ok
                neue_punkte = 50
                feedback = "👍 GUT! Schon recht nah dran!"
            elif gesamt_diff < 3.0:  # schlecht
                neue_punkte = 25
                feedback = "👌 OK! Noch etwas Übung nötig!"
            else:  # sehr schlecht
                neue_punkte = 10
                feedback = "💪 Versuche es nochmal!"
            
            # Bonus für höhere Level
            level_bonus = (self.level - 1) * 20  # 0, 20, 40, 60 Bonus-Punkte
            neue_punkte += level_bonus  # Level-Bonus hinzufügen
            
            self.punkte += neue_punkte  # Punkte hinzufügen (Zeile 14)
            self.punkte_label.configure(text=f"🏆 Punkte: {self.punkte}")  # Punkte aktualisieren (Zeile 26)
            
            # Ziel-Gerade auch anzeigen
            ziel_y = [self.ziel_gerade["m"] * x + self.ziel_gerade["b"] for x in x_werte]  # Ziel-Y-Werte
            self.ax.plot(x_werte, ziel_y, color='lime', linewidth=2, linestyle='--', label=f'Ziel: y={self.ziel_gerade["m"]}x+{self.ziel_gerade["b"]}')  # grüne Ziel-Gerade
            
            self.ax.legend()  # Legende anzeigen
            self.canvas.draw()  # Plot aktualisieren (Zeile 46)
            
            # Feedback anzeigen
            messagebox.showinfo("Ergebnis", f"{feedback}\n\n+{neue_punkte} Punkte (inkl. {level_bonus} Level-Bonus)\n\nDeine Gerade: y = {m_user}x + {b_user}\nZiel-Gerade: y = {self.ziel_gerade['m']}x + {self.ziel_gerade['b']}")
            
        except ValueError:  # bei ungültigen Eingaben
            messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben!")

    def run(self):  # Spiel starten (Zeile 61)
        self.root.mainloop()  # GUI-Hauptschleife (verwendet Zeile 12)

if __name__ == "__main__":  # nur ausführen wenn direkt gestartet
    spiel = GeradenZiehenSpiel()  # Spiel erstellen (Zeile 10)
    spiel.run()  # Spiel starten (Zeile 112)