"""
Classe madre comune.
Tutte le regole ereditano da 'Regola' e devono implementare il metodo 'verifica'.

In questo modo uso l'ereditarietà e mantengo il progetto ordinato.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Esito:
    nome: str
    superata: bool
    punti: int
    messaggio: str
    suggerimento: str = ""


class Regola(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    @abstractmethod
    def verifica(self, password: str) -> Esito:
        pass