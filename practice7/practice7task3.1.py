import math
def cPow(lst):
    h1 = math.sqrt(math.pow(lst[0],2)+math.pow(lst[1],2))
    h2 = math.sqrt(math.pow(lst[2],2)+math.pow(lst[3],2))
    print("Hypotenuses triangle1:",h1)
    print("Hypotenuses triangle2:",h2)
    if h1 > h2:
        print("Hypotenus of triangle1 larger:",h2)
    elif h1 == h2:
        print("Equal")
    else:
        print("Hypotenus of triangle2 larger:",h2)

tr=[]
print("Enter sides of triangle:")
for i in range(2):
    print("for",i+1,"triangle")
    tr.append(float(input("side1:")))
    tr.append(float(input("side2:")))

cPow(tr)
