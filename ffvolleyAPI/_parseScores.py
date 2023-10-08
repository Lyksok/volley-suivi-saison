def parseScores(teams: dict, tag: str,semaine:str, match: str):
    scores = match.split("/")
    t1, t2 = tag.split("v")

    s1, s2 = 0, 0

    for score in scores:
        p1, p2 = list(map(int, score.split("-")))

        teams[t1][semaine]["ptsG"] += p1
        teams[t2][semaine]["ptsG"] += p2
        teams[t1][semaine]["ptsP"] += p2
        teams[t2][semaine]["ptsP"] += p1

        if p1 > p2:
            s1 += 1
        else:
            s2 += 1

    teams[t1][semaine]["setG"] += s1
    teams[t2][semaine]["setG"] += s2

    if (s1, s2) in [(3, 0), (3, 1)]:
        teams[t1][semaine]["pts"] += 3

    elif (s1, s2) == (3, 2):
        teams[t1][semaine]["pts"] += 2
        teams[t2][semaine]["pts"] += 1

    elif (s1, s2) == (2, 3):
        teams[t1][semaine]["pts"] += 1
        teams[t2][semaine]["pts"] += 2

    elif (s1, s2) in [(0, 3), (1, 3)]:
        teams[t2][semaine]["pts"] += 3

    else:
        print(f"ERREUR: scores invalides pour le match {tag} de la semaine {semaine}")