from getpass import getpass

from programmaReal.gestore_regole import GestoreRegole


def stampa_risultati(password: str):
    gestore = GestoreRegole()

    esiti = gestore.valuta(password)
    punteggio = gestore.calcola_punteggio(esiti)
    livello = gestore.calcola_livello(punteggio)
    suggerimenti = gestore.ricava_suggerimenti(esiti)

    print()
    print("=" * 50)
    print("ANALISI PASSWORD")
    print("=" * 50)

    print()
    print("Controlli eseguiti:")
    for esito in esiti:
        stato = "OK" if esito.superata else "NO"
        print(f"- [{stato}] {esito.nome}: {esito.messaggio}")

    print()
    print(f"Punteggio totale: {punteggio}/100")
    print(f"Livello sicurezza: {livello}")

    print()
    print("Suggerimenti:")
    if suggerimenti:
        for suggerimento in suggerimenti:
            print(f"- {suggerimento}")
    else:
        print("- Nessun suggerimento urgente.")

    print()
    print("=" * 50)


def main():
    print("STIMATORE DI ROBUSTEZZA PASSWORD")
    print("-" * 50)

    password = getpass("Inserisci la password da valutare: ")

    stampa_risultati(password)


if __name__ == "__main__":
    main()