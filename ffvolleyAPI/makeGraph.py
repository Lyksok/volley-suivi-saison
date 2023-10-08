from ._timeRanking import timeRanking


def makeGraph():
    resp = ""

    while resp != "0":
        print("Quel type de graphe souhaitez-vous visualiser?")
        print("0. Retour")
        print("1. Classement au fil du temps")

        resp = input("\n Votre choix: ")

        if resp == "1":
            timeRanking()

    print()
