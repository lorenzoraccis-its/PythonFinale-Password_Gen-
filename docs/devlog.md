## 3 luglio — Classe base delle regole

Oggi abbiamo iniziato a costruire la parte centrale del progetto: il sistema delle regole.  
Abbiamo creato il file `programmaReal/regole/regola_base.py`, dove abbiamo definito la classe astratta `Regola`.  
Questa classe serve come base comune per tutti i controlli che verranno aggiunti in seguito.  
L’idea è che ogni regola, anche se controlla una cosa diversa, debba avere lo stesso metodo `verifica(password)`.  
In questo modo il resto del programma potrà usare tutte le regole nello stesso modo, senza sapere come funzionano internamente.  

Abbiamo creato anche la classe `Esito`, usando una `dataclass`.  
All’inizio avevamo pensato di far restituire alle regole solo `True` o `False`, ma ci siamo accorti che non bastava.  
Per il programma servono anche un messaggio da mostrare all’utente, un punteggio e un eventuale suggerimento.  
Per questo `Esito` contiene il nome del controllo, l’esito, i punti, il messaggio e il suggerimento.  

Abbiamo iniziato anche il file `docs/manuale-tecnico.md`, spiegando che il progetto sarà basato su regole indipendenti.  
Questa scelta ci sembra comoda perché permette di aggiungere nuovi controlli senza modificare troppo il resto del codice.  
Per ora il programma non analizza ancora davvero una password, ma abbiamo definito una base abbastanza solida per continuare.

## 4 luglio — Regola lunghezza e primo gestore

Oggi abbiamo implementato la prima regola concreta del progetto: RegolaLunghezza.  
Questa regola controlla quanti caratteri contiene la password inserita dall’utente.  
Abbiamo scelto una soglia minima di 12 caratteri, perché una password troppo corta è molto più facile da forzare.  
Abbiamo previsto anche un caso migliore per password da almeno 16 caratteri, assegnando un punteggio più alto.  

Durante questa fase abbiamo iniziato anche il file gestore_regole.py.  
Per ora il gestore contiene solo la regola sulla lunghezza, ma l’idea è che in seguito potrà contenere tutte le altre regole.  
Il metodo valuta applica le regole alla password e raccoglie gli oggetti Esito.  
Abbiamo aggiunto anche alcuni metodi per calcolare il punteggio, il livello e i suggerimenti.  

Questa parte ci ha aiutato a verificare che la scelta fatta il giorno precedente funzionasse davvero.  
La classe Esito è risultata utile perché permette di restituire più informazioni e non solo un vero/falso.  
Per ora il sistema è ancora limitato, perché controlla solo la lunghezza, ma la struttura inizia a funzionare.  
Nei prossimi passaggi aggiungeremo le altre regole senza dover riscrivere tutto il programma.

## 5 luglio — Regola varietà caratteri

Oggi abbiamo aggiunto la seconda regola concreta del progetto: `RegolaVarietaCaratteri`.  
Questa regola controlla quali tipi di caratteri sono presenti nella password.  
In particolare verifica se ci sono minuscole, maiuscole, numeri e simboli.  
Abbiamo deciso di separare questi controlli in metodi diversi, così il codice resta più leggibile.  

La parte più importante è stata il metodo `calcola_dimensione_alfabeto`.  
Questo metodo non serve solo per il punteggio, ma sarà usato anche nella stima brute force.  
Infatti, per calcolare lo spazio delle chiavi, dobbiamo sapere quanti caratteri potrebbe usare una password simile.  
Per esempio, una password con solo minuscole ha un alfabeto stimato di 26 caratteri.  
Una password con minuscole, maiuscole, numeri e simboli ha invece un alfabeto molto più grande.  

Abbiamo aggiornato anche `gestore_regole.py`, aggiungendo la nuova regola alla lista dei controlli.  
Ora il gestore non controlla più solo la lunghezza, ma anche la varietà dei caratteri.  
Questo conferma che la struttura a regole indipendenti funziona: basta aggiungere una nuova classe e inserirla nella lista.  
Il programma è ancora incompleto, ma il sistema di valutazione sta iniziando a diventare più realistico.

## 11 luglio — Primo main funzionante

Oggi abbiamo collegato le varie parti del progetto dentro `main.py`.  
Fino a questo momento avevamo sviluppato soprattutto classi separate, ma mancava ancora un punto di ingresso che le facesse lavorare insieme.  
Abbiamo quindi fatto in modo che il programma chieda una password all’utente e poi la passi al `GestoreRegole`.

Il gestore applica tutte le regole già implementate e restituisce una lista di `Esito`.  
Da questi esiti il programma calcola il punteggio totale, il livello di sicurezza e i suggerimenti.  
Questa fase è stata importante perché ci ha permesso di vedere il progetto funzionare davvero da terminale.

Abbiamo scelto di mantenere il `main.py` abbastanza semplice, senza inserire al suo interno la logica dei singoli controlli.  
Il suo compito è solo orchestrare il programma: leggere la password, chiamare il gestore e stampare i risultati.  
Questa separazione rende il codice più ordinato e sarà utile quando aggiungeremo la stima brute force e l’output finale.

Durante i test abbiamo verificato alcune password semplici, come parole corte o password con solo lettere minuscole.  
Il programma ha mostrato correttamente i messaggi delle regole e i suggerimenti.  
L’output per ora è ancora basilare, ma è sufficiente per controllare che il flusso principale funzioni.  
Nei prossimi passaggi dovremo migliorare la parte visiva e aggiungere la stima dei tempi di brute force.