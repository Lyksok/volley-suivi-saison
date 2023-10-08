import ffvolleyAPI as ff


def main():
    resp = ""
    while resp != "0":
        print("Que voulez-vous faire ?")
        print("0. Quitter")
        print("1. Ajouter un score")
        print("2. Visualiser les scores")
        print("3. Graphique de saison")
        resp = input("\nVotre choix: ")

        if (resp == "0"):
            break
        elif (resp=="1"):
            ff.addScore()

    print("Fermeture de l'application ...")
    return


if __name__ == '__main__':
    main()
