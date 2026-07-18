# Stimatore di robustezza password

Applicazione da terminale che valuta la robustezza di una password senza inviarla a servizi esterni. Applica quattro controlli indipendenti: lunghezza, varietà dei caratteri, presenza in un piccolo dizionario locale di password deboli e pattern prevedibili.

Il programma restituisce un punteggio da 0 a 100, un livello di robustezza, suggerimenti pratici e una stima del tempo necessario per un attacco brute-force in tre scenari. Al termine può anche generare una password di esempio con il modulo sicuro secrets.

Le stime sono didattiche: dipendono dalle ipotesi sul tipo di hash e sulla potenza dell'attaccante, quindi non rappresentano una garanzia assoluta di sicurezza.

## Membri del gruppo

- Fabio Di Vincenzo — GitHub: Fabio-Divi
- Lorenzo Raccis — GitHub: lorenzoraccis-its

Corso: Programmazione Python — Cybersecurity Specialist.

Repository: https://github.com/lorenzoraccis-its/PythonFinale-Password_Gen-.git

## Installazione

È richiesto Python 3.11 o superiore.

~~~powershell
git clone https://github.com/lorenzoraccis-its/PythonFinale-Password_Gen-.git
cd PythonFinale-Password_Gen-
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
~~~

Il programma usa soltanto moduli della libreria standard. Il file requirements.txt contiene pytest, usato per i test automatici.

## Come si usa

Aprire PowerShell nella cartella principale del repository ed eseguire:

~~~powershell
$env:PYTHONUTF8 = "1"
$env:PYTHONPATH = (Get-Location).Path
python .\programmaReal\main.py
~~~

La prima riga assicura la corretta visualizzazione di accenti, simboli e cornici della CLI. La password viene inserita in modo nascosto. Dopo il riepilogo, premere INVIO per visualizzare i controlli e la stima dei tempi; al termine è possibile chiedere la generazione di una password di esempio.

La guida completa è disponibile in docs/manuale-utente.md.

## Test

Dopo avere attivato l'ambiente virtuale e installato le dipendenze:

~~~powershell
python -m pytest -q -p no:cacheprovider tests
~~~

I test verificano le regole principali, il generatore e la struttura dei risultati della stima brute-force.

## Struttura del repository

~~~text
.
├── programmaReal/       ← sorgente dell'applicazione
│   ├── regole/          ← classe base e controlli concreti
│   ├── stima/           ← profili di attaccante e stimatore
│   ├── main.py          ← avvio dell'interfaccia da terminale
│   ├── analizzatore.py  ← coordinamento dell'analisi
│   └── estetica.py      ← stampa e colori della CLI
├── tests/               ← test pytest
├── docs/                ← proposta, manuali, devlog, scelte e uso dell'IA
├── VecchioProg/         ← prototipo iniziale, conservato come riferimento
├── requirements.txt
└── README.md
~~~

La struttura mantiene la cartella programmaReal come sorgente: nel modello generico del docente corrisponde al percorso src/progetto. Per dettagli sull'architettura e sulla gerarchia delle classi, consultare docs/manuale-tecnico.md e docs/scelte.md.
