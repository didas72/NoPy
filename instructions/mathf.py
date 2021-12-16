from math import fabs
import PySimpleGUI as sg

def mensagem_erro(mensagem):
    sg.Popup(mensagem, title='Erro', modal=True, grab_anywhere=True, keep_on_top=True)

def math(parts, variaveis):
    if (parts[0] in variaveis):
        try:
            val1 = float(variaveis[parts[0]])
        except:
            mensagem_erro("A variavel " + str(parts[0]) + " não contem números!")
            return False
    else:
        try:
            val1 = float(parts[0])
        except:
            mensagem_erro(str(parts[0]) + " não é um número nem uma variável!")
            return False
    

    if (parts[2] in variaveis):
        try:
            val2 = float(variaveis[parts[2]])
        except:
            mensagem_erro("A variavel " + str(parts[2]) + " não contem números!")
            return False
    else:
        try:
            val2 = float(parts[2])
        except:
            mensagem_erro(str(parts[2]) + " não é um número nem uma variável!")
            return False
        

    if (parts[1] == "mais" or parts[1] == "+"):
        return val1 + val2
    elif (parts[1] == "menos" or parts[1] == "-"):
        return val1 - val2
    elif (parts[1] == "vezes" or parts[1] == "*"):
        return val1 * val2
    elif (parts[1] == "dividir" or parts[1] == "/"):
        return val1 / val2
    elif (parts[1] == "resto" or parts[1] == "%"):
        return val1 % val2
    elif (parts[1] == "elevado"):
        return pow(val1, val2)
    elif (parts[1] == "binario_esquerda" or parts[1] == "binário_esquerda" or parts[1] == "<<"):
        return val1 << val2
    elif (parts[1] == "binario_direita" or parts[1] == "binário_direita" or parts[1] == ">>"):
        return val1 >> val2
    elif (parts[1] == "binario_e" or parts[1] == "binário_e" or parts[1] == "&"):
        return val1 & val2
    elif (parts[1] == "binario_ou" or parts[1] == "binário_ou" or parts[1] == "|"):
        return val1 | val2
    elif (parts[1] == "binario_diferente" or parts[1] == "binário_diferente" or parts[1] == "^"):
        return val1 ^ val2
    else:
        mensagem_erro(str(parts[1]) + " não é uma operação válida!")
        return False
    