# juego de piedra papel y tijera

# input
print("Escoja una opcion : \n")
print("1. Piedra \n")
print("2. Papel \n")
print("3. tijera \n")
opcion = int(input("\nDame la opcion \n: "))
if opcion==1:
    tu="piedra"
elif opcion==2:
    tu="Papel"
elif opcion==3:
    tu="Tijera"
else:
    print("Opcion equivocada \n")



import random

k=random.randint(1, 3)

if k==1:
    pc="piedra"
elif k==2:
    pc="Papel"
elif k==3:
    pc="Tijera"

print("\nSelecionaste : ",tu)
print("\nEl computador seleciono: ",pc,"\n")

if (opcion ==k ):
    print("Empate")
elif(opcion==1 and k==2):
    print("Perdiste")
elif(opcion==1 and k==3):
    print("Ganaste")
elif(opcion==2 and k==3):
    print("perdiste")
elif(opcion==2 and k==1):
    print("Ganaste")
elif(opcion==3 and k==1):
    print("Perdiste")
elif(opcion==3 and k==2):
    print("Ganaste")



    
