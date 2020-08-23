def onehot(x, max=8):
    l = []
    for i in range(max):
        l.append(0)
    
    l[x] = 1
    return l