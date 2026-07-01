import secrets
import string


#caratteri disponibili : maiuscole,minuscole,numeri,punteggiatura
#password da 12 car, tutti i tipi di car almeno una volta
#se tutti i set sono False o se lenght è minore del numero di set abilitati = ValueError


def generate_password(
    length: int = 12,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    avoid_ambiguous: bool = False,
) -> str:
    minimo_richiesto = sum([use_upper, use_lower, use_digits, use_symbols])
    if minimo_richiesto == 0:
        raise ValueError("Almeno un set di caratteri deve essere abilitato!")
    if length < minimo_richiesto:
        raise ValueError(f"Length troppo corta, minimo {minimo_richiesto}")
    password=[]
    ambigui = "Il1iOo0"
    pool = ""
    if use_upper :
        pool+=string.ascii_uppercase
    if use_lower :
        pool+=string.ascii_lowercase
    if use_digits :
        pool+=string.digits
    if use_symbols :
        pool+=string.punctuation
    pool_maiuscole = string.ascii_uppercase
    pool_minuscole = string.ascii_lowercase
    pool_numeri = string.digits
    pool_simboli = string.punctuation
    if avoid_ambiguous:
        for i in ambigui:
            pool = pool.replace(i, "")
            pool_maiuscole = pool_maiuscole.replace(i, "")
            pool_minuscole = pool_minuscole.replace(i, "")
            pool_numeri = pool_numeri.replace(i, "")
            pool_simboli = pool_simboli.replace(i, "")
    num_caratteri = len(pool)
    num_combinazioni = num_caratteri**length
    numero_combinazioni_secondo = int(input("Quante combinazioni al secondo : "))
    tempo_BF = num_combinazioni / numero_combinazioni_secondo
    tempo_anni = round(tempo_BF / 31536000)
    if tempo_anni > 1:
        print(f"tempo stimato in anni : {tempo_anni/2}")
    if tempo_anni < 1:
        tempo_mesi = tempo_BF / 2592000
        print(f"tempo stimato in mesi : {round(tempo_mesi/2)}")
        if tempo_mesi < 1:
            tempo_giorni = tempo_BF / 86400
            print(f"tempo stimato in giorni : {round(tempo_giorni/2)}")
            if tempo_giorni < 1:
                tempo_minuti = tempo_BF / 60
                print(f"tempo stimato in minuti : {round(tempo_minuti/2)}")
    password.append((secrets.choice(pool_maiuscole))) if use_upper == True else ""
    password.append(secrets.choice(pool_minuscole))  if use_lower == True else ""
    password.append(secrets.choice(pool_numeri))  if use_digits == True else ""
    password.append(secrets.choice(pool_simboli)) if use_symbols == True else ""
    minimo = len(password)
    for i in range(length-minimo) :
        password.append(secrets.choice(pool))
        secrets.SystemRandom().shuffle(password)
    mischiata = "".join(password)
    return mischiata



def build_alphabet() :
    upper = input("Maiuscole Y/n : ")
    lower = input("Minuscole Y/n : ")
    digits = input("Numeri Y/n : ")
    symbols = input("Simboli Y/n : ")
    ambiguous = input("Evita caratteri ambigui Y/n : ")
    use_upper = True if upper.lower() == "y" or upper == "" else False
    use_lower = True if lower.lower() == "y" or lower == "" else False
    use_digits = True if digits.lower() == "y" or digits == "" else False
    use_symbols = True if symbols.lower() == "y" or symbols == "" else False
    avoid_ambiguous = True if ambiguous.lower() == "y" or ambiguous == "" else False
    length = int(input("Lunghezza password : "))
    return length, use_upper, use_lower, use_digits, use_symbols, avoid_ambiguous



def __main__():
    print("""\n\n$ python password_generator.py
=== Password generator ===
1) Profilo default (12 caratteri, tutti i set)
2) Profilo custom\n""")
    scelta=input("Scelta : ")
    if scelta=="1":
        print(f"Password : {generate_password()}")
    elif scelta=="2":
        print(f"Password : {generate_password(*build_alphabet())}")
    else:
        print("Scelta non valida")

if __name__ == "__main__":
    __main__()
