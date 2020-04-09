# -*- coding: utf-8 -*-
from google.cloud.speech_v1 import enums
from google.cloud import speech_v1

import io
import os


def set_path():
    """This function sets settings.json in PATH.

    Returns
    -------

    """
    path = os.path.abspath('settings.json')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path


def sample_recognize(local_file_path):
    """This function transcribe a short audio file using synchronous speech
    recognition.

    Parameters
    ----------
    local_file_path : Path to local audio file, e.g. /path/audio.wav

    Returns
    -------

    """
    set_path()
    client = speech_v1.SpeechClient()

    with io.open(local_file_path, "rb") as f:
        content = f.read()

    audio = {
        "content": content
    }

    response = client.recognize({
        "language_code": "pt-BR",
        "sample_rate_hertz": 16000,
        "encoding": enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
    }, audio)

    for result in response.results:
        alternative = result.alternatives[0]
        print(u"{}".format(alternative.transcript))


sample_recognize(r'C:\Users\bruno\PycharmProjects\python-sandbox\data\1.mp3')
