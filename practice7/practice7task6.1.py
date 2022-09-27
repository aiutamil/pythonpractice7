def gcdEuclid(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdEuclid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def lcm(a, b):
    gcd, x, y = gcdEuclid(a, b)
    return (a * b) / gcd


a, b = list(map(int, input("Enter numbers:").split()))
gcd, x, y = gcdEuclid(a, b)
print("Greatest common divisor is:", gcd)
print("Least common divisor is:", lcm(a, b))
