import ffvolleyAPI as ff


def main():
    resp = ""
    while resp != "0":
        print("Que voulez-vous faire ?")
        print("0. Quitter")
        print("1. Ajouter un score")
        print("2. Visualiser les scores")
        print("3. Graphiques de saison")
        resp = input("\nVotre choix: ")

        if resp == "1":
            ff.addScore()
        if resp == "2":
            print("Cette fonctionnalitée n'est pas encore disponible :(")
        if resp == "3":
            ff.makeGraph()

    print("Fermeture de l'application ...")
    return


if __name__ == '__main__':
    main()
