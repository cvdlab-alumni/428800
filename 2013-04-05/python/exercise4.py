from pyplasm import *

# --- generate two windows with black color ---
windowssud = COLOR(BLACK)(INSR(PROD)(AA(QUOTE)([[1],[-4,63],[-33-4-5,25]])))
windowssud2 = COLOR(BLACK)(INSR(PROD)(AA(QUOTE)([[1],[-4,63],[-33-4-5-25-5-5-3,22]])))

# --- putting all togheter---
building = STRUCT([windowssud,windowssud2])
VIEW(building)