# Uso dell'IA

## Sintesi

Abbiamo usato un assistente IA come supporto per chiarire concetti, confrontare alternative, proporre piccoli esempi di codice, rivedere la struttura della documentazione e progettare la grafica testuale della CLI. Le decisioni sul progetto, l'integrazione dei moduli e le verifiche finali sono state controllate dal gruppo.

## Dettaglio per parte

| parte del progetto | domanda posta all'IA | cosa è stato accettato, modificato o rifiutato | perché |
|---|---|---|---|
| Classe base e polimorfismo | “Come posso creare in Python una classe astratta Regola con il metodo verifica(password) obbligatorio per le sottoclassi?” | Accettata l'idea di usare ABC, abstractmethod e una dataclass per Esito; i campi dell'esito e i punteggi sono stati adattati al progetto. | Serviva un contratto comune tra controlli diversi e un risultato più ricco di True o False. |
| Gestore delle regole | “Come posso applicare una lista di controlli diversi senza riempire il main di if?” | Accettato il ciclo sulle regole con una chiamata polimorfica a verifica; definite dal gruppo le fasce del punteggio. | La lista rende più semplice aggiungere controlli e mantiene il main leggero. |
| Controllo pattern | “Mi suggerisci un modo semplice per trovare ripetizioni come aaa e sequenze come abc, 123 o qwe in una password?” | Accettati i controlli su ripetizioni e blocchi di tre caratteri; ridotta manualmente la lista delle sequenze. | Volevamo un controllo didattico, leggibile e spiegabile, non un classificatore complesso. |
| Dizionario e hashing | “Come confronto una password con un piccolo dizionario locale usando SHA-256 senza mantenere la lista come struttura dati in chiaro?” | Accettato il calcolo dell'hash e il confronto con un set; rifiutata l'idea di interrogare un servizio di leak online. | Il progetto deve funzionare senza rete e non deve inviare la password a servizi terzi. |
| Stima brute-force | “Come si calcolano spazio delle chiavi, entropia e tempo medio di un attacco brute-force?” | Accettate le formule N = alfabeto^lunghezza e N / (2 × tentativi/s); scelti e dichiarati dal gruppo i tre profili di attaccante. | Le formule hanno una base teorica, mentre le velocità sono ipotesi didattiche che devono restare configurabili. |
| Generatore | “Come posso generare una password con minuscole, maiuscole, cifre e simboli usando una sorgente sicura?” | Accettato l'uso di secrets.choice e del mescolamento con SystemRandom; rifiutato random. | secrets è più adatto di random per password imprevedibili. |
| Grafica della CLI | “Proponi un'interfaccia da terminale semplice e leggibile per mostrare punteggio, livelli, controlli e tempi.” | Accettati e poi adattati cornici, colori ANSI, badge e barra del punteggio. La grafica del progetto è stata realizzata con il supporto dell'IA. | L'obiettivo era rendere il risultato più chiaro a un utente non tecnico senza modificare la logica di analisi. |
| Refactoring | “Come posso spostare le funzioni di stampa e l'analisi fuori dal main senza cambiare il comportamento del programma?” | Accettata la separazione in estetica.py e analizzatore.py; verificato manualmente che il flusso restasse invariato. | Il main era diventato troppo lungo e mescolava input, logica e presentazione. |
| Documentazione | “Quali sezioni servono in README, manuale tecnico, manuale utente e scelte implementative per spiegare correttamente un progetto Python?” | Usata una proposta di struttura come traccia; contenuti tecnici, esempi e limiti sono stati verificati e adattati al codice del progetto. | La documentazione deve corrispondere ai file reali e non descrivere funzionalità non presenti. |

## Cosa non abbiamo delegato all'IA

Non abbiamo affidato all'IA decisioni autonome sul progetto, pubblicazione del repository, gestione di password reali o esecuzione di comandi sul computer. Ogni suggerimento è stato controllato, adattato o rifiutato quando non era coerente con il codice e con l'obiettivo didattico.

L'IA non sostituisce la verifica: le formule della stima sono state riportate come ipotesi dichiarate, la grafica è stata integrata e provata nel terminale e la documentazione è stata riletta rispetto alla struttura effettiva del repository.
