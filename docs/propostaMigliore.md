# Proposta progetto — Stimatore di robustezza password (Brute Force Estimator)

**Autori:** Raccis, Vincenzo

## 1. Cosa fa il programma

Il programma riceve in input una password e ne valuta la robustezza tramite un insieme di
controlli indipendenti (lunghezza, varietà dei caratteri, presenza in dizionari/leak noti,
pattern deboli come sequenze o ripetizioni). Dai controlli emerge una stima dello **spazio delle
chiavi** e della relativa **entropia**, da cui il programma calcola il tempo necessario a un
attacco brute force esaustivo, simulato su **tre profili di attaccante** con potenza di calcolo
crescente:

1. PC di casa
2. "Garage di GPU" (mini-cluster / mining rig)
3. Supercomputer

Il cuore del progetto è proprio questo modello dei tempi: a partire dalla password inserita, il
programma genera anche dei **suggerimenti** per renderla più robusta e **ricalcola il tempo di
BF** sulla versione corretta, mostrando concretamente il guadagno ottenuto.

Come estensione, una volta completato e consolidato il modello di stima, verrà aggiunto un
**generatore di password sicure** (basato su `secrets`, non su `random`), riprendendo l'idea di
un esercizio già assegnato in precedenza.

## 2. A chi serve e che problema risolve

Il programma è pensato per utenti non esperti e per chi è particolarmente attento alla sicurezza
dei propri account ma non ha gli strumenti per valutarla concretamente. Risolve due problemi:

- evita di dover inserire la propria password in chiaro su siti terzi che ne stimano la
  robustezza ma, nel frattempo, potrebbero salvarla nel loro database;
- rende tangibile, tramite un tempo stimato (minuti, anni, secoli...), il concetto astratto di
  "password robusta", aiutando l'utente a capire perché una scelta è migliore di un'altra.

## 3. Competenze utilizzate

- Modulo `secrets` (non `random`) per la generazione di entropia crittograficamente sicura, in
  particolare nel generatore di password.
- Hashing, per il confronto con dizionari e leak noti senza dover trattare le password in chiaro.
- Programmazione a oggetti ed ereditarietà, per la gerarchia delle regole di verifica.

## 4. Gerarchia delle classi

```
Regola (classe base astratta)
 ├── verifica(password) -> Esito
 ├── RegolaLunghezza
 ├── RegolaVarietaCaratteri
 ├── RegolaDizionario
 └── RegolaPattern
```

- **`Esito`**: oggetto restituito da `verifica()`, contiene almeno l'esito booleano del controllo
  e un messaggio/peso utile per il punteggio complessivo.
- **`GestoreRegole`** (o nome equivalente): applica in sequenza tutte le `Regola`, aggrega gli
  `Esito` e ne ricava la varietà di caratteri effettivamente usata, necessaria per calcolare lo
  spazio delle chiavi.
- **`StimatoreBruteForce`**: a partire da lunghezza e alfabeto della password calcola spazio delle
  chiavi, entropia e tempo di BF sui tre profili.
- **`ProfiloAttaccante`**: rappresenta un attaccante con una velocità di tentativi al secondo
  associata (PC di casa, garage di GPU, supercomputer).

Il `main` si limiterà essenzialmente a raccogliere la password in input e a orchestrare le
chiamate alle classi sopra descritte.

## 5. Modello dei tempi di brute force (spina dorsale del progetto)

Questa è la parte centrale del progetto e va saputa argomentare in sede di orale: ogni numero
usato è un'ipotesi dichiarata, non un valore assoluto.

### 5.1 Spazio delle chiavi ed entropia

Dato l'alfabeto effettivamente usato nella password (minuscole, maiuscole, cifre, simboli), la
dimensione dello spazio delle chiavi è:

```
N = |alfabeto|^L
```

dove `L` è la lunghezza della password e `|alfabeto|` è la somma delle dimensioni dei set di
caratteri rilevati (es. 26 minuscole, 26 maiuscole, 10 cifre, ~32 simboli).

L'entropia in bit è:

```
H = log2(N)
```

### 5.2 Tempo medio di brute force

Per un attacco esaustivo che non sa a priori dove si trova la password nello spazio di ricerca,
il tempo medio atteso è:

```
tempo_medio = N / (2 * velocità_guess_al_secondo)
```

(si divide per 2 perché in media la password viene trovata a metà dello spazio esplorato; il
tempo nel caso peggiore sarebbe `N / velocità`).

### 5.3 Ipotesi sui profili di attaccante

Le velocità sono parametri configurabili nel codice (costanti), non hardcoded in modo rigido,
proprio per poterle giustificare e discutere. Come riferimento assumiamo un attacco offline contro
hash non protetti da salting/stretching (es. MD5/SHA1 senza protezioni aggiuntive), scenario
realistico in molti leak noti:

| Profilo | Scenario | Ordine di grandezza (guess/s) |
|---|---|---|
| PC di casa | una GPU consumer | ~10^10 |
| Garage di GPU | mini-cluster di GPU in parallelo | ~10^12 |
| Supercomputer | cluster HPC / hardware dedicato | ~10^16 |

Questi valori dipendono fortemente dall'algoritmo di hashing assunto: se la password fosse
protetta da un algoritmo lento (bcrypt, scrypt, Argon2) i tempi salirebbero di ordini di
grandezza. Questa distinzione va esplicitata nel codice/documentazione e tenuta pronta come
possibile domanda d'orale.

## 6. Fasi del progetto

1. Presa in input della password.
2. Implementazione della gerarchia `Regola` e sottoclassi: controllo lunghezza e varietà dei
   caratteri.
3. Controllo presenza in dizionari/leak noti, tramite confronto via hashing.
4. Controllo pattern deboli (sequenze, ripetizioni, ecc.).
5. Calcolo dello spazio delle chiavi e del tempo di brute force sui tre profili —
   **milestone a circa metà progetto**.
6. Implementazione dei suggerimenti automatici per migliorare la password.
7. Ricalcolo del tempo di BF sulla password corretta secondo i suggerimenti, confronto con
   l'originale.
8. **Estensione**: generatore di password sicure con `secrets`, e relativo calcolo del tempo di
   BF sulla password generata.
