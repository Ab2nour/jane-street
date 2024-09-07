from pprint import pprint

# Fonction pour vérifier si un nombre est premier
def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Générer une liste des premiers nombres premiers
def liste_nombres_premiers(limite):
    premiers = []
    for i in range(2, limite + 1):
        if est_premier(i):
            premiers.append(i)
    return premiers

# Générer les puissances de nombres premiers élevés à des puissances nombres premiers
def puissances_nombres_premiers(limite_premier, limite_puissance):
    nombres_premiers = liste_nombres_premiers(limite_premier)
    puissances_premiers = liste_nombres_premiers(limite_puissance)

    resultats = []
    for base in nombres_premiers:
        for puissance in puissances_premiers:
            resultat = base ** puissance
            resultats.append((base, puissance, resultat))
    return resultats

# Limites des nombres premiers (peut être ajusté)
limite_premier = 500
limite_puissance = 20

# Calculer les puissances
resultats = puissances_nombres_premiers(limite_premier, limite_puissance)

liste = []
# Affichage des résultats
for base, puissance, resultat in resultats:
    print(f"{base}^{puissance} = {resultat}")
    if resultat < 10e11:
        liste.append(resultat)

liste.sort(reverse=True)

pprint(liste)

