# cortar com arq.txt, ex: python principal.py -f "C:\path\para\arq_txt.txt" -a "C:\path\para\música.mp3"
# obs1: no arquivo de texto os minutos devem ser digitados assim: 1:20 2:30
# obs2: no arquivo com os minutos você deve dar um entrer apos o ultimo minuto, se não ira dar erro
# cortar com minutos, ex: python principal.py -m 0:00 0:10 -a "C:\path\para\música.mp3"
from utilitarios import verif_entrada
from utilitarios import corte

# programa principal
minutos, path_mp3 = verif_entrada()

if type(minutos) == type(list()):
    corte.minutos(minutos, path_mp3)
else:
    corte.file_txt(minutos, path_mp3)
