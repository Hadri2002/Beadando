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
