from ficheiro import loadLines

variaveis = {}
lines = loadLines("joel.txt")

from instructions.escrever import escrever
from instructions.ler import ler
from instructions.guardar import guardar

for line in lines:
    print("Line proc", line)

    #add splitting of parts by spaces and strings
    parts = []
    remain = line
    while True:
        if (remain.startswith("'")):
            try:
                strEndIndex = remain.index("'")
                parts.append(line[0:strEndIndex])
                remain = remain[1:strEndIndex+1]
            except:
                print("Tens de fechar sempre as aspas!")        
        else:
            try:
                partEndIndex = remain.index(" ")
                parts.append(line[0:partEndIndex])
                remain = remain[partEndIndex+1]
            except:
                parts.append(remain)
                break

    print(parts)
            
            
    #End of that

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
