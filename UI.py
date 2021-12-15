import PySimpleGUI as sg
import os
import webbrowser
from main import runCode

dirname = os.path.dirname(__file__)
icon_tantantAn = os.path.join(dirname, "Icon.ico")

def mensagem_erro(mensagem):
    sg.Popup(mensagem, title='Erro', modal=True, grab_anywhere=True, keep_on_top=True)

def pergunta_guardar(nome_ficheiro, PseudoPy):
    Guardar_pergunta_layout = [[sg.Text("Gostaria de guardar o programa?")],
                               [sg.Column([[sg.Button("Sim"), sg.Button("Não")]], justification='center')]]
    Guardar_pergunta = sg.Window("Guardar?", Guardar_pergunta_layout, font=("Arial", 12), use_default_focus=0 , no_titlebar=True, modal=True, grab_anywhere=True, keep_on_top=True)
    while True:
        event, values = Guardar_pergunta.read()
        if event == "Sim":
            guardar(nome_ficheiro, PseudoPy)
            break
        if event == "Não":
            apagar_vazio(nome_ficheiro, ficheiro_path=False)
            break
    Guardar_pergunta.close()

def abrir_ficheiro(main_window):
    main_window.close()
    escolha_ficheiro_layout=[[sg.Text("Escolha o Ficheiro: "), sg.Input(readonly=(True), change_submits=True, disabled_readonly_background_color="#363636"), sg.FileBrowse(key='File', button_text='Procurar')],
                [sg.Button("Voltar"), sg.Button('Abrir')] ]
    escolha_ficheiro = sg.Window("Escolha de Ficheiro", escolha_ficheiro_layout , finalize=True ,use_default_focus=0, modal=False , no_titlebar=True, grab_anywhere=True, keep_on_top=True)
    while True:
        event, values = escolha_ficheiro.read()
        if event == "Voltar":
            break
        if event == "Abrir":
            ficheiro_path = str(values['File'])
            if os.path.exists(ficheiro_path):
                if values:
                    #lista_fp = ficheiro_path.split('/')
                    #nome_ficheiro = lista_fp[-1]
                    nome_ficheiro = os.path.basename(ficheiro_path)
                    escolha_ficheiro.close()
                    PseudoPy_f(nome_ficheiro, main_window, ficheiro_path)
                    return nome_ficheiro and ficheiro_path
            else:
                mensagem = "O ficheiro escolhido não existe"
                mensagem_erro(mensagem)
    escolha_ficheiro.close()
    mainwindow()

def criarficheiro_f(main_window):
    main_window.close()
    nome_ficheiro_layout=[[sg.Text('Nome do arquivo a ser criado:'),sg.InputText()],
            [sg.Button("Ok", bind_return_key=True),sg.Button("Voltar")] ]
    criar_ficheiro = sg.Window("Criar Ficheiro", nome_ficheiro_layout, no_titlebar=True,grab_anywhere=True, keep_on_top=True)
    while True:
        event, values = criar_ficheiro.read()
        if event == "Voltar":
            break
        if event == "Ok":
            if values[0] != '':
                criar_ficheiro.disappear()
                nome_ficheiro = values[0] + ".txt"
                if not os.path.isfile(nome_ficheiro):
                    arquivo = open(nome_ficheiro,"w")
                    arquivo.close()
                    PseudoPy_f(nome_ficheiro, main_window, ficheiro_path=False)
                    return nome_ficheiro
                else:
                    criar_ficheiro.reappear()
                    mensagem = "Já exite um ficheiro com esse nome"
                    mensagem_erro(mensagem)
            else:
                mensagem = "Não se pode criar um ficheiro sem nome"
                mensagem_erro(mensagem)
    criar_ficheiro.close()
    mainwindow()

def texto_ficheiro(ficheiro_path, PseudoPy):
    ficheiro_aberto = open(ficheiro_path,'rt', encoding='utf-8')
    texto = ficheiro_aberto.readlines()
    for i in texto:
        if i[-1] == '\n':
            i = i. replace('\n', '')
        PseudoPy['-MLINE-'].print(i)
    ficheiro_aberto.close()

def apagar_vazio(nome_ficheiro, ficheiro_path):
    if not ficheiro_path:
        tamanho = os.path.getsize(nome_ficheiro)
        if tamanho == 0:
            os.remove(nome_ficheiro)
    if ficheiro_path:
        tamanho = os. path. getsize(ficheiro_path)
        if tamanho == 0:
            os.remove(ficheiro_path)

def PseudoPy_f(nome_ficheiro, main_window, ficheiro_path):
    main_window.close()
    menu_def = [['Ficheiro', ['Correr','Guardar', 'Voltar', 'Sair']],
                ['Ajuda', ['Sobre...']]]
    
    PseudoPy_layout = [[sg.MenuBar(menu_def, font=("Arial", 10), background_color='white', text_color='black')],
                        #[sg.Column([[sg.Button('Correr', border_width=0, button_color="#333333")]], justification = 'left')],
                       [sg.Multiline(size=(800, 600), font=("Arial", 12), background_color='#222021', text_color='white', key='-MLINE-')]]
    
    PseudoPy = sg.Window(("PseudoPy: " + nome_ficheiro) , PseudoPy_layout, default_element_size=(12, 1), auto_size_text=False, auto_size_buttons=False,      
        default_button_element_size=(12, 1), grab_anywhere=True ,finalize = True, resizable=True, margins=(0, 0), icon= icon_tantantAn, use_default_focus=0, enable_close_attempted_event=True)
    PseudoPy['-MLINE-'].Widget.config(wrap='none') 
    PseudoPy['-MLINE-'].Widget.config(insertbackground='white')
    PseudoPy.Maximize()
    if ficheiro_path:
        texto_ficheiro(ficheiro_path, PseudoPy)
    while True:
        event, values = PseudoPy.read(close=False)
        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Sair':
            if ficheiro_path:
                pergunta_guardar(ficheiro_path, PseudoPy)
            else:
                pergunta_guardar(nome_ficheiro, PseudoPy)
            #if os.path.isfile(nome_ficheiro):
                #apagar_vazio(nome_ficheiro, ficheiro_path)
            break
        if event == 'Correr':
            from ficheiro import loadLines
            if ficheiro_path:
                guardar(ficheiro_path, PseudoPy)
                lines = loadLines(ficheiro_path)
            else:
                guardar(nome_ficheiro, PseudoPy)
                lines = loadLines(nome_ficheiro)
            runCode(lines)
        if event == 'Guardar':
            if ficheiro_path:
                guardar(ficheiro_path, PseudoPy)
            else:
                guardar(nome_ficheiro, PseudoPy)
        if event == 'Sobre...':
            webbrowser.open("http://didas72.hopto.org/pseudo_python_PT.html", new=1)
        #if event == 'Apagar':
            #if ficheiro_path:
                #os.remove(ficheiro_path)
            #else:
                #os.remove(nome_ficheiro)
        if event == 'Voltar':
            if ficheiro_path:
                pergunta_guardar(ficheiro_path, PseudoPy)
            else:
                pergunta_guardar(nome_ficheiro, PseudoPy)
            break
    PseudoPy.close()
    if event == 'Voltar':
        mainwindow()

def guardar(nome_ficheiro, PseudoPy):
    save_file = open(nome_ficheiro, 'wt', encoding = 'UTF-8')
    save_file.write(PseudoPy['-MLINE-'].get())
    save_file.close()

def mainwindow():
    dirname = os.path.dirname(__file__)
    Logo_tantanTAN = os.path.join(dirname, "Logo.png")
    Logo = sg.Image(filename=Logo_tantanTAN)
    main_window_layout = [  [sg.Column([[Logo]], justification='center')],
                            [sg.Column([[sg.Text('PseudoPython', font= ("Arial", 30))]], justification='center')],
                            [sg.Column([[sg.Button('Abrir Ficheiro', font = ("Arial", 13)), sg.Button('Criar Ficheiro', font = ("Arial", 13))]], justification='center')]]

    main_window = sg.Window('PseudoPython', main_window_layout, use_default_focus=0, grab_anywhere=True, icon= icon_tantantAn)
    while True:
        event, values = main_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Abrir Ficheiro':
            abrir_ficheiro(main_window)
        if event == 'Criar Ficheiro':
            criarficheiro_f(main_window)
    main_window.close()

sg.theme_input_background_color('#363636')
sg.theme_input_text_color('white')
sg.theme_background_color("#333333")
sg.theme_button_color("#363636")
sg.theme_element_background_color("#333333")
sg.theme_element_text_color("white")
sg.theme_text_color("white")
sg.theme_text_element_background_color("#333333")

mainwindow()