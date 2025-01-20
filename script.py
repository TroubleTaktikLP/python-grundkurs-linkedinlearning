#!/usr/bin/env python3

# Aufgabe: Erstellen Sie eine Klasse 'BankAccount', die ein einfaches Bankkonto repräsentiert.

# 1. Die Klasse soll die folgenden Attribute (Member-Variablen) haben:
#    - Inhaber: Der Name des Kontoinhabers (öffentlich).
#    - Kontonummer: Eine eindeutige Kontonummer (öffentlich).
#    - __kontostand: Der aktuelle Kontostand (nicht öffentlich).

# 2. Implementieren Sie die folgenden Methoden:
#    - __init__: Initialisiert den Kontoinhaber, die Kontonummer und den anfänglichen Kontostand.
#    - einzahlen: Erhöht den Kontostand um einen bestimmten Betrag.
#    - abheben: Verringert den Kontostand um einen bestimmten Betrag, wenn genügend Guthaben vorhanden ist.
#    - get_kontostand: Gibt den aktuellen Kontostand zurück.

# 3. Implementieren Sie außerdem eine Methode __str__, die eine benutzerfreundliche Darstellung des Kontos zurückgibt.

# Optional:
# - Erstellen Sie eine Methode, die Transaktionen protokolliert und eine Liste von Ein- und Auszahlungen ausgibt.

class BankAccount:

    def __init__(self, inhaber: str, kontonummer: int, _kontostand: float):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self._kontostand = _kontostand
        self._transactions = []

    def __str__(self):
        return (f"Der Kontoinhaber {self.inhaber} mit der Kontonummer "
                f"{self.kontonummer} hat einen Kontostand von {self.get_kontostand()}.")

    def get_kontostand(self):
        return self._kontostand

    def einzahlen(self, betrag: float):
        self._kontostand += betrag
        self._transactions.append(dict(betrag=betrag, kontostand=self._kontostand))

    def abheben(self, betrag: float):
        if self._kontostand > betrag:
            self._kontostand -= betrag
            self._transactions.append(dict(betrag=-betrag, kontostand=self._kontostand))
        else:
            print("Du hast nicht genug Guthaben auf dem Konto.")

    def get_transactions(self):
        for transaction in self._transactions:
            print("Transaktion:", transaction["betrag"], "bei einem Kontostand von", transaction["kontostand"])

if __name__ == "__main__":
    thomas = BankAccount("Thomas Müller", 42544423235, 100.30)
    print(thomas)
    thomas.einzahlen(100.43)
    print(thomas.get_kontostand())
    thomas.abheben(100.43)
    thomas.get_transactions()