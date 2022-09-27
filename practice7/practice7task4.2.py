import math


def isInside(x, y, R):
    if math.pow(x, 2) + math.pow(y, 2) <= pow(R, 2):
        return True


R = input("Enter radius of circle:")
wannaExit = False
while(wannaExit!=True):
    x, y = list(map(int, input("Enter x,y of point").split()))
    wannaExit = bool(input(""))
    isInside(x, y, R)
