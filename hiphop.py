from dancers import *

class HipHop (Dancer):

    def __init__(self, name: str, category: Category, entryFeePaid = False, subscoreTechnique = 0, subscoreStyle = 0, score = 0):
        """
        Konstruktor a származtatott osztályhou
        :param name: A táncos, illetve a formáció neve
        :param category: A kategória amiben indulni szeretnének (solo, duo, team)
        :param entryFeePaid: Igaz, ha kifizették a nevezési díjt, és hamis, ha nem
        :param subscoreTechnique: Részpontszám, mely az adott előadás technikáját jellemzi 1-10-ig
        :param subscoreStyle: Részpontszám, mely az adott előadás stílusát jellemzi 1-10-ig
        """
        Dancer.__init__(self, name, category, entryFeePaid, subscoreTechnique)
        self.subscoreStyle = subscoreStyle
        self.score = subscoreTechnique + subscoreStyle
        if score != 0:
            self.score = score


    def audienceAward(self):
        """
        Közönségdíj jóváírására alkalmas metódus, maximum egyszer megtehető minden versenyzőnél
        :return: (void)
        """

        if self.score == self.subscoreTechnique + self.subscoreStyle:
            self.score += 1
            print("\nA pont jóváírása sikeresen megtörtént\n")
        else:
            print("\n", self.name, "számára már jóvá lett írva a közönségdíj miatt járó plusz pont!\n")
