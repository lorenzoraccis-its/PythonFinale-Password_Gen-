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
    # Regola Varietà Caratteri

Il 5 luglio è stata aggiunta la classe `RegolaVarietaCaratteri`, contenuta nel file:
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


programmaReal/regole/regola_pattern.py
Questa regola controlla se nella password sono presenti pattern semplici e prevedibili.
I pattern controllati sono principalmente:
ripetizioni di caratteri;
sequenze alfabetiche;
sequenze numeriche;
sequenze da tastiera.
Ripetizioni
La regola controlla ripetizioni di almeno tre caratteri uguali consecutivi.
Esempi di pattern deboli:
aaa
111
!!!
zzz
Una password come:
ciaooo123
viene segnalata perché contiene una ripetizione di o.
Sequenze
La regola controlla anche sequenze semplici, come:
abc
bcd
123
234
qwe
asd
zxc
Vengono controllate anche alcune sequenze inverse, per esempio:
cba
321
ewq
Questi pattern sono considerati deboli perché sono facili da indovinare e spesso presenti in password poco robuste.
Metodo ha_ripetizioni
Il metodo:
ha_ripetizioni(password)
scorre la password e verifica se esistono tre caratteri consecutivi uguali.
Esempio:
password = "ciaooo"
Risultato:
True
perché contiene ooo.
Metodo ha_sequenze
Il metodo:
ha_sequenze(password)
controlla se nella password sono presenti sequenze note.
Le sequenze considerate sono:
abcdefghijklmnopqrstuvwxyz
0123456789
qwertyuiop
asdfghjkl
zxcvbnm
Per ogni sequenza vengono controllati blocchi di tre caratteri.
Esempio:
password = "mario123"
Risultato:
True
perché contiene 123.
Metodo verifica
Il metodo principale della classe è:
verifica(password) -> Esito
Questo metodo richiama i controlli sulle ripetizioni e sulle sequenze.
Se trova almeno un problema, restituisce un Esito negativo con punteggio basso e un suggerimento.
Esempio di suggerimento:
Evita sequenze come abc/123/qwe e ripetizioni come aaa/111.
Se invece non vengono trovati pattern deboli, restituisce un Esito positivo.
