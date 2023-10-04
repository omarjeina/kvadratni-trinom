# kreirati program koji rastavlja kvadratni trinom na faktore preko srednjeg clana
# ax^2 + bx + c

print("Za kvadratni trinom oblika ax^2 + bx + c unesi sljedeće: ")
a = int(input("koeficijent a: "))
b = int(input("koeficijent b: "))
c = int(input("slobodni clan c: "))

z = a * c

par = []

for i in range(abs(b) + 100):
    for j in range(abs(b) + 100):
        if i + j == b and i * j == z:
            par.append(i)
            par.append(j)
        elif -i + j == b and -i * j == z:
            par.append(-i)
            par.append(j)
        elif i + -j == b and i * -j == z:
            par.append(i)
            par.append(-j)
        elif -i + -j == b and -i * -j == z:
            par.append(-i)
            par.append(-j)
        else:
            pass

def main():
    print(list(set(par)))

if __name__ == "__main__":
    main()
