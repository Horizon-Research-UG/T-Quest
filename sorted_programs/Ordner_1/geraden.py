import tkinter as tk  # GUI Framework (Zeile 8-14)
from tkinter import ttk, messagebox  # moderne Widgets und Dialoge (Zeile 8-14)
import matplotlib.pyplot as plt  # für Geraden-Plots (Zeile 50-56)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Plot in GUI (Zeile 50-56)

class Gerade:  # Klasse für eine Gerade y = mx + b (Zeile 58-64)
    def __init__(self, m, b, name="Gerade"):  # Konstruktor (Zeile 8-14)
        self.m = float(m)  # Steigung der Geraden (als Float für Berechnung)
        self.b = float(b)  # y-Achsenabschnitt (als Float für Berechnung)
        self.name = name  # Name der Geraden für Anzeige (verwendet in Zeile 12)

    def berechne_y(self, x):  # y-Wert für gegebenen x-Wert berechnen (Zeile 58)
        return self.m * x + self.b  # Formel y = mx + b anwenden (Zeile 7,8)

    def __str__(self):  # String-Darstellung der Geraden (Zeile 64)
        return f"{self.name}: y = {self.m}x + {self.b}"  # lesbare Form (Zeile 7,8,9)

class GeradenGUI:  # Hauptklasse für die GUI-Anwendung (Zeile 70-76)
    def __init__(self):  # Konstruktor der GUI (Zeile 16-22)
        self.geraden_liste = []  # Liste aller Geraden (verwendet in mehreren Funktionen)
        self.root = tk.Tk()  # Hauptfenster erstellen (verwendet in Zeile 18-22)
        self.root.title("🔢 Geraden-Rechner GUI - Mit Schriftgrößen-Kontrolle")  # Fenstertitel setzen
        self.root.geometry("1400x900")  # GRÖßERE Fenstergröße für bessere Übersicht
        self.root.configure(bg="#f0f0f0")  # heller Hintergrund
        self.wertetabelle_fenster = None  # Variable für Wertetabellen-Fenster
        self.schriftgroesse = 12  # Standard-Schriftgröße (änderbar mit Buttons)
        self.setup_gui()  # GUI-Elemente erstellen (Zeile 22)

    def setup_gui(self):  # GUI-Elemente erstellen und anordnen (Zeile 16)
        # Eingabe-Frame (links) - GRÖßER
        eingabe_frame = ttk.LabelFrame(self.root, text="📊 Gerade hinzufügen", padding=15)  # Rahmen für Eingaben
        eingabe_frame.pack(side=tk.LEFT, fill=tk.Y, padx=15, pady=15)  # links positionieren
        
        # Eingabefelder - mit ANPASSBARER Schriftgröße
        self.name_label = ttk.Label(eingabe_frame, text="Name:", font=("Arial", self.schriftgroesse))  # ANPASSBARES Label
        self.name_label.pack(pady=8)  # positionieren
        self.name_entry = ttk.Entry(eingabe_frame, width=25, font=("Arial", self.schriftgroesse-1))  # ANPASSBARES Eingabefeld
        self.name_entry.pack(pady=8)  # positionieren
        
        self.m_label = ttk.Label(eingabe_frame, text="Steigung (m):", font=("Arial", self.schriftgroesse))  # ANPASSBARES Label
        self.m_label.pack(pady=8)  # positionieren  
        self.m_entry = ttk.Entry(eingabe_frame, width=25, font=("Arial", self.schriftgroesse-1))  # ANPASSBARES Eingabefeld m
        self.m_entry.pack(pady=8)  # positionieren
        
        self.b_label = ttk.Label(eingabe_frame, text="y-Achsenabschnitt (b):", font=("Arial", self.schriftgroesse))  # ANPASSBARES Label
        self.b_label.pack(pady=8)  # positionieren
        self.b_entry = ttk.Entry(eingabe_frame, width=25, font=("Arial", self.schriftgroesse-1))  # ANPASSBARES Eingabefeld b
        self.b_entry.pack(pady=8)  # positionieren
        
        # Buttons - GRÖßER
        ttk.Button(eingabe_frame, text="✅ Hinzufügen", command=self.gerade_hinzufuegen).pack(pady=15)  # Add-Button
        ttk.Button(eingabe_frame, text="🗑️ Alle löschen", command=self.alle_loeschen).pack(pady=8)  # Clear-Button
        ttk.Button(eingabe_frame, text="📋 Wertetabellen", command=self.wertetabelle_anzeigen).pack(pady=8)  # Wertetabellen-Button
        
        # NEU: Schriftgrößen-Kontrolle Frame
        schrift_frame = ttk.LabelFrame(eingabe_frame, text="🔤 Schriftgröße", padding=10)  # Rahmen für Schrift-Buttons
        schrift_frame.pack(pady=15, fill=tk.X)  # Schrift-Frame positionieren
        
        # Schriftgrößen-Buttons nebeneinander
        button_frame = ttk.Frame(schrift_frame)  # Frame für Button-Anordnung
        button_frame.pack()  # Button-Frame positionieren
        
        ttk.Button(button_frame, text="🔍- Kleiner", command=self.schrift_kleiner).pack(side=tk.LEFT, padx=5)  # Kleiner-Button
        ttk.Button(button_frame, text="🔍+ Größer", command=self.schrift_groesser).pack(side=tk.LEFT, padx=5)  # Größer-Button
        
        # Aktuelle Schriftgröße anzeigen
        self.schrift_label = ttk.Label(schrift_frame, text=f"Größe: {self.schriftgroesse}")  # Anzeige der aktuellen Größe
        self.schrift_label.pack(pady=5)  # Label positionieren
        
        # Listen-Frame (mitte) - GRÖßER
        listen_frame = ttk.LabelFrame(self.root, text="📋 Geraden-Liste", padding=15)  # Rahmen für Liste
        listen_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=15, pady=15)  # mittig positionieren
        
        # Listbox für Geraden - GRÖßER
        self.geraden_listbox = tk.Listbox(listen_frame, width=35, height=25, font=("Arial", 11))  # GRÖßERE Liste
        self.geraden_listbox.pack(padx=15, pady=15)  # positionieren
        
        # Plot-Frame (rechts) - GRÖßER
        plot_frame = ttk.LabelFrame(self.root, text="📈 Geraden-Plot mit Achsen", padding=15)  # Rahmen für Plot
        plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=15, pady=15)  # rechts, erweiterbar
        
        # Matplotlib Figure - GRÖßER
        self.fig, self.ax = plt.subplots(figsize=(9, 7))  # GRÖßERER Plot (war 6,5)
        self.canvas = FigureCanvasTkAgg(self.fig, plot_frame)  # Canvas für Plot (Zeile 4)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Canvas positionieren

    def gerade_hinzufuegen(self):  # neue Gerade hinzufügen (GUI-Version)
        try:  # Fehlerbehandlung für Eingaben
            name = self.name_entry.get() or f"Gerade {len(self.geraden_liste)+1}"  # Name holen
            m = float(self.m_entry.get())  # Steigung als Float (Zeile 7)
            b = float(self.b_entry.get())  # y-Achsenabschnitt als Float (Zeile 8)
            
            neue_gerade = Gerade(m, b, name)  # neue Gerade erstellen (Zeile 6)
            self.geraden_liste.append(neue_gerade)  # zur Liste hinzufügen (Zeile 17)
            
            # Eingabefelder leeren
            self.name_entry.delete(0, tk.END)  # Name-Feld leeren
            self.m_entry.delete(0, tk.END)  # m-Feld leeren  
            self.b_entry.delete(0, tk.END)  # b-Feld leeren
            
            self.liste_aktualisieren()  # Liste aktualisieren (Zeile 58)
            self.plot_aktualisieren()  # Plot aktualisieren (Zeile 64)
            
        except ValueError:  # bei ungültigen Zahlen
            messagebox.showerror("Fehler", "Bitte gültige Zahlen für m und b eingeben!")  # Fehlermeldung

    def alle_loeschen(self):  # alle Geraden löschen (Reset-Funktion)
        self.geraden_liste.clear()  # Liste leeren (Zeile 17)
        self.liste_aktualisieren()  # Liste aktualisieren (Zeile 58)
        self.plot_aktualisieren()  # Plot aktualisieren (Zeile 64)

    def wertetabelle_anzeigen(self):  # NEU: Wertetabellen in separatem Fenster anzeigen
        if not self.geraden_liste:  # prüfen ob Geraden vorhanden
            messagebox.showinfo("Info", "Erst Geraden hinzufügen!")  # Info-Meldung
            return  # Funktion beenden
        
        # Wertetabellen-Fenster erstellen
        if self.wertetabelle_fenster:  # falls Fenster bereits offen
            self.wertetabelle_fenster.destroy()  # altes Fenster schließen
        
        self.wertetabelle_fenster = tk.Toplevel(self.root)  # neues Fenster erstellen
        self.wertetabelle_fenster.title("📋 Wertetabellen aller Geraden")  # Fenstertitel
        self.wertetabelle_fenster.geometry("800x600")  # Fenstergröße
        self.wertetabelle_fenster.configure(bg="#f8f8f8")  # heller Hintergrund
        
        # Scrollbares Text-Widget für Tabellen
        text_frame = ttk.Frame(self.wertetabelle_fenster)  # Rahmen für Text
        text_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)  # Rahmen positionieren
        
        # Text-Widget mit Scrollbar
        self.tabellen_text = tk.Text(text_frame, font=("Courier", 11), wrap=tk.WORD)  # Text-Widget
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.tabellen_text.yview)  # Scrollbar
        self.tabellen_text.configure(yscrollcommand=scrollbar.set)  # Scrollbar verknüpfen
        
        # Text-Widget und Scrollbar anordnen
        self.tabellen_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Text links
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Scrollbar rechts
        
        # Wertetabellen für alle Geraden erstellen
        self.tabellen_text.delete(1.0, tk.END)  # Text löschen (falls vorhanden)
        for gerade in self.geraden_liste:  # durch alle Geraden iterieren
            # Titel für jede Gerade
            self.tabellen_text.insert(tk.END, f"═══ {gerade.name} ═══\n")  # Gerade-Titel
            self.tabellen_text.insert(tk.END, f"Funktion: {gerade}\n\n")  # Formel anzeigen
            
            # Tabellenkopf
            self.tabellen_text.insert(tk.END, "   x   |   y   \n")  # Kopf
            self.tabellen_text.insert(tk.END, "-------+-------\n")  # Trennlinie
            
            # Wertetabelle (x von -10 bis 10)
            for x in range(-10, 11):  # durch x-Werte iterieren
                y = gerade.berechne_y(x)  # y-Wert berechnen
                self.tabellen_text.insert(tk.END, f"{x:4} | {y:6.1f}\n")  # formatierte Zeile
            
            self.tabellen_text.insert(tk.END, "\n" + "="*20 + "\n\n")  # Trennlinie zwischen Geraden

    def schrift_kleiner(self):  # NEU: Schriftgröße verkleinern (Zeile 103)
        if self.schriftgroesse > 8:  # Minimum-Schriftgröße 8 (lesbar bleiben)
            self.schriftgroesse -= 2  # um 2 Punkte verkleinern
            self.schrift_aktualisieren()  # alle Schriften aktualisieren (Zeile 108)
        else:  # wenn bereits minimal
            messagebox.showinfo("Info", "Minimale Schriftgröße erreicht!")  # Info-Meldung

    def schrift_groesser(self):  # NEU: Schriftgröße vergrößern (Zeile 103)
        if self.schriftgroesse < 24:  # Maximum-Schriftgröße 24 (nicht zu groß)
            self.schriftgroesse += 2  # um 2 Punkte vergrößern
            self.schrift_aktualisieren()  # alle Schriften aktualisieren (Zeile 108)
        else:  # wenn bereits maximal
            messagebox.showinfo("Info", "Maximale Schriftgröße erreicht!")  # Info-Meldung

    def schrift_aktualisieren(self):  # NEU: alle Schriftgrößen in GUI aktualisieren (Zeile 98,103)
        # Schriftgröße-Anzeige aktualisieren
        self.schrift_label.configure(text=f"Größe: {self.schriftgroesse}")  # Label aktualisieren (Zeile 23)
        
        # Label-Schriften aktualisieren
        font_label = ("Arial", self.schriftgroesse)  # Standard-Schrift für Labels
        self.name_label.configure(font=font_label)  # Name-Label aktualisieren
        self.m_label.configure(font=font_label)  # m-Label aktualisieren
        self.b_label.configure(font=font_label)  # b-Label aktualisieren
        
        # Eingabefelder aktualisieren
        font_eingabe = ("Arial", self.schriftgroesse - 1)  # etwas kleinere Schrift für Eingaben
        self.name_entry.configure(font=font_eingabe)  # Name-Feld aktualisieren
        self.m_entry.configure(font=font_eingabe)  # m-Feld aktualisieren
        self.b_entry.configure(font=font_eingabe)  # b-Feld aktualisieren
        
        # Listbox aktualisieren
        font_liste = ("Arial", self.schriftgroesse)  # Standard-Schrift für Liste
        self.geraden_listbox.configure(font=font_liste)  # Listbox-Schrift aktualisieren
        
        # Plot aktualisieren (Achsen-Beschriftungen)
        self.plot_aktualisieren()  # Plot neu zeichnen mit neuer Schriftgröße (Zeile 125)

    def liste_aktualisieren(self):  # Listbox mit aktuellen Geraden füllen (Zeile 44,52)
        self.geraden_listbox.delete(0, tk.END)  # alte Einträge löschen
        for gerade in self.geraden_liste:  # durch alle Geraden iterieren (Zeile 17)
            self.geraden_listbox.insert(tk.END, str(gerade))  # Gerade zur Liste hinzufügen (Zeile 12)

    def plot_aktualisieren(self):  # Plot mit allen Geraden aktualisieren - MIT ACHSEN! (Zeile 44,52)
        self.ax.clear()  # alten Plot löschen
        
        # X- und Y-ACHSEN prominent einzeichnen
        self.ax.axhline(y=0, color='black', linewidth=2, alpha=0.8)  # X-ACHSE (horizontal bei y=0)
        self.ax.axvline(x=0, color='black', linewidth=2, alpha=0.8)  # Y-ACHSE (vertikal bei x=0)
        
        # Gitternetz und Beschriftung - ANPASSBARE Schriftgröße
        self.ax.grid(True, alpha=0.3, linestyle='--')  # feines Gitternetz (gestrichelt)
        self.ax.set_xlabel("x-Achse", fontsize=self.schriftgroesse+2, fontweight='bold')  # ANPASSBARE x-Achsen Beschriftung
        self.ax.set_ylabel("y-Achse", fontsize=self.schriftgroesse+2, fontweight='bold')  # ANPASSBARE y-Achsen Beschriftung
        self.ax.set_title("Geraden y = mx + b", fontsize=self.schriftgroesse+4, fontweight='bold')  # ANPASSBARER Titel
        
        # Achsen-Bereich festlegen für bessere Sicht
        self.ax.set_xlim(-12, 12)  # x-Bereich erweitert
        self.ax.set_ylim(-12, 12)  # y-Bereich erweitert
        
        if self.geraden_liste:  # nur wenn Geraden vorhanden
            x_werte = range(-12, 13)  # x-Werte von -12 bis 12 (erweitert)
            farben = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']  # verschiedene Farben
            for i, gerade in enumerate(self.geraden_liste):  # durch alle Geraden (Zeile 17)
                y_werte = [gerade.berechne_y(x) for x in x_werte]  # y-Werte berechnen (Zeile 10)
                farbe = farben[i % len(farben)]  # Farbe auswählen (rotierend)
                self.ax.plot(x_werte, y_werte, label=gerade.name, linewidth=3, color=farbe)  # DICKERE Linie
            self.ax.legend(fontsize=self.schriftgroesse)  # ANPASSBARE Legende (Namen der Geraden)
        
        self.canvas.draw()  # Plot neu zeichnen (Zeile 33)

    def run(self):  # Hauptschleife starten (Zeile 76)
        self.plot_aktualisieren()  # initialen Plot erstellen (Zeile 64)
        self.root.mainloop()  # GUI starten (verwendet Zeile 19)

if __name__ == "__main__":  # nur ausführen wenn direkt gestartet
    app = GeradenGUI()  # GUI-Anwendung erstellen (Zeile 16)
    app.run()  # Anwendung starten (Zeile 70)