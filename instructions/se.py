def se(parts, variaveis):
    parts.pop(0)

    if (len(parts) < 4 or parts[-1].casefold() != "entao"):
        print("Um se tem de ter pelo menos mais tres partes e um entao no fim!")

    if (parts[0] in variaveis):
        try:
            val1 = float(variaveis[parts[0]])
        except:
            print("A variavel", parts[0], "não contem números!")
            exit()
    else:
        try:
            val1 = float(parts[0])
        except:
            print(parts[0], "não é um número nem uma variável!")
    

    if (parts[-2] in variaveis):
        try:
            val2 = float(variaveis[parts[-2]])
        except:
            print("A variavel", parts[-2], "não contem números!")
            exit()
    else:
        try:
            val2 = float(parts[-2])
        except:
            print(parts[-2], "não é um número nem uma variável!")

    if (parts[1] == "igual"):
        return val1 == val2
    elif (parts[1] == "maior"):
        if (parts[2] == "igual"):
            return val1 >= val2
        else:
            return val1 > val2
    elif (parts[1] == "menor"):
        if (parts[2] == "igual"):
            return val1 <= val2
        else:
            return val1 < val2
    elif (parts[1] == "diferente"):
        return val1 != val2
    else:
        print(parts[1], "não é uma comparação válida!")
        exit()
