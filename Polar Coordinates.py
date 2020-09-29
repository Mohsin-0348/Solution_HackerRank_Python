import cmath

if __name__ == "__main__":
    x = input().split()
    z = complex(''.join(x))
    r_phi = cmath.polar(z)
    for item in r_phi:
        print(item)
