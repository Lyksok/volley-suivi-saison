from ._scoreInput import scoreInput
from ._jsonInteraction import getTeams, getData, setData


def addScore():
    for i, v in getTeams().items():
        print(f"{i}. {v}")

    r = input("Choisi le rang du match: ")

    t1 = input("Choisi le numéro de la première équipe: ")
    t2 = input("Choisi le numéro de la deuxième équipe: ")
    print("Création de l'indice de jeu ...")
    st = f"{t1}v{t2}"

    scores = scoreInput()
    print("Les scores ont bien été pris en compte ...")

    data = getData()
    print("Retrait des anciennes données effectué ...")

    data["matchs"][r][st] = scores
    print("Indexage des scores avec l'indice de jeu ...")

    setData(data)
    print("Les scores ont bien été enregistrés !")
    return True
