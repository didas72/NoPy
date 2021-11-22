from mathf import math

def guardar(parts, variaveis):
    if (parts[2]=="em" and parts[-1][:1] == "="):
        if (parts[1][:1]=="="):
            variaveis[parts[-1]] = variaveis[parts[1]]
        else:
            variaveis[parts[-1]] = parts[1]
    elif (parts[4]=="em" and parts[-1][:1] == "="):
        parts.pop(0)
        variaveis[parts[-1]] = math(parts, variaveis)
    else:
        print("Não podes fazer isso!")
        exit()