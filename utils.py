

def get_number(L_int):
    res = 0
    for k,elt in enumerate(reversed(L_int)):
        res += elt * 10**k
    return res


def get_mask(list_of_sets):
    dico = {}
    for k,elt in enumerate(list_of_sets):
        for elt2 in elt:
            dico[elt2] = k
    return dico