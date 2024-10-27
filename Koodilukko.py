"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 50503188
Name:       Tuomas Kiiskinen
Email:      tuomas.kiiskinen1@gmail.com     tai     tuomas.kiiskinen@tuni.fi
Koodilukko

Projektini on koodilukko, joka vaatii nelinumeroisen oikean koodin ja niiden
jälkeen #-näppäiltynä, jotta tulisi vihreä valo eli pääsisi sisään.
Jos koodi on väärin syttyy punainen valo. Oletuskoodi on: 0000.

Jos haluaa vaihtaa sisäänpääsykoodia täytyy painaa neljä oikeaa numeroa
ja sitten lisäksi *-nappulaa. Mikäli koodi meni oikein tulee syötön ajaksi keltainen
valo. Kun haluttu tuleva nelinumeroinen koodi on syötetty täytyy painaa
vielä *-nappulaa ja uusi koodi tallentuu.

Tätä työtä tehdessäni tähtäsin kehittyneeseen versioon projektista.
"""


from tkinter import *


class laskin:
    def __init__(self):
        self.__ikkuna = Tk()
        self.__ikkuna.title("Koodilukko")
        self.__ikkuna.option_add("*Font", "Verdana 36")

        self.__koodi = ["0", "0", "0", "0"]     #Oletuskoodi lukolle
        self.__painallukset = []        #Näppäinyhdistelmät joita on painettu

        self.__tuleva_koodi = False     #totuusarvo, joka kertoo kirjoitetaanko uutta koodia


        #Numeroiden syötekenttä
        self.__teksti_kentta = Label(self.__ikkuna, text="", width=13, height=1,
                                     background="black", foreground="red")
        self.__teksti_kentta.grid(row=1, column=0, columnspan=5, sticky=N+W)

        # Väriä vaihtava suorakaide
        self.__valo = Label(self.__ikkuna, width=3, height=8,
                            background="white",
                            relief="raised")
        self.__valo.grid(row=1, column=4, rowspan=5)


        laskuri = 0

        nappaimet = [("nro1", "1"), ("nro2", "2"),
                     ("nro3", "3"),
                     ("nro4", "4"), ("nro5", "5"),
                     ("nro6", "6"),
                     ("nro7", "7"), ("nro8", "8"),
                     ("nro9", "9"),
                     ("kerroin", "*"), ("nro0", "0"),
                     ("risuaita", "#")]

        self.__nappulat = []           #Self.__nappulat on tulevien nappuloiden
                                       #lista, johon syötetään
                                       #yllä olevan listan arvot.

        # Syöttää jokaisen nappulan erikseen näytölle, ja vaihtaa niistä
        # merkin, eteenpäin menevän syötteen, rivin ja sarakkeen.
        for rivi in range(2, 6):

            for sarake in range(1, 4):

                nappain, merkki = nappaimet[laskuri]

                nappain = Button(self.__ikkuna, text=merkki, width=4, height=1,
                                 background="grey", foreground="white",
                                 command=lambda merkki=merkki: self.suoritus(merkki))

                nappain.grid(row=rivi, column=sarake)
                self.__nappulat.append(nappain)      #Tallentaa edellä
                laskuri = laskuri + 1                #syötetyn nappulan listaan



        self.__ikkuna.mainloop()



    def suoritus(self, nappain):
        """Saa painetut nappulat parametreinaan ja suorittaa nappulalle
        tarkoitetut toimenpiteet."""

        self.syotteen_tarkistus(nappain)        #Lisää tarvittavat painallukset

        self.syotteen_paivitys()        #Päivittää syötteet näytölle

        if self.__tuleva_koodi == True:       #jos haluttiin syöttää uusi koodi arvo on True
            if len(self.__painallukset) == 4 and nappain == "*":
                self.uuden_koodin_syotto()      #Suoritetaan tulevan koodin tallennus
                return

        elif nappain == "*":            #jos menee oikein syttyy keltainen valo
            self.__tuleva_koodi = self.uusi_koodi()
            return

        if nappain == "#" and not self.__tuleva_koodi:   #Kokeillaan oliko sisäänpääsykoodi oikein
            self.koodin_tarkistus()   #jos painallus on: #.


    def uusi_koodi(self):
        """Kokeilee onko syötetty koodi oikein. Jos koodi on oikein, syttyy
        keltainen valo ja funktio palauttaa True. Jos koodi on väärin syttyy
        punainen valo ja funktio palauttaa False."""

        if self.__painallukset == self.__koodi:
            self.__painallukset.clear()
            self.__valo.configure(background="yellow")
            self.__teksti_kentta.configure(text="")
            return True

        else:
            self.__painallukset.clear()
            self.__valo.configure(background="red")
            self.__teksti_kentta.configure(text="")
            return False


    def syotteen_tarkistus(self, nappain):
        """Saa parametrinaan syötetyn näppäimen. Jos näppäin on numero, lisätään
        se jo syötettyjen numeroiden perään. Jos numeroita on jo neljä, poistetaan
        vanhin numero."""

        if not self.__tuleva_koodi:                     #Kokeilee syötetäänkö
            self.__valo.configure(background="white")#Tulevaa sisäänpääsykoodia

        if nappain != "*" and nappain != "#":
            self.__painallukset.append(nappain)     #lisää painalluksen listaan
                                                #Muistiin jos se ei ole # tai *
        painallukset = ""
        for nro in self.__painallukset:
            painallukset = painallukset + nro

        if len(painallukset) > 4:           #Jos painettuja numeroita on jo
            self.__painallukset.pop(0)      #neljä ennestään, poistetaan vanhin


    def uuden_koodin_syotto(self):
        """Tallentaa uudet syöttetyt numerot vanhan sisäänpääsykoodin tilalle"""

        self.__koodi = []                  #Muuntaa painallukset listasta stringiksi
        for nro in self.__painallukset:
            self.__koodi.append(nro)

        #Nollaa tekstikentät, syötteet ja Muuttaa värin valkoiseksi. Muuttaa
        #self.__tuleva_koodi Falseksi joten, tiedetään että tuleva koodi
        # on kirjoitettu
        self.__valo.configure(background="white")
        self.__tuleva_koodi = False
        self.__teksti_kentta.configure(text="")
        self.__painallukset = []


    def koodin_tarkistus(self):
        """Kokeilee onko syötetty nelinumeroinen koodi oikein. Jos on oikein,
        syttyy vihreä valo. Jos syöte on väärin syttyy punainen valo.
        Näiden jälkeen nollataan tekstikenttä sekä painallukset."""

        if self.__painallukset == self.__koodi:      #jos koodi menee oikein syttyy vihreä valo
            self.__valo.configure(background="green")

        else:
            self.__valo.configure(background="red")

        self.__teksti_kentta.configure(text="")
        self.__painallukset.clear()


    def syotteen_paivitys(self):
        """Päivittää laskimen näytölle syötetyt numerot."""

        teksti = ""
        for numero in self.__painallukset:
            teksti = teksti + numero
        self.__teksti_kentta.configure(text=teksti)



def main():
    suoritus = laskin()


if __name__ == "__main__":
    main()
