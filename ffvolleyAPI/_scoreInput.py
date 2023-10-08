import re


def scoreInput() -> str:
    """

    :rtype: str
    """
    score_pattern = r"^(?:[1-9]|[1-9][0-9])-(?:[1-9]|[1-9][0-9])$"

    scores = []
    print("Entrez les scores sous la forme score1-score2 (écrire FIN pour arrêter)")
    i = 1
    while (score_input := input(f"Score pour set n°{i}: ")) != "FIN":
        if re.match(score_pattern, score_input):
            scores.append(score_input)
            if i == 5:
                break
            else:
                i += 1
        else:
            print("ERREUR: mauvais format -> score1-score2")

    return "/".join(scores)
