class VierGewinnt:
    def __init__(self, hoehe=6, breite=7):
        self.hoehe = hoehe
        self.breite = breite
        self.spielbrett = [[' ' for x in range(breite)] for i in range(hoehe)]