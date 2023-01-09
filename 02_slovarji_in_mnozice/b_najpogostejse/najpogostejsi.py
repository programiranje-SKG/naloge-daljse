"""
---------------------------------------
Najpogostejše
---------------------------------------
"""


def freq(s):
    """
    Funkcija sestavi in vrne slovar pogostosti črk v nizu s.
    >>> freq("abcaad")
    {'a': 3, 'b': 1, 'c': 1, 'd': 1}
    """
    pass


def max_freq(f):
    """
    vrne ključ v slovarju `f` z največjo shranjeno vrednostjo.
    >>> max_freq({'a': 3, 'b': 1, 'c': 1, 'd': 1})
    'a'
    """
    pass


def najpogostejse(s):
    """
    vrne besedo in znak, ki se v podanem nizu največkrat pojavita. V nizu 'in to in ono in to smo mi' se največkrat
    pojavita beseda 'in' in znak ' ' (presledek).
    >>> najpogostejse('aa bb aa')
    ('aa', 'a')
    >>> najpogostejse('in to in ono in to smo mi')
    ('in', ' ')
    """
    pass


def najpogostejse_urejene(s):
    """
    Tezja naloga
    vrne vse besede in črke, ki se v podanem nizu pojavijo, urejene po številu pojavitev (besede in črke z enakim
    številom pojavitev uredite po abecednem vrstnem redu).
    >>> najpogostejse_urejene('aa bb aa')
    (['aa', 'bb'], ['a', ' ', 'b'])
    >>> najpogostejse_urejene('in to in ono in to smo mi')
    (['in', 'to', 'mi', 'ono', 'smo'], [' ', 'o', 'i', 'n', 'm', 't', 's'])
    """
    pass


if __name__ == '__main__':
    pass
