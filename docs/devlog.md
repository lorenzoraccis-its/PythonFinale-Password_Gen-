# Devlog

Diario di bordo del gruppo. Le date e le attività riportate di seguito corrispondono ai passaggi principali registrati nella cronologia Git del progetto.

## Entry

### Settimana 1 — 1-5 luglio 2026

In questa prima settimana abbiamo trasformato l'idea iniziale in una struttura concreta. Volevamo evitare un unico file pieno di controlli con molti if, perché sarebbe diventato difficile da leggere e modificare. Abbiamo quindi scelto di rappresentare ogni controllo come una regola separata.

Fabio ha definito la classe astratta Regola e la dataclass Esito. La classe base obbliga tutte le regole a esporre lo stesso metodo verifica(password), mentre Esito raccoglie il risultato del controllo, i punti, un messaggio e un eventuale suggerimento. All'inizio avevamo pensato di restituire soltanto True o False, ma non sarebbe bastato per costruire un output utile per l'utente.

Lorenzo ha lavorato sulla prima regola concreta, RegolaLunghezza, e sul primo GestoreRegole. Abbiamo impostato 12 caratteri come soglia minima e 16 come soglia consigliata. Il gestore raccoglie gli esiti, calcola il punteggio e converte il valore numerico in un livello leggibile.

Successivamente abbiamo aggiunto RegolaVarietaCaratteri. Ci ha richiesto un po' di attenzione perché la varietà non serve soltanto al punteggio: viene usata anche per stimare la dimensione dell'alfabeto e, quindi, lo spazio delle chiavi. Abbiamo separato minuscole, maiuscole, cifre e simboli in metodi distinti per rendere il controllo più chiaro.

La difficoltà principale è stata decidere quali informazioni dovessero essere responsabilità di una singola regola e quali del gestore. Abbiamo scelto che ogni regola producesse solo il proprio Esito, lasciando al gestore il compito di sommare punti e raccogliere suggerimenti. Per la settimana seguente abbiamo pianificato i controlli più specifici e il modello di stima brute-force.

### Settimana 2 — 6-11 luglio 2026

In questa settimana abbiamo completato i controlli che rendono l'analisi meno superficiale. Fabio ha implementato RegolaDizionario, basata su un insieme locale e didattico di hash SHA-256 di password deboli. Non volevamo collegarci a servizi online, sia per non introdurre dipendenze dalla rete sia per non trasmettere password a terzi.

Per migliorare il riconoscimento delle varianti più comuni, il controllo normalizza gli spazi iniziali e finali e converte in minuscolo prima di calcolare l'hash. Abbiamo discusso il compromesso: è utile per intercettare piccole varianti di password comuni, ma non è un modello da usare per l'autenticazione reale.

Lorenzo ha aggiunto RegolaPattern, che rileva ripetizioni di almeno tre caratteri e sequenze alfabetiche, numeriche o da tastiera. La parte che ci ha fatto perdere più tempo è stata stabilire quali sequenze considerare senza rendere il controllo troppo complicato. Abbiamo scelto una lista piccola e spiegabile: alfabeti, cifre e sequenze qwerty, asdf e zxc.

Abbiamo poi realizzato la parte distintiva del progetto: tre profili di attaccante con velocità diverse. Il modello calcola lo spazio delle chiavi, l'entropia e il tempo medio e peggiore per un PC di casa, un garage di GPU e un supercomputer. I valori sono dichiarati come ipotesi, non come misure universali.

Tra l'8 e l'11 luglio abbiamo aggiornato il manuale tecnico e collegato le classi in un primo main funzionante. In questa fase abbiamo verificato manualmente password molto corte, password presenti nel dizionario e password con più categorie di caratteri. La settimana successiva era dedicata a generatore, interfaccia e pulizia del codice.

### Settimana 3 — 12-16 luglio 2026

Nell'ultima settimana abbiamo lavorato soprattutto sull'esperienza d'uso e sul riordino del codice. Fabio ha migliorato il flusso di analisi nel main e ha completato le parti che mostrano riepilogo, controlli, livello e suggerimenti. Il programma usa getpass, quindi la password non appare mentre viene digitata nel terminale.

Lorenzo ha aggiunto il generatore di password. Abbiamo scelto secrets al posto di random perché secrets usa una sorgente adatta a valori di sicurezza. Il generatore crea password di almeno 12 caratteri e, nel normale utilizzo del programma, ne genera 16 con almeno una minuscola, una maiuscola, una cifra e un simbolo.

Abbiamo dedicato tempo anche alla grafica della CLI. Le cornici, i colori ANSI, i badge e la barra del punteggio sono stati progettati con il supporto dell'IA e poi adattati al nostro programma. Dopo un primo inserimento nel main, ci siamo accorti che il file stava diventando troppo lungo e difficile da seguire.

La decisione più importante è stata quindi il refactoring del 16 luglio. Abbiamo spostato la presentazione in estetica.py e il coordinamento dell'analisi in analizzatore.py. Il main ora si limita ad avviare il programma, raccogliere l'input e chiedere se generare una password di esempio.

Abbiamo controllato che il refactoring non cambiasse il risultato dell'analisi: le stesse regole continuano a essere applicate nello stesso ordine e l'utente riceve gli stessi dati, ma il codice è più diviso per responsabilità. In chiusura abbiamo rivisto manuali e scelte implementative, preparando anche una piccola suite pytest per verificare i controlli principali.

## Bilancio finale

Siamo soddisfatti soprattutto di avere costruito un programma con una logica separata dall'interfaccia, invece di limitarci a stampare un giudizio generico sulla password. La gerarchia Regola ci ha permesso di collegare quattro verifiche diverse senza creare dipendenze inutili tra loro.

Abbiamo capito meglio la differenza tra un controllo didattico e un sistema di sicurezza reale. Il dizionario locale e SHA-256 servono a mostrare un meccanismo di confronto, ma non sostituiscono un archivio di leak aggiornato né una corretta gestione delle credenziali in produzione. Allo stesso modo, i tempi del brute-force dipendono dall'hash, dall'hardware e dallo scenario.

All'inizio abbiamo sottovalutato il lavoro necessario per rendere leggibile l'output. La grafica del terminale, i messaggi e le pause tra le sezioni richiedono decisioni di usabilità, non soltanto codice. La separazione finale tra main, analizzatore ed estetica è stata utile proprio per non mescolare queste responsabilità.

La divisione del lavoro è stata complementare: Fabio si è concentrato soprattutto sulle regole, sul collegamento dell'analisi e sulla documentazione; Lorenzo sulla regola di lunghezza, sui profili di attaccante, sul generatore, sulla grafica e sul refactoring. Entrambi abbiamo verificato le integrazioni e discusso le scelte comuni.

Con un'altra settimana avremmo aggiunto una lista di hash più completa caricata da file, opzioni da riga di comando e altri test sui casi limite. Per ora il progetto raggiunge l'obiettivo didattico perché mostra sia la valutazione qualitativa sia una stima quantitativa, dichiarando con chiarezza i suoi limiti.
