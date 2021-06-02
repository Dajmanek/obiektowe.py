class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 3:
            print("Imie musi miec minimum 3 znaki")
            self._name = "Imie"
            return
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        if len(value) < 3:
            print("Nazwisko musi miec minimum 3 znaki")
            self._surname = "Nazwisko"
            return
        self._surname = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            print("Wartosc musi byc liczba calkowita")
            self._age = 5
            return
        if 0 > value > 130:
            print("Wiek musi byc wiekszy od 0 i mniejszy od 130")
            self._age = 5
            return
        self._age = value

    def __str__(self):
        return f"Imie: {self.name}\nNazwisko: {self.surname}\nWiek: {self.age}"


class Student(Person):

    def __init__(self, name, surname, age, field_of_study):
        super().__init__(name, surname, age)
        self.field_of_study = field_of_study
        self.student_book = {}

    def put_grade(self, subject_name, grade):
        self.student_book[subject_name] = grade

    def get_grades(self):
        return self.student_book


class Employe(Person):

    def __init__(self, name, surname, age, job_title):
        #super(Employe, self).__init__(name, surname, age)
        super().__init__(name, surname, age)
        self.job_title = job_title
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

    def get_skills(self):
        return self.skills


def main():
    while True:
        print("Dostepne opcje: [student, pracownik]")
        print("Zarejestruj sie jako: ", end='')
        input_text = input().lower()
        if input_text == "pracownik" or input_text == "student":
            break
        continue

    #dane podstawowe
    print("Podaj imie: ", end='')
    imie = input()
    print("Podaj nazwisko: ", end='')
    nazwisko = input()
    print("Podaj wiek: ", end='')
    wiek = int(input())

    #pracownik
    if input_text == "pracownik":
        print("Podaj stanowisko: ", end='')
        stanowisko = input()
        pracownik = Employe(imie, nazwisko, wiek, stanowisko)
        print("Podaj umiejetnosci (aby zakonczyc wpisz koniec)")
        while True:
            umiejetnosc = input()
            if umiejetnosc.lower() == "koniec":
                break
            pracownik.add_skill(umiejetnosc)
        print("\n\nPodsumowanie\n")
        print(pracownik.__str__())
        print(f"Stanowisko: {pracownik.job_title}")
        print(f"Umiejetnosci:")
        print("\n".join("- {}".format(s) for s in pracownik.get_skills()))
        return

    # student
    print("Podaj kierunek: ", end='')
    kierunek = input()
    student = Student(imie, nazwisko, wiek, kierunek)
    print("Podaj oceny w formacie \"przedmiot:ocena\", wpisz koniec aby zakonczyc")
    while True:
        input_text = input()
        if input_text.lower() == "koniec":
            break
        splited = input_text.split(":")
        if not splited[1].isdigit():
            print("Blad: ocena musi byc liczba calkowita")
            continue
        student.put_grade(splited[0], int(splited[1]))
    print("\n\nPodsumowanie\n")
    print(student.__str__())
    print(f"Kierunek: {student.field_of_study}")
    print(f"Oceny:")
    print("\n".join("- {}: {}".format(k, v) for k, v in student.student_book.items()))


main()