import math

from programmaReal.stima.profilo_attaccante import ProfiloAttaccante


class StimatoreBruteForce:
    def __init__(self):
        # il valore del supercomputer l'ho sentito al TG5 giorni fa sul serio
        self.profili = [
            ProfiloAttaccante(
                nome="PC di casa",
                scenario="Una GPU consumer",
                guess_al_secondo=10**10
            ),
            ProfiloAttaccante(
                nome="Garage di GPU",
                scenario="Mini-cluster / mining rig",
                guess_al_secondo=10**12
            ),
            ProfiloAttaccante(
                nome="Supercomputer",
                scenario="Cluster HPC / hardware dedicato",
                guess_al_secondo=10**16
            )
        ]

        ###manca qualcosa ancora eh (tanto)