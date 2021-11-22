from ficheiro import loadLines

variaveis = {}
lines = loadLines("joel.txt")

print(len(lines))
print(lines)

from instructions.escrever import escrever
from instructions.ler import ler
from instructions.guardar import guardar

for line in lines:
    
    parts = line.split(' ')

    if (len(line) > 1):
        instruction = parts[0].casefold()

        if (instruction == "escrever"):
            escrever(parts, variaveis)
        elif (instruction == "ler"):
            ler(parts, variaveis)
        elif (instruction == "guardar"):
            guardar(parts, variaveis)
        elif (instruction.startswith("!")):
            continue
        else:
            print(parts[0], "não é uma instrução válida! Se quiseres por um comenta´rio, começa a linha com '!'")
            exit()
            
exit()
