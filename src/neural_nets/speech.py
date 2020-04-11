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


def local_short_recognition(local_file_path):
    """This function transcribes a local short audio file using speech
    recognition.

    Parameters
    ----------
    local_file_path : Path to local audio file, e.g. /path/audio.wav.

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
        "encoding": enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED
    }, audio)

    for result in response.results:
        alternative = result.alternatives[0]
        print(u"{}".format(alternative.transcript))


def sample_long_running_recognize(storage_uri):
    """This function transcribes a cloud long audio file using speech
    recognition.

    Parameters
    ----------
    storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]

    Returns
    -------

    """
    set_path()
    client = speech_v1.SpeechClient()
    audio = {
        "uri": storage_uri
    }
    operation = client.long_running_recognize({
        "sample_rate_hertz": 16000,
        "language_code": "pt-BR",
        "encoding": enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
    }, audio)

    for result in operation.result().results:
        alternative = result.alternatives[0]
        print(u"{}".format(alternative.transcript))


if __name__ == '__main__':
    sample_long_running_recognize('gs://speech-bruno/3_1.mp3')
