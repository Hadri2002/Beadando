from helper_functions import *


def new_competitor(hiphop_list: list, contemporary_list: list) -> None:
    """
    Új versenyző felvételére használható függvény, melyben a megfelelő adatokat először egy osztály példányába
    elmentjük, majd a fájlba kiiratjuk
    :param hiphop_list: Az eddig felvitt hiphop_list táncosok adatait tartalmazó lista.
    :param contemporary_list: Az eddig felvitt hiphop_list táncosok adatait tartalmazó lista.
    :return: felveszi az új versenyzőt az adatbázisba (void függvény)
    """

    style_select = 0
    name = ""
    while style_select == 0:
        try:
            temp_style = int(input(
                "Adja meg, hogy melyik stílusban szeretne felvenni egy új versenyzőt! (1 - hiphop, 2 - kortárs) "))
            if temp_style == 1 or temp_style == 2:
                style_select = temp_style
            else:
                print("\nHibás adatmegadás, kérem a megfelelő egész számot írja be a stílus kiválasztásához!\n")
        except ValueError:
            print("\nHibás adatmegadás, kérem a megfelelő egész számot írja be a stílus kiválasztásához!\n")

    if style_select == 1:  # hiphop_list

        # versenyző adatainak felvétele
        while name == "":
            tester = 0
            temp_name = input("Adja meg a táncos/formáció nevét! ")
            for element in hiphop_list:
                if temp_name == element[0]:
                    print("\nMár van ilyen nevű versenyző!\n")
                    tester += 1
            if tester == 0:
                name = temp_name

        category = category_select()
        entry_fee_paid = entry_fee_select()
        print("A technikához kapcsolódó pontszám felvétele: ")
        subscore_technique = score_select()
        print("A stílushoz kapcsolódó pontszám felvétele: ")
        subscore_style = score_select()
        dancer1 = HipHop(name, category, entry_fee_paid, subscore_technique, subscore_style)

        # versenyző adatainak fájlbaírása
        f = open("hiphop.txt", "a")
        f.write(dancer1.name + "\t" + str(dancer1.category) + "\t" + str(dancer1.entryFeePaid) + "\t" +
                str(dancer1.subscoreTechnique) + "\t" + str(dancer1.subscoreStyle) + "\t" + str(
            dancer1.score) + "\n")
        f.close()

        print("\nA felvétel sikeresen megtörtént!\n")

    elif style_select == 2:  # contemporary_list

        # versenyző adatainak felvétele
        while name == "":
            tester = 0
            temp_name = input("Adja meg a táncos/formáció nevét! ")
            for element in contemporary_list:
                if temp_name == element[0]:
                    print("\nMár van ilyen nevű versenyző!\n")
                    tester += 1
            if tester == 0:
                name = temp_name

        category = category_select()
        entry_fee_paid = entry_fee_select()
        print("A technikához kapcsolódó pontszám felvétele: ")
        subscore_technique = score_select()
        print("A kreativitáshoz kapcsolódó pontszám felvétele: ")
        subscore_creativity = score_select()
        dancer1 = Contemporary(name, category, entry_fee_paid, subscore_technique, subscore_creativity)

        # versenyző adatainak fájlbaírása
        f = open("contemporary.txt", "a")
        f.write(dancer1.name + "\t" + str(dancer1.category) + "\t" + str(dancer1.entryFeePaid) + "\t" +
                str(dancer1.subscoreTechnique) + "\t" + str(dancer1.subscoreCreativity) + "\t" + str(
            dancer1.score) + "\n")
        f.close()

        print("\nA felvétel sikeresen megtörtént!\n")


def audience_award(hiphop_list: list, contemporary_list: list) -> None:
    """
    A versenyzők számára közönségdíjat hagyhatunk jóvá a függvénnyel. Minden versenyző maximum egyszer kaphat plusz
    pontot a közönségdíj alapján
    :param hiphop_list: Az eddig felvitt hiphop_list táncosok adatait tartalmazó lista.
    :param contemporary_list: Az eddig felvitt kortárs táncosok adatait tartalmazó lista.
    :return: A megadott versenyzőhöz tartozó pontszámot megváltoztatja, majd azt az adatbázisban is átírja
    """

    print("Az alábbi menüpont segítségével a közönségdíjat írhatja jóvá a választott táncos számára!")
    style_select = 0
    person_index = 0

    hiphop_names = []
    contemporary_names = []
    for element in hiphop_list:
        hiphop_names.append(element[0])
    for element in contemporary_list:
        contemporary_names.append(element[0])

    while style_select == 0:
        try:
            temp_style = int(input("Adja meg, hogy melyik stílusban szerepel a versenyző, akinek jóváírná a "
                                   "közönségdíjért járó plusz pontot! (1 - hiphop, 2 - kortárs) "))
            if temp_style == 1 or temp_style == 2:
                style_select = temp_style
            else:
                print("\nHibás adatmegadás, kérem a megfelelő egész számot írja be a stílus kiválasztásához!\n")
        except ValueError:
            print("\nHibás adatmegadás, kérem a megfelelő egész számot írja be a stílus kiválasztásához!\n")

    tester = 0
    while tester == 0:
        if style_select == 1:  # hiphop_list
            dancer1 = HipHop("", Category.SOLO)
            print("\nA nyilvántartásban szereplő versenyzők:", hiphop_names, "\n")
            name = input("Adja meg a táncos / formáció nevét, akinek a közönségdíjat jóvá szeretné hagyni! ")

            for element in hiphop_list:
                if name == element[0]:
                    dancer1 = HipHop(element[0], element[1], element[2], element[3], element[4], element[5])
                    person_index = hiphop_list.index(element)
                else:
                    tester += 1
            if tester == len(hiphop_list):
                print("\nNincs ilyen versenyző a nyilvántartásban!\n")
                tester = 0

            else:
                dancer1.audience_award()  # pont jóváírása

                # adat megváltoztatása a fájlban
                with open("hiphop.txt", "r") as f:
                    get_all = f.readlines()

                with open("hiphop.txt", 'w') as f:
                    for i, line in enumerate(get_all, 0):
                        if i == person_index:
                            f.writelines(dancer1.name + "\t" + str(dancer1.category) + "\t" +
                                         str(dancer1.entryFeePaid)
                                         + "\t" + str(dancer1.subscoreTechnique) + "\t" +
                                         str(dancer1.subscoreStyle) + "\t" + str(dancer1.score) + "\n")
                        else:
                            f.writelines(line)

        elif style_select == 2:  # kortárs
            dancer1 = Contemporary("", Category.SOLO)
            print("\nA nyilvántartásban szereplő versenyzők:", contemporary_names, "\n")
            name = input("Adja meg a táncos / formáció nevét, akinek a közönségdíjat jóvá szeretné hagyni! ")
            for element in contemporary_list:
                if name == element[0]:
                    dancer1 = Contemporary(element[0], element[1], element[2], element[3], element[4],
                                           element[5])
                    person_index = contemporary_list.index(element)
                else:
                    tester += 1
            if tester == len(contemporary_list):
                print("\nNincs ilyen versenyző a nyilvántartásban!\n")
                tester = 0

            else:
                dancer1.audience_award()  # pont jóváírása

                # adat megváltoztatása a fájlban
                with open("contemporary.txt", "r") as f:
                    get_all = f.readlines()

                with open("contemporary.txt", 'w') as f:
                    for i, line in enumerate(get_all, 0):
                        if i == person_index:
                            f.writelines(
                                dancer1.name + "\t" + str(dancer1.category) + "\t" + str(dancer1.entryFeePaid)
                                + "\t" + str(dancer1.subscoreTechnique) + "\t" + str(
                                    dancer1.subscoreCreativity) + "\t" + str(dancer1.score) + "\n")
                        else:
                            f.writelines(line)


def entry_fee(hiphop_list: list, contemporary_list: list) -> None:
    """
    Amennyiben a vizsgált versenyző nem fizette be a nevezési díjat azt befizetetté teszi, ha pedig már befizette akkor
    nem történik változás
    :param hiphop_list:
    :param contemporary_list:
    :return:
    """

    style_select = 0
    person_index = 0

    hiphop_names = []
    contemporary_names = []
    for element in hiphop_list:
        hiphop_names.append(element[0])
    for element in contemporary_list:
        contemporary_names.append(element[0])

    while style_select == 0:
        try:
            temp_style = int(input(
                "Adja meg, hogy melyik stílusban szerepel a versenyző, aki a nevezési díj befizetést tette! "
                "(1 - hiphop, 2 - kortárs) "))
            if temp_style == 1 or temp_style == 2:
                style_select = temp_style
            else:
                print("\nHibás adatmegadás, kérem a megfelelő egész számot írja be a stílus kiválasztásához!\n")
        except ValueError:
            print("\nHibás adatmegadás, kérem a megfelelő egész számot írja be a stílus kiválasztásához!\n")

    tester = 0
    while tester == 0:

        if style_select == 1:  # hiphop_list
            dancer1 = HipHop("", Category.SOLO)
            print("\nA nyilvántartásban szereplő versenyzők: " + str(hiphop_names) + "\n")
            name = input("Adja meg a táncos / formáció nevét, aki a befizetést tette! ")
            for element in hiphop_list:
                if name == element[0]:
                    dancer1 = HipHop(element[0], element[1], element[2], element[3], element[4], element[5])
                    person_index = hiphop_list.index(element)
                else:
                    tester += 1
            if tester == len(hiphop_list):
                print("\nNincs ilyen versenyző a nyilvántartásban!\n")
                tester = 0

            else:
                if dancer1.entryFeePaid is True:
                    print("\nA versenyző már befizette a nevezési díjat!\n")
                else:
                    print("\n" + dancer1.name + " rendezte a(z) " + str(dancer1.category.value) +
                          " Ft tartozását!\n")
                    dancer1.entryFeePaid = True

                # fájlban átírás
                with open("hiphop.txt", "r") as f:
                    get_all = f.readlines()

                with open("hiphop.txt", 'w') as f:
                    for i, line in enumerate(get_all, 0):
                        if i == person_index:
                            f.writelines(
                                dancer1.name + "\t" + str(dancer1.category) + "\t" + str(dancer1.entryFeePaid)
                                + "\t" + str(dancer1.subscoreTechnique) + "\t" + str(
                                    dancer1.subscoreStyle) + "\t" + str(dancer1.score) + "\n")
                        else:
                            f.writelines(line)

        elif style_select == 2:  # contemporary_list
            dancer1 = Contemporary("", Category.SOLO)
            print("\nA nyilvántartásban szereplő versenyzők: " + str(contemporary_names) + "\n")
            name = input("Adja meg a táncos / formáció nevét, aki a befizetést tette! ")
            for element in contemporary_list:
                if name == element[0]:
                    dancer1 = Contemporary(element[0], element[1], element[2], element[3], element[4],
                                           element[5])
                    person_index = contemporary_list.index(element)
                else:
                    tester += 1
            if tester == len(contemporary_list):
                print("\nNincs ilyen versenyző a nyilvántartásban!\n")
                tester = 0

            else:
                if dancer1.entryFeePaid is True:
                    print("\nA versenyző már befizette a nevezési díjat!\n")
                else:
                    print(dancer1.name + " rendezte a(z) " + str(dancer1.category.value) + " Ft tartozását!\n")
                    dancer1.entryFeePaid = True

                # fájlban átírás
                with open("contemporary.txt", "r") as f:
                    get_all = f.readlines()

                with open("contemporary.txt", 'w') as f:
                    for i, line in enumerate(get_all, 0):
                        if i == person_index:
                            f.writelines(
                                dancer1.name + "\t" + str(dancer1.category) + "\t" + str(dancer1.entryFeePaid)
                                + "\t" + str(dancer1.subscoreTechnique) + "\t" + str(
                                    dancer1.subscoreCreativity) + "\t" + str(dancer1.score) + "\n")
                        else:
                            f.writelines(line)


def winner(hiphop_list: list, contemporary_list: list) -> None:
    """
    A versenyzők közül a legnagyobb pontszámmal rendelkezők nevét megadja
    :param hiphop_list: Az eddig felvitt hiphop_list táncosok adatait tartalmazó lista.
    :param contemporary_list: Az eddig felvitt kortárs táncosok adatait tartalmazó lista.
    :return: Megadja mindkét stílusban a legtöbb pontszámmal rendelkezők nevét (void)
    """

    hiphop_scores = []
    contemporary_scores = []
    for i in range(len(hiphop_list)):
        hiphop_scores.append(hiphop_list[i][5])

    for i in range(len(contemporary_list)):
        contemporary_scores.append(contemporary_list[i][5])

    print("\n")

    max_hiphop = max(hiphop_scores)
    for i in range(len(hiphop_list)):
        if hiphop_list[i][5] == max_hiphop:
            print("A hiphop kategória nyertese(i): " + hiphop_list[i][0])

    max_contemporary = max(contemporary_scores)
    for i in range(len(contemporary_list)):
        if contemporary_list[i][5] == max_contemporary:
            print("A kortárs kategória nyertese(i): " + contemporary_list[i][0])

    print("\n")
