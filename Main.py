import random

def TestName(Name):
    if Name == "":
        return False
    for Character in Name:
        if (not Character.isalpha() 
            and Character != "-" 
            and Character != " "):
            return False
    return True

print()
print("Jeu de dés")
print("----------")
print()

print("Deux joueurs lancent chacun 2 dés (à 6 faces, lancement automatique par le programme)")
print("Celui des deux qui obtient le plus haut score est déclaré gagnant.")
print("En cas de scores égaux, ils sont déclarés ex aequo.")

print()
NomJoueur1 = ""
while not TestName(NomJoueur1):
    NomJoueur1 = input("Joueur 1, quel est ton nom ? ").strip()
NomJoueur2 = ""
while not TestName(NomJoueur2):
    NomJoueur2 = input("Joueur 2, quel est ton nom ? ").strip()

Tirage1 = random.randint(1, 6) + random.randint(1, 6)
Tirage2 = random.randint(1, 6) + random.randint(1, 6)

print()
print(NomJoueur1 + " a un score de " + str(Tirage1))
print(NomJoueur2 + " a un score de " + str(Tirage2))

print()
if Tirage1 > Tirage2:
    print(NomJoueur1 + " a gagné !")
elif Tirage2 > Tirage1:
    print(NomJoueur2 + " a gagné !")
else:
    print(NomJoueur1 + " et " + NomJoueur2 + " sont ex aequo.")
 
print()
print("Au revoir.")
