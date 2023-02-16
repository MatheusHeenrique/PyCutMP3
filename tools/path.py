from sys import argv


class Path:

    def get_path(self):
        list_of_argv = argv

        # verificações
        file_txt = minutes = None
        audio = list_of_argv.index('-a')

        for item in list_of_argv:
            match item:
                case '-f':
                    file_txt = list_of_argv.index('-f')
                case '-m':
                    minutes = list_of_argv.index('-m')

        path_txt = path_audio = None
        if file_txt is not None:
            path_txt = list_of_argv[file_txt + 1]
            path_audio = list_of_argv[audio + 1]
        else:
            list_of_minutes = list()
            list_of_minutes.append(self.get_minutes(list_of_argv[minutes + 2]))
            list_of_minutes.append(self.get_minutes(list_of_argv[minutes + 1]))
            path_txt = list_of_minutes
            path_audio = list_of_argv[audio + 1]
        return path_txt, path_audio

    def get_minutes(self, minutes):
        numbers = list()
        number_string = ''

        for item in minutes:
            if item.isnumeric():
                number_string += item
            else:
                numbers.append(int(number_string))
                number_string = ''

        numbers.append(int(number_string))
        return numbers
