#!/usr/bin/env python3

from bank_account.bank_account import BankAccount


# Aufgabe: Erstellen Sie ein neues Jugendbankkonto, dass von der Klasse
# BankAccount erbt und beschränken sie die Abhebungen auf maximal 25€.

class JugendBankAccount(BankAccount):
    def abheben(self, betrag: float) -> None:
        if betrag <= 25:
            super().abheben(betrag)
        else:
            raise ValueError("Abhebung fehlgeschlagen: Maximalbetrag von 25 EUR überschritten.")
