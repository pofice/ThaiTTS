import os
from moviepy.editor import AudioFileClip

def convert_mp3_to_mp4(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.mp3'):
            mp3_path = os.path.join(directory, filename)
            mp4_path = os.path.splitext(mp3_path)[0] + '.mp4'
            audio_clip = AudioFileClip(mp3_path)
            audio_clip.write_audiofile(mp4_path, codec='aac')
            print(f'Converted {mp3_path} to {mp4_path}')

# Use current directory
convert_mp3_to_mp4('.')