import os
from pythaitts import TTS
import re

def sanitize_filename(text):
    return re.sub(r'[^\w\s]', '', text).replace(' ', '_') + '.wav'

# 确保 output 文件夹存在
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

tts = TTS()

# 读取 text.txt 文件中的每一行文本
with open('text.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 将每一行文本转换为语音并保存为 .wav 文件
for line in lines:
    text = line.strip()
    if text:  # 确保文本不为空
        filename = os.path.join(output_dir, sanitize_filename(text))
        tts.tts(text, filename=filename)
        print(f'Saved: {filename}')