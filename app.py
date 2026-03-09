from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    table = []
    message = ""
    n = ""
    borne_max = ""
    operation = "multiplication"

    if request.method == "POST":
        operation = request.form.get("operation", "multiplication")
        n = request.form.get("n", "").strip()
        borne_max = request.form.get("borne_max", "").strip()

        # Validation de base
        if not n.isdigit():
            message = "Erreur : le nombre doit être un entier positif."
        else:
            n_int = int(n)

            # Pour multiplication et puissance, on a besoin de borne_max
            if operation in ("multiplication", "puissance"):
                if not borne_max.isdigit():
                    message = "Erreur : la borne max doit être un entier positif."
                else:
                    max_int = int(borne_max)

            # Limites simples
            if not message:
                if not (0 <= n_int <= 20):
                    message = "Erreur : le nombre doit être entre 0 et 20."
                elif operation in ("multiplication", "puissance") and not (1 <= max_int <= 20):
                    message = "Erreur : la borne max doit être entre 1 et 20."
                else:
                    if operation == "multiplication":
                        for i in range(1, max_int + 1):
                            table.append(f"{i:>2} × {n_int:<2} = {i * n_int:>4}")
                    elif operation == "puissance":
                        for i in range(1, max_int + 1):
                            table.append(f"{n_int:>2} ^ {i:<2} = {n_int ** i:>6}")
                    elif operation == "factorielle":
                        try:
                            if n_int > 12:
                                message = "Limité à 12! pour éviter des nombres trop grands."
                            else:
                                resultat = math.factorial(n_int)
                                table.append(f"{n_int}! = {resultat}")
                        except ValueError:
                            message = "Erreur : la factorielle n’est définie que pour les entiers ≥ 0."

    return render_template(
        "index.html",
        table=table,
        message=message,
        n=n,
        borne_max=borne_max,
        operation=operation,
    )

if __name__ == "__main__":
    app.run(debug=True)