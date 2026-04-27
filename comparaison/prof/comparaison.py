import time
from collections import deque
import matplotlib.pyplot as plt


def chronometrer(f, *args, **kwargs):
    """Retourne le temps d'exécution de f (en secondes) ainsi que son résultat."""
    debut = time.perf_counter()
    resultat = f(*args, **kwargs)
    fin = time.perf_counter()
    return fin - debut, resultat


# ---------------------------------------------------------------------------
# Fonctions à tester
# ---------------------------------------------------------------------------

def append_list(n):
    lst = []
    for _ in range(n):
        lst.append(0)
    return lst


def append_dict(n):
    d = {}
    for i in range(n):
        d[i] = 0
    return d


def append_deque(n):
    dq = deque()
    for _ in range(n):
        dq.append(0)
    return dq


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def mesurer_jusqu_a_1s(f):
    """Retourne une liste de tuples (n, durée) en doublant n jusqu'à dépasser 1 s."""
    resultats = []
    n = 1
    while True:
        duree, _ = chronometrer(f, n)
        resultats.append((n, duree))
        print(f"n = {n:>12,} -> {duree:.4f} s")
        if duree > 1:
            print(f"\nIl faut environ {n:,} opérations pour dépasser 1 seconde.\n")
            break
        n *= 2
    return resultats


def tracer_courbe(resultats, label):
    """Trace la courbe temps en fonction de n pour une série de résultats."""
    ns, durees = zip(*resultats)
    plt.plot(ns, durees, marker="o", label=label)


if __name__ == "__main__":
    series = [
        (append_list,  "list.append"),
        (append_dict,  "dict[i] = 0"),
        (append_deque, "deque.append"),
    ]

    for f, label in series:
        print(f"=== {label} ===")
        resultats = mesurer_jusqu_a_1s(f)
        tracer_courbe(resultats, label)

    plt.xlabel("Nombre d'opérations")
    plt.ylabel("Temps (s)")
    plt.title("Temps d'exécution selon la structure de données")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

