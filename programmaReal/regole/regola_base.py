"""
classe madre comune.
Tutte le regole ereditano da `Regola` e devono implementare il metodo `verifica`.
In questo modo uso l’ereditarietà e mantengo il progetto ordinato.

"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Esito:
    nome: str  # Nome della regola controllata, ad esempio "controllo della lunghezza della password" .
    superata: bool  # True se la regola va bene, False altrimenti.
    punti: int  # Punti per dare un punteggio alla password.
    messaggio: str  # messaggio di risultato.
    suggerimento: str = ""  


# Regola e' una classe astratta: serve come modello per tutte le regole figlie.
class Regola(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    # @abstractmethod obbliga le classi figlie a riscrivere questo metodo.
    @abstractmethod
    def verifica(self, password: str) -> Esito:
        # Qui non scriviamo il controllo vero: lo faranno le classi figlie.
        pass
