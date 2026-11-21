import os
import random
import sys

from termcolor import cprint

from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

LIGNES = 8
COLONNES = 10


def placer_bateaux(grille):
    bateaux = []
    for type_de_bateau in [PorteAvion, Croiseur, Torpilleur, SousMarin]:
        possibles = []
        for ligne in range(grille.lignes):
            for colonne in range(grille.colonnes):
                for vertical in (False, True):
                    bateau = type_de_bateau(ligne, colonne, vertical)
                    if grille.peut_ajouter(bateau):
                        possibles.append(bateau)
        bateau = random.choice(possibles)
        grille.ajoute(bateau)
        bateaux.append(bateau)
    return bateaux


def demander_tir(public):
    while True:
        saisie = input("Votre tir (ligne colonne, ex : 3 5 ; q pour quitter) : ").strip()
        if saisie.lower() == "q":
            return None
        try:
            ligne, colonne = (int(mot) for mot in saisie.replace(",", " ").split())
        except ValueError:
            cprint("Entrez deux nombres entiers, par exemple : 3 5", "red")
            continue
        if not public.dans_la_grille(ligne, colonne):
            cprint("Cette case n'est pas dans la grille.", "red")
            continue
        if public.case(ligne, colonne) != public.vide:
            cprint("Vous avez déjà tiré ici !", "yellow")
            continue
        return ligne, colonne


def jouer():
    secret = Grille(LIGNES, COLONNES)
    public = Grille(LIGNES, COLONNES)
    bateaux = placer_bateaux(secret)
    coups = 0

    cprint("=== BATAILLE NAVALE ===", "cyan", attrs=["bold"])
    print(f"{len(bateaux)} bateaux sont cachés. Lignes 0 à {LIGNES - 1}, "
          f"colonnes 0 à {COLONNES - 1}.\n")

    while not all(bateau.coulé(secret) for bateau in bateaux):
        print(public.affichage())
        tir = demander_tir(public)
        if tir is None:
            cprint("Partie abandonnée.", "yellow")
            return
        ligne, colonne = tir
        coups += 1

        touche = None
        for bateau in bateaux:
            if (ligne, colonne) in bateau.positions():
                touche = bateau

        secret.tirer(ligne, colonne)

        if touche is None:
            public.tirer(ligne, colonne)
            cprint("Plouf... dans l'eau.", "blue")
        elif touche.coulé(secret):
            for l, c in touche.positions():
                public.tirer(l, c, touche=touche.marque)
            cprint(touche.message_coule, "yellow", attrs=["bold"])
        else:
            public.tirer(ligne, colonne, touche="💣")
            cprint("Touché !", "red", attrs=["bold"])
        print()

    print(public.affichage())
    cprint(f"Bravo, tous les bateaux sont coulés en {coups} coups !", "green", attrs=["bold"])


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if os.name == "nt":
        os.system("")
    jouer()