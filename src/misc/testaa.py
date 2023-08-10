def process_keys(payload, key_list):
    """
    Process the given keys in the payload dictionary.

    Parameters:
        payload (dict): The dictionary containing the data.
        key_list (list): List of keys to be processed.

    Returns:
        dict: A dictionary containing processed key-value pairs from the payload.
    """
    return {key: payload.get(key) for key in key_list if isinstance(key, str)}


def process_nested(payload, keys):
    """
    Process nested keys in the payload dictionary.

    Parameters:
        payload (dict): The dictionary containing the data.
        keys (list, dict, or str): Keys to be processed.

    Returns:
        dict, any: Processed nested dictionary or value.
    """
    if isinstance(keys, list):
        return process_keys(payload, keys)
    elif isinstance(keys, dict):
        return {inner_key: process_nested(payload, inner_nested_keys) for inner_key, inner_nested_keys in keys.items()}
    else:
        return payload.get(keys, keys)


def restructure_dict(payload, keys):
    """
    Restructure the payload dictionary based on the provided keys.

    Parameters:
        payload (dict): The dictionary containing the data.
        keys (dict): Dictionary specifying the structure of the output.

    Returns:
        dict: A restructured dictionary based on the provided keys.
    """
    return {outer_key: process_nested(payload, nested_keys) for outer_key, nested_keys in keys.items()}
