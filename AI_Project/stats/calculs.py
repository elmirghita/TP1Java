

def moyenne(liste):
    somme = 0
    for x in liste:
        somme = somme + x
    return somme / len(liste)


def mediane(liste):
    triees = sorted(liste)
    n = len(triees)
    milieu = n // 2
    if n % 2 == 1:
        return triees[milieu]
    else:
        return (triees[milieu - 1] + triees[milieu]) / 2


def mode(liste):
    valeur_mode = liste[0]
    max_fois = liste.count(valeur_mode)
    for x in liste:
        fois = liste.count(x)
        if fois > max_fois:
            max_fois = fois
            valeur_mode = x
    return valeur_mode


def variance(liste):
    m = moyenne(liste)
    somme_carres = 0
    for x in liste:
        somme_carres = somme_carres + (x - m) ** 2
    return somme_carres / len(liste) - 1


def ecart_type(liste):
    return variance(liste) ** 0.5


def etendue(liste):
    return max(liste) - min(liste)

def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)


def arrangement(n, r):
    if r > n:
        return 0
    return fact(n) // fact(n - r)

def combinaison(n, r):
    if r > n:
        return 0
    return fact(n) // (fact(r)*fact(n - r))


def proba_conditionnelle(p_a_inter_b, p_b):
    if not (0 <= p_a_inter_b <= 1 and 0 <= p_b <= 1):
        raise ValueError("Les probabilités doivent être entre 0 et 1")
    if p_b == 0:
        raise ValueError("P(B) doit être différent de 0")
    if p_a_inter_b > p_b:
        raise ValueError("P(A∩B) ne peut pas dépasser P(B)")
    return p_a_inter_b / p_b

def esperance(valeurs, probas):
    if len(valeurs) == 0:
        raise ValueError("La liste est vide")
    if len(valeurs) != len(probas):
        raise ValueError("Il faut autant de valeurs que de probabilités")
    if any(p < 0 or p > 1 for p in probas):
        raise ValueError("Chaque probabilité doit être entre 0 et 1")
    if abs(sum(probas) - 1) > 1e-9:
        raise ValueError("La somme des probabilités doit valoir 1")

    total = 0
    for x, p in zip(valeurs, probas):
        total = total + x * p
    return total


def bayes(p_a, p_b_sachant_a, p_b_sachant_non_a):
    for p in (p_a, p_b_sachant_a, p_b_sachant_non_a):
        if not 0 <= p <= 1:
            raise ValueError("Les probabilités doivent être entre 0 et 1")

    p_b = p_b_sachant_a * p_a + p_b_sachant_non_a * (1 - p_a)
    if p_b == 0:
        raise ValueError("P(B) vaut 0 : calcul impossible")
    return p_b_sachant_a * p_a / p_b