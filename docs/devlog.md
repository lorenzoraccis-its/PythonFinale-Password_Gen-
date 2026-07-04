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