from random import randint
 
MY_PV = 50
HIS_PV = 50
nbre_de_potions = 3

print("-" * 50)
print("Affrontes ton ennemi dans un duel sans merci !\nChoisis de l'attaquer ou de prendre une potion.\nAttention !\nPrendre une potion te fera passer un tour !\nBonne chance !")
print("-" * 50)

while MY_PV > 0 and HIS_PV > 0 :
    players_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    if players_choice == "1" :
        mes_dégats = randint(5, 10)
        dégats_ennemis = randint(5, 15)
        MY_PV -= dégats_ennemis
        HIS_PV -= mes_dégats
        print(f"Vous avez infligé {mes_dégats} points de dégats à l'ennemi. ⚔️\nL'ennemi vous a infligé {dégats_ennemis} points de dégats. ⚔️")
        if MY_PV <= 0 or HIS_PV <= 0 :
            break
        else :
            print(f"Il vous reste {MY_PV} points de vie.♥️\nIl reste {HIS_PV} points de vie à l'ennemi. ♥️")
        print("-" * 50)
    elif players_choice == "2" :
        if nbre_de_potions == 0 :
            print("Vous n'avez plus de potions !")
            print("-" * 50)
        else :
            potion = randint(15, 50)
            MY_PV += potion
            print(f"Vous récupérez {potion} points de vie. ♥️")
            nbre_de_potions -=1
            print(f"Il vous reste {nbre_de_potions} potions 🧪")
            dégats_ennemis = randint(5, 15)
            MY_PV -= dégats_ennemis
            print(f"L'ennemi vous a infligé {dégats_ennemis} points de dégats. ⚔️\nIl vous reste {MY_PV} points de vie. ♥️\nIl reste {HIS_PV} points de vie à l'ennemi. ♥️")
            print("-" * 50)
            print("Vous passez votre tour...")
            dégats_ennemis_2 = randint(5, 15)
            MY_PV -= dégats_ennemis_2
            print(f"L'ennemi vous a infligé {dégats_ennemis_2} points de dégats. ⚔️\nIl vous reste {MY_PV} points de vie. ♥️\nIl reste {HIS_PV} points de vie à l'ennemi. ♥️")
            print("-" * 50)
    else :
        print("Erreur de saisie, veuillez choisir 1 ou 2.")
if HIS_PV <= 0 : 
    print("L'ennemi est vaincu !\nBravo ! Vous avez gagné ! 🏆")
    print("Fin du jeu")

if MY_PV <= 0 : 
    print("L'ennemi vous a terrassé !\nVous avez perdu ! 🪦")
    print("Fin du jeu")
