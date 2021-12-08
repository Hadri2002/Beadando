from dancers import *

class Contemporary (Dancer):

    def __init__(self, name: str, category: Category, entryFeePaid = False, subscoreTechnique = 0, subscoreCreativity = 0):
        """
        Konstruktor a származtatott osztályhou
        :param name: A táncos, illetve a formáció neve
        :param category: A kategória amiben indulni szeretnének (solo, duo, team)
        :param entryFeePaid: Igaz, ha kifizették a nevezési díjt, és hamis, ha nem
        :param subscoreTechnique: Részpontszám, mely az adott előadás technikáját jellemzi 1-10-ig
        :param subscoreCreativity: Részpontszám, mely az adott előadás kreativitását jellemzi 1-10-ig
        """
        Dancer.__init__(self, name, category, entryFeePaid, subscoreTechnique)
        self.subscoreCreativity = subscoreCreativity
        self.score = subscoreTechnique + subscoreCreativity

    def audienceAward(self):
        """
        Közönségdíj jóváírására alkalmas metódus, maximum egyszer megtehető minden versenyzőnél
        :return: (void)
        """

        if self.score == self.subscoreTechnique + self.subscoreCreativity:
            self.score += 1
        else:
            print(self.name, "számára már jóvá lett írva a közönségdíj miatt járó plusz pont!")