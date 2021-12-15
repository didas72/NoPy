import PySimpleGUI as sg
def ler(parts, variaveis):
    ler_pro_layout = [[sg.Input(font=("Arail", 12)), sg.Button('Ok', visible=False, bind_return_key=True)]]
    ler_pro = sg.Window('Ler', ler_pro_layout,  keep_on_top= True, modal = True, no_titlebar=True)
    while True:
        event, values = ler_pro.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Ok':
            variaveis[parts[1]] = values[0]
            valor_inserido = values[0]
            break
    ler_pro.close()
    return valor_inserido
    