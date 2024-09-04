import PySimpleGUI as sg
#image path in downloads folder
pasta= r'\Users\ANACLARAFARIARODRIGU\Downloads'

#layout interface image
layout=[ 
    [sg.Text("example image")],
    [sg.Image(filename=pasta, subsample=4)],
    [sg.Button('ok')],
]

#create window
window=sg.window("exemplo de imagem",layout)

#loop events
while True:
    event, values=window.read()
    if event==sg.WINDOW_CLOSED or event=="ok": break 

#close window
window.close