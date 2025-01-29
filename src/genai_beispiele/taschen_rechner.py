# Klasse TasschenRechner
# Beispiel für eine Klasse, die eine einfache Taschenrechner-Funktionalität 
# bereitstellt. Die Klasse enthält die Methoden add, sub, mul und div. Bei
# der Division soll eine Division durch 0 abgefangen werden und eine Exception
# geworfen werden. Der Taschenrechner beinhaltet die letzeten drei Rechnungen
# Ergebnise in seinem Speicher und können abefragt werden.
# Die Klasse soll mit unit tests getestet werden.

class Taschenrechner():
    def __init__(self):
        self._ergebnisse = []
        self._eingabe1 = []
        self._eingabe2 = []
        self._operator = []

    def verlauf(self, eingabe1, eingabe2, ergebnis, operator):
        if(len(self._ergebnisse) == 3):
            self._ergebnisse.pop(0)
            self._eingabe1.pop(0)
            self._eingabe2.pop(0)
            self._operator.pop(0)
        self._ergebnisse.append(ergebnis)
        self._eingabe1.append(eingabe1)
        self._eingabe2.append(eingabe2)
        self._operator.append(operator)

    def sum(self, eingabe1, eingabe2):
        ergebnis = eingabe1 + eingabe2
        self.verlauf(eingabe1, eingabe2, ergebnis, "+")
        return ergebnis

    def sub(self, eingabe1, eingabe2):
        ergebnis = eingabe1 - eingabe2
        self.verlauf(eingabe1, eingabe2, ergebnis, "-")
        return ergebnis

    def mul(self, eingabe1, eingabe2):
        ergebnis = eingabe1 * eingabe2
        self.verlauf(eingabe1, eingabe2, ergebnis, "*")
        return ergebnis

    def div(self, eingabe1, eingabe2):
        if (eingabe2 == 0):
            raise ValueError("Division durch 0 nicht möglich")
        ergebnis = eingabe1 / eingabe2
        self.verlauf(eingabe1, eingabe2, ergebnis, "/")
        return ergebnis

    def __str__(self):
        verlauf = "\n"
        for i in range(len(self._ergebnisse)):
            verlauf += f"{self._eingabe1[i]} {self._operator[i]} {self._eingabe2[i]} = {self._ergebnisse[i]}\n"
        return verlauf
