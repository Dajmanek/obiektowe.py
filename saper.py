import random


def get_number(a, b, text):
    """Funkcja pobiera liczbę całkowitą z zakresu a - b i zwraca ją"""
    while True:
        try:
            number = int(input(f"{text} (zakres: {a} - {b}): "))
        except ValueError as e:
            print("Blad: Podana wartosc nie jest liczbą.")
            continue
        if a <= number <= b:
            return number
        else:
            print("Wyszedłeś poza zakres!")
            continue


def lay_mines(number_of_mines, rows, columns):
    """Funkcja generuje zbiór współrzędnych min na planszy"""
    mines = set()
    while len(mines) < number_of_mines:
        m = random.randrange(rows)
        n = random.randrange(columns)
        mines.add((m, n))
    return mines


def number_of_neighboring_mines(filed, mines, rows, columns):
    """Funkcja dla pola filed liczy ile sąsiadów to miny"""
    count = 0
    i = filed[0]
    j = filed[1]
    for m, n in [(i-1, j-1), (i-1, j), (i - 1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
        if 0 <= m and 0 <= n < columns and (m, n) in mines:
            count += 1

    return count


def create_board(mines, rows, columns, mine):
    board = []
    for r in range(rows):
        line = []
        for c in range(columns):
            if (r, c) in mines:
                line.append(mine)
            else:
                line.append(number_of_neighboring_mines((r, c), mines, rows, columns))
        board.append(line)

    return board


