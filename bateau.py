class Bateau :
    marque = "⛵"
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self):
        resultat = []
        for i in range(self.longueur):
            if self.vertical:
                resultat.append((self.ligne + i, self.colonne))
            else:
                resultat.append((self.ligne, self.colonne + i))
        return resultat

    def coulé(self, grille):
        for ligne, colonne in self.positions():
            if grille.cases[ligne * grille.colonnes + colonne] != "x":
                return False
        return True

class PorteAvion(Bateau):
    marque = "🚢"
    message_coule = "Le porte-avion est coulé !"
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 4, vertical)


class Croiseur(Bateau):
    marque = "⛴"
    message_coule = "Le croiseur est coulé !"
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 3, vertical)


class Torpilleur(Bateau):
    marque = "🚣"
    message_coule = "Le torpilleur est coulé !"
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)


class SousMarin(Bateau):
    marque = "🐟"
    message_coule = "Le sous-marin est coulé !"
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)