from enum import Enum


class Category(Enum):
    """A lehetséges nevezési kategóriákat taglaló enum. {kategória neve} = {nevezesi dij az adott formációban történő
    jelentkezéshez}"""

    SOLO = 3000
    DUO = 5000
    TEAM = 7000

    def get_entry_fee(self) -> int:
        return self.value


class Dancer:
    """A résztvevő táncosok közös tulajdonságait tartalmazó szülőosztály"""

    def __init__(self, name: str, category: Category, entry_fee_paid=False, subscore_technique=0):
        """
        Konstruktor a szülőosztályhoz
        :param name: A táncos, illetve a formáció neve
        :param category: A kategória amiben indulni szeretnének (solo, duo, team)
        :param entry_fee_paid: Igaz, ha kifizették a nevezési díjt, és hamis, ha nem
        :param subscore_technique: Részpontszám, mely az adott előadás technikáját jellemzi 1-10-ig
        """
        self.name = name
        self.category = category
        self.entryFeePaid = entry_fee_paid
        if 10 >= subscore_technique >= 0:
            self.subscoreTechnique = subscore_technique
        self.score = 0


class HipHop (Dancer):

    def __init__(self, name: str, category: Category, entry_fee_paid=False, subscore_technique=0, subscore_style=0,
                 score=0):
        """
        Konstruktor a származtatott osztályhou
        :param name: A táncos, illetve a formáció neve
        :param category: A kategória amiben indulni szeretnének (solo, duo, team)
        :param entry_fee_paid: Igaz, ha kifizették a nevezési díjt, és hamis, ha nem
        :param subscore_technique: Részpontszám, mely az adott előadás technikáját jellemzi 1-10-ig
        :param subscore_style: Részpontszám, mely az adott előadás stílusát jellemzi 1-10-ig
        """
        Dancer.__init__(self, name, category, entry_fee_paid, subscore_technique)
        self.subscoreStyle = subscore_style
        self.score = subscore_technique + subscore_style
        if score != 0:
            self.score = score

    def audience_award(self):
        """
        Közönségdíj jóváírására alkalmas metódus, maximum egyszer megtehető minden versenyzőnél
        :return: (void)
        """

        if self.score == self.subscoreTechnique + self.subscoreStyle:
            self.score += 1
            print("\nA pont jóváírása sikeresen megtörtént\n")
        else:
            print("\n" + self.name + " számára már jóvá lett írva a közönségdíj miatt járó plusz pont!\n")


class Contemporary (Dancer):

    def __init__(self, name: str, category: Category, entry_fee_paid=False, subscore_technique=0, subscore_creativity=0,
                 score=0):
        """
        Konstruktor a származtatott osztályhou
        :param name: A táncos, illetve a formáció neve
        :param category: A kategória amiben indulni szeretnének (solo, duo, team)
        :param entry_fee_paid: Igaz, ha kifizették a nevezési díjt, és hamis, ha nem
        :param subscore_technique: Részpontszám, mely az adott előadás technikáját jellemzi 1-10-ig
        :param subscore_creativity: Részpontszám, mely az adott előadás kreativitását jellemzi 1-10-ig
        """
        Dancer.__init__(self, name, category, entry_fee_paid, subscore_technique)
        self.subscoreCreativity = subscore_creativity
        self.score = subscore_technique + subscore_creativity
        if score != 0:
            self.score = score

    def audience_award(self):
        """
        Közönségdíj jóváírására alkalmas metódus, maximum egyszer megtehető minden versenyzőnél
        :return: (void)
        """

        if self.score == self.subscoreTechnique + self.subscoreCreativity:
            self.score += 1
            print("\nA pont jóváírása sikeresen megtörtént\n")
        else:
            print("\n" + self.name + " számára már jóvá lett írva a közönségdíj miatt járó plusz pont!\n")
