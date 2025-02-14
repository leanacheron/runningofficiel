def calculer_allure_vitesse(distance, temps):
    """
    Calcule l'allure et la vitesse en fonction de la distance et du temps donnés.

    :param distance: La distance parcourue (en kilomètres).
    :param temps: Le temps écoulé (en minutes).
    :return: Un tuple contenant l'allure (minutes par kilomètre) et la vitesse (kilomètres par heure).
    """
    # Calcul de l'allure (minutes par kilomètre)
    allure = temps / distance

    # Calcul de la vitesse (kilomètres par heure)
    temps_heures = temps / 60  # Conversion du temps en heures
    vitesse = distance / temps_heures

    return allure, vitesse

# Exemple d'utilisation
distance = 10  # en kilomètres
temps = 50  # en minutes

allure, vitesse = calculer_allure_vitesse(distance, temps)
print(f"Allure: {allure:.2f} min/km")
print(f"Vitesse: {vitesse:.2f} km/h")