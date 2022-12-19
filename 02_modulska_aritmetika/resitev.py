

class zP:
    def __init__(self, module):
        self.module = module

    def vrni_modul(self):
        return self.module

    def __str__(self):
        return f"Z_{self.module}"

    def vsota(self, prvo, drugo):
        return (prvo + drugo) % self.module

    def zmnozek(self, prvo, drugo):
        return (prvo * drugo) % self.module

    def nasprotno(self, stevilo):
        return (self.module - stevilo) % self.module

    def razlika(self, prvo, drugo):
        return self.vsota(prvo, self.nasprotno(drugo))

    def obratno(self, stevilo):
        obrat = 1
        while self.zmnozek(stevilo, obrat) != 1:
            obrat += 1

        return obrat

    def kolicnik(self, prvo, drugo):
        return self.zmnozek(prvo, self.obratno(drugo))

    def potenca(self, stevilo, eksponent):
        if eksponent < 0:
            return self.obratno(self.potenca(stevilo, -eksponent))

        rezultat = 1
        for i in range(eksponent):
            rezultat = self.zmnozek(rezultat, stevilo)

        return rezultat

    def potenca_rekurzija(self, stevilo, eksponent):
        if eksponent == 0:
            return 1
        if eksponent < 0:
            return self.obratno(self.potenca(stevilo, -eksponent))
        t = self.potenca(stevilo, eksponent / 2)
        kvadrat = self.zmnozek(t, t)
        if eksponent % 2 == 0:
            return kvadrat
        return self.zmnozek(kvadrat, stevilo)

    def stevilo_kvadratnih_korenov(self, stevilo):
        st_korenov = 0
        for b in range(self.module):
            if self.zmnozek(b, b) == stevilo:
                st_korenov += 1
        return st_korenov

    def je_potenca(self, osnova, iskani_rezultat):
        potenca = 1
        for exp in range(self.module):
            if iskani_rezultat == potenca:
                return True
            potenca = self.zmnozek(potenca, osnova)
        return False

    def je_multiplikativni_generator(self, stevilo):
        for k in range(1, self.module):
            if not self.je_potenca(stevilo, k):
                return False
        return True


if __name__ == '__main__':
    z_7 = zP(7)
    print(z_7.module)
