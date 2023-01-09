"""
------------------------------
Inventar
------------------------------

Neka trgovina shranjuje svoj inventar v slovarju, katerega ključi so artikli in vrednosti količine:

inv = {'sir': 8, 'kruh': 15, 'makovka': 10, 'pasja radost': 2, 'pašteta': 10, 'mortadela': 4, 'klobasa': 7}
Pazi: vrednosti so števila (npr. 10) in ne nizi ("10").
"""


def zaloga(inventar, artikel):
    """
    Funkcija naj pove, koliko izdelka `artikel` imamo na zalogi. Če bi imeli gornji slovar z inventarjem shranjen v slovarju
    'inv', mora klic zaloga(inv, "makovka") vrniti 10.
    >>> inv = {'sir': 8, 'kruh': 15, 'makovka': 10, 'pasja radost': 2, 'pašteta': 10, 'mortadela': 4, 'klobasa': 7}
    >>> zaloga(inv, "makovka")
    10
    """
    pass


def prodaj(inventar, artikel, kolicina):
    """
    Funkcija zmanjša količino artikla `artikel` v inventarju `inventar` za `kolicina`. Klic `prodaj(inv, "makovka", 3)`
    (prodali smo tri makovke) mora spremeniti slovar `inv` tako, da zmanjša vrednost pri ključu "makovke" za 3.
    Funkcija ne vrača ničesar.
    >>> inv
    {'sir': 8, 'kruh': 15, 'makovka': 10, 'pasja radost': 2, 'pašteta': 10, 'mortadela': 4, 'klobasa': 7}
    >>> prodaj(inv, "makovka", 3)
    >>> inv
    {'sir': 8, 'kruh': 15, 'makovka': 7, 'pasja radost': 2, 'pašteta': 10, 'mortadela': 4, 'klobasa': 7}
    """
    pass


def primanjkljaj(inventar, narocilo):
    """
    Funkcija prejme dva slovarja: prvi predstavlja trenutni inventar, drugi pa, kaj neka stranka naroča; naročilo je
    predstavljeno s slovarjem enake oblike kot inventar. Funkcija mora vrniti nov slovar, v katerem bo zapisano,
    koliko česa moramo še kupiti, da bomo lahko stranki dobavili vse, kar si želi. Če bi, recimo, stranka želela tri
    paštete, devet klobas in eno pivo, mora funkcija vrniti slovar {"klobasa": 2, "pivo": 1}. Dve klobasi zato, ker
    jih imamo sedem, stranka pa jih želi devet. Paštet ne bo potrebno naročati, saj jih imamo dovolj. Pivo pa
    potrebujemo, saj nimamo nobenega.
    >>> primanjkljaj(inv, {"pašteta": 3, "klobasa": 9, "pivo": 1})
    {"klobasa": 2, "pivo": 1}
    """
    pass



if __name__ == '__main__':
    # -------------------------------------------------------
    # inventar
    inv = {'sir': 8, 'kruh': 15, 'makovka': 10, 'pasja radost': 2, 'pašteta': 10, 'mortadela': 4, 'klobasa': 7}
    # print(zaloga(inv))
    # prodaj(inv, "makovka", 3)
    # print(zaloga(inv))
    # print(primanjkljaj(inv, {"pašteta": 3, "klobasa": 9, "pivo": 1}))
    # -------------------------------------------------------

