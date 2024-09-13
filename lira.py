import PySimpleGUI as sg
matriz = [
    [1,2,3],
    [4,5,6]
    ]  

#Os primeiro colchete se trata da linha e o segundo se trata da coluna
print(matriz[1][2])

#O primeiro FOR acessa a linha
for linha in matriz: 
    #O segundo FOR acessa os valores da coluna em sua respectiva linha
    for valor in linha: