import PySimpleGUI as sg

# All the stuff inside your window.
layout = [ ]
Sonic_flamenguista_com_cachumba=0
for dois in range(3):
    linha = []


    for contador in range(3):
        linha.append(sg.Button('', size=(6, 3), key= Sonic_flamenguista_com_cachumba))
        Sonic_flamenguista_com_cachumba +=1 
    layout.append(linha)

jogador_atual= "X" 

matriz = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
    ]  
    
def ler_jogadas(event):
    global matriz

    for contador1 in range(3):
        for contador2 in range(3):
            if matriz[contador1][contador2] == event:
                matriz[contador1][contador2] = jogador_atual

print(matriz)

# Create the Window
window = sg.Window('Hello Example', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break


    for i in range(9):
    
        if event == i:
            ler_jogadas(event)
            window[event].update(jogador_atual)
            
    
    jogador_atual = "O" if jogador_atual == "X" else "X"

    
    print(matriz)
window.close()
