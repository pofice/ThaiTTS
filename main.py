import os
from pythaitts import TTS
import re

def sanitize_filename(text):
    return re.sub(r'[^\w\s]', '', text).replace(' ', '_') + '.wav'

# Ensure output directory exists
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

tts = TTS()

# Custom function to convert numbers to Thai words
def number_to_thai_word(number):
    thai_numbers = {
        0: 'ศูนย์', 1: 'หนึ่ง', 2: 'สอง', 3: 'สาม', 4: 'สี่',
        5: 'ห้า', 6: 'หก', 7: 'เจ็ด', 8: 'แปด', 9: 'เก้า',
        10: 'สิบ', 20: 'ยี่สิบ', 30: 'สามสิบ', 40: 'สี่สิบ',
        50: 'ห้าสิบ', 60: 'หกสิบ', 70: 'เจ็ดสิบ', 80: 'แปดสิบ', 90: 'เก้าสิบ'
    }

    if number in thai_numbers:
        return thai_numbers[number]

    if number < 100:
        tens, ones = divmod(number, 10)
        return thai_numbers[tens * 10] + thai_numbers[ones]

    return str(number)  # Fallback for numbers not handled

def convert_numbers_to_words(text):
    words = text.split()
    converted_words = []
    for word in words:
        if word.isdigit():
            converted_word = number_to_thai_word(int(word))
            converted_words.append(converted_word)
        else:
            converted_words.append(word)
    return ' '.join(converted_words)

# Read each line of text from text.txt
with open('text.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Convert each line of text to speech and save as .wav file
for line in lines:
    text = line.strip()
    if text:  # Ensure text is not empty
        text = convert_numbers_to_words(text)
        filename = os.path.join(output_dir, sanitize_filename(text))
        tts.tts(text, filename=filename)
        print(f'Saved: {filename}')