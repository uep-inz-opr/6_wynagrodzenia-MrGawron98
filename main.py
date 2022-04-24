class Pracownik:
    total = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate(self):
        a = self.salary
        c = round(0.0976*a, 2) + round(0.015*a, 2) + round(0.0245*a, 2)
        d = a - c
        e = round(d * 0.09, 2)
        f = round(d * 0.0775, 2)
        g = 111.25
        h = round(a - g - c, 0)
        i = round((0.18 * h), 2) - 46.33
        j = round(i - f, 0)
        k = a - c - e - j
        l = round(0.0976*a, 2) + round(0.065*a, 2) + round(0.0193*a, 2) + round(0.0245*a, 2) + round(0.001*a, 2)
        m = a + l
        Pracownik.total += m

        result = f"{self.name} {k:.2f} {l:.2f} {m:.2f}"
        return(result)

    def koszt_pracodawcy(self):
        return


n = int(input())
pracownicy = []

for i in range(n):
    line = input()
    raw = line.split()
    p = Pracownik(raw[0], int(raw[1]))
    pracownicy.append(p)

for pracownik in pracownicy:
    print(pracownik.calculate())
print(Pracownik.total)

