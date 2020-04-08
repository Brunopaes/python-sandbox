# -*- coding: utf-8 -*-
from google.cloud.speech_v1 import enums
from google.cloud import speech_v1

import io
import os


def sample_recognize(local_file_path):
    """
    Transcribe a short audio file using synchronous speech recognition

    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """

    path = r"C:\Users\bruno\PycharmProjects\python-sandbox\src\neural_nets" \
           r"\settings.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path
    client = speech_v1.SpeechClient()

    language_code = "pt-BR"
    sample_rate_hertz = 16000
    encoding = enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED

    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"{}".format(alternative.transcript))


sample_recognize(r'C:\Users\bruno\Downloads\4.m4a')
