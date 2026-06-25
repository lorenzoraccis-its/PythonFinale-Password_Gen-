Raccis - di Vincenzo 

abbiamo colto la palla al balzo decidendo di fare un programma basandoci sull'esempio 9, essendo che si era già svolto un esercizio simile in classe, e se si ricorda, io (Raccis) avevo provato a implementare una stima di robustezza della password in base a quante guess un supercomputer malintenzionato facesse al secondo. Ma non vorrei limitarmi a seguire solo ciò che dice l'esempio 9.
N.B. :  BF sta per Brute Force, vabbè lo saprà immagino.

Cosa fa il programma : In base alla password che metti in input, e in base a lunghezza , varietà dei caratteri , dizionari, leak noti e pattern (magari evitiamo di mettere 5 minuscole di fila dai). Fa una stima di quanto tempo servirebbe per fare un brute force, in base a 3 tipi diversi di velocità : -computer di casa,  -un garage pieno di computer (mini server, oppure tipo la gente che mina i bitcoin anche se loro lo fanno con le GPU)  -supercomputer (come se la NASA volesse scoprire la tua password con un bruteforce XD).
Inoltre vorremmo implementare i suggerimenti da applicare alla password inserita inizialmente, e stimare il tempo di BF di quella con i suggerimenti applicati.
Un'ultima mini-implementazione sarebbe quella di un generatore di password (molto simile al compito da lei assegnato tempo fa); mi dica lei se è una modifica che vale la pena farla.

A chi serve e che problema risolve : serve a tutti, soprattutto ai più inesperti e/o agli ansiogeni che hanno paura che gli freghino la password a loro insaputa. Risolve il problema dei siti in cui ti dicono la robustezza della tua password ma nel frattempo se la salvano nel loro database. Inoltre aiuta le persone ad usare password più robuste.

Competenze da usare : Libreria Secret (NON la random), hashing (confronto con dizionari/leak), OOP, ereditarietà 

Gerarchia : la classe base è "Regola" con "verifica(password)" -> "Esito" → RegolaLunghezza, RegolaVarietaCaratteri, RegolaDizionario, RegolaPattern. Probabilmente una delle poche cose da fare nel main sarà inserire la password 

Piano : 
	- Presa in input della password
	- check della presenza dei caratteri (e lunghezza) 
	- check se è presente nei leak noti
	- calcolo tempo BF   -----> contiamo che per metà saremo a questo punto
	- implementazione suggerimento + generatore password da zero
	- calcolo tempo BF della password suggerita / generata
