# -*- coding: utf-8 -*-
import json


def read_json(path):
    """This function opens a json file and parses it content into a python dict.
    Parameters
    ----------
    path : str
        The json file path.
    Returns
    -------
    json.load : dict
        The json content parsed into a python dict.
    """
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError as e:
        print(e.args[-1])
