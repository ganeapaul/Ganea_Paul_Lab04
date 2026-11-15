
from pathlib import Path


def citeste_numere():
    fisier = Path(__file__).with_name("numere.txt")

    try:
        with open(fisier, "r", encoding="utf-8") as f:
            linii = [linie.strip() for linie in f]
    except FileNotFoundError:
        print("Eroare: fisierul numere.txt nu exista.")
        return None

    if len(linii) != 2:
        print("Eroare: fisierul trebuie sa contina exact doua numere, pe linii separate.")
        return None

    for numar in linii:
        if not 1 <= len(numar) <= 200 or not all(c in "0123456789" for c in numar):
            print("Eroare: fiecare numar trebuie sa aiba intre 1 si 200 de cifre (0-9).")
            return None

    a = linii[0].lstrip("0") or "0"
    b = linii[1].lstrip("0") or "0"
    return a, b


def aduna(a, b):
    a = a[::-1]
    b = b[::-1]
    rezultat = []
    transport = 0

    for i in range(max(len(a), len(b))):
        cifra_a = int(a[i]) if i < len(a) else 0
        cifra_b = int(b[i]) if i < len(b) else 0
        suma = cifra_a + cifra_b + transport
        rezultat.append(str(suma % 10))
        transport = suma // 10

    if transport:
        rezultat.append(str(transport))

    return "".join(rezultat[::-1]).lstrip("0") or "0"


def inmulteste(a, b):
    rezultat = [0] * (len(a) + len(b))

    for i in range(len(a) - 1, -1, -1):
        transport = 0
        for j in range(len(b) - 1, -1, -1):
            pozitie = i + j + 1
            produs = int(a[i]) * int(b[j]) + rezultat[pozitie] + transport
            rezultat[pozitie] = produs % 10
            transport = produs // 10
        rezultat[i] += transport

    return "".join(str(cifra) for cifra in rezultat).lstrip("0") or "0"


def main():
    numere = citeste_numere()
    if numere is None:
        return

    a, b = numere
    print(f"Primul numar: {a}")
    print(f"Al doilea numar: {b}")
    print(f"Suma: {aduna(a, b)}")
    print(f"Produsul: {inmulteste(a, b)}")


if __name__ == "__main__":
    main()
