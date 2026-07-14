from getpass import getpass

from programmaReal.gestore_regole import GestoreRegole
from programmaReal.generatore import genera_password_sicura


SOGLIA_PASSWORD_ACCETTABILE = 65


def linea(carattere="=", lunghezza=60):
    print(carattere * lunghezza)


def titolo_principale():
    linea("=")
    print("STIMATORE DI ROBUSTEZZA PASSWORD".center(60))
    linea("=")


def titolo_sezione(titolo):
    print()
    linea("=")
    print(titolo)
    linea("=")


def sottotitolo(titolo):
    print()
    print(titolo)
    linea("-", len(titolo))


def stampa_riepilogo(punteggio, livello):
    sottotitolo("RIEPILOGO GENERALE")
    print(f"Punteggio totale:     {punteggio}/100")
    print(f"Livello sicurezza:    {livello}")


def stampa_controlli(esiti):
    sottotitolo("CONTROLLI DI SICUREZZA")

    print(f"{'ESITO':<8} {'CONTROLLO':<30} MESSAGGIO")
    linea("-", 60)

    for esito in esiti:
        stato = "OK" if esito.superata else "NO"
        print(f"{stato:<8} {esito.nome:<30} {esito.messaggio}")


def stampa_suggerimenti(suggerimenti):
    sottotitolo("SUGGERIMENTI")

    if not suggerimenti:
        print("Nessun suggerimento urgente.")
        return

    for numero, suggerimento in enumerate(suggerimenti, start=1):
        print(f"{numero}. {suggerimento}")


def stampa_esito_finale(punteggio, livello, suggerimenti):
    titolo_sezione("ESITO FINALE")

    if punteggio >= SOGLIA_PASSWORD_ACCETTABILE:
        print("VALIDAZIONE SUPERATA")
        print(f"La password risulta accettabile. Livello rilevato: {livello}")
        print("La password inserita non è stata modificata.")
    else:
        print("VALIDAZIONE NON SUPERATA")
        print(f"La password non è abbastanza robusta. Livello rilevato: {livello}")
        print("La password inserita non è stata modificata dal programma.")
        stampa_suggerimenti(suggerimenti)


def analizza_password(titolo, password, mostra_password=False):
    gestore = GestoreRegole()

    esiti = gestore.valuta(password)
    punteggio = gestore.calcola_punteggio(esiti)
    livello = gestore.calcola_livello(punteggio)
    suggerimenti = gestore.ricava_suggerimenti(esiti)

    titolo_sezione(titolo)

    if mostra_password:
        print(f"Password generata: {password}")

    stampa_riepilogo(punteggio, livello)
    stampa_controlli(esiti)

    return {
        "punteggio": punteggio,
        "livello": livello,
        "suggerimenti": suggerimenti,
        "esiti": esiti
    }


def main():
    titolo_principale()

    password = getpass("Inserisci la password da valutare: ")

    risultato = analizza_password(
        titolo="ANALISI PASSWORD INSERITA",
        password=password,
        mostra_password=False
    )

    stampa_esito_finale(
        punteggio=risultato["punteggio"],
        livello=risultato["livello"],
        suggerimenti=risultato["suggerimenti"]
    )

    print()
    scelta = input("Vuoi generare una password sicura di esempio? (s/n): ").lower().strip()

    if scelta == "s":
        password_generata = genera_password_sicura(16)

        analizza_password(
            titolo="ANALISI PASSWORD GENERATA CON SECRETS",
            password=password_generata,
            mostra_password=True
        )

    print()
    linea("=")
    print("Fine programma.")
    linea("=")


if __name__ == "__main__":
    main()