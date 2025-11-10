def is_pangram(sentence):
    test=set(sentence.lower())
    al="abcdefghijklmnopqrstuvwxyz"
    alpha=set(al)
    new_set=alpha.intersection(test)
    if alpha==new_set:
        return True
    else:
        return False
