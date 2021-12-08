from enum import Enum

class Category(Enum):
    """A lehetséges nevezési kategóriákat taglaló enum. {kategória neve} = {nevezesi dij az adott formációban történő
    jelentkezéshez}"""

    SOLO = 3000
    DUO = 5000
    TEAM = 7000

    def getEntryFee(self) -> int:
        return self.value


class Dancer:
    """A résztvevő táncosok közös tulajdonságait tartalmazó szülőosztály"""

    def __init__(self, name: str, category: Category, entryFeePaid = False, subscoreTechnique = 0):
        """
        Konstruktor a szülőosztályhoz
        :param name: A táncos, illetve a formáció neve
        :param category: A kategória amiben indulni szeretnének (solo, duo, team)
        :param entryFeePaid: Igaz, ha kifizették a nevezési díjt, és hamis, ha nem
        :param subscoreTechnique: Részpontszám, mely az adott előadás technikáját jellemzi 1-10-ig
        """
        self.name = name
        self.category = category
        self.entryFeePaid = entryFeePaid
        if subscoreTechnique >= 0 and subscoreTechnique <= 10:
            self.subscoreTechnique = subscoreTechnique
        self.score = 0

