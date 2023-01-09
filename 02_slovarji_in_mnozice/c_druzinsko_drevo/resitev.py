"""
V seznamu family je spravljeno družinsko drevo:

>>> family = [('bob', 'mary'), ('bob', 'tom'), ('bob', 'judy'), ('alice', 'mary'), \\
    ('alice', 'tom'), ('alice', 'judy'), ('renee', 'rob'), ('renee', 'bob'),  \\
    ('sid', 'rob'), ('sid', 'bob'), ('tom', 'ken'), ('ken', 'suzan'), ('rob', 'jim')]

V vsaki terki sta zapisani dve imeni: ime starša in ime otroka. Terka ('bob', 'mary') nam pove, da je Bob Maryjin oče,
terka ('bob', 'tom') pa, da je Bob Tomov oče, itd.
"""


def family_tree(family):
    """
    sprejeme seznam v kateri je spravljeno družinsko drevo in vrne slovar v katerem je za vsakega starša spravljen
    seznam vseh njegovih otrok.
    >>> family_tree(family)
    {'renee': ['rob', 'bob'], 'ken': ['suzan'], 'rob': ['jim'], 'sid': ['rob', 'bob'], ... , 'bob': ['mary', 'tom', 'judy']}
    """
    tree = {}
    for parent, child in family:
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)
    return tree


def children(tree, name):
    """
    v družinskem drevesu `tree` vrne seznam vseh otrok osebe. V primeru, da oseba nima otrok vrnite prazen seznam.
    >>> tree = family_tree(family)
    >>> children(tree, 'alice')
    ['mary', 'tom', 'judy']
    >>> children(tree, 'mary')
    []
    """
    if name in tree:
        return tree[name]
    return []


def grandchildren(tree, name):
    """
    vrne seznam vseh vnukov in vnukinj osebe.
    """
    names = []
    for child in children(tree, name):
        for grandchild in children(tree, child):
            names.append(grandchild)
    return names


def successors(tree, name):
    """
    (tezja naloga)
    vrne seznam vseh naslednikov osebe.
    >>> successors(tree, 'tom')
    ['ken', 'suzan']
    >>> successors(tree, 'sid')
    ['rob', 'bob', 'jim', 'mary', 'tom', 'judy', 'ken', 'suzan']
    """
    names = []
    todo = [name]
    while todo:
        cs = children(tree, todo.pop())
        names.extend(cs)
        todo.extend(cs)
    return names


if __name__ == '__main__':
    family = [('bob', 'mary'), ('bob', 'tom'), ('bob', 'judy'), ('alice', 'mary'),
              ('alice', 'tom'), ('alice', 'judy'), ('renee', 'rob'), ('renee', 'bob'),
              ('sid', 'rob'), ('sid', 'bob'), ('tom', 'ken'), ('ken', 'suzan'), ('rob', 'jim')]
    print(family_tree(family))
