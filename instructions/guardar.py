from instructions.mathf import math
import PySimpleGUI as sg

def guardar(parts, variaveis):
    if (parts[2]=="em"):
        if (parts[1] in variaveis):
            variaveis[parts[-1]] = variaveis[parts[1]]
        else:
            variaveis[parts[-1]] = parts[1]
    elif (parts[4]=="em"):
        parts.pop(0)
        variaveis[parts[-1]] = math(parts, variaveis)
        if (variaveis[parts[-1]] == False):
            return False
    else:
        sg.Popup("Não podes fazer isso!", title='Erro', modal=True, grab_anywhere=True, keep_on_top=True)
        return False

    return True    