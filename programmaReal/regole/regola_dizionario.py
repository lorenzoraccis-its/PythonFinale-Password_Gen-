import hashlib

from programmaReal.regole.regola_base import Regola, Esito


def calcola_hash_sha256(testo: str) -> str:
    return hashlib.sha256(testo.encode("utf-8")).hexdigest()


# Simulazione didattica di un piccolo database di password deboli/leak note.
# Non salvo le password in chiaro: salvo solo gli hash SHA-256.
HASH_PASSWORD_DEBOLI = {
    "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password
    "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",  # 123456
    "15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225",  # 123456789
    "65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5",  # qwerty
    "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918",  # admin
    "1c8bfe8f801d79745c4631d09fff36c82aa37fc4cce4fc946683d7b336b63032",  # letmein
    "cf8276ca60061baf2611917c50717a2b1bcbff0c0d25e00b95ef667ab8f158f0",  # ciao123
    "2547887be5eaec9c95584fb892e5ca8d38b85e4265babb9c7c7f7b5256e0d635",  # vincenzo
    "d7ab9e0a5734e9c1741773ce4e8a3167840ec58da39e6b083d1eaf3c79cce158",  # raccis
    "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f",  # password123
    "91b4d142823f7d20c5f08df69122de43f35f057a988d9619f6d3138485c9a203",  # 000000
    "bcb15f821479b4d5772bd0ca866c00ad5f926e3580720659cc80d39c9d09802a",  # 111111
    "6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090",  # abc123
    "e4ad93ca07acb8d908a3aa41e920ea4f4ef4f26e7f86cf8291c5db289780a5ae",  # iloveyou
    "daaad6e5604e8e17bd9f108d91e26afe6281dac8fda0091040a7a6d7bd9b43b5",  # qwerty123
}


class RegolaDizionario(Regola):
    def __init__(self):
        super().__init__("Controllo dizionario/leak")

    def verifica(self, password: str) -> Esito:
        password_normalizzata = password.strip().lower()
        hash_password = calcola_hash_sha256(password_normalizzata)

        if hash_password in HASH_PASSWORD_DEBOLI:
            return Esito(
                nome=self.nome,
                superata=False,
                punti=0,
                messaggio="Password trovata nel dizionario di password deboli/leak simulate.",
                suggerimento="Non usare parole comuni, nomi, password già viste o combinazioni prevedibili."
            )

        return Esito(
            nome=self.nome,
            superata=True,
            punti=25,
            messaggio="La password non risulta presente nel dizionario locale di password deboli.",
            suggerimento=""
        )