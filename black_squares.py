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