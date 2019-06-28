from utilitarios import convert_string
from pydub import AudioSegment
import os


def minutos(lista_minutos, path_mp3):
    # abrindo audio
    audio = AudioSegment.from_mp3(path_mp3)

    # pegando minutagem exata para cortar
    inicio_fim_corte = calculo_corte(lista_minutos)

    # fazendo o corte
    novo_audio = audio[inicio_fim_corte[0]:inicio_fim_corte[1]]

    # salvando
    local_salvar = os.path.dirname(path_mp3)
    local_salvar = os.path.join(local_salvar, 'file.mp3')

    novo_audio.export(local_salvar, format='mp3')


def calculo_corte(lista):
    lista_resp = list()

    for m in lista:
        if len(m) == 2:
            conta = ((m[0] * 60) + m[1]) * 1000
            lista_resp.append(conta)

        elif len(m) == 3:
            conta = (((((m[0] * 60) + m[1]) * 60) + m[2]) * 1000)
            lista_resp.append(conta)

    lista_resp.sort()
    return lista_resp


def file_txt(path_txt, path_mp3):
    # abrindo audio
    audio = AudioSegment.from_mp3(path_mp3)

    # convertendo strings para minutos e organizando em listas
    lista_minutos = list()

    for linha in open(path_txt):
        lista_lixo = list()

        string1 = linha[:linha.index(' ')]
        string2 = linha[linha.index(' ') + 1:-1]

        lista_lixo.append(convert_string(string1))
        lista_lixo.append(convert_string(string2))

        lista_minutos.append(lista_lixo)

    # cortando a musica
    for c in range(0, len(lista_minutos)):
        # pegando minutagem exata para cortar
        inicio_fim_corte = calculo_corte(lista_minutos[c])

        # fazendo o corte
        novo_audio = audio[inicio_fim_corte[0]:inicio_fim_corte[1]]

        # salvando
        local_salvar = os.path.dirname(path_mp3)
        local_salvar = os.path.join(local_salvar, f'file{c}.mp3')

        novo_audio.export(local_salvar, format='mp3')

