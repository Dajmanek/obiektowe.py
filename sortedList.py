import collections.abc

_identiy = lambda a: a


class SortedList(collections.abc.Sequence):
    def __init__(self, data=None, key=None):
        self._key = key or _identiy
        if data is None:
            self.data = []
        elif isinstance(data, SortedList):
            self.data = data.data[:]
        else:
            self.data = sorted(data, key=self._key)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        raise TypeError("należy użyć metody add!")

    def __delitem__(self, index):
        del self.data[index]

    def _find_index(self, value):
        key = self._key(value)
        left = 0
        right = len(self.data) - 1
        while left <= right:
            mid = (left + right) // 2
            if self._key(self.data[mid]) > key:
                right = mid - 1
            elif self._key(self.data[mid]) < key:
                left = mid + 1
            elif self._key(self.data[mid]) == key:
                return mid
        return left

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def __contains__(self, word):
        index = self._find_index(word)
        return index < len(self.data) and self.data[index] == word

    def __reversed__(self):
        return reversed(self.data)

    def add(self, x):
        index = self._find_index(x)
        if index > len(self.data) - 1:
            self.data.append(x)
        else:
            self.data.insert(index, x)

    def clear(self):
        self.data = []
        print("Lista została wyczyszczona")

    def remove(self, item):
        index = self._find_index(item)
        if index < len(self.data) and self.data[index] == item:
            del self.data[index]

    def remove_every(self, item):
        index = self._find_index(item)
        while index < len(self.data) and self.data[index] == item:
            print(index)
            del self.data[index]

    def pop(self, x=-1):
        return self.data.pop(x)

    def copy(self):
        return type(self)(self, self._key)

    def extend(self, second):
        for x in second:
            self.add(x)

    def count(self, word):
        counter = 0
        index = self._find_index(word)
        while index < len(self.data) and self.data[index] == word:
            counter += 1
            index += 1
        return counter

    def index(self, item):
        index = self._find_index(item)

        if index < len(self.data) and self.data[index] == item:
            return index
        else:
            raise ValueError("brak wartosci na liscie")

    @property
    def key(self):
        return self._key


if __name__ == '__main__':
    lista = SortedList([9, 9, 9])
    lista.add(6)
    lista.add(8)
    lista.add(9)
    print(lista)
    # lista.remove_every(9)
    lista2 = reversed(lista)
    print(lista2)
    # print(lista.count(9))

# slowa, sortowanie czy dziala na 05.05
# naprawic odwracanie

print("------------------------")

print(list(reversed(lista)))

slowalen = SortedList(["aaab", "aaaa", "aaac"], lambda x: x[3])
print(list(slowalen))