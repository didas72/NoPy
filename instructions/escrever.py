import PySimpleGUI as sg

def escrever(parts, variaveis):
    if (parts[1].startswith("'")):
        parts[1] = parts[1].replace("'","")
        texto_escrito = (parts[1])
    elif (parts[1] in variaveis):
        texto_escrito = (variaveis[parts[1]])
    return texto_escrito