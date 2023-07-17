print("=== JUEGO PIEDRA, PAPEL O TIJERA ===")
print("Reglas: ")
print(" 1. Tienes que ganar 3 veces para tener la victoria")
print(" 2. Si hay 3 empates la partida queda en empate")
print(" 3. Si hay 3 derrotas la partida la pierdes")
print(" 4. Diviertete!\n")

import random as r

victoria = []
derrota = []
empate = []
conteo_victorias = 0
conteo_derrotas = 0
conteo_empates = 0

while True:
    juego = int(input("[1] Jugar\n[2] Ver registro de partida\n[3] Salir\nEliga para empezar: "))
    if juego == 1:
        while True:
            print("=" * 100)
            print("Es tu turno, escoge!")
            usuario = int(input("[1] Piedra, [2] Papel o [3] Tijera \nEscoga una opción: "))
            maquina = r.randint(1, 3)
            posibles = (1, 2, 3)

            if not usuario in posibles:
                print("Error!")

            else: 
                if (usuario == 1 and maquina == 3) or (usuario == 2 and maquina == 1) or (usuario == 3 and maquina == 2):
                    escogido = "Gano"
                    conteo_victorias += 1
                elif (usuario == 1 and maquina == 1) or (usuario == 2 and maquina == 2) or (usuario == 3 and maquina == 3):
                    escogido = "Empato"
                    conteo_empates += 1
                else:
                    escogido = "Perdio"
                    conteo_derrotas += 1

                if maquina == 1: maquina = "Piedra" 
                elif maquina == 2: maquina = "Papel"
                elif maquina == 3: maquina = "Tijera"

                print("=======================================================")
                print(f">> Usted {escogido} porque la maquina escogio {maquina}")
                print("=======================================================")

                if conteo_victorias > 2: 
                    print("Felicidades, usted gano!\n")
                    victoria.append("Gano")
                    conteo_victorias = 0
                    conteo_empates = 0
                    conteo_derrotas = 0
                    break
                elif conteo_empates > 2: 
                    print("Fue un Empate!\n")
                    empate.append("Empato")
                    conteo_victorias = 0
                    conteo_empates = 0
                    conteo_derrotas = 0
                    break
                elif conteo_derrotas > 2: 
                    print("Usted ha perdido :(, mejor suerte la próxima!\n")
                    derrota.append("Perdio")
                    conteo_victorias = 0
                    conteo_empates = 0
                    conteo_derrotas = 0
                    break

    elif juego == 2:
        print("*" * 100)
        print(f"Usted ha ganado un total de {len(victoria)} veces")
        print(f"Usted ha perdido un total de {len(derrota)} veces")
        print(f"Usted ha empatado un total de {len(empate)} veces")    
        print("*" * 100)

    elif juego == 3:
        print("GRACIAS POR JUGAR!!")
        break