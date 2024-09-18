# 2 - Resolver mediante recursividad el problema de las torres de Hanoi
# No utilizar listas, la función solo debe devolver un print con los movimientos.

def mover_pieza (piezas: int, poste_inicial: str, poste_destino: str, poste_auxiliar: str)-> None:

    if piezas == 1:
        print (f"mover una pieza del {poste_inicial} al {poste_destino}")
    else:
        mover_pieza(piezas - 1, poste_inicial, poste_auxiliar, poste_destino)
        print(f"mover pieza {piezas} de {poste_inicial} a {poste_destino}")
        mover_pieza(piezas - 1, poste_auxiliar, poste_destino, poste_inicial)   

mover_pieza(5, "poste_inicial", "poste_destino", "poste_auxiliar")



