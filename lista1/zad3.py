import random
import time


class Die:
    value = None

    def __init__(self, sides):
        self.sides = sides

    def get_sides(self):
        return self.sides

    def get_value(self):
        return self.value

    def roll(self):
        self.value = random.randrange(1, self.sides + 1)


print("Witaj w grze Oczko")
time.sleep(0.5)

while True:
    print("Wpisz \"start\" aby zacząć gre lub \"stop\" aby zamknąć program: ", end='')
    input_text = input().lower()
    if input_text == "stop":
        print("Zamykanie...")
        time.sleep(0.5)
        exit()

    if input_text == "start":
        break

print("Start!")
time.sleep(0.5)

points_bot = 0
points_player = 0

die = Die(6)

while True:
    print("Rzut komputera...")
    die.roll()
    points_bot += die.get_value()
    time.sleep(1)
    while True:
        print("Twoja kolej (wpisz \"rzut\" aby rzucic kośćmi): ", end='')
        input_text = input().lower()
        if input_text == "rzut":
            break

    print("Rzucam...")
    time.sleep(1)
    die.roll()
    points_player += die.get_value()
    print(f"Wylosowales {die.get_value()}pkt. Aktualnie posiadasz {points_player}pkt.")
    while True:
        print("Wpisz \"koniec\" aby zrezygnować z rzucania i wyświetlić wynik lub \"graj\" aby grać dalej: ", end='')
        input_text = input().lower()
        if input_text == "koniec":
            if points_player > 21:
                print("Przegrałeś!")
                print("Przekroczyłeś 21 punktow.")
                print(f"Komputer uzyskał {points_bot}pkt.")
                exit()
            if points_bot == points_player:
                print(f"Gra zakończyła się remisem ({points_bot}pkt.])")
                exit()
            print("Wygrałeś!" if points_player > points_bot else "Przegrałeś :(")
            print(f"Uzyskałeś {points_player}pkt.")
            print(f"Komputer uzyskał {points_bot}pkt.")
            exit()
        if input_text == "graj":
            break