def main():
    mass = int(input())
    energy=int (energy_calc(mass))
    print(energy)

def energy_calc(m):
    c = int(300000000)
    E = int(m * pow(c,2))

    return E


main()
