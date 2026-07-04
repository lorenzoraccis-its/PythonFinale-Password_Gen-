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