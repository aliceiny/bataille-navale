from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin
from grille import Grille

def test_init_par_defaut():
    b = Bateau(2, 3)
    assert b.ligne == 2
    assert b.colonne == 3
    assert b.longueur == 1
    assert b.vertical is False

def test_init_avec_valeurs():
    b = Bateau(0, 1, longueur=4, vertical=True)
    assert b.longueur == 4
    assert b.vertical is True

def test_positions_horizontal():
    assert Bateau(2, 3, longueur=3).positions() == [(2, 3), (2, 4), (2, 5)]


def test_positions_vertical():
    assert Bateau(2, 3, longueur=3, vertical=True).positions() == [(2, 3), (3, 3), (4, 3)]

def test_positions_defaut():
    assert Bateau(0, 0).positions() == [(0, 0)]

def test_coulé():
    g = Grille(2, 3)
    b = Bateau(1, 0, longueur=2)
    g.ajoute(b)
    assert b.coulé(g) is False

    g.tirer(1, 0)
    assert b.coulé(g) is False   

    g.tirer(1, 1)
    assert b.coulé(g) is True   

def test_types_de_bateaux():
    p = PorteAvion(0, 0)
    assert p.longueur == 4
    assert p.marque == "🚢"
    assert p.vertical is False
    assert Croiseur(0, 0).longueur == 3
    assert Torpilleur(0, 0).longueur == 2
    assert SousMarin(0, 0, True).longueur == 2
    assert SousMarin(0, 0, True).vertical is True


def test_le_type_est_pris_en_compte_dans_la_grille():
    g = Grille(3, 5)
    g.ajoute(Croiseur(0, 0))
    g.ajoute(SousMarin(1, 0, vertical=True))
    assert g.cases[0:3] == ["⛴", "⛴", "⛴"]
    assert g.cases[5] == "🐟"
    assert g.cases[10] == "🐟"