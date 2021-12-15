import PySimpleGUI as sg

def mensagem_erro_c(mensagem):
    sg.Popup(mensagem, title='Erro', modal=True, grab_anywhere=True, keep_on_top=True)

def runCode(lines):
    Correr_layout = [[sg.Button('Iniciar')],
        [sg.Multiline(size=(800, 600), font=("Arial", 12), background_color='#222021', text_color='white', key='-CORRERMLINE-', disabled=True)]]

    Correr = sg.Window('Correr' , Correr_layout, default_element_size=(12, 1), auto_size_text=False, auto_size_buttons=False,      
        default_button_element_size=(12, 1), grab_anywhere=True ,finalize = True, resizable=True, margins=(0, 0), use_default_focus=0)

    Correr['-CORRERMLINE-'].Widget.config(wrap='none')
    Correr['-CORRERMLINE-'].Widget.config(insertbackground='white')
    Correr.Maximize()
    if (len(lines) and lines[0] == "Erro"):
        mensagem_erro_c("Erro ao ler o ficheiro!")

    variaveis = {}
    linha = 0
    nestLevel = 0
    lastCondition = False
    loopStack = []
    labelsFound = []
    labelLines = []

    from instructions.escrever import escrever
    from instructions.ler import ler
    from instructions.guardar import guardar
    from instructions.se import se
    from instructions.enquanto import enquanto

    while True:
        event, values = Correr.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Iniciar":
            linha = 0

        Correr['-CORRERMLINE-'].print("Programa iniciado")

        while (linha < len(lines)):
            parts = []
            remain = lines[linha].strip()

            while True:
                if (len(remain) <= 0): break

                if (remain.startswith("'")):
                    try:
                        strEndIndex = remain[1:len(remain)].index("'")
                        parts.append(remain[0:strEndIndex+2])
                        remain = remain[strEndIndex+3:len(remain)]
                    except:
                        print("Tens de fechar sempre as aspas!")
                        exit()
                else:
                    try:
                        partEndIndex = remain[0:len(remain)].index(" ")
                        parts.append(remain[0:partEndIndex].casefold())
                        remain = remain[partEndIndex+1:len(remain)]
                    except:
                        parts.append(remain.casefold())
                        break

            if (len(lines[linha]) > 1):
                instruction = parts[0]

                try:
                    if (nestLevel == 0):
                        # register label
                        if (lines[linha].endswith(":")):
                            if (lines[linha] not in labelsFound):
                                labelsFound.append(lines[linha].strip(":"))
                                labelLines.append(linha)
                        elif (instruction == "escrever"):
                            texto_escrito = escrever(parts, variaveis)
                            Correr['-CORRERMLINE-'].print(texto_escrito)
                        elif (instruction == "ler"):
                            valor_inserido = ler(parts, variaveis)
                            Correr['-CORRERMLINE-'].print('>>> ' + valor_inserido)
                        elif (instruction == "guardar"):
                            if not guardar(parts, variaveis):
                                break
                        elif (instruction == "se"):
                            res = se(parts, variaveis)
                            if (not res[1]): break

                            if (res[0]):
                                nestLevel = 0
                                lastCondition = True
                            else:
                                nestLevel = 1
                                lastCondition = False
                        elif (instruction == "enquanto"):
                            res = enquanto(parts, variaveis)
                            if (not res[1]): break
                            if (res[0]):
                                loopStack.append(linha)
                            else:
                                nestLevel = -1
                        elif (instruction == "fim"):
                            if (parts[1] == "de" and (parts[2] == "condicao" or parts[2] == "condição")):
                                nestLevel = 0
                            elif (parts[1] == "de" and parts[2] == "enquanto"):
                                try:
                                    linha = loopStack.pop() - 1
                                except:
                                    mensagem_erro_c("Não podes por fim de enquanto sem comecar um enquanto!")
                                    break
                        elif (instruction == "senao" or instruction == "senão"):
                            if (lastCondition):
                                nestLevel = 1
                            else:
                                nestLevel = 0
                            pass
                        elif (instruction.startswith("!")):
                            pass
                        elif (instruction == "sair"):
                            break
                        elif (instruction == "ir"):
                            if (parts[1] in labelsFound):
                                linha = labelLines[labelsFound.index(parts[1])]
                            else:
                                found = False
                                for cock in lines:
                                    if parts[1] + ":" in cock:
                                        linha = lines.index(cock) - 1
                                        found = True
                                        break

                                if (not found):
                                    mensagem_erro_c("A etiqueta não foi definida.")
                                    break
                        else:
                            mensagem_erro_c(parts[0] + " não é uma instrução válida! Se quiseres por um comentário, começa a linha com '!'")
                            break
                    else:
                        if (nestLevel > 0): #nestLevel de um se
                            if (instruction == "fim"):
                                if (parts[1] == "de" and (parts[2] == "condicao" or parts[2] == "condição")):
                                    nestLevel -= 1
                            elif (instruction == "se"):
                                nestLevel += 1
                            elif (instruction == "senao" or instruction == "senão"):
                                nestLevel -= 1
                        else: #nestLevel de um enquanto
                            if (instruction == "fim"):
                                if (parts[1] == "de" and parts[2] == "enquanto"):
                                    nestLevel += 1
                            elif (instruction == "enquanto"):
                                nestLevel -= 1
                except:
                    mensagem_erro_c(lines[linha] + " deu um erro!")
                    break

            linha += 1
    
        Correr['-CORRERMLINE-'].print("Fim do programa\n\n")
    Correr.close()