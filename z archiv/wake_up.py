import tkinter as tk  # GUI Framework (verwendet Zeile 23, 45, 67)
from tkinter import ttk  # moderne Widgets (verwendet Zeile 56, 78)
import load_plugins  # Plugin-System (verwendet Zeile 89, 95)

navigation_stack = []  # globaler Verlauf (verwendet Zeile 34, 67, 89)

class NavigationManager:
    """Verwaltet die Navigation zwischen den verschiedenen Ebenen - TICKET-KONFORM"""
    
    @staticmethod
    def push_level(level_name, load_function):
        """Fügt eine neue Ebene zum Verlauf hinzu"""
        # Prüfen, ob Level bereits im Stack (vermeidet Duplikate)
        if navigation_stack and navigation_stack[-1][0] == level_name:
            print(f"⚠️ Level '{level_name}' bereits aktiv, nicht doppelt hinzugefügt")
            return
            
        navigation_stack.append((level_name, load_function))
        print(f"📍 Navigation: {level_name} hinzugefügt. Stack-Tiefe: {len(navigation_stack)}")
        print(f"📋 Vollständiger Pfad: {' → '.join([item[0] for item in navigation_stack])}")
    
    @staticmethod
    def go_back(window):
        """KONTEXTSENSITIVER Back-Button: Geht NUR eine Ebene zurück (Ticket-Anforderung)"""
        current_depth = len(navigation_stack)
        print(f"⬅️ Back-Button gedrückt. Aktuelle Tiefe: {current_depth}")
        print(f"📍 Aktueller Pfad: {' → '.join([item[0] for item in navigation_stack])}")
        
        if current_depth <= 1:
            # Ebene 1 (Wake up/TimeQuest) -> bleiben wo wir sind
            print("✅ Bereits in Basis-Ebene (Wake up), kein weiterer Rückschritt möglich")
            return
        
        # EINE Ebene zurückgehen (kontextsensitiv)
        current_level = navigation_stack.pop()
        new_depth = len(navigation_stack)
        
        print(f"⬅️ Verlasse: '{current_level[0]}' (Tiefe {current_depth} → {new_depth})")
        
        # Zur DIREKT vorherigen Ebene wechseln
        if navigation_stack:
            previous_level, previous_function = navigation_stack[-1]
            print(f"📍 Kontextsensitive Navigation zurück zu: '{previous_level}' ✅")
            print(f"📋 Neuer Pfad: {' → '.join([item[0] for item in navigation_stack])}")
            # Direkte Funktion aufrufen (KEIN push_level!)
            previous_function(window)
        else:
            # Fallback (sollte nie passieren bei korrekter Logik)
            print("⚠️ Fallback: zurück zu TimeQuest")
            NavigationManager.reset_to_start(window)
    
    @staticmethod
    def reset_to_start(window):
        """SEPARATER Reset-Button: Führt IMMER zurück zu 'Wake up' (Ticket-Anforderung)"""
        print("🏠 Reset-Button: Springe direkt zu 'Wake up' (alle Ebenen überspringen)")
        print(f"📍 Vorher: {' → '.join([item[0] for item in navigation_stack])}")
        
        # Stack komplett leeren und neu initialisieren
        navigation_stack.clear()
        NavigationManager.load_main_level(window)
        
        print("✅ Reset abgeschlossen: Zurück bei Wake up/TimeQuest")
    
    @staticmethod
    def get_breadcrumb():
        """Gibt den aktuellen Navigationspfad als String zurück"""
        if not navigation_stack:
            return "TimeQuest"
        path = " → ".join([item[0] for item in navigation_stack])
        return path
    
    @staticmethod
    def add_breadcrumb_to_window(window):
        """Fügt eine Breadcrumb-Navigation zum Fenster hinzu"""
        breadcrumb_text = NavigationManager.get_breadcrumb()
        breadcrumb_label = tk.Label(window, text=f"🔍 {breadcrumb_text}", 
                                   bg="#000000", fg="#888888", 
                                   font=("Arial", 10))
        breadcrumb_label.place(relx=0.5, rely=0.95, anchor="center")
        return breadcrumb_label
    
    @staticmethod
    def add_navigation_buttons(window):
        """Fügt sowohl Back- als auch Reset-Button hinzu (Ticket-konform)"""
        current_depth = len(navigation_stack)
        
        # KONTEXTSENSITIVER Back-Button (nur wenn Tiefe > 1)
        if current_depth > 1:
            back_button = ttk.Button(window, text="← Zurück")
            back_button.configure(command=lambda: NavigationManager.go_back(window))
            back_button.place(relx=0.05, rely=0.05, anchor="nw")
        
        # SEPARATER Reset-Button (nur wenn nicht bereits in Wake up)
        if current_depth > 1:
            reset_button = ttk.Button(window, text="🏠 Wake up")
            reset_button.configure(command=lambda: NavigationManager.reset_to_start(window))
            reset_button.place(relx=0.95, rely=0.05, anchor="ne")
        
        # Breadcrumb hinzufügen
        NavigationManager.add_breadcrumb_to_window(window)
    
    @staticmethod
    def load_main_level(window):
        """Lädt die Haupt-Ebene (TimeQuest)"""
        navigation_stack.clear()
        navigation_stack.append(("TimeQuest", lambda w: NavigationManager.load_main_level(w)))
        clear_window(window)
        window.title("FUTURE")
        create_center_button(window)

def create_window():  # Basis-Fenster (verwendet Zeile 125)
    root = tk.Tk()  # Hauptfenster (für GUI-System)
    root.title("TimeQuest")  # Projekt-Name (sichtbar Titel-Bar)
    root.geometry("800x600")  # Standard-Größe (Desktop-optimiert)
    root.configure(bg="#000000")  # schwarz (futuristisch wie Anforderung)
    root.resizable(True, True)  # skalierbar (USB-Stick Kompatibilität)
    return root  # Fenster-Objekt (für weitere Funktionen)

def add_quest_button(window):  # Quest-Button (verwendet Zeile 131)
    btn = ttk.Button(window, text="Quest")  # Haupt-Button (wie Anforderung)
    btn.configure(command=lambda: start_quest(window))  # Quest-Start (Zeile 95)
    btn.place(relx=0.5, rely=0.5, anchor="center")  # Fenster-Mitte (Design-Anforderung)
    print("How mutch Time you wanna offer?")  # Terminal-Output (Anforderung)
    return btn  # Button-Objekt (für Referenz)

def switch_to_plugins(window):  # Wechsel zu Plugins im gleichen Fenster
    print("🔄 switch_to_plugins() aufgerufen")
    
    # Navigation-Stack aktualisieren
    NavigationManager.push_level("Plugins", lambda w: switch_to_plugins_direct(w))
    
    # Plugins direkt laden
    switch_to_plugins_direct(window)

def switch_to_plugins_direct(window):  # Direkter Wechsel ohne Stack-Update
    print("🔄 switch_to_plugins_direct() aufgerufen")
    
    # Alle Widgets im Fenster löschen (aber Fenster behalten)
    clear_window(window)
    
    # Plugin-Inhalte aus load_plugins.py laden (separates Modul!)
    load_plugins.load_into_window(window, back_callback=lambda: NavigationManager.go_back(window))
    
    # Titel ändern um zu zeigen, dass wir in Plugins sind
    window.title("FUTURE - Plugins Loaded")

def clear_window(window):  # Fenster-Inhalt löschen (wiederverwendbar)
    for widget in window.winfo_children():
        widget.destroy()

def switch_to_level(window, level_module):  # Zu beliebigem Level wechseln
    clear_window(window)
    # Dynamisch das entsprechende Modul laden
    level_module.load_into_window(window, back_callback=lambda: switch_back_to_main(window))

def switch_back_to_main(window):  # Zurück zum Hauptmenü
    # Alle Widgets löschen
    for widget in window.winfo_children():
        widget.destroy()
    
    # Titel zurücksetzen
    window.title("FUTURE")
    
    # Original-Button wieder erstellen
    create_center_button(window)

def style_future_design():  # futuristisches Design anwenden (Zeile 14)
    style = ttk.Style()  # Style-Objekt (verwendet Zeile 2)
    style.theme_use("clam")  # minimalistisches Theme (edel & clean)
    style.configure("TButton", foreground="#00FFFF")  # cyan Text (Zukunfts-Farbe)
    style.configure("TButton", background="#111111")  # dunkler Button (edel)
    style.configure("TButton", font=("Arial", 16, "bold"))  # klare, große Schrift
    return style  # Style zurückgeben

def main():  # Hauptprogramm - super einfach (alle Funktionen verwenden)
    window = create_future_window()  # Fenster erstellen (Zeile 4)
    style_future_design()  # Design anwenden (Zeile 11)
    
    # Navigation-Stack initialisieren
    NavigationManager.load_main_level(window)
    
    window.mainloop()  # Fenster starten und warten

if __name__ == "__main__":  # nur ausführen wenn direkt gestartet
    main()  # Programm starten (Zeile 18)