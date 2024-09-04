import PySimpleGUI as sg
def sonic_flamenguista():

    # All the stuff inside your window.
    layout = [  [sg.Text("What's your name?")],
                [sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Hello Example', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        print('Hello', values[0], '!')

    window.close()


# All the stuff inside your window.
layout = [  [sg.InputText(default_text='digite o nome do aluno')],
            [sg.InputText(default_text='digite o nome do aluno')],
            [sg.InputText(default_text='digite o nome do aluno')],
            [sg.Button('Avançar',key='rato petista'), sg.Button('Cancelar')] ]

# Create the Window
window = sg.Window('Entrada do Boletim', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == "rato petista":
        sonic_flamenguista()



    print('Aluno', values[0], '!')

# All the stuff inside your window.
layout = [  [sg.InputText(default_text='digite a nota do aluno')],
            [sg.InputText(default_text='digite a nota do aluno')],
            [sg.InputText(default_text='digite a nota do aluno')],
            [sg.Button('Avançar'), sg.Button('Cancelar')] ]

window.close()

