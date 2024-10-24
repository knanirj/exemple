
# Lecture des côtés A, B et C
A, B, C = map(float, input("Entrez les trois côtés du triangle (A, B et C) : ").split())

# Organiser les côtés dans l'ordre décroissant
sides = [A, B, C]
sides.sort(reverse=True)  # Tri en ordre décroissant
A, B, C = sides  # A est le plus grand côté

# Vérification des conditions pour former un triangle
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    # Type de triangle
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    elif A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")

    # Vérification si les côtés sont égaux
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")
