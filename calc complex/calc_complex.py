
from time import sleep
import PySimpleGUI as sg
#layout
sg.theme('DarkAmber')
layout=[
    [sg.Text('Z1 : '),sg.Text('Real :'),sg.Input(key='x1',size=(10,1)),sg.Text('Imaginario :'),sg.Input(key='y1',size=(10,1))],
    [sg.Text('Z2 : '),sg.Text('Real :'),sg.Input(key='x2',size=(10,1)),sg.Text('Imaginario :'),sg.Input(key='y2',size=(10,1))],
    [sg.Text(' [1] Conjugado [2] Soma [3] Subtracao \n [4] Multiplicacao [5] Divisao [6]sair ')],
    [sg.Text('Opcao desejada : '),sg.Input(key='op',size=(10,1)),sg.Button('Calc')],
    [sg.Text('Resultado :'),sg.Text('',key='res')]
]
#janela
janela=sg.Window('CALCULADORA DE NUMEROS COMPLEXOS',layout)
op = 0
while True:
    eventos,valores=janela.read()
    x1=float(valores['x1'])
    y1=float(valores['y1'])
    x2=float(valores['x2'])
    y2=float(valores['y2'])
    op=int(valores['op'])
    z1 = complex(x1,y1)
    z2 = complex(x2,y2)
    sleep(1.5)
    if eventos == sg.WINDOW_CLOSED or op==6:
        break
    if  op == 1:
        c1=z1.conjugate()
        c2=z2.conjugate()
        res=('z1 = ',c1,'z2 = ',c2)
        janela['res'].update(res)
        sleep(1.5)
    elif op == 2:
        sz = z1+z2
        janela['res'].update(sz)
        sleep(1.5)
    elif op == 3:
        subz = z1-z2
        janela['res'].update(subz)
        sleep(1.5)
    elif op == 4:
        mz = z1*z2
        janela['res'].update(mz)
        sleep(1.5)
    elif op == 5:
        dz = z1/z2
        janela['res'].update(dz)
        sleep(1.5)
    else:
        erro=('selecione uma opcao valida')
        janela['res'].update(erro)
        sleep(1.5)

