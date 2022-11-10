from pydub import AudioSegment

available_syllables = set(["ма", "ши", "на", "ли", "си", "чка", "річ", "ти", "са", "ста", "вок", "ка"])

def split_in_syllables(word: str):
    i = 0
    current_syllable = ""
    result = []
    while i < len(word):
        current_syllable += word[i]
        if current_syllable in available_syllables:
            result.append(current_syllable)
            current_syllable = ""
        i += 1
    return result

if __name__ == '__main__':
    words = ["малина", "марічка", "річна", "річка", "стати", "каста", "калина", "каса", "качка"]
    for word in words:
        combined = AudioSegment.empty()
        syllables = split_in_syllables(word)
        for syllable in syllables:
            syllable_voice = AudioSegment.from_wav(f'./audio/{syllable}.wav')
            combined += syllable_voice
        combined.export(f"./output/{word}.wav", format="wav")
        print(f"Generated audio representation of word {word}")

