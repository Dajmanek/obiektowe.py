import abc
import numbers


class Temperature(abc.ABC):

    def __init__(self, temperature):
        self.temperature = temperature

    def __str__(self):
        return f"{round(self.temperature)} stopni w skali"

    def __repr__(self):
        values = ", ".join("{}".format(i) for i in self.__dict__.keys())
        return f"{self.__class__.__name__}({values})"

    def above_freezing(self):
        return self.convert_to_Celsius().temperature > 0

    @abc.abstractmethod
    def convert_to_Fahrenheit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def convert_to_Celsius(self):
        raise NotImplementedError

    @abc.abstractmethod
    def convert_to_Kelvin(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def temperature(self):
        return self._temperature

    @temperature.setter
    @abc.abstractmethod
    def temperature(self, value):
        if isinstance(value, numbers.Real):
            self._temperature = value
        else: self._temperature = 0


class Fahrenheit(Temperature):

    def __init__(self, temperature):
        super().__init__(temperature)

    def __str__(self):
        return f"{super().__str__()} Fahrenheit"

    def convert_to_Fahrenheit(self):
        return self

    def convert_to_Celsius(self):
        return Celsius(0.556 * (self.temperature - 32))

    def convert_to_Kelvin(self):
        return Kelvin(0.556 * (self.temperature - 32) + 273.16)

    @property
    def temperature(self):
        return super().temperature

    @temperature.setter
    def temperature(self, value):
        super(type(self), type(self)).temperature.__set__(self, value)


class Celsius(Temperature):
    def __init__(self, temperature):
        super().__init__(temperature)

    def __str__(self):
        return f"{super().__str__()} Celsius"

    def convert_to_Fahrenheit(self):
        return Fahrenheit(self.temperature / 0.556 + 32)

    def convert_to_Celsius(self):
        return self

    def convert_to_Kelvin(self):
        return Kelvin(self.temperature + 273.16)

    @property
    def temperature(self):
        return super().temperature

    @temperature.setter
    def temperature(self, value):
        super(type(self), type(self)).temperature.__set__(self, value)


class Kelvin(Temperature):
    def __init__(self, temperature):
        super().__init__(temperature)

    def __str__(self):
        return f"{super().__str__()} Kelvin"

    def convert_to_Fahrenheit(self):
        return Fahrenheit((self.temperature - 273.16) / 0.556 + 32)

    def convert_to_Celsius(self):
        return Celsius(self.temperature - 273.16)

    def convert_to_Kelvin(self):
        return self

    @property
    def temperature(self):
        return super().temperature

    @temperature.setter
    def temperature(self, value):
        super(type(self), type(self)).temperature.__set__(self, value)


def print_list(list):
    for temp in list:
        if temp.above_freezing():
            print(f"{temp} - (powyżej zera)")
        else:
            print(f"{temp}")


lista = [Fahrenheit(0), Fahrenheit(15), Fahrenheit(-20), Fahrenheit(50),
         Celsius(0), Celsius(-20), Celsius(15), Celsius(50),
         Kelvin(260), Kelvin(0), Kelvin(300), Kelvin(280)]

print("Lista 1")
print_list(lista)

lista_fahrenheit = [temp.convert_to_Fahrenheit() for temp in lista]
print("\n\nLista Fehrenheita")
print_list(filter(lambda temp: not temp.above_freezing(), lista_fahrenheit))

lista_celsius = [temp.convert_to_Celsius() for temp in lista]
print("\n\nLista Celsiusa")
print_list(filter(lambda temp: not temp.above_freezing(), lista_celsius))

lista_kelvin = [temp.convert_to_Kelvin() for temp in lista]
print("\n\nLista Kelvina")
print_list(filter(lambda temp: not temp.above_freezing(), lista_kelvin))
