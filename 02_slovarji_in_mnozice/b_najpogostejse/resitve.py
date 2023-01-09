"""
---------------------------------------
Najpogostejše
---------------------------------------
"""


def freq(xs):
    """
    Funkcija sestavi in vrne slovar pogostosti črk v nizu s.
    >>> freq("abcaad")
    {'a': 3, 'b': 1, 'c': 1, 'd': 1}
    """
    hist = {}
    for x in xs:
        if x not in hist:
            hist[x] = 0
        hist[x] += 1
    return hist


def max_freq(f):
    """
    vrne ključ v slovarju `f` z največjo shranjeno vrednostjo.
    >>> max_freq({'a': 3, 'b': 1, 'c': 1, 'd': 1})
    'a'
    """
    max_freqs = 0
    max_item = None
    for item, item_freq in f.items():
        if item_freq > max_freqs:
            max_freqs = item_freq
            max_item = item
    return max_item


def najpogostejse(s):
    """
    vrne besedo in znak, ki se v podanem nizu največkrat pojavita. V nizu 'in to in ono in to smo mi' se največkrat
    pojavita beseda 'in' in znak ' ' (presledek).
    >>> najpogostejse('aa bb aa')
    ('aa', 'a')
    >>> najpogostejse('in to in ono in to smo mi')
    ('in', ' ')
    """
    return max_freq(freq(s.split())), max_freq(freq(s))


def max_sorted(f):
    """
    pomozna funkcija za najpogostejse_urejene
    """
    xs = []
    for k, v in f.items():
        xs.append((-v, k))
    xs.sort()

    ys = []
    for k, v in xs:
        ys.append(v)
    return ys


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
    return max_sorted(freq(s.split())), max_sorted(freq(s))


if __name__ == '__main__':
    pass
