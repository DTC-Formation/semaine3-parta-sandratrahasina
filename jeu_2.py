#Jeu 2: Devinez le nombre / multiplayers

#Générez un nombre aléatoire entre 1 et 100.
#Demandez à l'utilisateur de deviner le nombre.
#Comparez la réponse de l'utilisateur avec le nombre généré.
#Affichez des messages "Trop grand" ou "Trop petit" en fonction de la réponse de l'utilisateur.
#Répétez les étapes 2 à 4 jusqu'à ce que l'utilisateur devine correctement le nombre.

import random

my_random_number = random.randint(1, 100)

print(my_random_number)

print("Bienvenue dans ce jeu, veullez indiquer le nombre de participants s'il vous plait")

nombre_de_participant = input()

print("Vous serez "+nombre_de_participant+" à participer")

all_participant = []

index = 0

while  index < int(nombre_de_participant) : 
    print("Entrez le nom du participant n° "+str(index+1)+" ")
    nom_participant = input()
    this_participant = {"nom": nom_participant, "nombre_tentative": 0}
    print("vous pouver commencer à deviner le chiffe gagnant "+nom_participant)

    iterator = 0
    while iterator < 5 :
        this_participant["nombre_tentative"] = iterator + 1
        input_player = input()
        if(my_random_number < int(input_player)) :
            print(input_player + " est trop grand, reesayer")
        elif(my_random_number > int(input_player)) :
            print(input_player + " est trop petit, reesayer")
        else :
            print("felicitation vous avez trouvez le bon chiffre")
            break
        iterator = iterator + 1
    all_participant.append(this_participant)  
    index = index + 1

print("---------------------------------------------")
print("-------------le jeu est terminer-------------")
print("-----les resultats s'afficheront en bas------")
print("---------------------------------------------")

def printScore(participant):
    return participant["nom"] + " a fait " + str(participant["nombre_tentative"]) + " tentative"

result = list(map(printScore, all_participant))

for i in result :
    print("-" + i)

gagnant = all_participant[0]
for participant in all_participant :
    if(gagnant["nombre_tentative"] > participant["nombre_tentative"]) :
        gagnant = participant


print("Felicitation, le gangant est : " + gagnant["nom"])
