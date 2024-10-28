def uneven_remover(list):
    newlist = []
    for i in list:
        if(i % 2 == 0):
            newlist.append(i)
    return newlist