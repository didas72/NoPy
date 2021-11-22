def escrever(parts, variaveis):
    if (parts[1].startswith("'")):
        parts[1] = parts[1].replace("'","")
        print(parts[1])
    elif (parts[1] in variaveis):
        print(variaveis[parts[1]])