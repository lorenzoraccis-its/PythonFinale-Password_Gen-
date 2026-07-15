from getpass import getpass
import os
from programmaReal.gestore_regole import GestoreRegole
from programmaReal.generatore import genera_password_sicura
from programmaReal.stima.stimatoreBF import StimatoreBruteForce


SOGLIA_PASSWORD_ACCETTABILE = 65
LARGHEZZA = 78


class Colori:
    RESET = "\033[0m"
    GRASSETTO = "\033[1m"

    ROSSO = "\033[91m"
    VERDE = "\033[92m"
    GIALLO = "\033[93m"
    BLU = "\033[94m"
    VIOLA = "\033[95m"
    AZZURRO = "\033[96m"
    GRIGIO = "\033[90m"


def colore(testo, codice_colore):
    return f"{codice_colore}{testo}{Colori.RESET}"


def box_titolo(titolo):
    print()
    print(colore("╔" + "═" * (LARGHEZZA - 2) + "╗", Colori.VIOLA))
    print(
        colore("║", Colori.VIOLA)
        + colore(titolo.center(LARGHEZZA - 2), Colori.GRASSETTO)
        + colore("║", Colori.VIOLA)
    )
    print(colore("╚" + "═" * (LARGHEZZA - 2) + "╝", Colori.VIOLA))


def box_sezione(titolo, icona=""):
    print()
    testo = f"{icona} {titolo}".strip()

    print(colore("┌" + "─" * (LARGHEZZA - 2) + "┐", Colori.BLU))
    print(
        colore("│", Colori.BLU)
        + f" {testo}".ljust(LARGHEZZA - 2)
        + colore("│", Colori.BLU)
    )
    print(colore("└" + "─" * (LARGHEZZA - 2) + "┘", Colori.BLU))


def stampa_header():
    print()
    print(colore("╔" + "═" * (LARGHEZZA - 2) + "╗", Colori.AZZURRO))
    print(
        colore("║", Colori.AZZURRO)
        + colore("STIMATORE DI ROBUSTEZZA PASSWORD".center(LARGHEZZA - 2), Colori.GRASSETTO)
        + colore("║", Colori.AZZURRO)
    )
    print(colore("╚" + "═" * (LARGHEZZA - 2) + "╝", Colori.AZZURRO))


def badge_livello(livello):
    if livello == "Molto robusta":
        return colore("MOLTO ROBUSTA", Colori.VERDE)

    if livello == "Buona":
        return colore("BUONA", Colori.GIALLO)

    if livello == "Debole":
        return colore("DEBOLE", Colori.GIALLO)

    return colore("MOLTO DEBOLE", Colori.ROSSO)


def badge_esito(superata):
    if superata:
        return colore("OK", Colori.VERDE)

    return colore("NO", Colori.ROSSO)


def barra_punteggio(punteggio):
    lunghezza_barra = 34

    if punteggio < 0:
        punteggio = 0

    if punteggio > 100:
        punteggio = 100

    pieni = int((punteggio / 100) * lunghezza_barra)
    vuoti = lunghezza_barra - pieni

    if punteggio >= 85:
        colore_barra = Colori.VERDE
    elif punteggio >= 65:
        colore_barra = Colori.GIALLO
    else:
        colore_barra = Colori.ROSSO

    barra = "█" * pieni + "░" * vuoti

    return colore(barra, colore_barra) + f"  {punteggio}/100"


def formatta_riga(nome, valore):
    etichetta = f"{nome + ':':<24}"
    print(f"  {colore(etichetta, Colori.GRASSETTO)} {valore}")


def stampa_riepilogo(stima, punteggio, livello, mostra_password=False, password=""):
    box_sezione("Riepilogo generale", "📌")

    if mostra_password:
        formatta_riga("Password generata", colore(password, Colori.AZZURRO))

    formatta_riga("Lunghezza", stima["lunghezza"])
    formatta_riga("Livello", badge_livello(livello))
    formatta_riga("Punteggio", barra_punteggio(punteggio))


def stampa_controlli(esiti):
    box_sezione("Controlli di sicurezza", "🛡️")

    print(f"  {'ESITO':<10} {'CONTROLLO':<32} {'PUNTI':<8} MESSAGGIO")
    print("  " + "─" * 72)

    for esito in esiti:
        stato = badge_esito(esito.superata)

        print(
            f"  {stato:<18} "
            f"{esito.nome:<32} "
            f"{esito.punti:<8} "
            f"{esito.messaggio}"
        )


def stampa_tempi_bruteforce(stima):
    box_sezione("Quanto tempo servirebbe per forzarla?", "⚡")

    print(f"  {'PROFILO':<22} {'TEMPO MEDIO':<24} {'CASO PEGGIORE'}")
    print("  " + "─" * 72)

    for profilo in stima["profili"]:
        print(
            f"  {profilo['nome']:<22} "
            f"{profilo['tempo_medio_formattato']:<24} "
            f"{profilo['tempo_peggiore_formattato']}"
        )


def stampa_suggerimenti(suggerimenti):
    box_sezione("Suggerimenti operativi", "💡")

    if not suggerimenti:
        print(colore("  Nessun intervento urgente richiesto.", Colori.VERDE))
        print("  La password ha già un buon livello di sicurezza.")
        return

    for numero, suggerimento in enumerate(suggerimenti, start=1):
        print(f"  {colore(str(numero) + '.', Colori.GIALLO)} {suggerimento}")


def stampa_esito_finale(risultato):
    punteggio = risultato["punteggio"]
    livello = risultato["livello"]
    suggerimenti = risultato["suggerimenti"]

    box_titolo("ESITO FINALE")

    if punteggio >= SOGLIA_PASSWORD_ACCETTABILE:
        print(colore("  VALIDAZIONE SUPERATA", Colori.VERDE))
        print(f"  Livello rilevato: {badge_livello(livello)}")
        print("  La password inserita non è stata modificata.")
        print("  Stato complessivo: password accettabile.")
    else:
        print(colore("  VALIDAZIONE NON SUPERATA", Colori.ROSSO))
        print(f"  Livello rilevato: {badge_livello(livello)}")
        print("  La password inserita non è stata modificata.")
        print("  Stato complessivo: servono miglioramenti.")

        stampa_suggerimenti(suggerimenti)


def analizza_password(titolo, password, mostra_password=False):
    gestore = GestoreRegole()
    stimatore = StimatoreBruteForce()

    esiti = gestore.valuta(password)
    punteggio = gestore.calcola_punteggio(esiti)
    livello = gestore.calcola_livello(punteggio)
    suggerimenti = gestore.ricava_suggerimenti(esiti)

    dimensione_alfabeto = gestore.dimensione_alfabeto(password)
    stima = stimatore.stima(password, dimensione_alfabeto)

    box_titolo(titolo)

    stampa_riepilogo(
        stima=stima,
        punteggio=punteggio,
        livello=livello,
        mostra_password=mostra_password,
        password=password
    )

    stampa_controlli(esiti)
    stampa_tempi_bruteforce(stima)

    return {
        "punteggio": punteggio,
        "livello": livello,
        "suggerimenti": suggerimenti,
        "esiti": esiti,
        "stima": stima
    }


def main():
    os.system("cls" if os.name == "nt" else "clear")
    stampa_header()

    print()
    password = getpass(colore("Inserisci la password da valutare: ", Colori.GRASSETTO))

    risultato = analizza_password(
        titolo="ANALISI PASSWORD INSERITA",
        password=password,
        mostra_password=False
    )

    stampa_esito_finale(risultato)

    print()
    scelta = input(
        colore("Vuoi generare una password sicura di esempio? (s/n): ", Colori.GRASSETTO)
    ).lower().strip()

    if scelta == "s":
        password_generata = genera_password_sicura(16)

        analizza_password(
            titolo="PASSWORD GENERATA CON SECRETS",
            password=password_generata,
            mostra_password=True
        )

    print()
    print(colore("╔" + "═" * (LARGHEZZA - 2) + "╗", Colori.VERDE))
    print(
        colore("║", Colori.VERDE)
        + "Analisi completata.".center(LARGHEZZA - 2)
        + colore("║", Colori.VERDE)
    )
    print(colore("╚" + "═" * (LARGHEZZA - 2) + "╝", Colori.VERDE))
    print()


if __name__ == "__main__":
    main()