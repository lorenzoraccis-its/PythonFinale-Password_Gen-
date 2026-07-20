
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