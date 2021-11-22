def math(parts, variaveis):
    if (parts[0].startswith("=")):
        if (parts[0] in variaveis):
            val1 = variaveis[parts[0]]
        else:
            print("A variavel", parts[0], "não existe.")
            exit()
    else:
        try:
            val1 = float(parts[0])
        except:
            print(parts[0], "não é um número nem uma variável!")

    if (parts[2].startswith("=")):
        if (parts[2] in variaveis):
            val2 = variaveis[parts[0]]
        else:
            print("A variavel", parts[2], "não existe.")
            exit()
    else:
        try:
            val2 = float(parts[2])
        except:
            print(parts[2], "não é um número nem uma variável!")

    if (parts[1] == "mais" or parts[1] == "+"):
        return val1 + val2
    elif (parts[1] == "menos" or parts[1] == "-"):
        return val1 - val2
    elif (parts[1] == "vezes" or parts[1] == "*"):
        return val1 * val2
    elif (parts[1] == "dividir" or parts[1] == "/"):
        return val1 * val2
    elif (parts[1] == "resto" or parts[1] == "%"):
        return val1 % val2
    else:
        print(parts[1], "não é uma operação válida!")
        exit()
    