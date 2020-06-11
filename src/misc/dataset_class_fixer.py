# -*- coding: utf-8 -*-
from helpers import read_json
from tqdm import tqdm

import json
import os

path = r'C:\Users\bruno\Desktop\juntas_moto+carro_new\labels'
out_path = r'C:\Users\bruno\Desktop\juntas_moto+carro_new\new'

list_dir = os.listdir(path)

for elem in tqdm(list_dir[100:]):
    dict_ = read_json(os.path.join(path, elem))
    try:
        dict_.get('annotations').get('instances')[0]['class'] = 'junta_carro'
    except IndexError:
        print(elem)
        continue

    with open(os.path.join(out_path, elem), 'w') as f:
        json.dump(dict_, f)
