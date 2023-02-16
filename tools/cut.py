from pydub import AudioSegment
from tools.path import Path
import os


class Cut(Path):

    def __init__(self):
        super().__init__()
        self.path_txt = None
        self.path_audio = None

    def get_info(self):
        self.path_txt, self.path_audio = super().get_path()

        response = None
        if type(self.path_txt) == type(list()):
            response = True  # usar cut_audio_with_minutes
        else:
            response = False  # usar cut_audio_with_file_txt

        return response

    def cut_audio_with_minutes(self):
        # abrindo audio
        audio = AudioSegment.from_mp3(self.path_audio)

        # pegando minutagem exata para cortar
        cutting_time = self.cut_calculation(self.path_txt)

        # fazendo o corte
        new_audio = audio[cutting_time[0]:cutting_time[1]]

        # salvando
        where_to_save = os.path.dirname(self.path_audio)
        where_to_save = os.path.join(where_to_save, 'file.mp3')

        new_audio.export(where_to_save, format='mp3')

    def cut_audio_with_file_txt(self):
        # abrindo audio
        audio = AudioSegment.from_mp3(self.path_audio)

        # convertendo strings para minutos e organizando em listas
        list_of_minutes = list()

        for line in open(self.path_txt):
            lista_lixo = list()

            string1 = line[:line.index(' ')]
            string2 = line[line.index(' ') + 1:-1]

            lista_lixo.append(super().get_minutes(string1))
            lista_lixo.append(super().get_minutes(string2))

            list_of_minutes.append(lista_lixo)

        # cortando a musica
        for i in range(0, len(list_of_minutes)):
            # pegando minutagem exata para cortar
            cut_list = self.cut_calculation(list_of_minutes[i])

            # fazendo o corte
            new_audio = audio[cut_list[0]:cut_list[1]]

            # salvando
            where_to_save = os.path.dirname(self.path_audio)
            where_to_save = os.path.join(where_to_save, f'file{i}.mp3')

            new_audio.export(where_to_save, format='mp3')

    def cut_calculation(self, list_of_minutes):
        new_minutes_list = list()

        for i in list_of_minutes:
            if len(i) == 2:
                conta = ((i[0] * 60) + i[1]) * 1000
                new_minutes_list.append(conta)
            elif len(i) == 3:
                conta = (((((i[0] * 60) + i[1]) * 60) + i[2]) * 1000)
                new_minutes_list.append(conta)

        new_minutes_list.sort()
        return new_minutes_list
