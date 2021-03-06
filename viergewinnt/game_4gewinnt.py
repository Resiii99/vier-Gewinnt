"""
Module Docstring
Spieler 1 hat den Spielstein X
Spieler 2 hat den Spielstein O
"""
from random import randint


class VierGewinnt:
    """
    Klasse erstellt ein Spiel 4gewinnt
    """
    def __init__(self, hoehe=6, breite=7):
        self.hoehe = hoehe
        self.breite = breite
        self.spielbrett = [[' ' for x in range(breite)] for i in range(hoehe)]
        self.gespielte_Steine = 0

    def get_spalte(self, index: int):
        """
        Gibt eine Spalte am angegebenen Index aus

        Parameter
        -------------
        index:  int
                Index, welche Spalte ausgegeben wird

        Returns
        -------------
        List: Spalte
        """
        return [i[index] for i in self.spielbrett]

    def get_reihe(self, index: int):
        """
        Gibt eine Reihe am angegebenen Index aus

        Parameter
        -------------
        index:  int
                Index, welche Reihe ausgegeben wird

        Returns
        -------------
        List: Reihe
        """
        return self.spielbrett[index]

    def get_diagonale(self):
        """
        Gibt alle Diagonalen im Spiel aus
        """
        diagonale = []

        for i in range(self.hoehe + self.breite - 1):
            diagonale.append([])
            for j in range(max(i - self.hoehe + 1, 0), min(i + 1, self.hoehe)):
                diagonale[i].append(self.spielbrett[self.hoehe - i + j - 1][j])

        for i in range(self.hoehe + self.breite - 1):
            diagonale.append([])
            for j in range(max(i - self.hoehe + 1, 0), min(i + 1, self.hoehe)):
                diagonale[i].append(self.spielbrett[i - j][j])

        return diagonale

    def spielzug_machen(self, team: str, spl: int):
        """
        Macht einen Spielzug --> Setzt in der angegebenen Spalte ein X oder O an die unterste freie Stelle einer Spalte

        Parameter
        -------------
        team:   str
                X oder O
        spl:    int
                Spalte, die vom Spieler per Input ausgewählt wird

        Returns
        -------------
        List: Spielbrett

        """

        i = self.hoehe - 1
        while self.spielbrett[i][spl] != ' ':
            i -= 1
        self.spielbrett[i][spl] = team
        self.gespielte_Steine += 1
        return self.spielbrett

    def check_gewonnen(self):
        """
        Überprüft das Spielbrett nach jedem Spielzug auf eine der beiden Gewinnvarianten.
        4 X oder O in einer Reihe (Reihe, Spalte, Diagonale).
        Wenn kein Gewinn eruiert wird, soll keine Ausgabe erfolgen.
        """
        vier_in_einer_reihe_x = [['X', 'X', 'X', 'X']]
        vier_in_einer_reihe_o = [['O', 'O', 'O', 'O']]

        # Reihencheck:
        for i in range(self.hoehe):
            for j in range(self.breite - 3):
                if self.get_reihe(i)[j:j + 4] in vier_in_einer_reihe_x:
                    return "Spieler 1"

                if self.get_reihe(i)[j:j + 4] in vier_in_einer_reihe_o:
                    return "Spieler 2"

        # Spaltencheck:
        for i in range(self.breite):
            for j in range(self.hoehe - 3):
                if self.get_spalte(i)[j:j + 4] in vier_in_einer_reihe_x:
                    return "Spieler 1"

                if self.get_spalte(i)[j:j + 4] in vier_in_einer_reihe_o:
                    return "Spieler 2"

        # Diagonalencheck:
        for i in self.get_diagonale():
            for j, _ in enumerate(i):
                if i[j:j + 4] in vier_in_einer_reihe_x:
                    return "Spieler 1"

                if i[j:j + 4] in vier_in_einer_reihe_o:
                    return "Spieler 2"

        return None

    def check_unentschieden(self):
        """
        Wenn das Spielfeld voll ist, soll das Spiel mit einem Unentschieden beendet werden.
        """
        maxspielsteine = self.breite*self.hoehe

        if self.gespielte_Steine >= maxspielsteine:
            return True
        else:
            return None

    def spiel_starten(self):
        """
        Startet ein Spiel. Das Spielfeld wird dargestellt, es wird der Spielmodus (Mensch gegen Mensch oder Mensch gegen
        Computer) festgelegt. Die Spieler werden nacheinander zum Input aufgefordert und ihre Spielzüge werden
        durchgeführt. Nach jeder Durchführung wird auf Gewinn überprüft. Bei Gewinn eines Spielers wird abgebrochen.
        """
        print("Willkommen bei 4 Gewinnt - vorab musst du festlegen, ob du gegen den Computer oder gegen einen Freund spielst:")
        spieleranzahl = int(input(f'Wähle 1 für ein Spiel gegen den Computer, oder 2 für ein Spiel gegen deinen Freund: '))

        if spieleranzahl == 2: #Spieleranzahl: 2 -> Mensch gegen Mensch
            while True:

                for i in self.spielbrett:
                    print(i)
                if self.check_gewonnen() is not None:
                    break
                if self.check_unentschieden() is True:
                    print("Unentschieden - Das spiel ist vorbei!")
                    return None

                spl = int(input(f'Spieler 1 – wähle eine Spalte von 1 bis {self.breite} : ')) - 1

                if spl > -1 and spl < self.breite and self.spielbrett[0][spl] == ' ':
                    self.spielzug_machen('X', spl)
                elif spl > -1 and spl < self.breite and self.spielbrett[0][spl] != ' ':
                    print(f'Diese Spalte ist voll. Wähle in der nächsten Runde ein leeres Feld.')
                else:
                    print(f'Bitte gib in der nächsten Runde eine Zahl zwischen 1 und {self.breite} ein!')

                for i in self.spielbrett:
                    print(i)
                if self.check_gewonnen() is not None:
                    break
                if self.check_unentschieden() is True:
                    print("Unentschieden - Das spiel ist vorbei!")
                    return None

                spl = int(input(f'Spieler 2 – bitte Spalte von 1 bis {self.breite} auswählen: ')) - 1

                if spl > -1 and spl < self.breite and self.spielbrett[0][spl] == ' ':
                    self.spielzug_machen('O', spl)
                elif spl > -1 and spl < self.breite and self.spielbrett[0][spl] != ' ':
                    print(f'Diese Spalte ist voll. Wähle in der nächsten Runde ein leeres Feld.')
                else:
                    print(f'Bitte gib in der nächsten Runde eine Zahl zwischen 1 und {self.breite} ein!')

            print(f'Gratuliere {self.check_gewonnen()}, du hast gewonnen!')

        elif spieleranzahl == 1: # Spieleranzahl 1 -> Mensch gegen Computer
            print("Humans first - du beginnst und das ist euer Spielfeld:")
            while True:

                for i in self.spielbrett:
                    print(i)
                if self.check_gewonnen() is not None:
                    break
                if self.check_unentschieden() is True:
                    print("Unentschieden - Das spiel ist Vorbei!")
                    return None

                spl = int(input(f'Wähle eine Spalte von 1 bis {self.breite} : ')) - 1

                if spl > -1 and spl < self.breite and self.spielbrett[0][spl] == ' ':
                    self.spielzug_machen('X', spl)
                elif spl > -1 and spl < self.breite and self.spielbrett[0][spl] != ' ':
                    print(f'Diese Spalte ist voll. Wähle in der nächsten Runde ein leeres Feld.')
                else:
                    print(f'Spielzug verschenkt! Gib in der nächsten Runde eine Zahl zwischen 1 und {self.breite} ein!')

                for i in self.spielbrett:
                    print(i)
                if self.check_gewonnen() is not None:
                    break
                if self.check_unentschieden() is True:
                    print("Unentschieden - Das spiel ist Vorbei!")
                    return None

                computer = randint(0, self.breite-1)
                if self.spielbrett[0][computer] == ' ':
                    print("Der Computer wählt die Spalte ", computer + 1)
                    self.spielzug_machen('O', computer)
                else:
                    print("Volle Spalte - Der Computer hat den Spielzug verschenkt.")


            if self.check_gewonnen() == "Spieler 1":
                print(f'Gratuliere {self.check_gewonnen()}, du hast den Computer geschlagen!')
            else:
                print("Schade, diese Runde geht an den Computer - Versuchs doch noch mal :-) ")
            if self.check_unentschieden() is True:
                print("Unentschieden - Das spiel ist Vorbei!")
                return None
        else:
            print("Starte das Spiel erneut und wähle eine gültige Spieleranzahl (1 oder 2)")


if __name__ == '__main__':
    meinspiel = VierGewinnt()
    meinspiel.spiel_starten()