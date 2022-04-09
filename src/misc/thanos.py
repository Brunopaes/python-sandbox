from PIL import Image

import json
import io
import os


def binarize(filepath):
    return bytearray(open(filepath, "rb").read())


def de_binarize(bytes_):
    return Image.open(io.BytesIO(bytes_))


if __name__ == '__main__':
    directory = r'C:\Users\Bruno\iCloudDrive\Documents' \
                r'\Playboy\Playboy Photos\alejandra-guilmant'

    dict_ = {}
    for file in os.listdir(directory):
        dict_[file] = '{}'.format(binarize(r'{}\{}'.format(directory, file)))

    json.dump(dict_, open('export.json', 'w'))
    de_binarize(bytearray(df.bin[0], 'utf-8'))
