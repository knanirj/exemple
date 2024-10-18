# Lire les valeurs d'entrée
temps = float(input("Entrez le temps passé en heures: "))
vitesse = float(input("Entrez la vitesse moyenne en km/h: "))

# Calculer la distance
distance = temps * vitesse

# Calculer la quantité de carburant nécessaire
carburant_necessaire = distance / 12

# Afficher le résultat avec 3 décimales
print(f"Quantité de carburant dépensée: {carburant_necessaire:.3f} litres")
