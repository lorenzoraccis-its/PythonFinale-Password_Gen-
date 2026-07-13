from getpass import getpass

from programmaReal.gestore_regole import GestoreRegole
from programmaReal.generatore import genera_password_sicura


def stampa_risultati(password: str, mostra_password: bool = False):
    gestore = GestoreRegole()

    esiti = gestore.valuta(password)
    punteggio = gestore.calcola_punteggio(esiti)
    livello = gestore.calcola_livello(punteggio)
    suggerimenti = gestore.ricava_suggerimenti(esiti)

    print()
    print("=" * 50)
    print("ANALISI PASSWORD")
    print("=" * 50)

    if mostra_password:
        print(f"Password generata: {password}")

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

    print()
    scelta = input("Vuoi generare una password sicura di esempio? (s/n): ").lower().strip()

    if scelta == "s":
        password_generata = genera_password_sicura(16)

        print()
        print("PASSWORD GENERATA CON SECRETS")
        stampa_risultati(password_generata, mostra_password=True)

    print()
    print("Fine programma.")


if __name__ == "__main__":
    main()