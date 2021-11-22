def guardar(parts, variaveis):
    if (parts[0]=="guardar" and parts[2]=="em" and parts[-1][:1] == "="):
        if (parts[1][:1]=="="):
            variaveis[parts[-1]] = variaveis[parts[1]]
        else:
            variaveis[parts[-1]] = parts[1]
    else:
        print("Não podes fazer isso!")
        exit()
    print(variaveis)