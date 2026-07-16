
from programmaReal.gestore_regole import GestoreRegole

from programmaReal.stima.stimatoreBF import StimatoreBruteForce
import estetica

class AnalizzatorePassword:
    def __init__(self):
        self.gestore = GestoreRegole()
        self.stimatore = StimatoreBruteForce()

    def analizza_password(titolo, password, mostra_password=False):
        gestore = GestoreRegole()
        stimatore = StimatoreBruteForce()

        esiti = gestore.valuta(password)
        punteggio = gestore.calcola_punteggio(esiti)
        livello = gestore.calcola_livello(punteggio)
        suggerimenti = gestore.ricava_suggerimenti(esiti)

        dimensione_alfabeto = gestore.dimensione_alfabeto(password)
        stima = stimatore.stima(password, dimensione_alfabeto)

        estetica.box_titolo(titolo)

        estetica.stampa_riepilogo(
            stima=stima,
            punteggio=punteggio,
            livello=livello,
            mostra_password=mostra_password,
            password=password
        )
        input("Premi INVIO per continuare...")
        estetica.stampa_controlli(esiti)
        estetica.stampa_tempi_bruteforce(stima)
        input("Premi INVIO per continuare...")
        return {
            "punteggio": punteggio,
            "livello": livello,
            "suggerimenti": suggerimenti,
            "esiti": esiti,
            "stima": stima
        }