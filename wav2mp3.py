import os
from pydub import AudioSegment

def convert_wav_to_mp3(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.wav'):
            wav_path = os.path.join(directory, filename)
            mp3_path = os.path.splitext(wav_path)[0] + '.mp3'
            audio = AudioSegment.from_wav(wav_path)
            audio.export(mp3_path, format='mp3')
            print(f'Converted {wav_path} to {mp3_path}')

# 使用当前目录
convert_wav_to_mp3('.')