"""
Floristic Gardening Planning Tool

"""

import random
import typing


def ermittlePflegehinweis(einPflanzenbild) -> str:
    choice = mylist = ["010", "010", "001", "000", "002", "002", "010", "020", "021", "030", "031"]

    code = random.choice(mylist)
    return f"Code {code} :: {allePflegehinweise()[code]}"


def allePflegehinweise() -> dict:
    """
    dies sind Pflegehinweise
    alle oder einer
    """

    pflegehinweise = {'000': 'Systemausfall', '999': 'Antwortzeit zu lang'}
    # Bodenfeuchtigkeit
    pflegehinweise['001'] = f"Pflanze zu trocken, bitte wässern"
    pflegehinweise['002'] = f"Pflanze zu nass, nicht mehr wässern"
    # Dünger
    pflegehinweise['010'] = f"Pflanze fehlen Nährstoffe, bitte düngen"

    # Luftqualität
    pflegehinweise['020'] = f"Pflanze benötigt mehr Luftfeuchtigkeit"
    pflegehinweise['021'] = f"Pflanze benötigt weniger Luftfeuchtigkeit"

    # Licht
    pflegehinweise['030'] = f"Pflanze benötigt mehr UV-Licht"
    pflegehinweise['031'] = f"Pflanze benötigt weniger UV-Licht"

    return pflegehinweise


if __name__ == '__main__':
    print(ermittlePflegehinweis("kein Bild"))
    print(ermittlePflegehinweis("kein Bild"))