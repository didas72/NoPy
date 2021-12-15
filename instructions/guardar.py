from instructions.mathf import math
from UI import mensagem_erro

def guardar(parts, variaveis):
    if (parts[2]=="em"):
        if (parts[1] in variaveis):
            variaveis[parts[-1]] = variaveis[parts[1]]
        else:
            variaveis[parts[-1]] = parts[1]
    elif (parts[4]=="em"):
        parts.pop(0)
        variaveis[parts[-1]] = math(parts, variaveis)
    else:
        mensagem_erro("Não podes fazer isso!")
        return False

    return True    