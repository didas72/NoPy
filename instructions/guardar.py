from instructions.mathf import math

def guardar(parts, variaveis):
    if (parts[2]=="em" and parts[-1] in variaveis):
        if (parts[1] in variaveis):
            variaveis[parts[-1]] = variaveis[parts[1]]
        else:
            variaveis[parts[-1]] = parts[1]
    elif (parts[4]=="em" and parts[-1] in variaveis):
        parts.pop(0)
        variaveis[parts[-1]] = math(parts, variaveis)
    else:
        print("Não podes fazer isso!")
        exit()