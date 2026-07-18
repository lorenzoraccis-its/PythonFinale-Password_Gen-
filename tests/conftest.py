from pathlib import Path
import sys


RADICE_PROGETTO = Path(__file__).resolve().parents[1]

if str(RADICE_PROGETTO) not in sys.path:
    sys.path.insert(0, str(RADICE_PROGETTO))
