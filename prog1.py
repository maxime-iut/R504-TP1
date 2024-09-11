#!/bin/python3


from fonctions import puissance


def main():
    print("Puissance d'un nombre\n")

    a = input("Valeur de 'a': ")
    b = input("Valeur de 'b': ")

    res = puissance(a, b)
    print(f"\n{a}^{b} = {res}")


if __name__ == "__main__":
   main()

