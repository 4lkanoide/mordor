from time import sleep
import datetime


def isint(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False


def tempo(ano, mes, dia):
    atual = datetime.datetime.now()
    anos = atual.year - ano




segundos = float()

data = {
    'ano' : int(),
    'mes' : int(),
    'dia' : int(),
}

while True:
    data['ano'] = input('Que ano você nasceu?(AAAA) ')
    data['mes'] = input('Que mês você nasceu?(MM) ')
    data['dia'] = input('Que dia você nasceu?(DD) ')
    if len(data['ano']) != 4 and isint(data['ano']) is False:
        print('ERRO')
    elif len(data['mes']) != 2 and isint(data['mes']) is False:
        print('ERRO')
    elif len(data['dia']) != 2 and isint(data['dia']) is False:
        print('ERRO')
    else:
        tempo()
