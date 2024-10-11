from pythaitts import TTS
import re

def sanitize_filename(text):
    return re.sub(r'[^\w\s]', '', text).replace(' ', '_') + '.wav'

tts = TTS()
text = "ไม่มี"  # Double spaces to simulate a pause
filename = sanitize_filename(text)
file = tts.tts(text, filename=filename)  # It will get wav file path.