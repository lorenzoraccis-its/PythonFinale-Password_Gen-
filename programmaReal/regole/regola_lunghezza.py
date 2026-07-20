from regole.regola_base import Regola, Esito


class RegolaLunghezza(Regola):
    def __init__(self, lunghezza_minima: int = 12):
        super().__init__("Controllo lunghezza")
        self.lunghezza_minima = lunghezza_minima

    def verifica(self, password: str) -> Esito:
        lunghezza = len(password)

        if lunghezza >= 16:
            return Esito(
                nome=self.nome,
                superata=True,
                punti=30,
                messaggio=f"Lunghezza ottima: {lunghezza} caratteri.",
                suggerimento=""
            )

        if lunghezza >= self.lunghezza_minima:
            return Esito(
                nome=self.nome,
                superata=True,
                punti=25,
                messaggio=f"Lunghezza buona: {lunghezza} caratteri.",
                suggerimento="Per alzare ancora il livello, puoi arrivare almeno a 16 caratteri."
            )

        return Esito(
            nome=self.nome,
            superata=False,
            punti=5,
            messaggio=f"Password troppo corta: {lunghezza} caratteri.",
            suggerimento=f"Porta la password almeno a {self.lunghezza_minima} caratteri."
        )