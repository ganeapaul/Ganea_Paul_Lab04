
def este_prim(numar):
    if numar < 2:
        return False

    divizor = 2
    while divizor * divizor <= numar:
        if numar % divizor == 0:
            return False
        divizor += 1

    return True


def afiseaza_perechi_goldbach(numar):
    gasit = False

    for p in range(2, numar // 2 + 1):
        q = numar - p
        if este_prim(p) and este_prim(q):
            print(f"{p} + {q} = {numar}")
            gasit = True

    if not gasit:
        print("Nu s-au găsit perechi de numere prime.")


def main():
    text = input("Introdu un număr natural par mai mare decat 2: ")

    try:
        numar = int(text)
    except ValueError:
        print("Eroare: trebuie să introduci un numar intreg.")
        return

    if numar <= 2 or numar % 2 != 0:
        print("Eroare: numărul trebuie să fie par și mai mare decat 2.")
        return

    print(f"Perechile Goldbach pentru {numar}:")
    afiseaza_perechi_goldbach(numar)


if __name__ == "__main__":
    main()
