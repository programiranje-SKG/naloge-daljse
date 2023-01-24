
class Zp:
    def __init__(self, module):
        """
        Izdela objekt, ki predstavlja množico Z_modul.
        """
        self.module = module

    def vsota(self, prvo, drugo):
        """
        Vrne modulsko vsoto števil prvo in drugo v okviru množice, ki jo predstavlja trenutni objekt. Obe števili sta
        iz intervala [0, p-1], kjer je p modul množice trenutnega objekta.
        """
        pass

    def zmnozek(self, prvo, drugo):
        """
        Vrne modulski zmnožek števil prvo in drugo v okviru množice, ki jo predstavlja trenutni objekt. Obe števili sta
        iz intervala [0, p-1], kjer je p modul množice trenutnega objekta.
        """
        pass

    def nasprotno(self, stevilo):
        """
        Vrne modulsko nasprotno vrednost števila 'stevilo'. Število je iz intervala [0, p-1], kjer je p modul
        množice trenutnega objekta.
        """
        pass

    def razlika(self, prvo, drugo):
        """
        Vrne modulsko razliko števil prvo in drugo v okviru množice, ki jo predstavlja trenutni objekt. Obe števili sta
        iz intervala [0, p-1], kjer je p modul množice trenutnega objekta.
        """
        pass

    def obratno(self, stevilo):
        """
        Vrne modulsko obratno vrednost števila stevilo. Število se nahaja
        v intervalu [1, p - 1], kjer je p modul množice trenutnega objekta.
        """
        pass

    def kolicnik(self, prvo, drugo):
        """
        Vrne modulski količnik števil prvo in drugo. Parameter prvo se nahaja v intervalu [0, p  - 1], parameter drugo
        pa v intervalu [1, p  - 1].
        """
        pass

    def potenca(self, stevilo, eksponent):
        """
        Vrne modulsko potenco števila 'stevilo' na število 'eksponent'. Parameter 'eksponent' se nahaja v intervalu
        [-10^3, 10^3]. Parameter 'stevilo' se nahaja v intervalu [1, p-1].
        """
        pass

    def stevilo_kvadratnih_korenov(self, stevilo):
        """
        Vrne moč množice (število elementov) modulskih kvadratnih korenov števila 'stevilo', torej število števil b
        iz intervala [0, p-1], za katera je produkt b * b (modulsko množenje) enak številu 'stevilo'.
        """
        pass

    def je_potenca(self, osnova, iskani_rezultat):
        """
        Preveri, če je 'iskani_rezultat' potenca števila 'osnova' v množici, ki jo predstavlja trenutni objekt.
        """
        pass

    def je_multiplikativni_generator(self, stevilo):
        """
        Vrne True natanko v primeru, če je število stevilo multiplikativni generator množice, ki jo predstavlja
        trenutni objekt. Parameter 'stevilo' se nahaja v intervalu [1, p  - 1].

        Pri implementaciji si lahko pomagaš s funkcijo je_potenca(osnova, iskani_rezultat).
        """
        pass


if __name__ == '__main__':
    z_7 = Zp(7)
    print(z_7.module)
