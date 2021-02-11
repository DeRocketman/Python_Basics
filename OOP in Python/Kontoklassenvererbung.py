class VerwalteterGeldbetrag:
    def __init__(self, anfangsbetrag):
        self.Betrag = anfangsbetrag

    def einzahlenMoeglich(self, betrag):
        return True

    def auszahlenMoeglich(self, betrag):
        return True

    def einzahlen(self, betrag):
        if betrag < 0 or not self.einzahlenMoeglich(betrag):
            return False
        else:
            self.Betrag += betrag
            return True

    def auszahlen(self, betrag):
        if betrag < 0 or not self.auszahlenMoeglich(betrag):
            return False
        else:
            self.Betrag -= betrag
            return True

    def zeige(self):
        print("Betrag: {:.2f}".format(self.Betrag))


class AllgemeinesKonto(VerwalteterGeldbetrag):
    def __init__(self, kundendaten, kontostand):
        super().__init__(kontostand)
        self.Kundendaten = kundendaten

    def geldtransfer(self, ziel, betrag):
        if self.auszahlenMoeglich(betrag) and ziel.einzahlenMoeglich(betrag):
            self.auszahlen(betrag)
            self.einzahlen(betrag)
            return True
        else:
            return False

    def zeige(self):
        self.Kundendaten.zeige()
        VerwalteterGeldbetrag.zeige(self)


class AllgemeinesKontoMitTagesumsatz(AllgemeinesKonto):
    def __init__(self, kundendaten, kontostand, max_tagesumsatz=1500):
        super().__init__(kundendaten, kontostand)
        self.MaxTagesumsatz = max_tagesumsatz
        self.UmsatzHeute = 0.0

    def transferMoeglich(self, betrag):
        return self.UmsatzHeute + betrag <= self.MaxTagesumsatz

    def auszahlenMoeglich(self, betrag):
        return self.transferMoeglich(betrag)

    def einzahlenMoeglich(self, betrag):
        return self.transferMoeglich(betrag)

    def einzahlen(self, betrag):
        if AllgemeinesKonto.einzahlen(self, betrag):
            self.UmsatzHeute += betrag
            return True
        else:
            return False

    def auszahlen(self, betrag):
        if AllgemeinesKonto.auszahlen(self, betrag):
            self.UmsatzHeute += betrag
            return True
        else:
            return False

    def zeige(self):
        AllgemeinesKonto.zeige(self)
        print("Heute schon {:.2f} von {:.2f} Euro umgesetzt".format(self.UmsatzHeute, self.MaxTagesumsatz))


class GirokontoKundendaten:
    def __init__(self, inhaber, kontonummer):
        self.Inhaber = inhaber
        self.Kontonummer = kontonummer

    def zeige(self):
        print("Inhaber:", self.Inhaber)
        print("Kontonummer:", self.Kontonummer)


class GirokontoMitTagesumsatz(AllgemeinesKontoMitTagesumsatz):
    def __init__(self, inhaber, kontonummer, kontostand, max_tagesumsatz=1500):
        kundendaten = GirokontoKundendaten(inhaber, kontonummer)
        super().__init__(kundendaten, kontostand, max_tagesumsatz)


# Die Vererbung wurde im oberen Bereich dargestellt. Die Entwicklung von main.py zu diesem Skript ist sehr
# gut nach zu vollziehen.

k1 = GirokontoMitTagesumsatz("Heini Meinsi", 99003231, 3200.0)
k2 = GirokontoMitTagesumsatz("Moritz Pusemukkel", 99003239, 2500.0)

print("Kontodaten vor Umsatzentwicklung:")
print("")
k1.zeige()
print("")
k2.zeige()

print(k1.geldtransfer(k2, 160))
print(k2.geldtransfer(k1, 500))
print(k1.geldtransfer(k1, 840))
print(k2.einzahlen(5000))

print("Kontodaten nach Umsatzentwicklung:")
print("")
k1.zeige()
print("")
k2.zeige()
