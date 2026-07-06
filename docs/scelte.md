# Scelte implementative

## 1. Controllo dizionario tramite hashing

Il **6 luglio** abbiamo aggiunto il controllo dizionario con la classe `RegolaDizionario`, contenuta nel file:

```text
programmaReal/regole/regola_dizionario.py
```

Questa regola serve a verificare se la password inserita dall’utente è presente in una piccola lista di password deboli simulate.

L’obiettivo non è creare un vero database di leak, ma dimostrare il funzionamento di un controllo basato su password comuni o già compromesse.

---

## 2. Perché non salviamo password in chiaro

Una scelta importante è stata **non salvare direttamente le password deboli in chiaro nel codice**.

Invece di scrivere una lista come:

```python
password_deboli = ["password", "123456", "qwerty"]
```

abbiamo scelto di salvare gli hash SHA-256 di queste password.

Quindi nel codice non confrontiamo direttamente la password, ma confrontiamo il suo hash.

Il flusso è:

```text
password inserita
        ↓
normalizzazione
        ↓
calcolo hash SHA-256
        ↓
confronto con hash noti
```

Questa scelta è più coerente con il tema della sicurezza, perché evita di trattare direttamente password in chiaro.

---

## 3. Normalizzazione della password

Prima di calcolare l’hash, la password viene normalizzata con:

```python
password.strip().lower()
```

Questo significa che:

* vengono tolti eventuali spazi all’inizio o alla fine;
* la password viene trasformata in minuscolo.

Questa scelta è stata fatta per intercettare meglio password deboli scritte con piccole variazioni, per esempio:

```text
Password
PASSWORD
 password 
```

Tutte queste varianti vengono trattate come la stessa password debole.

Il compromesso è che questa normalizzazione rende il controllo dizionario meno preciso sul maiuscolo/minuscolo.

Però, per un progetto didattico, è una scelta accettabile perché aiuta a riconoscere password comuni anche se scritte con variazioni semplici.

---

## 4. Perché SHA-256

Abbiamo scelto **SHA-256** perché è disponibile direttamente nel modulo standard `hashlib`.

Questo ci permette di implementare il controllo senza installare librerie esterne.

La funzione usata è:

```python
hashlib.sha256(testo.encode("utf-8")).hexdigest()
```

SHA-256 non viene usato qui per salvare password reali in modo sicuro, ma solo per simulare il confronto con una lista di hash noti.

È importante distinguere le due cose:

* per un progetto didattico va bene usare SHA-256 per confrontare hash già presenti;
* in un sistema reale non basterebbe salvare password con SHA-256 semplice;
* in un sistema reale bisognerebbe usare salt e algoritmi lenti come `bcrypt`, `scrypt` o `Argon2`.
