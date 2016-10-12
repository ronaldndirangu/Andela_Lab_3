def find_missing(lista, listb):
    missing = set(lista) ^ set(listb)
    if len(missing) != 0:
        for miss in missing:
            return miss
    else:
        return 0
