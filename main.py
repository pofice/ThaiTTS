from pythaitts import TTS

tts = TTS()
file = tts.tts("ยินดีที่ได้รู้จักค่ะ", filename="cat.wav") # It will get wav file path.
wave = tts.tts("ยินดีที่ได้รู้จักค่ะ",return_type="waveform") # It will get waveform.