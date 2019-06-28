from sys import argv


def verif_entrada():
    # criando lista do sys.argv
    listaArgv = argv

    # verificações
    file = minutos = None
    mp3 = listaArgv.index('-a')

    for c in range(0, 2):
        try:
            if c == 0:
                file = listaArgv.index('-f')
            else:
                minutos = listaArgv.index('-m')
        except:
            continue

    if file is not None:
        path_txt = listaArgv[file + 1]
        return path_txt, listaArgv[mp3 + 1]
    else:
        lista_min = list()
        lista_min.append(convert_string(listaArgv[minutos + 1]))
        lista_min.append(convert_string(listaArgv[minutos + 2]))
        return lista_min, listaArgv[mp3 + 1]


def convert_string(string):
    lista_num = list()
    numero = ''

    for n in string:
        if n.isnumeric():
            numero += n
        else:
            lista_num.append(int(numero))
            numero = ''

    lista_num.append(int(numero))
    return lista_num
