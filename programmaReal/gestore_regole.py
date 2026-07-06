from programmaReal.regole.regola_base import Esito
from programmaReal.regole.regola_lunghezza import RegolaLunghezza
from programmaReal.regole.regola_varieta import RegolaVarietaCaratteri
from programmaReal.regole.regola_dizionario import RegolaDizionario
from programmaReal.regole.regola_pattern import RegolaPattern


class GestoreRegole:
    def __init__(self):
        self.regole = [
            RegolaLunghezza(),
            RegolaVarietaCaratteri(),
            RegolaDizionario(),
            RegolaPattern()
        ]

    def valuta(self, password: str) -> list[Esito]:
        esiti = []

        for regola in self.regole:
            esito = regola.verifica(password)
            esiti.append(esito)

        return esiti

    def calcola_punteggio(self, esiti: list[Esito]) -> int:
        totale = 0

        for esito in esiti:
            totale += esito.punti

        if totale > 100:
            totale = 100

        return totale

    def calcola_livello(self, punteggio: int) -> str:
        if punteggio >= 85:
            return "Molto robusta"

        if punteggio >= 65:
            return "Buona"

        if punteggio >= 40:
            return "Debole"

        return "Molto debole"

    def ricava_suggerimenti(self, esiti: list[Esito]) -> list[str]:
        suggerimenti = []

        for esito in esiti:
            if esito.suggerimento != "":
                suggerimenti.append(esito.suggerimento)

        return suggerimenti

    def dimensione_alfabeto(self, password: str) -> int:
        return RegolaVarietaCaratteri.calcola_dimensione_alfabeto(password)