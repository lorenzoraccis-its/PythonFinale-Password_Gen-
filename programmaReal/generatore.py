import secrets
import string

from programmaReal.regole.regola_dizionario import HASH_PASSWORD_DEBOLI, calcola_hash_sha256
from programmaReal.regole.regola_pattern import RegolaPattern
from programmaReal.regole.regola_varieta import RegolaVarietaCaratteri


def genera_password_sicura(lunghezza: int = 16) -> str:
    """
    Generatore di password sicure.
    Uso secrets e non random, perché secrets è più adatto per scopi di sicurezza.
    """

    if lunghezza < 12:
        lunghezza = 12

    minuscole = string.ascii_lowercase
    maiuscole = string.ascii_uppercase
    cifre = string.digits
    simboli = "!@#$%&*?-_"

    alfabeto = minuscole + maiuscole + cifre + simboli

    # Garantisco almeno un carattere per ogni categoria.
    caratteri = [
        secrets.choice(minuscole),
        secrets.choice(maiuscole),
        secrets.choice(cifre),
        secrets.choice(simboli)
    ]

    while len(caratteri) < lunghezza:
        caratteri.append(secrets.choice(alfabeto))

    # Mescolo usando SystemRandom, sempre adatto a generazione sicura.
    secrets.SystemRandom().shuffle(caratteri)

    return "".join(caratteri)


def password_in_dizionario(password: str) -> bool:
    password_normalizzata = password.strip().lower()
    hash_password = calcola_hash_sha256(password_normalizzata)

    return hash_password in HASH_PASSWORD_DEBOLI



    password = password.strip()

    if password == "":
        return genera_password_sicura(16)

    controllo_pattern = RegolaPattern()

    if password_in_dizionario(password):
        return genera_password_sicura(16)

    if controllo_pattern.ha_ripetizioni(password) or controllo_pattern.ha_sequenze(password):
        return genera_password_sicura(max(16, len(password) + 4))

    nuova = password

    if not RegolaVarietaCaratteri.contiene_minuscole(nuova):
        nuova += secrets.choice(string.ascii_lowercase)

    if not RegolaVarietaCaratteri.contiene_maiuscole(nuova):
        nuova += secrets.choice(string.ascii_uppercase)

    if not RegolaVarietaCaratteri.contiene_cifre(nuova):
        nuova += secrets.choice(string.digits)

    if not RegolaVarietaCaratteri.contiene_simboli(nuova):
        nuova += secrets.choice("!@#$%&*?-_")

    alfabeto_extra = string.ascii_letters + string.digits + "!@#$%&*?-_"

    while len(nuova) < 12:
        nuova += secrets.choice(alfabeto_extra)

    return nuova