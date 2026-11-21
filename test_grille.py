from grille import Grille
from bateau import Bateau

def test_init():
    g = Grille(2, 3)
    assert g.lignes == 2
    assert g.colonnes == 3
    assert g.vide == "~"
    assert g.cases == ["~", "~", "~", "~", "~", "~"]


def test_tirer():
    g = Grille(2, 3)
    g.tirer(1, 2)
    assert g.cases == ["~", "~", "~", "~", "~", "x"]

def test_str():
    g = Grille(5, 8)
    vide = "~~~~~~~~"
    assert str(g) == "\n".join([vide, vide, vide, vide, vide])

    g.tirer(2, 3)
    assert str(g) == "\n".join([vide, vide, "~~~x~~~~", vide, vide])

def test_tirer_hors_grille():
    g = Grille(2, 3)
    assert g.tirer(0, 3) is False   # colonne trop grande
    assert g.tirer(2, 0) is False   # ligne trop grande
    assert g.tirer(-1, 0) is False  # négatif
    assert g.cases == ["~"] * 6     # rien n'a changé

def test_ajoute():
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=False))
    assert g.cases == ["~", "~", "~", "⛵", "⛵", "~"]


def test_ajoute_refuse_si_depasse():
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=True))
    g.ajoute(Bateau(1, 0, longueur=4, vertical=True))
    assert g.cases == ["~", "~", "~", "~", "~", "~"]


def test_tirer_avec_touche_personnalisee():
    g = Grille(2, 3)
    g.tirer(0, 1, touche="💣")
    assert g.cases == ["~", "💣", "~", "~", "~", "~"]

def test_ajoute_refuse_le_chevauchement():
    g = Grille(2, 3)
    assert g.ajoute(Bateau(0, 0, longueur=2)) is True
    avant = list(g.cases)
    assert g.ajoute(Bateau(0, 1, longueur=2)) is False  # la case (0, 1) est prise
    assert g.cases == avant