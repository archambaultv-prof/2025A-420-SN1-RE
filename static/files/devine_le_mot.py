import random

# Liste des mots possibles pour le jeu
mots = ["python", "programmation", "ordinateur", "developpeur"]
# Choisir un mot au hasard dans la liste
mot_secret = random.choice(mots)

# Variable pour stocker les lettres déjà trouvées par l'utilisateur
lettres_trouvees = ""
# Compteur d'erreurs (maximum 8 erreurs autorisées)
nb_erreur = 0

# Boucle principale du jeu - continue tant qu'on n'a pas dépassé 8 erreurs
while nb_erreur < 8:
    # Variable pour afficher le mot avec les lettres trouvées et les _ pour les lettres manquantes
    pendule = ""
    # Variable booléenne pour vérifier si toutes les lettres ont été trouvées
    toutes_lettres_trouvees = True
    
    # Parcourir chaque lettre du mot secret
    for lettre in mot_secret:
        # Si la lettre a déjà été trouvée, l'afficher
        if lettre in lettres_trouvees:
            pendule = pendule + lettre + " "
        else:
            # Sinon, afficher un underscore et marquer qu'il reste des lettres à trouver
            pendule = pendule + "_ "
            toutes_lettres_trouvees = False

    # Si toutes les lettres ont été trouvées, le joueur a gagné !
    # On sort de la boucle principale avec l'instruction break
    if toutes_lettres_trouvees:
        print("Bravo !")
        break

    # Afficher l'état actuel du mot à deviner
    print(f"Mot a deviner : {pendule}")

    # Demander à l'utilisateur de saisir une lettre
    lettre_utilisateur = input("Entrez une lettre: ")

    # Vérifier si la lettre proposée est dans le mot secret
    lettre_dans_le_mot = False
    for lettre_courante in mot_secret:
        if lettre_utilisateur == lettre_courante:
            lettre_dans_le_mot = True

    # Traiter le résultat de la vérification
    if lettre_dans_le_mot:
        print("Bonne réponse !")
        # Si la lettre est correcte, l'ajouter aux lettres trouvées
        lettres_trouvees = lettres_trouvees + lettre_utilisateur
    else:
        print("Raté")
        # Si la lettre est incorrecte, incrémenter le compteur d'erreurs
        nb_erreur = nb_erreur + 1
