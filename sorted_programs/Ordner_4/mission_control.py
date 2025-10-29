
def read_and_print():
    with open ("y - datenbank/offen", "r") as a:
        x = a.read().strip()  # read() statt readlines() + strip() entfernt \n
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

