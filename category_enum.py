from enum import Enum

class Category(Enum):
    """A lehetséges nevezési kategóriákat taglaló enum. {kategória neve} = {nevezesi dij az adott formációban történő
    jelentkezéshez}"""

    SOLO = 3000
    DUO = 5000
    TEAM = 7000

    def getEntryFee(self) -> int:
        """
        Getter függvény az adott kategóriához tartozó nevezési díj lekéréséhez
        :return: nevezési díj forintban
        """
        return self.value

