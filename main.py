from ficheiro import loadLines

def runCode(lines):
    if (len(lines) and lines[0] == "Erro"):
        print("Cannot read file")
        exit()

    print("Start with len", len(lines))

    variaveis = {}
    linha = 0
    nestLevel = 0
    loopStack = []

    from instructions.escrever import escrever
    from instructions.ler import ler
    from instructions.guardar import guardar
    from instructions.se import se

    while (True):
        parts = []
        remain = lines[linha].strip()

        while True:
            if (len(remain) <= 0): break

            if (remain.startswith("'")):
                try:
                    strEndIndex = remain[1:len(remain)].index("'")
                    parts.append(remain[0:strEndIndex+2])
                    remain = remain[strEndIndex+2:len(remain)]
                except:
                    print("Tens de fechar sempre as aspas!")
                    exit()
            else:
                try:
                    partEndIndex = remain[0:len(remain)].index(" ")
                    parts.append(remain[0:partEndIndex])
                    remain = remain[partEndIndex+1:len(remain)]
                except:
                    parts.append(remain)
                    break

        if (len(lines[linha]) > 1):
            instruction = parts[0].casefold()

            if (nestLevel == 0):
                if (instruction == "escrever"):
                    escrever(parts, variaveis)
                elif (instruction == "ler"):
                    ler(parts, variaveis)
                elif (instruction == "guardar"):
                    guardar(parts, variaveis)
                elif (instruction == "se"):
                    if (se(parts, variaveis)):
                        nestLevel = 0
                    else:
                        nestLevel = 1
                elif (instruction == "fim"):
                    if (parts[1] == "da" and parts[2] == "condicao"):
                        nestLevel = 0
                    elif (parts[1] == "de" and parts[2] == "enquanto"):
                        linha = loopStack.pop() - 1
                elif (instruction.startswith("!")):
                    continue
                else:
                    print(parts[0], "não é uma instrução válida! Se quiseres por um comentário, começa a linha com '!'")
                    exit()
            else:
                if (instruction == "fim"):
                    if (parts[1] == "da" and parts[2] == "condicao"):
                        nestLevel -= 1
                    elif (parts[1] == "de" and parts[2] == "enquanto"):
                        #Ignore
                        continue
                elif (instruction == "se"):
                    nestLevel += 1

        linha += 1
    
    print("End")
    exit()

lines = loadLines("joel.txt")
runCode(lines)