def escrever(parts, variaveis):
    if (parts[1].startswith("'")):
        parts.pop(0)
        escreve = ' '.join(parts)
        escreve = escreve.replace("'","")
        print(escreve)
    elif (parts[1] in variaveis):
        print(variaveis[parts[1]])