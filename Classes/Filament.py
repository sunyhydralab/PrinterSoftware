class Filament:
    def __init__(self, color=None, amount=None):
        self._color = color
        self._amountRemaining = amount

    def changeColor(self, color):
        self._color = color

    def getColor(self):
        return self._color

    def useFilament(self, used):
        self._amountRemaining -= used

    def getFilament(self):
        return self._amountRemaining

    def setFilament(self, amount):
        self._amountRemaining = amount

    def isEmpty(self):
        return self._amountRemaining <= 0

    def willBeEmpty(self, jobSize):
        return self._amountRemaining - jobSize <= 0
