#!/bin/python3


from fonctions import puissance


def main():
    print("Puissance d'un nombre\n")

    a = input("Valeur de 'a': ")
    b = input("Valeur de 'b': ")

    if not type(a) is int or not type(b) is int:
        raise TypeError("Que des integer !!!")

    res = puissance(a, b)
    print(f"\n{a}^{b} = {res}")


if __name__ == "__main__":
   main()

