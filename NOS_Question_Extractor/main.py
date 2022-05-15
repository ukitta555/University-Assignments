from moviepy.editor import *

from secret import DEEPGRAM_API_KEY


def mp4_to_mp3(mp4, mp3):
    mp4_without_frames = AudioFileClip(mp4)
    mp4_without_frames.write_audiofile(mp3)
    mp4_without_frames.close() # function call mp4_to_mp3("my_mp4_path.mp4", "audio.mp3")


from deepgram import Deepgram
import asyncio

# The API key you created in step 1

# Replace with your file path and audio mimetype
VIDEO = "08-NOS.720p.mov"
PATH_TO_FILE = "audio.mp3"
MIMETYPE = 'audio/mp3'

# mp4_to_mp3(VIDEO, PATH_TO_FILE)

async def main():
    # Initializes the Deepgram SDK
    dg_client = Deepgram(DEEPGRAM_API_KEY)

    with open(PATH_TO_FILE, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': MIMETYPE}
        options = {'punctuate': True, 'language': 'uk'}

        print('Requesting transcript...')
        print('Your file may take up to a couple minutes to process.')
        print('While you wait, did you know that Deepgram accepts over 40 audio file formats? Even MP4s.')
        print('To learn more about customizing your transcripts check out developers.deepgram.com')

        response = await dg_client.transcription.prerecorded(source, options)
        with open("08-NOS.txt", 'w', encoding='utf-8') as f:
            response = response.get('results').get('channels')[0].get('alternatives')[0].get('transcript').split('.')
            for line in response:
                f.writelines(line+"\n")
            # f.write(response)




asyncio.run(main())