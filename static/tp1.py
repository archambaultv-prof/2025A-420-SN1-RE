import math  # Module math utilisé: radians, sin, cos, sqrt

# Bannière simple + petite « animation » avec une boucle for (non imbriquée)
print("\n=== TP1 – Lancer de projectile Angle Birds ===")

# Choix d’un niveau de difficulté via match/case
difficulte = input("Entrez la difficulté (F/M/D): ").strip().upper()
distance_porc = float(input("Distance horizontale du cochon en mètre (> 0): "))
hauteur_porc = float(input("Hauteur du cochon en mètre (>= 0): "))
vitesse_vent = float(
    input("Vitesse du vent en mètre par seconde, positif = vent arrière, négatif = vent de face: ")
)

# Constantes physiques
G = 9.81  # accélération gravitationnelle (m/s^2)

match difficulte:
    case "F":
        tolerance_m = 2.5  # marge horizontale/verticale (m)
        nb_essais = 8  # nombre d’essais possibles
    case "M":
        tolerance_m = 1.0
        nb_essais = 6
    case "D":
        tolerance_m = 0.5
        nb_essais = 4
    case _:
        # Valeur par défaut si autre saisie
        tolerance_m = 1.0
        nb_essais = 7
        print("(Difficulté invalide – passage au niveau Moyen par défaut.)")

# Validation de base des paramètres de la scène
if distance_porc <= 10 or hauteur_porc < 0:
    print("\nErreur: distance doit être > 0 et hauteur >= 0. Relancez le programme.")
else:
    # En mode Expert, on limite les tirs "directs": angle minimal = atan2(h, d) + 5°
    if difficulte == "D":
        angle_min_deg = math.degrees(math.atan2(hauteur_porc, distance_porc)) + 5.0
        # On évite un angle minimal impossible (>= 90°)
        if angle_min_deg >= 90.0:
            angle_min_deg = 89.0
        print(f"(Expert) Angle minimal requis ≈ {angle_min_deg:.1f}°")
    else:
        angle_min_deg = 0.0  # pas de contrainte en Facile/Moyen

    # Boucle principale pour permettre plusieurs tirs (while) sans perdre un essai sur saisie invalide
    essais_valides = 0
    while essais_valides < nb_essais:
        print(f"\n— Tir {essais_valides + 1} —")
        angle_deg = float(input(f"Angle de tir en degrés, ({angle_min_deg:.1f} < angle < 90): "))
        vitesse_initiale = float(input("Vitesse initiale en mètre par seconde (> 0): "))

        # Détection de valeurs erronées
        if angle_deg <= angle_min_deg or angle_deg >= 90:
            print(
                f"Valeur d’angle invalide. L’angle doit être > {angle_min_deg:.1f}° et < 90°. Réessayez."
            )
            continue
        if vitesse_initiale <= 0:
            print("Vitesse initiale invalide (doit être > 0). Réessayez.")
            continue

        # Conversion et composantes initiales
        angle_rad = math.radians(angle_deg)
        v0x = vitesse_initiale * math.cos(angle_rad)
        v0y = vitesse_initiale * math.sin(angle_rad)
        # Modèle simple du vent: on ajoute la vitesse du vent à la composante
        # horizontale (le vent ne change pas la vitesse verticale ici)
        vx_effectif = v0x + vitesse_vent

        # Si la composante horizontale est nulle ou négative, on redemande (vent trop fort)
        if vx_effectif <= 0:
            print("La composante horizontale est nulle/négative (vent contraire trop fort). Réessayez.")
            continue

        # Résultats finaux
        # Calcul analytique du temps de vol (sans vent sur y): t_sol = 2*v0y/G
        t_sol = (2.0 * v0y) / G
        x_sol = vx_effectif * t_sol

        t_cochon = distance_porc / vx_effectif
        y_cochon = v0y * t_cochon - 0.5 * G * (t_cochon**2)

        # Détermination si le projectile touche la cible
        if abs(y_cochon - hauteur_porc) <= tolerance_m:
            print("Touché ! Le projectile atteint la cible")
            break  # sort de la boucle while (réussite)
        else:
            print(f"Raté… Le projectile retombe au sol aux alentours de x ≈ {x_sol:.2f} m")
            if y_cochon < 0:
                print(f"Le projectile est tombé au sol avant d'atteindre la cible ({distance_porc:.2f} m).")
            else:
                print(
                    f"Au niveau de la cible (x = {distance_porc:.2f} m), le projectile est à y ≈ {y_cochon:.2f} m"
                    f" (cible à y = {hauteur_porc:.2f} m)"
                )
            # On ne consomme l'essai que lorsque les paramètres sont valides et que le tir a été simulé
            essais_valides = essais_valides + 1

print("\nMerci d’avoir joué à Angle Birds.")

