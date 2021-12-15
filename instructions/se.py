from UI import mensagem_erro

def se(parts, variaveis):
    parts.pop(0)

    if (len(parts) < 4 or (parts[-1] != "entao" and parts[-1] != "então")):
        mensagem_erro("Um 'se' tem de ter pelo menos mais três partes e um então no fim!")
        return (True, False)

    
    if (parts[0] in variaveis):
        try:
            val1 = float(variaveis[parts[0]])
        except:
            if (parts[1] == "igual" or parts[1] == "diferente"):
                val1 = variaveis[parts[0]]
            else:
                mensagem_erro("A variavel " + str(parts[0]) + " não contem números!")
                return (True, False)
    elif ((parts[1] == "igual" or parts[1] == "diferente") and parts[0].startswith("'")):
        val1 = parts[0].strip("'")
    else:
        try:
            val1 = float(parts[0])
        except:
            mensagem_erro(str(parts[0]) + " não é um número nem uma variável!")
            return (True, False)      

    
    if (parts[-2] in variaveis):
        try:
            val2 = float(variaveis[parts[-2]])
        except:
            if ((parts[1] == "igual" or parts[1] == "diferente")):
                val1 = variaveis[parts[-2]]
            else:
                mensagem_erro("A variavel " + str(parts[-2]) + " não contem números!")
                return (True, False)
    elif ((parts[1] == "igual" or parts[1] == "diferente") and parts[-2].startswith("'")):
        val2 = parts[-2].strip("'")
    else:
        try:
            val2 = float(parts[-2])
        except:
            mensagem_erro(str(parts[-2]) + " não é um número nem uma variável!")
            return (True, False)


    if (parts[1] == "igual"):
        return (val1 == val2, True)
    elif (parts[1] == "maior"):
        if (parts[2] == "igual"):
            return (val1 >= val2, True)
        else:
            return (val1 > val2, True)
    elif (parts[1] == "menor"):
        if (parts[2] == "igual"):
            return (val1 <= val2, True)
        else:
            return (val1 < val2, True)
    elif (parts[1] == "diferente"):
        return (val1 != val2, True)
    else:
        mensagem_erro(str(parts[1]) + "não é uma comparação válida!")
        return (True, False)
