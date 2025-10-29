import subprocess  # für Programmstart (Zeile 4-6)
import sys  # für Programm beenden (Zeile 4-6)
import os  # für Pfad-Operationen (Zeile 4-6)

def start_program(program_name):  # startet ein Programm und beendet aktuelles (Zeile 7-13)
    """Einfache Verknüpfung zwischen T-Quest Programmen - mit korrektem Pfad"""
    current_dir = os.path.dirname(os.path.abspath(__file__))  # aktueller Ordner ermitteln
    program_path = os.path.join(current_dir, program_name)  # vollständiger Pfad erstellen
    subprocess.Popen([sys.executable, program_path], cwd=current_dir)  # Programm mit richtigem Pfad starten
    sys.exit()  # aktuelles Programm beenden

def start_main_menu():  # zurück zum Hauptmenü (verwendet in edit_menu.py)
    start_program("quest_rahmen_v4.py")  # Hauptmenü starten (Zeile 4)

def start_edit_menu():  # zum Edit-Menü (verwendet in quest_rahmen_v4.py)
    start_program("edit_menu.py")  # Edit-Menü starten (Zeile 4)

def start_dashboard():  # Dashboard starten (für zukünftige Erweiterung)
    start_program("dashboard.py")  # Dashboard starten (Zeile 4)