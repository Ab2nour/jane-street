import copy
def black_gen():
    all_possibility = {}
    all_possibility[10] = [[10]]
    all_possibility[11] = []
    all_possibility[12] = []
    for k in range(9,-1,-1):
        all_possibility[k] = [[k] + elt for elt in all_possibility[k+3]] + all_possibility[k+1]
        all_possibility[k].append([k])

    final_res = []
    for elt in all_possibility[0]:
        if 1 in elt or 9 in elt:
            continue
        final_res.append(elt)
    return final_res


def nb_to_gen_from_black_config(black_config):
    # contain tuples that represent (start, length) of each numbers to generate in the black config case.
    config = copy.copy(black_config)
    size_to_gen = []
    if config[0] != 0:
        config.insert(0, -1)
    if config[-1] != 10:
        config.append(11)
    for k in range(len(config)-1):
        size_to_gen.append((config[k]+1, config[k+1] - config[k] -1))
    return size_to_gen