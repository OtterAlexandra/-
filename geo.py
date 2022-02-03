def get_spn(toponym):
    lc = [float(x) for x in toponym['boundedBy']['Envelope']['lowerCorner'].split()]
    uc = [float(x) for x in toponym['boundedBy']['Envelope']['upperCorner'].split()]
    return abs(uc[0] - lc[0]), abs(uc[1] - lc[1]))
