import logging

import num2words
from pydub import AudioSegment

logger = logging.getLogger(__name__)

def detect_num_and_convert(word):
    numbers = "0123456789.-"
    is_number = all(map(lambda x: x in numbers, word))
    if is_number:
        try:
            return num2words.num2words(word, lang="uk")
        except Exception as e:
            print(e)
            return word
    else:
        return word

if __name__ == '__main__':
    for i in [97563, 1000000, -1000000, 13234.4112, 244719]:
        combined = AudioSegment.empty()
        text = detect_num_and_convert(str(i))
        for part in text.split(" "):
            voice_part = AudioSegment.from_wav(f'./audio/{part}.wav')
            combined += voice_part
        print(f"Generated audio representation of number {str(i)}")
        combined.export(f"./output/{str(i)}.wav", format="wav")