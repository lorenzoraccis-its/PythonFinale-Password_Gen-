from programmaReal.regole.regola_base import Regola, Esito


class RegolaPattern(Regola):
    def __init__(self):
        super().__init__("Controllo pattern deboli")

    def ha_ripetizioni(self, password: str) -> bool:
        """
        Controlla ripetizioni tipo:
        aaa, 111, !!!, zzz
        """

        for i in range(len(password) - 2):
            if password[i] == password[i + 1] == password[i + 2]:
                return True

        return False

    def ha_sequenze(self, password: str) -> bool:
        """
        Controlla sequenze semplici tipo:
        abc, bcd, 123, 234, qwe
        """

        password = password.lower()

        sequenze_note = [
            "abcdefghijklmnopqrstuvwxyz",
            "0123456789",
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
        ]

        for sequenza in sequenze_note:
            for i in range(len(sequenza) - 2):
                pezzo = sequenza[i:i + 3]

                if pezzo in password:
                    return True

                if pezzo[::-1] in password:
                    return True

        return False

    def verifica(self, password: str) -> Esito:
        problemi = []

        if self.ha_ripetizioni(password):
            problemi.append("ripetizioni")

        if self.ha_sequenze(password):
            problemi.append("sequenze")

        if problemi:
            return Esito(
                nome=self.nome,
                superata=False,
                punti=0,
                messaggio=f"Pattern deboli trovati: {', '.join(problemi)}.",
                suggerimento="Evita sequenze come abc/123/qwe e ripetizioni come aaa/111."
            )

        return Esito(
            nome=self.nome,
            superata=True,
            punti=15,
            messaggio="Non sono stati trovati pattern deboli evidenti.",
            suggerimento=""
        )