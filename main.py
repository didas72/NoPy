from ficheiro import loadLines

variaveis = {}
lines = loadLines("joel.txt")

from instructions.escrever import escrever
from instructions.ler import ler

for line in lines:
    
    parts = line.split(' ')

    if (len(line) > 1):
        instruction = parts[0].casefold()

        if (instruction == "escrever"):
            escrever(parts, variaveis)
        elif(instruction == "ler"):
            ler(parts, variaveis)
            
exit()
