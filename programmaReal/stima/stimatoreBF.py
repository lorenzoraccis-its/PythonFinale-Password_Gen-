import math
from stima.profilo_attaccante import ProfiloAttaccante


class StimatoreBruteForce:
    def __init__(self):
        # Valori configurabili: sono ipotesi dichiarate, non verità assolute.
        self.profili = [
            ProfiloAttaccante(
                nome="PC di casa",
                scenario="Una GPU consumer",
                guess_al_secondo=10**10
            ),
            ProfiloAttaccante(
                nome="Garage di GPU",
                scenario="Mini-cluster / mining rig",
                guess_al_secondo=10**12
            ),
            ProfiloAttaccante(
                nome="Supercomputer",
                scenario="Cluster HPC / hardware dedicato",
                guess_al_secondo=10**16
            )
        ]

    def calcola_spazio_chiavi(self, lunghezza: int, dimensione_alfabeto: int) -> int:
        """
        Formula:
        N = |alfabeto| ^ L
        """

        if lunghezza <= 0 or dimensione_alfabeto <= 0:
            return 0

        return dimensione_alfabeto ** lunghezza

    def calcola_entropia(self, lunghezza: int, dimensione_alfabeto: int) -> float:

        if lunghezza <= 0 or dimensione_alfabeto <= 0:
            return 0.0

        return lunghezza * math.log2(dimensione_alfabeto)

    def stima(self, password: str, dimensione_alfabeto: int) -> dict:
        lunghezza = len(password)

        spazio_chiavi = self.calcola_spazio_chiavi(
            lunghezza=lunghezza,
            dimensione_alfabeto=dimensione_alfabeto
        )

        entropia = self.calcola_entropia(
            lunghezza=lunghezza,
            dimensione_alfabeto=dimensione_alfabeto
        )

        risultati_profili = []

        for profilo in self.profili:
            if spazio_chiavi == 0:
                tempo_medio_secondi = 0
                tempo_peggiore_secondi = 0
            else:
                # Tempo medio = N / (2 * velocità)
                tempo_medio_secondi = spazio_chiavi / (2 * profilo.guess_al_secondo)

                # Caso peggiore = N / velocità
                tempo_peggiore_secondi = spazio_chiavi / profilo.guess_al_secondo

            risultati_profili.append({
                "nome": profilo.nome,
                "scenario": profilo.scenario,
                "guess_al_secondo": profilo.guess_al_secondo,
                "tempo_medio_secondi": tempo_medio_secondi,
                "tempo_peggiore_secondi": tempo_peggiore_secondi,
                "tempo_medio_formattato": self.formatta_tempo(tempo_medio_secondi),
                "tempo_peggiore_formattato": self.formatta_tempo(tempo_peggiore_secondi)
            })

        return {
            "lunghezza": lunghezza,
            "dimensione_alfabeto": dimensione_alfabeto,
            "spazio_chiavi": spazio_chiavi,
            "entropia": entropia,
            "profili": risultati_profili
        }

    @staticmethod
    def formatta_numero(numero: int) -> str:
        if numero < 1_000_000:
            return str(numero)

        testo = str(numero)
        esponente = len(testo) - 1
        mantissa = testo[0] + "," + testo[1:4]

        return f"{mantissa} × 10^{esponente}"

    @staticmethod
    def formatta_tempo(secondi: float) -> str:
        if secondi < 0.000001:
            return "meno di un microsecondo"

        if secondi < 0.001:
            return f"{secondi * 1_000_000:.2f} microsecondi"

        if secondi < 1:
            return f"{secondi * 1000:.2f} millisecondi"

        if secondi < 60:
            return f"{secondi:.2f} secondi"

        minuti = secondi / 60
        if minuti < 60:
            return f"{minuti:.2f} minuti"

        ore = minuti / 60
        if ore < 24:
            return f"{ore:.2f} ore"

        giorni = ore / 24
        if giorni < 365:
            return f"{giorni:.2f} giorni"

        anni = giorni / 365
        if anni < 100:
            return f"{anni:.2f} anni"

        secoli = anni / 100
        if secoli < 1000:
            return f"{secoli:.2f} secoli"

        return f"{anni:.2e} anni"