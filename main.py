from main_functions import *


def menu_options():
    """
    A menüpontok kiírására alkalmas függvény
    """

    print("Válasszon az alábbi menüpontok közül:\n\t0 - Kilépés"
          "\n\t1 - Új versenyző felvétele"
          "\n\t2 - Közönségdíj jóváírása"
          "\n\t3 - Nevezési díj befizetés"
          "\n\t4 - Nyertes lekérése")


print("\nÜdvözlöm a IX. Országos Tánckupa nyilvántartó programjában.\n")

menu = ""
fileHipHop = "hiphop.txt"
fileContemporary = "contemporary.txt"
hiphop = list_upload(fileHipHop)
contemporary = list_upload(fileContemporary)

while menu != "0":
    menu_options()
    menu = input()

    if menu == "1":
        new_competitor(hiphop, contemporary)
        hiphop = list_upload(fileHipHop)
        contemporary = list_upload(fileContemporary)

    elif menu == "2":
        audience_award(hiphop, contemporary)
        hiphop = list_upload(fileHipHop)
        contemporary = list_upload(fileContemporary)

    elif menu == "3":
        entry_fee(hiphop, contemporary)
        hiphop = list_upload(fileHipHop)
        contemporary = list_upload(fileContemporary)

    elif menu == "4":
        winner(hiphop, contemporary)
        hiphop = list_upload(fileHipHop)
        contemporary = list_upload(fileContemporary)

    elif menu == "0":
        break

    else:
        print("\nHibás menüpontot adott meg, adja meg a megfelelő egész számot!\n")
