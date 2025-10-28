
def read_and_print():
    with open (r"C:\Users\49176\OneDrive - Heiner Reinecke\Mit PC verknüpft\Desktop\NeuroGames - nicht verschieben\t1\T-Quest\y - datenbank\offen", "r") as a:
        x = a.readlines()
        print(x)

def main():
    read_and_print()


def zitat_1():
    print("unser Leben besteht aus wenigen bewussten Entscheidungen...")
    import time
    time.sleep(1.4)
    print("...und deren Folgen")


if __name__ == "__main__":
    main()

