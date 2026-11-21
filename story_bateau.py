from bateau import Bateau

# Premier jeu
b1 = Bateau(2, 3, longueur=3)
b2 = Bateau(1, 4, longueur=3, vertical=True)
communes = set(b1.positions()) & set(b2.positions())
print("Cases communes :", communes)
if communes:
    print("Les bateaux se chevauchent")
else:
    print("Les bateaux ne se chevauchent pas")

# Deuxième jeu
b1 = Bateau(2, 3, longueur=3)
b2 = Bateau(0, 0, longueur=2, vertical=True)
communes = set(b1.positions()) & set(b2.positions())
print("Cases communes :", communes)
if communes:
    print("Les bateaux se chevauchent")
else:
    print("Les bateaux ne se chevauchent pas")