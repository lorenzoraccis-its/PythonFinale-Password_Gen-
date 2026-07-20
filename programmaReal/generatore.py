import secrets
import string

from regole.regola_dizionario import HASH_PASSWORD_DEBOLI, calcola_hash_sha256


def genera_password_sicura(lunghezza: int = 16) -> str:

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



