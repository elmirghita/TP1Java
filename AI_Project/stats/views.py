from django.shortcuts import render
from . import calculs


def accueil(request):
    contexte = {"nom": "Django"}
    return render(request, "stats/accueil.html", contexte)


def descriptives(request):
    contexte = {}

    if request.method == "POST":
        texte = request.POST.get("nombres", "")
        try:
            # "4, 8, 6" -> ["4", " 8", " 6"] -> [4.0, 8.0, 6.0]
            valeurs = [float(x) for x in texte.split(",")]

            contexte["moyenne"] = calculs.moyenne(valeurs)
            contexte["mediane"] = calculs.mediane(valeurs)
            contexte["mode"] = calculs.mode(valeurs)
            contexte["variance"] = calculs.variance(valeurs)
            contexte["ecart_type"] = calculs.ecart_type(valeurs)
            contexte["etendue"] = calculs.etendue(valeurs)
        except ValueError:
            contexte["erreur"] = "Entrez des nombres séparés par des virgules."

    return render(request, "stats/descriptives.html", contexte)

def denombrement(request):
    contexte = {}

    if request.method == "POST":
        try:
            n = int(request.POST.get("n", ""))
            k = int(request.POST.get("k", ""))
            operation = request.POST.get("operation")

            if operation == "arrangement":
                contexte["resultat"] = calculs.arrangement(n, k)
                contexte["nom_operation"] = "Arrangement"
            elif operation == "combinaison":
                contexte["resultat"] = calculs.combinaison(n, k)
                contexte["nom_operation"] = "Combinaison"
        except ValueError as e:
            contexte["erreur"] = str(e) or "Entrez deux entiers n et k."

    return render(request, "stats/denombrement.html", contexte)

def probabilites(request):
    contexte = {}

    if request.method == "POST":
        operation = request.POST.get("operation")
        try:
            if operation == "conditionnelle":
                a_inter_b = float(request.POST.get("a_inter_b", ""))
                p_b = float(request.POST.get("p_b", ""))
                contexte["resultat"] = calculs.proba_conditionnelle(a_inter_b, p_b)
                contexte["nom_operation"] = "P(A|B)"

            elif operation == "esperance":
                valeurs = [float(x) for x in request.POST.get("valeurs", "").split(";")]
                probas = [float(x) for x in request.POST.get("probas", "").split(";")]
                contexte["resultat"] = calculs.esperance(valeurs, probas)
                contexte["nom_operation"] = "Espérance E(X)"

            elif operation == "bayes":
                p_a = float(request.POST.get("p_a", ""))
                p_b_a = float(request.POST.get("p_b_a", ""))
                p_b_non_a = float(request.POST.get("p_b_non_a", ""))
                contexte["resultat"] = calculs.bayes(p_a, p_b_a, p_b_non_a)
                contexte["nom_operation"] = "Théorème de Bayes : P(A|B)"
        except ValueError as e:
            contexte["erreur"] = str(e) or "Vérifiez vos entrées (utilisez le point : 0.25)."

    return render(request, "stats/probabilites.html", contexte)