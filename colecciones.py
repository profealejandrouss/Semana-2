from os import system
system("cls")
pets=[]


print(pets)
pets.append("Gato")
pets.append("Perro")
pets.append("Hamster")
pets.append("Manati")
pets.append(123)
pets.append(True)
pets.append(True)
print(pets)
pets.remove(123)
print(pets)
pets.remove(True)
pets.remove(True)
print(pets)
print(pets[2])
print(pets[3])
pets[3]="Gnu"
print(pets)
print(pets[3])
#pets[4]="Narval"
pets.append("Narval")
print(pets)

for i in range(5):
    print(pets[i])
    
pets.remove("Gato")

print(f"Hay {len(pets)} animales")
for i in range(len(pets)):
    print(pets[i])
    
print("POR CADA MASCOTA EN MASCOTAS")
    
for pet in pets:
    print(pet)
    
buscado="Gato"    
if buscado in pets:
    print(f"Hay un {buscado}")
else:
    print(f"No hay un {buscado}")
    
