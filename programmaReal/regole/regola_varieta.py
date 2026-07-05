import string

from programmaReal.regole.regola_base import Regola, Esito


class RegolaVarietaCaratteri(Regola):
    MINUSCOLE = string.ascii_lowercase
    MAIUSCOLE = string.ascii_uppercase
    CIFRE = string.digits
    SIMBOLI = string.punctuation

    def __init__(self):
        super().__init__("Controllo varietà caratteri")

    @classmethod
    def contiene_minuscole(cls, password: str) -> bool:
        return any(c in cls.MINUSCOLE for c in password)

    @classmethod
    def contiene_maiuscole(cls, password: str) -> bool:
        return any(c in cls.MAIUSCOLE for c in password)

    @classmethod
    def contiene_cifre(cls, password: str) -> bool:
        return any(c in cls.CIFRE for c in password)

    @classmethod
    def contiene_simboli(cls, password: str) -> bool:
        return any(c in cls.SIMBOLI for c in password)

    @classmethod
    def gruppi_presenti(cls, password: str) -> list[str]:
        gruppi = []

        if cls.contiene_minuscole(password):
            gruppi.append("minuscole")

        if cls.contiene_maiuscole(password):
            gruppi.append("maiuscole")

        if cls.contiene_cifre(password):
            gruppi.append("cifre")

        if cls.contiene_simboli(password):
            gruppi.append("simboli")

        return gruppi

    @classmethod
    def calcola_dimensione_alfabeto(cls, password: str) -> int:
        """
        Calcola |alfabeto| in base ai tipi di caratteri presenti.
        Esempio:
        - solo minuscole: 26
        - minuscole + maiuscole: 52
        - minuscole + maiuscole + cifre + simboli: 94 circa
        """

        dimensione = 0

        if cls.contiene_minuscole(password):
            dimensione += 26

        if cls.contiene_maiuscole(password):
            dimensione += 26

        if cls.contiene_cifre(password):
            dimensione += 10

        if cls.contiene_simboli(password):
            dimensione += 32

        return dimensione

    def verifica(self, password: str) -> Esito:
        gruppi = self.gruppi_presenti(password)
        numero_gruppi = len(gruppi)

        if numero_gruppi == 4:
            return Esito(
                nome=self.nome,
                superata=True,
                punti=30,
                messaggio="Ottima varietà: sono presenti minuscole, maiuscole, cifre e simboli.",
                suggerimento=""
            )

        if numero_gruppi == 3:
            return Esito(
                nome=self.nome,
                superata=True,
                punti=22,
                messaggio=f"Buona varietà: gruppi presenti: {', '.join(gruppi)}.",
                suggerimento="Per migliorare, aggiungi anche il gruppo mancante."
            )

        if numero_gruppi == 2:
            return Esito(
                nome=self.nome,
                superata=False,
                punti=10,
                messaggio=f"Varietà bassa: gruppi presenti: {', '.join(gruppi)}.",
                suggerimento="Aggiungi maiuscole, minuscole, cifre e simboli."
            )

        return Esito(
            nome=self.nome,
            superata=False,
            punti=0,
            messaggio="Varietà molto bassa: la password usa quasi un solo tipo di carattere.",
            suggerimento="Usa un mix di minuscole, maiuscole, numeri e simboli."
        )