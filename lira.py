import PySimpleGUI as sg
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]  

#Os primeiro colchete se trata da linha e o segundo se trata da coluna
print(matriz[1][2])


matriz[0][0]=10
print(matriz) 

for i in range(3): 
    for be  in range (3):
        print(matriz[i][be], end='')
    print('')

