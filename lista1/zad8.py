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
            print("Błędna wartość")
            return
        if value == "test":
            return
        self._name = value


    # def _get_name(self):
    #     return self._name
    #
    # def _set_name(self, value):
    #     if not isinstance(value, str):
    #         print("Błędna wartość")
    #         return
    #     if value == "test":
    #         return
    #     self._name = value
    #
    # def _del_name(self):
    #     print("Nie można usunąć Imienia!")
    #
    # name = property(_get_name, _set_name, _del_name, "Imię")