class Pet:

    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.tiredness = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            print("Nazwa musi być tekstem")
            return
        if not value.isalpha():
            print("Nazwa moze zawierac tylko litery")
            return
        if len(value) < 3:
            print("Nazwa musi składać się przynajmniej z trzech znaków")
            return
        self._name = value

    def get_mood(self):
        sum = self.hunger + self.tiredness
        if sum < 5:
            return "szczęśliwy"
        if 5 <= sum <= 10:
            return "zadowolony"
        if 11 <= sum <= 15:
            return "podenerwowany"
        return "wściekły"

    def talk(self):
        self._passage_of_time()
        return self.get_mood()

    def eat(self, food=4):
        self.hunger -= food
        self._passage_of_time()

    def play(self, fun=4):
        self.tiredness -= fun
        self._passage_of_time()

    def _passage_of_time(self):
        self.hunger += 1
        self.tiredness += 1

    def __str__(self):
        print(f"Imię: {self.name}")
        print(f"Głód: {self.hunger}")
        print(f"Poziom znudzenia: {self.tiredness}")
        print(f"Nastrój: {self.get_mood()}")


def help():
    print("\nDostępne komendy:")
    print(" pomoc - wyświetla liste komend")
    print(" jedzenie - karmi zwierzaka zwierzaka")
    print(" zabawa - Zabawa ze zwierzakiem")
    print(" głód - wyświetla stan głodu")
    print(" znudzenie - wyświetla poziom znudzenia")
    print(" nastrój - wyświetla nastrój")
    print(" info - wyświetla wszystkie informacje o zwierzaku")
    print(" stop - aby zamknąć program\n")

def main():
    pet = Pet("Puszek")
    pet.__str__()
    help()
    while True:
        input_text = input().lower()
        if input_text == "stop":
            print("Zamykanie...")
            return

        if input_text == "pomoc":
            help()
            continue

        if input_text == "jedzenie":
            print("Podaj ilość: ", end='')
            input_text = input()
            if not isinstance(input_text, int):
                print("Błąd: wartość musi być liczbą całkowitą")
                continue
            pet.eat(input_text)
            print(f"Zwierzak został nakarmiony, aktualny poziomn głodu: {pet.hunger}")
            continue

        if input_text == "zabawa":
            print("Podaj czas zabawy: ")
            input_text = input()
            if not isinstance(input_text, int):
                print("Błąd: wartość musi być liczbą całkowitą")
                continue
            pet.eat(input_text)
            print(f"Zabawa zakończona, aktualny poziom znudzenia zwierzaka: {pet.tiredness}")
            continue

        if input_text.replace('ó', "o").replace('ł', 'l') == "glod":
            print(f"Poziom głodu: {pet.hunger}")
            continue

        if input_text == "znudzenie":
            print(f"Aktualny poziom znudzenia zwierzaka: {pet.tiredness}")
            continue

        if input_text.replace('ó', 'o') == "nastroj":
            print(f"Nastrój zwierzaka: {pet.talk()}")
            continue

        if input_text == "info":
            pet.__str__()
            continue

        print("Nie odnaleziono komendy podanej nazwie.")


main()
