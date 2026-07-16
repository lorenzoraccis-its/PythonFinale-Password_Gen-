from getpass import getpass
import os
from programmaReal.generatore import genera_password_sicura
import estetica
from analizzatore import AnalizzatorePassword


def main():
    os.system("cls" if os.name == "nt" else "clear")
    estetica.stampa_header()

    print()
    password = getpass(estetica.colore("Inserisci la password da valutare: ", estetica.Colori.GRASSETTO))

    risultato = AnalizzatorePassword.analizza_password(
        titolo="ANALISI PASSWORD INSERITA",
        password=password,
        mostra_password=False
    )

    estetica.stampa_esito_finale(risultato)

    print()
    scelta = input(
        estetica.colore("Vuoi generare una password sicura di esempio? (s/n): ", estetica.Colori.GRASSETTO)
    ).lower().strip()

    if scelta == "s":
        password_generata = genera_password_sicura(16)

        AnalizzatorePassword.analizza_password(
            titolo="PASSWORD GENERATA CON SECRETS",
            password=password_generata,
            mostra_password=True
        )

    print()
    print(estetica.colore("╔" + "═" * (estetica.LARGHEZZA - 2) + "╗", estetica.Colori.VERDE))
    print(
        estetica.colore("║", estetica.Colori.VERDE)
        + "Analisi completata.".center(estetica.LARGHEZZA - 2)
        + estetica.colore("║", estetica.Colori.VERDE)
    )
    print(estetica.colore("╚" + "═" * (estetica.LARGHEZZA - 2) + "╝", estetica.Colori.VERDE))
    print()


if __name__ == "__main__":
    main()