import matplotlib.pyplot as plt
from ._jsonInteraction import getData, getTeams
from ._parseScores import parseScores


def __openScores(team_points, data) -> int:
    for semaine, matchs in data["matchs"].items():
        if matchs == {}:
            print(f"Valeur manquante pour semaine {semaine} ...")
            return int(semaine) - 1
        for team_index, scores in matchs.items():
            if scores == "":
                print(f"Valeur manquante pour semaine {semaine} ...")
            else:
                print(f"Ouverture des scores du match {team_index}")
                parseScores(team_points, team_index, semaine, scores)


def __sumRanks(team_points: dict, team: str, semaine: int) -> dict:
    team_sum = {"team": team, "pts": 0, "setG": 0, "ptsG": 0, "ptsP": 0}
    for i in range(1, semaine + 1):
        team_sum["pts"] += team_points[team][str(i)]["pts"]
        team_sum["setG"] += team_points[team][str(i)]["setG"]
        team_sum["ptsG"] += team_points[team][str(i)]["ptsG"]
        team_sum["ptsP"] += team_points[team][str(i)]["ptsP"]
    print(team_sum)
    return {"team": team, "pts": team_sum["pts"], "setG": team_sum["setG"],
            "average": team_sum["ptsG"] / team_sum["ptsP"]}


def __makeRank(team_points: dict, semaine: int) -> list:
    def custom_sort(d):
        return d["pts"], d["setG"], d["average"]

    list_of_teams = [__sumRanks(team_points, k, semaine) for k, _ in team_points.items()]
    return __assignRank(sorted(list_of_teams, key=custom_sort))


def __assignRank(l_of_teams: list) -> list:
    new_list = []
    for i in range(len(l_of_teams)):
        new_list.append({"rank": i, "team": l_of_teams[i]["team"], "setG": l_of_teams[i]["setG"],
                         "average": l_of_teams[i]["average"]})
    return new_list


def findTeamData(semaine: list, team) -> dict:
    for i in semaine:
        if i["team"] == team:
            return i


def __drawGraph(classements: list):
    x = [i for i in range(1, len(classements) + 1)]
    for team in getTeams().keys():
        y = []
        for semaine in classements:
            team_info = findTeamData(semaine, team)
            y.append(team_info["rank"])
        plt.plot(x, y, label=getTeams()[team])

    plt.xlabel("Semaines")
    plt.ylabel("Equipes")
    plt.legend()
    plt.title("Classement des équipes par classement chaque semaine")
    plt.plot()

def timeRankRanking():
    data = getData()
    teams = getTeams()

    print("Création du répertoire des points par équipe par semaine")
    team_points = dict()

    for index in teams.keys():
        team_points[index] = {str(i): {"pts": 0, "setG": 0, "ptsG": 0, "ptsP": 0} for i in range(1, 20)}

    print("Indexage de chaque points pour chaque équipe par semaine")
    semaine_max = __openScores(team_points, data)

    classements = []
    for semaine in range(1, semaine_max + 1):
        classements.append(__makeRank(team_points, semaine_max))
