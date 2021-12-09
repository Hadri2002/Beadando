from hiphop import *
from contemporary import *

def menu_options():
    """
    A menüpontok kiírására alkalmas függvény <3
    """

    print("Válasszon az alábbi menüpontok közül:\n\t0 - Kilépés"
          "\n\t1 - Új versenyző felvétele"
          "\n\t2 - Közönségdíj jóváírása"
          "\n\t3 - Nevezési díj befizetés"
          "\n\t4 - Nyertes lekérése")

def newCompetitor(hiphop: list, contemporary: list) -> None:
    """
    Új versenyző felvételére használható függvény, melyben a megfelelő adatokat először egy osztály példányába elmentjük,
    majd a fájlba kiiratjuk
    :param hiphop: Az eddig felvitt hiphop táncosok adatait tartalmazó lista.
    :param contemporary: Az eddig felvitt hiphop táncosok adatait tartalmazó lista.
    :return: felveszi az új versenyzőt az adatbázisba (void függvény)
    """

    styleSelect = 0
    tempStyle = ""
    tester = 0
    while styleSelect == 0:
        try:
            tempStyle = int(input(
                "Adja meg, hogy melyik stílusban szeretne felvenni egy új versenyzőt! (1 - hiphop, 2 - kortárs) "))
        except ValueError:
            print("Hibás adatmegadás, kérem a megfelelő egész számot írja be a stílus kiválasztásához!")

        if tempStyle == 1 or tempStyle == 2:
            styleSelect = tempStyle

            name = ""
        if styleSelect == 1:  # hiphop

            # versenyző adatainak felvétele
            while name == "":
                tester = 0
                tempName = input("Adja meg a táncos/formáció nevét! ")
                for element in hiphop:
                    if tempName == element[0]:
                        print("Már van ilyen nevű versenyző!")
                        tester += 1
                if tester == 0:
                    name = tempName

            category = categorySelect()
            entryFee = entryFeeSelect()
            print("A technikához kapcsolódó pontszám felvétele: ")
            subscoreTechnique = scoreSelect()
            print("A stílushoz kapcsolódó pontszám felvétele: ")
            subscoreStyle = scoreSelect()
            dancer1 = HipHop(name, category, entryFee, subscoreTechnique, subscoreStyle)

            # versenyző adatainak fájlbaírása
            f = open("hiphop.txt", "a")
            f.write(dancer1.name)
            f.write("\t")
            f.write(str(dancer1.category))
            f.write("\t")
            f.write(str(dancer1.entryFeePaid))
            f.write("\t")
            f.write(str(dancer1.subscoreTechnique))
            f.write("\t")
            f.write(str(dancer1.subscoreStyle))
            f.write("\t")
            f.write(str(dancer1.score))
            f.write("\n")
            f.close()

            print("A felvétel sikeresen megtörtént!")

        elif styleSelect == 2:  # contemporary

            # versenyző adatainak felvétele
            while name == "":
                tester = 0
                tempName = input("Adja meg a táncos/formáció nevét! ")
                for element in contemporary:
                    if tempName == element[0]:
                        print("Már van ilyen nevű versenyző!")
                        tester += 1
                if tester == 0:
                    name = tempName

            category = categorySelect()
            entryFee = entryFeeSelect()
            print("A technikához kapcsolódó pontszám felvétele: ")
            subscoreTechnique = scoreSelect()
            print("A kreativitáshoz kapcsolódó pontszám felvétele: ")
            subscoreCreativity = scoreSelect()
            dancer1 = Contemporary(name, category, entryFee, subscoreTechnique, subscoreCreativity)

            # versenyző adatainak fájlbaírása
            f = open("contemporary.txt", "a")
            f.write(dancer1.name)
            f.write("\t")
            f.write(str(dancer1.category))
            f.write("\t")
            f.write(str(dancer1.entryFeePaid))
            f.write("\t")
            f.write(str(dancer1.subscoreTechnique))
            f.write("\t")
            f.write(str(dancer1.subscoreCreativity))
            f.write("\t")
            f.write(str(dancer1.score))
            f.write("\n")
            f.close()

            print("A felvétel sikeresen megtörtént!")

        elif type(tempStyle) == int:
            print("Hibás adatmegadás, kérem a megfelelő egész számot írja be a stílus kiválasztásához!")

def categorySelect() -> Category:
    """
    Segédfüggvény a kategória kiválasztásához. Integer megadásával visszaadja a választott kategóriát.
    :return: A kiválasztott kategória enumot adja vissza
    """

    value = 0
    temp = ""
    while value == 0:
        try:
            temp = int(input("Adja a kategória számát! (1 - solo, 2 - duo, 3 - csapat) "))
        except ValueError:
            print("Hibás adatmegadás, kérem a megfelelő egész számot írja be a kategória kiválasztásához!")

        if type(temp) == int and temp >= 1 and temp <= 3:
            value = temp
        elif type(temp) == int and (temp <= 1 or temp >= 3):
            print("Hibás adatmegadás, kérem a megfelelő egész számot írja be a kategória kiválasztásához!")

        if value == 1:
            return Category.SOLO
        elif value == 2:
            return Category.DUO
        elif value == 3:
            return Category.TEAM

def entryFeeSelect() -> bool:
    """
    Segédfüggvény, mellyel kiválaszthatjuk, hogy a nevezési díjat kifizette-e a versenyző vagy nem
    :return: True ha kifizette, false ha nem fizette ki
    """

    value = 0
    temp = ""
    while value == 0:
        try:
            temp = int(input("Adja, hogy a versenyző kifizette-e a nevezési díjat! (1 - nincs kifizetve, 2 - ki van fizetve) "))
        except ValueError:
            print("Hibás adatmegadás, kérem a megfelelő egész számot írja be a kiválasztásához!")

        if type(temp) == int and temp >= 1 and temp <= 2:
            value = temp
        elif type(temp) == int and (temp <= 1 or temp >= 2):
            print("Hibás adatmegadás, kérem a megfelelő egész számot írja be a kiválasztásához!")

        if value == 1:
            return False
        elif value == 2:
            return True

def scoreSelect() -> int:
    """
    Segédfüggvény, mellyel megadhatjuk a pontokat egy 0-10-ig tartó skálán
    :return: A pontszám
    """

    value = -1
    temp = ""
    while value == -1:
        try:
            temp = int(input("Adja meg a pontszámot (0 - 10-ig) "))
        except ValueError:
            print("Hibás adatmegadás, kérem egész számot írjon be!")

        if type(temp) == int and temp >= 0 and temp <= 10:
            value = temp
    return value

def listUpload(filepath: str) -> list:
    """
    A táncosok adatait tartalmazó lista feltöltésére alkalmas függvény
    :param filepath: a file amiben a versenyzők adatai vannak tárolva
    :return: a versenyzők adatait tartalmazó lista
    """

    file = open(filepath, "r")
    dancers_list = []
    for sor in file:
        adat = sor.strip().split("\t")

        if adat[1] == "Category.SOLO":
            tempCategory = Category.SOLO
        elif adat[1] == "Category.DUO":
            tempCategory = Category.DUO
        else:
            tempCategory = Category.TEAM

        if adat[2] == "True":
            tempEntryFee = True;
        elif adat[2] == "False":
            tempEntryFee = False
        dancer_list = [adat[0], tempCategory, tempEntryFee, int(adat[3]), int(adat[4]), int(adat[5])]
        dancers_list.append(dancer_list)

    file.close()
    return dancers_list

def audienceAward(hiphop: list, contemporary: list) -> None:
    """
    A versenyzők számára közönségdíjat hagyhatunk jóvá a függvénnyel. Minden versenyző maximum egyszer kaphat plusz
    pontot a közönségdíj alapján
    :param hiphop: Az eddig felvitt hiphop táncosok adatait tartalmazó lista.
    :param contemporary: Az eddig felvitt kortárs táncosok adatait tartalmazó lista.
    :return: A megadott versenyzőhöz tartozó pontszámot megváltoztatja, majd azt az adatbázisban is átírja
    """

    print("Az alábbi menüpont segítségével a közönségdíjat írhatja jóvá a választott táncos számára!")
    styleSelect = 0
    tempStyle = ""

    hiphopNames = []
    contemporaryNames = []
    for element in hiphop:
        hiphopNames.append(element[0])
    for element in contemporary:
        contemporaryNames.append(element[0])

    while styleSelect == 0:
        try:
            tempStyle = int(input("Adja meg, hogy melyik stílusban szerepel a versenyző, akinek jóváírná a közönségdíjért járó plusz pontot! (1 - hiphop, 2 - kortárs) "))
        except ValueError:
            print("Hibás adatmegadás, kérem a megfelelő egész számot írja be a stílus kiválasztásához!")

        if tempStyle == 1 or tempStyle == 2:
            styleSelect = tempStyle

            tester = 0
            while tester == 0:
                if styleSelect == 1: #hiphop
                    print("A nyilvántartásban szereplő versenyzők:", hiphopNames)
                    name = input("Adja meg a táncos / formáció nevét, akinek a közönségdíjat jóvá szeretné hagyni! ")

                    for element in hiphop:
                        if name == element[0]:
                            dancer1 = HipHop(element[0], element[1], element[2], element[3], element[4], element[5])
                            personIndex = hiphop.index(element)
                        else:
                            tester += 1
                    if tester == len(hiphop):
                        print("\nNincs ilyen versenyző a nyilvántartásban!\n")
                        tester = 0

                    else:
                        dancer1.audienceAward() # pont jóváírása


                        # adat megváltoztatása a fájlban
                        with open("hiphop.txt", "r") as f:
                            get_all = f.readlines()

                        with open("hiphop.txt", 'w') as f:
                            for i, line in enumerate(get_all, 0):
                                if i == personIndex:
                                    f.writelines(dancer1.name + "\t" + str(dancer1.category) + "\t" + str(dancer1.entryFeePaid)
                                                 + "\t" + str(dancer1.subscoreTechnique) + "\t" + str(dancer1.subscoreStyle) + "\t" + str(dancer1.score) + "\n")
                                else:
                                    f.writelines(line)


                elif styleSelect == 2: #kortárs
                    print("A nyilvántartásban szereplő versenyzők:", contemporaryNames)
                    name = input("Adja meg a táncos / formáció nevét, akinek a közönségdíjat jóvá szeretné hagyni! ")
                    for element in contemporary:
                        if name == element[0]:
                            dancer1 = Contemporary(element[0], element[1], element[2], element[3], element[4], element[5])
                            personIndex = contemporary.index(element)
                        else:
                            tester += 1
                    if tester == len(contemporary):
                        print("\nNincs ilyen versenyző a nyilvántartásban!\n")
                        tester = 0

                    else:
                        dancer1.audienceAward() # pont jóváírása

                        # adat megváltoztatása a fájlban
                        with open("contemporary.txt", "r") as f:
                            get_all = f.readlines()

                        with open("contemporary.txt", 'w') as f:
                            for i, line in enumerate(get_all, 0):
                                if i == personIndex:
                                    f.writelines(
                                        dancer1.name + "\t" + str(dancer1.category) + "\t" + str(dancer1.entryFeePaid)
                                        + "\t" + str(dancer1.subscoreTechnique) + "\t" + str(
                                            dancer1.subscoreCreativity) + "\t" + str(dancer1.score) + "\n")
                                else:
                                    f.writelines(line)

        elif type(tempStyle) == int:
           print("Hibás adatmegadás, kérem a megfelelő egész számot írja be a stílus kiválasztásához!")

def entryFee(hiphop: list, contemporary: list) -> None:
    """
    Amennyiben a vizsgált versenyző nem fizette be a nevezési díjat azt befizetetté teszi, ha pedig már befizette akkor
    nem történik változás
    :param hiphop:
    :param contemporary:
    :return:
    """

    styleSelect = 0
    tempStyle = ""

    hiphopNames = []
    contemporaryNames = []
    for element in hiphop:
        hiphopNames.append(element[0])
    for element in contemporary:
        contemporaryNames.append(element[0])

    while styleSelect == 0:
        try:
            tempStyle = int(input(
                "Adja meg, hogy melyik stílusban szerepel a versenyző, akinek a nevezési díját megtekintené! (1 - hiphop, 2 - kortárs) "))
        except ValueError:
            print("Hibás adatmegadás, kérem a megfelelő egész számot írja be a stílus kiválasztásához!")

        if tempStyle == 1 or tempStyle == 2:
            styleSelect = tempStyle

            tester = 0
            while tester == 0:

                if styleSelect == 1: # hiphop
                    print("A nyilvántartásban szereplő versenyzők:", hiphopNames)
                    name = input("Adja meg a táncos / formáció nevét, aki a befizetést tette! ")
                    for element in hiphop:
                        if name == element[0]:
                            dancer1 = HipHop(element[0], element[1], element[2], element[3], element[4], element[5])
                            personIndex = hiphop.index(element)
                        else:
                            tester += 1
                    if tester == len(hiphop):
                        print("Nincs ilyen versenyző a nyilvántartásban!")
                        tester = 0

                    else:
                        if dancer1.entryFeePaid == True:
                            print("A versenyző már befizette a nevezési díjat!\n")
                        else:
                            print(dancer1.name + " rendezte a(z) " + str(dancer1.category.value) + " Ft tartozását!\n")
                            dancer1.entryFeePaid = True

                        # fájlban átírás
                        with open("hiphop.txt", "r") as f:
                            get_all = f.readlines()

                        with open("hiphop.txt", 'w') as f:
                            for i, line in enumerate(get_all, 0):
                                if i == personIndex:
                                    f.writelines(
                                        dancer1.name + "\t" + str(dancer1.category) + "\t" + str(dancer1.entryFeePaid)
                                        + "\t" + str(dancer1.subscoreTechnique) + "\t" + str(
                                            dancer1.subscoreStyle) + "\t" + str(dancer1.score) + "\n")
                                else:
                                    f.writelines(line)


                elif styleSelect == 2: # contemporary
                    print("A nyilvántartásban szereplő versenyzők:", contemporaryNames)
                    name = input("Adja meg a táncos / formáció nevét, aki a befizetést tette! ")
                    for element in contemporary:
                        if name == element[0]:
                            dancer1 = Contemporary(element[0], element[1], element[2], element[3], element[4], element[5])
                            personIndex = contemporary.index(element)
                        else:
                            tester += 1
                    if tester == len(contemporary):
                        print("Nincs ilyen versenyző a nyilvántartásban!")
                        tester = 0

                    else:
                        if dancer1.entryFeePaid == True:
                            print("A versenyző már befizette a nevezési díjat!\n")
                        else:
                            print(dancer1.name + "rendezte a(z) " + str(dancer1.category.value) + " Ft tartozását!\n")
                            dancer1.entryFeePaid = True

                        # fájlban átírás
                        with open("contemporary.txt", "r") as f:
                            get_all = f.readlines()

                        with open("contemporary.txt", 'w') as f:
                            for i, line in enumerate(get_all, 0):
                                if i == personIndex:
                                    f.writelines(
                                        dancer1.name + "\t" + str(dancer1.category) + "\t" + str(dancer1.entryFeePaid)
                                        + "\t" + str(dancer1.subscoreTechnique) + "\t" + str(
                                            dancer1.subscoreCreativity) + "\t" + str(dancer1.score) + "\n")
                                else:
                                    f.writelines(line)


        elif type(tempStyle) == int:
           print("Hibás adatmegadás, kérem a megfelelő egész számot írja be a stílus kiválasztásához!")

def winner(hiphop: list, contemporary: list) -> None:
    """
    A versenyzők közül a legnagyobb pontszámmal rendelkezők nevét megadja
    :param hiphop: Az eddig felvitt hiphop táncosok adatait tartalmazó lista.
    :param contemporary: Az eddig felvitt kortárs táncosok adatait tartalmazó lista.
    :return: Megadja mindkét stílusban a legtöbb pontszámmal rendelkezők nevét (void)
    """

    hiphopScores = []
    contemporaryScores = []
    for i in range(len(hiphop)):
        hiphopScores.append(hiphop[i][5])

    for i in range(len(contemporary)):
        contemporaryScores.append(contemporary[i][5])

    maxHiphop = max(hiphopScores)
    for i in range(len(hiphop)):
        if hiphop[i][5] == maxHiphop:
            print("A hiphop kategória nyertese(i): " + hiphop[i][0])

    maxContemporary = max(contemporaryScores)
    for i in range(len(contemporary)):
        if contemporary[i][5] == maxContemporary:
            print("A kortárs kategória nyertese(i): " + contemporary[i][0])

    print("\n")



# main

print("Üdvözlöm a IX. Országos Tánckupa nyilvántartó programjában.\n")

menu = ""
fileHipHop = "hiphop.txt"
fileContemporary = "contemporary.txt"
hiphop = listUpload(fileHipHop)
contemporary = listUpload(fileContemporary)

while menu != "0":
    menu_options()
    menu = input()

    if menu == "1":
        newCompetitor(hiphop, contemporary)
        hiphop = ()
        contemporary = ()
        hiphop = listUpload(fileHipHop)
        contemporary = listUpload(fileContemporary)


    elif menu == "2":
        audienceAward(hiphop, contemporary)
        hiphop = listUpload(fileHipHop)
        contemporary = listUpload(fileContemporary)

    elif menu == "3":
        entryFee(hiphop, contemporary)
        hiphop = listUpload(fileHipHop)
        contemporary = listUpload(fileContemporary)

    elif menu == "4":
        winner(hiphop, contemporary)
        hiphop = listUpload(fileHipHop)
        contemporary = listUpload(fileContemporary)

    elif menu == "0":
        break

    else:
        print("Hibás menüpontot adott meg.")