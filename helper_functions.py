from classes import *


def category_select() -> Category:
    """
    Segédfüggvény a kategória kiválasztásához. Integer megadásával visszaadja a választott kategóriát.
    :return: A kiválasztott kategória enumot adja vissza
    """

    value = 0
    while value == 0:
        try:
            temp = int(input("Adja a kategória számát! (1 - solo, 2 - duo, 3 - csapat) "))
            if 3 >= temp >= 1:
                value = temp
            else:
                print("\nHibás adatmegadás, kérem a megfelelő egész számot írja be a kategória kiválasztásához!\n")
        except ValueError:
            print("\nHibás adatmegadás, kérem a megfelelő egész számot írja be a kategória kiválasztásához!\n")

        if value == 1:
            return Category.SOLO
        elif value == 2:
            return Category.DUO
        elif value == 3:
            return Category.TEAM


def entry_fee_select() -> bool:
    """
    Segédfüggvény, mellyel kiválaszthatjuk, hogy a nevezési díjat kifizette-e a versenyző vagy nem
    :return: True ha kifizette, false ha nem fizette ki
    """

    value = 0
    while value == 0:
        try:
            temp = int(input("Adja, hogy a versenyző kifizette-e a nevezési díjat! "
                             "(1 - nincs kifizetve, 2 - ki van fizetve) "))
            if 2 >= temp >= 1:
                value = temp
            else:
                print("\nHibás adatmegadás, kérem a megfelelő egész számot írja be a kiválasztáshoz!\n")
        except ValueError:
            print("\nHibás adatmegadás, kérem a megfelelő egész számot írja be a kiválasztásához!\n")

        if value == 1:
            return False
        elif value == 2:
            return True


def score_select() -> int:
    """
    Segédfüggvény, mellyel megadhatjuk a pontokat egy 0-10-ig tartó skálán
    :return: A pontszám
    """

    value = -1
    while value == -1:
        try:
            temp = int(input("Adja meg a pontszámot (0 - 10-ig) "))
            if 10 >= temp >= 0:
                value = temp
            else:
                print("\nNem 0-10 közötti értéket adott meg!\n")
        except ValueError:
            print("\nHibás adatmegadás, kérem egész számot írjon be!\n")

    return value


def list_upload(filepath: str) -> list:
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
            temp_category = Category.SOLO
        elif adat[1] == "Category.DUO":
            temp_category = Category.DUO
        else:
            temp_category = Category.TEAM

        temp_entry_fee = False

        if adat[2] == "True":
            temp_entry_fee = True
        elif adat[2] == "False":
            temp_entry_fee = False
        dancer_list = [adat[0], temp_category, temp_entry_fee, int(adat[3]), int(adat[4]), int(adat[5])]
        dancers_list.append(dancer_list)

    file.close()
    return dancers_list
