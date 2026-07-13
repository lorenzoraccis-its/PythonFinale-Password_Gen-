# Manuale tecnico — Brute Force Estimator

## 1. Obiettivo del documento

Questo documento descrive la struttura interna del progetto.

È pensato per chi vuole capire come è organizzato il codice o per chi in futuro volesse estenderlo aggiungendo nuovi controlli sulla password.

In questa prima fase il progetto non è ancora completo, ma è stata definita la base della gerarchia delle regole.

---

## 2. Idea generale dell’architettura

Il programma sarà diviso in più parti:

```text
programmaReal/
│
├── main.py
├── gestore_regole.py
├── generatore.py
│
├── regole/
│   ├── regola_base.py
│   ├── regola_lunghezza.py
│   ├── regola_varieta.py
│   ├── regola_dizionario.py
│   └── regola_pattern.py
│
└── stima/
    ├── profilo_attaccante.py
    └── stimatore_brute_force.py
```

 è stata aggiunta la classe `RegolaVarietaCaratteri`, contenuta nel file:
`programmaReal/regole/regola_varieta.py`

Questa regola controlla quali categorie di caratteri sono presenti nella password. Le categorie considerate sono:
* Lettere minuscole
* Lettere maiuscole
* Cifre numeriche
* Simboli

La regola assegna un punteggio più alto quando la password usa più categorie diverse. Una password che contiene solo lettere minuscole è considerata meno robusta rispetto a una password che contiene minuscole, maiuscole, numeri e simboli.

## Metodi principali

La classe contiene alcuni metodi di supporto:
* `contiene_minuscole(password)`
* `contiene_maiuscole(password)`
* `contiene_cifre(password)`
* `contiene_simboli(password)`

Questi metodi restituiscono `True` se la password contiene almeno un carattere della categoria controllata.

È presente anche il metodo:
* `gruppi_presenti(password)`: restituisce una lista con i gruppi di caratteri trovati nella password.

### Esempio:
```python
password = "ciao123"
gruppi_presenti = ["minuscole", "cifre"]
```
# 2. generatore password sicura (su richiesta)

Alla fine dell’analisi, il programma chiede:

    Vuoi generare una password sicura di esempio? (s/n):
Se l’utente risponde:

    s
il programma genera una password sicura usando il modulo secrets. 
Esempio:

    Password generata: K7!faQ2_mP9z
La password generata è separata dalla password inserita dall’utente (e verrà analizzata pure quella).
