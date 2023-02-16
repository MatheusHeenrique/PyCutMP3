from tools.cut import Cut

audio_cutter = Cut()
type_of_request = audio_cutter.get_info()

if type_of_request:
    audio_cutter.cut_audio_with_minutes()
else:
    audio_cutter.cut_audio_with_file_txt()
