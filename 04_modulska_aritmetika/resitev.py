

class Zp:
    def __init__(self, module):
        """
        Izdela objekt, ki predstavlja množico Z_modul.
        """
        self.module = module

    def __str__(self):
        """
        Vrne niz oblike Z_p, kjer je p modul množice
        """
        return f"Z_{self.module}"

    def vsota(self, prvo, drugo):
        """
        Vrne modulsko vsoto števil prvo in drugo v okviru množice, ki jo predstavlja trenutni objekt. Obe števili sta
        iz intervala [0, p-1], kjer je p modul množice trenutnega objekta.
        """
        return (prvo + drugo) % self.module

    def zmnozek(self, prvo, drugo):
        """
        Vrne modulski zmnožek števil prvo in drugo v okviru množice, ki jo predstavlja trenutni objekt. Obe števili sta
        iz intervala [0, p-1], kjer je p modul množice trenutnega objekta.
        """
        return (prvo * drugo) % self.module

    def nasprotno(self, stevilo):
        """
        Vrne modulsko nasprotno vrednost števila 'stevilo'. Število je iz intervala [0, p-1], kjer je p modul
        množice trenutnega objekta.
        """
        return (self.module - stevilo) % self.module

    def razlika(self, prvo, drugo):
        """
        Vrne modulsko razliko števil prvo in drugo v okviru množice, ki jo predstavlja trenutni objekt. Obe števili sta
        iz intervala [0, p-1], kjer je p modul množice trenutnega objekta.
        """
        return self.vsota(prvo, self.nasprotno(drugo))

    def obratno(self, stevilo):
        """
        Vrne modulsko obratno vrednost števila stevilo. Število se nahaja
        v intervalu [1, p - 1], kjer je p modul množice trenutnega objekta.
        """
        obrat = 1
        while self.zmnozek(stevilo, obrat) != 1:
            obrat += 1

        return obrat

    def kolicnik(self, prvo, drugo):
        """
        Vrne modulski količnik števil prvo in drugo. Parameter prvo se nahaja v intervalu [0, p  - 1], parameter drugo
        pa v intervalu [1, p  - 1].
        """
        return self.zmnozek(prvo, self.obratno(drugo))

    def potenca(self, stevilo, eksponent):
        """
        Vrne modulsko potenco števila 'stevilo' na število 'eksponent'. Parameter 'eksponent' se nahaja v intervalu
        [-10^3, 10^3]. Parameter 'stevilo' se nahaja v intervalu [1, p-1].
        """
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
        """
        Vrne moč množice (število elementov) modulskih kvadratnih korenov števila 'stevilo', torej število števil b
        iz intervala [0, p-1], za katera je produkt b * b (modulsko množenje) enak številu 'stevilo'.
        """
        st_korenov = 0
        for b in range(self.module):
            if self.zmnozek(b, b) == stevilo:
                st_korenov += 1
        return st_korenov

    def je_potenca(self, osnova, iskani_rezultat):
        """
        Preveri, če je 'iskani_rezultat' potenca števila 'osnova' v množici, ki jo predstavlja trenutni objekt.
        """
        potenca = 1
        for exp in range(self.module):
            if iskani_rezultat == potenca:
                return True
            potenca = self.zmnozek(potenca, osnova)
        return False

    def je_multiplikativni_generator(self, stevilo):
        """
        Vrne True natanko v primeru, če je število stevilo multiplikativni generator množice, ki jo predstavlja
        trenutni objekt. Parameter 'stevilo' se nahaja v intervalu [1, p  - 1].

        Pri implementaciji si lahko pomagaš s funkcijo je_potenca(osnova, iskani_rezultat).
        """
        for k in range(1, self.module):
            if not self.je_potenca(stevilo, k):
                return False
        return True


if __name__ == '__main__':
    z_7 = Zp(7)
    print(z_7.module)
