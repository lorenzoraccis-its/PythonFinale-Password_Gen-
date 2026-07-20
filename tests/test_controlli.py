from generatore import genera_password_sicura
from gestore_regole import GestoreRegole
from stima.stimatoreBF import StimatoreBruteForce


def test_password_debole_viene_segnalata():
    gestore = GestoreRegole()
    esiti = gestore.valuta("password")

    assert gestore.calcola_livello(gestore.calcola_punteggio(esiti)) == "Molto debole"
    assert any(not esito.superata for esito in esiti)


def test_password_robusta_supera_tutti_i_controlli():
    gestore = GestoreRegole()
    esiti = gestore.valuta("V3nto!R0ssa#2026")

    assert gestore.calcola_punteggio(esiti) == 100
    assert all(esito.superata for esito in esiti)


def test_generatore_crea_password_di_almeno_sedici_caratteri():
    password = genera_password_sicura()
    gestore = GestoreRegole()

    assert len(password) >= 16
    assert gestore.dimensione_alfabeto(password) == 94


def test_stimatore_restituisce_tre_profili():
    stima = StimatoreBruteForce().stima("Ab1!", 94)

    assert stima["lunghezza"] == 4
    assert stima["dimensione_alfabeto"] == 94
    assert len(stima["profili"]) == 3
