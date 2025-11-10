# Importera modulen random för att generar slumpmässiga tal. 
import random

# Funktionen som generar ett slumpmssigt tal
def kasta_tarning():
    return random.randint(1, 6)

# Funktonen som åberopar kasta_tarning två gånger samt summerar talen 
def summa_av_kast():
    tarning1 = kasta_tarning
    tarning2 = kasta_tarning
    total = tarning1 + tarning2
    return total