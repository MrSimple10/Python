def findx(point):
    ix = iy = 0
    for i, v in enumerate(point):
        if v == '(':
            ix = i
        elif v == ',':
            iy = i
            break
    xvalue = int(point[ix+1:iy])
    return xvalue

def findy(point):
    ix = iy = 0
    for i, v in enumerate(point):
        if v == ',':
            ix = i
        elif v == ')':
            iy = i
            break
    yvalue = int(point[ix+1:iy])
    return yvalue