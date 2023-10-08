import json


def getTeams() -> dict:
    """
    Renvoie le nom de toutes les équipes avec un indice associé
    :rtype: dict
    """
    with open("data.json", "r") as f:
        data = json.load(f)
        data: dict = data["equipes"]

    return data


def getData() -> dict:
    """
        Renvoie l'ensemble des données
        :rtype: dict
        """
    with open("data.json", "r") as f:
        data = json.load(f)

    return data


def setData(new_data) -> bool:
    """
    Réécris les données avec les nouvelles données
    :rtype: bool
    """
    with open("data.json", "w") as f:
        json.dump(new_data, f)

    return True
