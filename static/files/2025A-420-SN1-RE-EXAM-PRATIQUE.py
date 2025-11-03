import numpy as np

###############################################################################
# 🏒 GO HABS GO 🏒
#
# Avant toute chose, désactivez l'intelligence artificielle dans PyCharm.
# Allez dans File > Settings > Tools > AI Assistant et décochez les cases.
###############################################################################

###############################################################################
# 🏒 GO HABS GO 🏒
#
# Ce fichier contient les consignes pour l'examen pratique du cours 420-SN1-RE
# à l'automne 2025 enseigné par Vincent Archambault-Bouffard.
#
#
# Instructions générales :
# 1. Vous avez 2 heures pour compléter cet examen pratique.
# 2. Vous devez travailler seul(e) et ne pas utiliser de ressources externes.
# 3. Vous écrivez votre code directement dans ce fichier en respectant les
#    consignes de chaque question. Écrire le code de chaque section directement
#    sous les consignes correspondantes.
# 4. L'examen comporte 3 sections pour un total de 100 points.
# 5. À la fin de l'examen, sauvegardez ce fichier et soumettez-le sur Omnivox.
#
# 
# Pour chaque section, les critères suivants seront évalués :
# - Fonctionnalité : Le code fonctionne-t-il comme prévu ?
# - Clarté : Le code est-il bien structuré et facile à comprendre ?
# - Utilisation des bibliothèques : Les bibliothèques appropriées sont-elles
#   utilisées correctement ?
# - Qualité du code : Le code suit-il les bonnes pratiques de programmation
#   (nom des variables, commentaires, etc.) ?
###############################################################################


###############################################################################
# 🏒 GO HABS GO 🏒
#
# Section 1 : Génération aléatoire de données (30 points)
#
# Instructions :
# 1. À l'aide de Numpy, écrire une fonction pour générer un tableau 2D de
#    dimensions 82 x 6 qui représente les statistiques des 82 parties d'une
#    saison de hockey pour les Canadiens de Montréal. Chaque ligne représente
#    une partie avec 6 colonnes :
#    - Buts marqués par les Canadiens en 1ère période
#    - Buts accordés par les Canadiens en 1ère période
#    - Buts marqués par les Canadiens en 2ème période
#    - Buts accordés par les Canadiens en 2ème période
#    - Buts marqués par les Canadiens en 3ème période
#    - Buts accordés par les Canadiens en 3ème période
# 2. Les buts marqués doivent être des entiers aléatoires entre 0 et 4.
# 3. Les buts accordés doivent être des entiers aléatoires entre 0 et 3.
#    ATTENTION PAS LE MÊME MAXIMUM QUE LES BUTS MARQUÉS!
# 4. La fonction se nomme generer_statistiques_saison et retourne le tableau
#    2D. Elle ne prend pas de paramètres.
# 5. Faites appel à cette fonction et affichez le tableau généré.
###############################################################################                                       
                                                                                                  
                                                                                                                     
                                                                                                                     
                                                                                                                     
                                                                                                                     
                             
                                                                                                                     
                                                                                                                     
###############################################################################
# 🏒 GO HABS GO 🏒
#
# Section 2 : Statistiques de la saison (35 points)
#
# Les analystes sportifs adorent les statistiques du genre "Les Canadiens ont
# gagné 8 fois l'an passé alors qu'ils tiraient de l'arrière après la 2e
# période". Nous allons donc calculer quelques statistiques pour qu'ils
# puissent avoir l'air malins à la télé.
#
# Instructions :
# 1. Écrire une fonction nommée calculer_victoire_ecrasante qui prend en
#    paramètre un tableau 2D comme celui généré à la section 1 et une
#    différence de buts (entier) et retourne le nombre (entier) de parties où
#    les Canadiens ont gagné par au moins cette différence de buts (incluse).
#    (10 points)
# 2. Écrire une fonction nommée calculer_remontee qui prend en paramètre un
#    tableau 2D comme celui généré à la section 1 et une période (entier, 1 ou
#    2) et retourne le nombre (entier) de parties où les Canadiens étaient en
#    arrière à la fin de cette période mais ont finalement gagné la partie. (10
#    points)
# 3. Écrire une fonction nommée calculer_moyenne_buts_Canadiens qui prend en
#    paramètre un tableau 2D comme celui généré à la section 1 et une période
#    (1, 2 ou 3) et retourne la moyenne (float) de buts marqués par les
#    Canadiens dans cette période sur toute la saison. (10 points)
# 4. Faites appel à chacune de ces fonctions pour afficher le script télé des
#    analystes sportifs ci-dessous. En gros vous devez calculer les paramètres
#    à passer à la fonction script_analystes et faire l'appel de cette
#    fonction. (5 points)
# 
# Rappel : Vous pouvez parcourir un tableau Numpy avec des boucles for. Exemple : 
# for ligne in tableau_2D: 
#     for valeur in ligne:                                                        
#         print(valeur)
###############################################################################

def script_analystes(nb_victoires, nb_victoires_par_2_buts,
                     nb_remontees_apres_1ere, nb_remontees_apres_2e,
                     moyenne_buts_1ere, moyenne_buts_2e, moyenne_buts_3e):
    """
    Quoi de mieux qu'une bonne analyse sportive des Canadiens de Montréal?

    Cette fonction sert aussi d'aide mémoire pour la syntaxe des fonctions,
    f-strings, et autres concepts vus en classe. :-)
    """
    print(f"La saison passée, les Canadiens ont remporté un total de {nb_victoires} parties.")
    if nb_victoires_par_2_buts > 10:
        print(f"Mais surtout, on retient qu'ils ont gagné {nb_victoires_par_2_buts} parties par au moins 2 buts d'écart!")
    else:
        print(f"Chaque partie était serrée, avec seulement {nb_victoires_par_2_buts} victoires par au moins 2 buts d'écart.")

    print(f"Ils ont réussi à revenir de l'arrière {nb_remontees_apres_1ere} fois après la 1ère période!")
    if nb_remontees_apres_1ere > 5:
        print("Une vraie force mentale!")
    else:
        print("Mais ils doivent travailler sur leur début de match.")
    
    print(f"Après la 2ème période, ils ont réussi à remonter la pente {nb_remontees_apres_2e} fois.")
    if nb_remontees_apres_2e > nb_remontees_apres_1ere:
        print("Incroyable, ils sont encore plus forts en fin de match!")
    else:
        print("Ils doivent vraiment améliorer leur jeu en 2ème période.")

    buts = [moyenne_buts_1ere, moyenne_buts_2e, moyenne_buts_3e]
    periode_max = buts.index(max(buts)) + 1
    print(f"En moyenne, les Canadiens marquent le plus de buts en période numéro {periode_max}")
    if periode_max == 1:
        print("Ils commencent fort dès le début!")
    elif periode_max == 2:
        print("Ils dominent au milieu du match!")
    else:
        print("Ils finissent toujours en force!")

def generer_statistiques_saison_au_secours():
    """
    Si vous n'arrivez pas à générer les données aléatoires, utilisez cette
    fonction qui retourne un tableau 2D pré-rempli avec des données fictives
    (mais pas de la bonne taille).
    """
    return np.array([
        [2, 1, 1, 0, 3, 2],
        [0, 2, 2, 1, 1, 0],
        [1, 0, 0, 1, 2, 3],
        [3, 1, 1, 2, 0, 0],
        [0, 0, 2, 2, 1, 1],
        [1, 3, 0, 0, 2, 2],
        [2, 2, 1, 1, 3, 1],
        [4, 0, 0, 1, 1, 2],
        [1, 1, 3, 0, 0, 0],
        [0, 2, 2, 3, 1, 1],
        [2, 1, 1, 0, 3, 2],
        [0, 2, 2, 1, 1, 0],
        [1, 0, 0, 1, 2, 3],
        [3, 1, 1, 2, 0, 0],
        [0, 0, 2, 2, 1, 1],
        [1, 3, 0, 0, 2, 2],
        [2, 2, 1, 1, 3, 1],
        [4, 0, 0, 1, 1, 2],
        [1, 1, 3, 0, 0, 0],
        [0, 2, 2, 3, 1, 1],
        [2, 1, 1, 0, 3, 2],
        [0, 2, 2, 1, 1, 0],
        [1, 0, 0, 1, 2, 3],
        [3, 1, 1, 2, 0, 0],
        [0, 0, 2, 2, 1, 1],
        [1, 3, 0, 0, 2, 2],
        [2, 2, 1, 1, 3, 1],
        [4, 0, 0, 1, 1, 2],
        [1, 1, 3, 0, 0, 0],
        [0, 2, 2, 3, 1, 1],
    ])






###############################################################################
# 🏒 GO HABS GO 🏒
#
# Section 3 : Visualisation des données (35 points)
#
# Instructions :
# 1. Utiliser Matplotlib pour créer un graphique en barres (plt.bar) qui montre
#    la moyenne de buts marqués par les Canadiens dans chaque période (1ère,
#    2ème, 3ème).
# 2. Le graphique doit avoir un titre, des étiquettes pour les axes, et une
#    légende.
# 3. Sauvegarder le graphique sous le nom "moyenne_buts_canadiens.png".
# 4. Faire appel à plt.show() pour afficher le graphique. (15 points)
#
# 5. Utiliser Matplotlib pour créer un graphique (plt.plot) qui montre les
#    points cumulés par les Canadiens au fil des 82 parties de la saison. Pour
#    cet examen, les points se calculent comme suit : une victoire rapporte 2
#    points, une nulle 1 point, et une défaite 0 point.
# 6. Le graphique doit avoir un titre, des étiquettes pour les axes, et une
#    légende.
# 7. Sauvegarder le graphique sous le nom "points_cumules_canadiens.png".
# 8. Faire appel à plt.show() pour afficher le graphique. (20 points)
###############################################################################






###############################################################################
# 🏒 GO HABS GO 🏒
#
# Fin de l'examen pratique
################################################################################