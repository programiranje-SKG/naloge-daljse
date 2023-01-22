
"""
Miklavž ima knjigo, v katero zapisuje, kaj počnejo otroci. Knjiga je takšne oblike:
"""
knjiga = {
     "Ana":
         ["pometanje stopnic", "jezikanje", "kuhanje kosila", "pretep z bratom", "pometanje stopnic", "kuhanje kosila"],
     "Benjamin":
         ["brisanje mize", "jezikanje", "prepisana naloga", "pretep s sestro"],
     "Cilka":
         [],
     "Dani":
         ["prepir z mamo", "kuhanje kosila", "kuhanje kosila"],
     "Eva":
         ["pretep z bratom", "nenarejena naloga"],
     "Franc":
         ["pomivanje posode", "brisanje mize", "pometanje stopnic",
          "kuhanje kosila", "kuhanje kosila", "pometanje stopnic"],
     "Greta":
         ["pometanje stopnic", "jezikanje"],
     "Helga":
         ["pometanje stopnic", "jezikanje", "kuhanje kosila", "prepir z mamo", "pometanje stopnic", "kuhanje kosila"],
 }

"""
Vsako delo prinaša pozitivne ali negativne točke. Točkovalnik je, na primer takšen:
"""

tockovalnik = {
    'pometanje stopnic': 3,
    'kuhanje kosila': 5,
    'pomivanje posode': 3,
    'brisanje mize': 1,
    'pretep z bratom': -3,
    'pretep s sestro': -3,
    'prepir z mamo': -5,
    'nenarejena naloga': -4,
    'prepisana naloga': -7,
    'jezikanje': -4
}

"""
Ko pride ustrezni čas leta, otroci pišejo pisma z željami za darila. Tule so cene daril.
"""

cena = {
    'sanke': 20,
    'zvezek': 5,
    'lok za violino': 30,
    'barvice': 7,
    'bomboni': 3
}


def oceni(dela):
    """
    dobi seznam del in vrne njihovo skupno vrednost.

    parametri:
        dela (str): seznam del
    vrne
        (int): skupno vrednost daril
    """
    return sum(tockovalnik[delo] for delo in dela)


def povzetek_knjige(stran):
    """
    dobi del knjige (ali celo knjigo) in vrne slovar, katerega ključi
    so imena otrok in vrednosti njihove ocene.

    parametri:
        stran (dict): del knjige ali cela knjiga. Kljuci so imena, vrednosti pa seznam del
    vrne:
        (dict): kljuci imena, vrednosti ocene
    """
    return {ime: oceni(dela) for ime, dela in stran.items()}


def izberi(dela, spisek):
    """
    dobi seznam otrokovih dejanj in seznam njegovih želja. Vrniti mora množico daril,
    ki jih bo ta otrok prejel. Otrok prejme le darila, ki si jih želi in katerih cena
    ne presega števila otrokovih točk.

    parametri:
        dela (list): seznam del otrok
        spisek (set): mnozica daril, ki si jih zeli otrok
    vrne:
        (set): mnozica daril, ki ustrezajo pogojem
    """
    return {darilo for darilo in spisek if cena[darilo] <= oceni(dela)}

def strosek(dela, spisek):
    """
    vrne strošek, ki ga bo Miklavžu naredil ta otrok.

    parametri:
        dela (list): seznam del otroka
        spisek (set): mnozica daril, ki si jih otrok zeli
    vrne:
        (int): Miklavzev strosek za tega otroka
    """
    return sum(cena[stvar] for stvar in izberi(dela, spisek))


def najpridnejsi_otrok(otroci):
    """
    vrne ime najpridnejšega otroka.

    parametri:
        otroci (dict): kljuci: imena, vrednosti: seznami del otrok
    vrne:
        (str): ime otroka
    """
    return max((oceni(dela), ime) for ime, dela in otroci.items())[1]


def poreden(dela):
    """
    vrne True ali False glede na to, dali je otrok s takimi deli poreden ali ne.

    parametri:
        dela (list): seznam del otroka
    vrne:
        (bool): ali je otrok poreden
    """
    return any(tockovalnik[delo] <= -5 for delo in dela)


def obdarovani(otroci):
    """
    vrne množico imen otrok, ki niso poredni.

    parametri:
        knjiga (dict): Kljuci so imena, vrednosti pa seznam del
    vrne:
        (list): seznam imen
    """
    return {ime for ime, dela in otroci.items() if not poreden(dela)}


if __name__ == '__main__':
    print(oceni(knjiga['Ana']))
