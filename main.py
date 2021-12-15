def runCode(lines):
    if (len(lines) and lines[0] == "Erro"):
        print("Erro ao ler o ficheiro!")
        exit()

    variaveis = {}
    linha = 0
    nestLevel = 0
    lastCondition = False
    loopStack = []
    labelsFound = []
    labelLines = []

    from instructions.escrever import escrever
    from instructions.ler import ler
    from instructions.guardar import guardar
    from instructions.se import se
    from instructions.enquanto import enquanto

    while (linha < len(lines)):
        parts = []
        remain = lines[linha].strip()

        while True:
            if (len(remain) <= 0): break

            if (remain.startswith("'")):
                try:
                    strEndIndex = remain[1:len(remain)].index("'")
                    parts.append(remain[0:strEndIndex+2])
                    remain = remain[strEndIndex+3:len(remain)]
                except:
                    print("Tens de fechar sempre as aspas!")
                    exit()
            else:
                try:
                    partEndIndex = remain[0:len(remain)].index(" ")
                    parts.append(remain[0:partEndIndex].casefold())
                    remain = remain[partEndIndex+1:len(remain)]
                except:
                    parts.append(remain.casefold())
                    break

        if (len(lines[linha]) > 1):
            instruction = parts[0]

            try:
                # register label
                if (lines[linha].endswith(":")):
                    if (lines[linha] not in labelsFound):
                        labelsFound.append(lines[linha].strip(":"))
                        labelLines.append(linha)
                elif (nestLevel == 0):
                    if (instruction == "escrever"):
                        escrever(parts, variaveis)
                    elif (instruction == "ler"):
                        ler(parts, variaveis)
                    elif (instruction == "guardar"):
                        guardar(parts, variaveis)
                    elif (instruction == "se"):
                        if (se(parts, variaveis)):
                            nestLevel = 0
                            lastCondition = True
                        else:
                            nestLevel = 1
                            lastCondition = False
                    elif (instruction == "enquanto"):
                        if (enquanto(parts, variaveis)):
                            loopStack.append(linha)
                        else:
                            nestLevel = -1
                    elif (instruction == "fim"):
                        if (parts[1] == "de" and (parts[2] == "condicao" or parts[2] == "condição")):
                            nestLevel = 0
                        elif (parts[1] == "de" and parts[2] == "enquanto"):
                            try:
                                linha = loopStack.pop() - 1
                            except:
                                print("Não podes por fim de enquanto sem comecar um enquanto!")
                                exit()
                    elif (instruction == "senao" or instruction == "senão"):
                        if (lastCondition):
                            nestLevel = 1
                        else:
                            nestLevel = 0
                        pass
                    elif (instruction.startswith("!")):
                        pass
                    elif (instruction == "sair"):
                        break
                    elif (instruction == "ir"):
                        if (parts[1] in labelsFound):
                            linha = labelLines[labelsFound.index(parts[1])]
                        else:
                            found = False
                            for cock in lines:
                                if parts[1] + ":" in cock:
                                    linha = lines.index(cock) - 1
                                    found = True
                                    break

                            if (not found):
                                print("A etiqueta", parts[1], "não foi encontrada!")
                                exit()
                    else:
                        print(parts[0], "não é uma instrução válida! Se quiseres por um comentário, começa a linha com '!'")
                        exit()
                else:
                    if (nestLevel > 0): #nestLevel de um se
                        if (instruction == "fim"):
                            if (parts[1] == "de" and (parts[2] == "condicao" or parts[2] == "condição")):
                                nestLevel -= 1
                        elif (instruction == "se"):
                            nestLevel += 1
                        elif (instruction == "senao" or instruction == "senão"):
                            nestLevel -= 1
                    else: #nestLevel de um enquanto
                        if (instruction == "fim"):
                            if (parts[1] == "de" and parts[2] == "enquanto"):
                                nestLevel += 1
                        elif (instruction == "enquanto"):
                            nestLevel -= 1
            except:
                print(lines[linha], "deu um erro!")
                exit()

        linha += 1
    
    print("Fim do programa")
    exit()