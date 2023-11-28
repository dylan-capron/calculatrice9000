def saisie_nombre():
    while True:
        try:
            nombre = float(input("Entrez un nombre : "))
            return nombre
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

def saisie_operation():
    operations_valides = ['+', '-', '*', '/']
    while True:
        operation = input("Entrez l'opération (+, -, *, /) : ")
        if operation in operations_valides:
            return operation
        else:
            print("Erreur : Opération invalide. Veuillez entrer une opération valide.")

def afficher_historique(historique):
    print("Historique :")
    for operation in historique:
        print(operation)

def calculatrice():
    print("Bienvenue !")

    historique = []

    while True:
        nombre1 = saisie_nombre()
        nombre2 = saisie_nombre()
        operation = saisie_operation()
        try:
            if operation == '+':
                resultat = nombre1 + nombre2
            elif operation == '-':
                resultat = nombre1 - nombre2
            elif operation == '*':
                resultat = nombre1 * nombre2
            elif operation == '/':
                resultat = nombre1 / nombre2
        except ZeroDivisionError:
            print("Erreur : Division par zéro.")
            continue

        print(f"Résultat de {nombre1} {operation} {nombre2} = {resultat}")
        historique.append(f"{nombre1} {operation} {nombre2} = {resultat}")

        continuer = input("Voulez-vous effectuer une autre opération ? (O/N) ").upper()
        if continuer != 'O':
            afficher_historique(historique)
            effacer_historique = input("Voulez-vous effacer l'historique ? (O/N) ").upper()
            if effacer_historique == 'O':
                historique = []
            print("Au revoir !")
            break

if __name__ == "__main__":
    calculatrice()
