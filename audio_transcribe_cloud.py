import io
import os
# Imports the Google Cloud client library
#from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.cloud import speech_v1p1beta1 as speech

CURRENT_DIRECTORY = '/home/joseenrique/python'
# Instantiates a client
client = speech.SpeechClient()
text_file = open("Output" + ".txt", "w")
#os.path.basename(os.path.realpath(file))[:-4]
for directory, subdirectories, files in os.walk(CURRENT_DIRECTORY):
    for file in sorted(files):
        if file[-7:] == ".wav":
            # The name of the audio file to transcribe
            file_name = os.path.join(CURRENT_DIRECTORY, file)
            print("Currently processing file: " + file_name)
            # Loads the audio into memory
            with io.open(file_name, 'rb') as audio_file:
                content = audio_file.read()
                audio = types.RecognitionAudio(content=content)

            config = speech.types.RecognitionConfig(
                encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=44100,
                language_code='nl-NL',
                audio_channel_count=1,
                enable_speaker_diarization=True,
                diarization_speaker_count=2)

            # Detects speech in the audio file
            response = client.recognize(config, audio)
            for result in response.results:
              text_file.write(result.alternatives[0].transcript.encode('utf-8'))
text_file.close()
            
