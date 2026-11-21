from termcolor import colored

class Grille:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.vide = "~"
        self.cases = [self.vide] * (lignes * colonnes)

    def dans_la_grille(self, ligne, colonne):
        return 0 <= ligne < self.lignes and 0 <= colonne < self.colonnes

    def case(self, ligne, colonne):
        return self.cases[ligne * self.colonnes + colonne]

    def tirer(self, ligne, colonne, touche="x"):
        if self.dans_la_grille(ligne, colonne):
            self.cases[ligne * self.colonnes + colonne] = touche
            return True
        return False

    def peut_ajouter(self, bateau):
        for ligne, colonne in bateau.positions():
            if not self.dans_la_grille(ligne, colonne):
                return False
            if self.case(ligne, colonne) != self.vide:
                return False
        return True

    def ajoute(self, bateau):
        if not self.peut_ajouter(bateau):
            return False
        for ligne, colonne in bateau.positions():
            self.cases[ligne * self.colonnes + colonne] = bateau.marque
        return True

    def __str__(self):
        lignes = []
        for ligne in range(self.lignes):
            debut = ligne * self.colonnes
            fin = debut + self.colonnes
            lignes.append("".join(self.cases[debut:fin]))
        return "\n".join(lignes)

    def affichage(self):
        couleurs = {"~": "blue", "x": "white", "💣": "red"}
        sortie = ["   " + "".join(f"{c:<3}" for c in range(self.colonnes))]
        for ligne in range(self.lignes):
            texte = f"{ligne:>2} "
            for colonne in range(self.colonnes):
                caractere = self.case(ligne, colonne)
                if caractere in ("~", "x"):
                    espaces = "  "
                else:
                    espaces = " "
                texte += colored(caractere, couleurs.get(caractere, "green")) + espaces
            sortie.append(texte)
        return "\n".join(sortie)