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


# Gestore delle regole

L’8 luglio è stata completata la classe `GestoreRegole`, contenuta nel file:

```text
programmaReal/gestore_regole.py
```

Questa classe ha il compito di coordinare tutte le regole di verifica della password.

Prima ogni regola funzionava in modo separato.
Con il gestore, invece, il programma può applicare tutte le regole in sequenza e raccogliere i risultati.

## Lista delle regole

Il gestore contiene una lista di regole:

```python
self.regole = [
    RegolaLunghezza(),
    RegolaVarietaCaratteri(),
    RegolaDizionario(),
    RegolaPattern()
]
```

Ogni elemento della lista è un oggetto che eredita dalla classe base `Regola`.

Questo permette di usare tutte le regole nello stesso modo, chiamando sempre il metodo:

```python
verifica(password)
```

## Metodo `valuta`

Il metodo principale del gestore è:

```python
valuta(password)
```

Questo metodo riceve la password e applica tutte le regole presenti nella lista.

Il risultato è una lista di oggetti `Esito`.

Esempio logico:

```text
password
   ↓
RegolaLunghezza
   ↓
RegolaVarietaCaratteri
   ↓
RegolaDizionario
   ↓
RegolaPattern
   ↓
lista di Esito
```

In questo modo il resto del programma non deve sapere come funziona ogni regola internamente.

## Metodo `calcola_punteggio`

Il metodo:

```python
calcola_punteggio(esiti)
```

somma i punti restituiti dalle varie regole.

Il punteggio massimo viene limitato a `100`, così il risultato finale rimane sempre leggibile per l’utente.

Esempio:

| Controllo                   |  Punti |
| --------------------------- | -----: |
| Controllo lunghezza         |     25 |
| Controllo varietà caratteri |     22 |
| Controllo dizionario        |     25 |
| Controllo pattern           |     15 |
| **Totale**                  | **87** |

## Metodo `calcola_livello`

Il metodo:

```python
calcola_livello(punteggio)
```

trasforma il punteggio numerico in un livello testuale.

I livelli previsti sono:

| Punteggio | Livello       |
| --------: | ------------- |
|   `>= 85` | Molto robusta |
|   `>= 65` | Buona         |
|   `>= 40` | Debole        |
|    `< 40` | Molto debole  |

Questa scelta rende il risultato più facile da capire per l’utente finale.

## Metodo `ricava_suggerimenti`

Il metodo:

```python
ricava_suggerimenti(esiti)
```

raccoglie tutti i suggerimenti prodotti dalle regole.

Se una regola trova un problema, può restituire un suggerimento.

Esempio:

```text
Porta la password almeno a 12 caratteri.
Usa un mix di minuscole, maiuscole, numeri e simboli.
Evita sequenze come abc/123/qwe.
```

Il gestore li raccoglie in una lista unica, così il `main.py` potrà mostrarli all’utente.

## Metodo `dimensione_alfabeto`

Il metodo:

```python
dimensione_alfabeto(password)
```

richiama il calcolo della dimensione dell’alfabeto dalla classe `RegolaVarietaCaratteri`.

Questo valore sarà usato dallo `StimatoreBruteForce` per calcolare lo spazio delle chiavi.

Esempio:

```python
password = "ciao"
dimensione_alfabeto = 26

password = "Ciao123!"
dimensione_alfabeto = 94
```

## Vantaggio del gestore

Il vantaggio principale di `GestoreRegole` è che centralizza l’esecuzione dei controlli.

Senza questa classe, il `main.py` dovrebbe chiamare manualmente ogni regola.
Con il gestore, invece, il `main.py` dovrà solo chiedere:

```python
esiti = gestore.valuta(password)
```

Questo rende il codice più ordinato e più facile da estendere.

Se in futuro verrà aggiunta una nuova regola, basterà inserirla nella lista `self.regole`.

## Classi della stima brute force

# 9.1 ProfiloAttaccante
È una dataclass.

Contiene :

    nome: str
    scenario: str
    guess_al_secondo: float

## 9.2 StimatoreBruteForce
Questa classe calcola:

* spazio delle chiavi;

* entropia;

* tempo medio;

* caso peggiore.

Contiene anche i tre profili di attaccante:

    PC di casa        10^10 guess/s
    Garage di GPU     10^12 guess/s
    Supercomputer     10^16 guess/s


## generatore.py, con SECRETS 

### Contiene la logica per generare password sicure.
Usa il modulo secrets, non random.
* Responsabilità:
1. generare password casuali con buona varietà;
1. garantire almeno una minuscola;
1. garantire almeno una maiuscola;
1. garantire almeno una cifra;
1. garantire almeno un simbolo;
1. restituire una password generata come esempio.


## Grafica

Abbiamo implementato la grafica per rendere la CLI un po' più felice

_(L'AI ha aiutato)_

## Grafica pt.2 

Essendo che la grafica l'avevamo messa tutta nel main (usando molteplici metodi)
abbiamo pensato che rendesse il main troppo pieno, quindi abbiamo deciso di trasferire le 
funzioni estetiche nel nuovo file **estetica.py** , in modo tale
da rendere il **main** più pulito

* di conseguenza, nel main abbiamo aggiunto : 


    import estetica
    estetica.<nome_metodo> (per le chiamate alle funzioni)

inoltre, ci tengo a precisare che questo è un ottimo _refatcoring_ , perchè l'esperienza utente è
rimasta **invariata**.


## Pulizia main 

Dopo aver pulito il main dalle sue funzioni estetiche, 
abbiamo spostato 

    analizza_password()

nel file (tutto per lui) : 

    analizzatore.py
    class AnalizzatorePassword:

in modo tale che nel file main, ci sia solo il main.

### utilme pulizie

Rimossi gli import che non venivano più usati, per un codice più pulito

# Fine

