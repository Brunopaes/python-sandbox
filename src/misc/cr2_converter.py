# -*- coding: utf-8 -*-
import imageio
import rawpy
import tqdm
import os


def raw_to_jpg(directory_path):
    destination_path = os.path.abspath(
        os.path.join('data\\', directory_path.split("\\")[-1])
    )
    try:
        os.mkdir(destination_path)
    except FileExistsError:
        pass
    for picture in tqdm.tqdm(os.listdir(directory_path)):
        try:
            with rawpy.imread(os.path.join(directory_path, picture)) as raw:
                rgb = raw.postprocess()

            imageio.imsave(os.path.join(
                destination_path,
                '{}.JPG'.format(picture.split('.')[0])
            ), rgb)

        except rawpy._rawpy.LibRawFileUnsupportedError:
            pass


if __name__ == '__main__':
    raw_to_jpg(r"C:\Users\Bruno\Desktop\100CANON")
