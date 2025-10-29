import time  # für time.sleep (Zeile 5)
from ebene_1_v2 import fast_game

def main():  # Hauptmenü-Funktion (Zeile 17)
    print("Starte das Menü...")  # Begrüßung
    time.sleep(0.5)  # kurze Pause für bessere UX (Zeile 1)

    input("Drücke Enter, um fortzufahren...")

    print("Schnelles Spiel (1)")
    print("Dashboard (2)")
    print("Bearbeiten (3)")
    choice = input("Wähle eine Option: ")
    if choice == "1":
        print("Schnelles Spiel ausgewählt")
        fast_game.main()  # schnelles Spiel starten (Zeile 14)
    elif choice == "2":
        print("Dashboard ausgewählt")
    elif choice == "3":
        print("Bearbeiten ausgewählt")
    else:
        print("Ungültige Auswahl")  # Fehlerbehandlung

if __name__ == "__main__":  # nur ausführen wenn direkt gestartet
    main()  # Hauptmenü starten