def process_fields(payload, fields):
    """
    Process the fields of a payload dictionary.

    Parameters:
    payload (dict): The payload dictionary to extract values from.
    fields (list or dict): A list of field names or a dictionary with subfields.

    Returns:
    dict: A dictionary containing the extracted values from the payload.
    """
    result = {}
    for field in fields:
        if isinstance(field, dict):
            for sub_key, sub_fields in field.items():
                result[sub_key] = process_fields(payload, sub_fields)
        else:
            result[field] = payload[field]
    return result


def restructure_payload(payload, keys):
    """
    Restructure a payload dictionary based on specified keys and fields.

    Parameters:
    payload (dict): The payload dictionary to restructure.
    keys (dict): A dictionary where keys are key types and values are field lists or dictionaries.

    Returns:
    dict: The restructured payload dictionary.
    """
    restructured_payload = {}

    for key_type, key_fields in keys.items():
        restructured_payload[key_type] = process_fields(
            payload[key_type], key_fields)

    return restructured_payload


payload = {
    "key": {
        "seriesId": "WIND.GENERATION.01.SUM",
        "seriesType": "GENERATION",
        "aggregationHour": "01"
    },
    "data": {
        "bbdsId": "generate-from-key",
        "ticker": "CLCGWIND Index",
        "historyType": "Mid Close",
        "frequency": "Daily",
        "referencePeriodEndDate": "2023-08-01",
        "ardValue": 10,
        "value": 10
    }
}

keys = {
    "key": ["seriesId", "seriesType", "aggregationHour"],
    "data": [
        {"tickerDetails": ["ticker", "historyType", "frequency"]},
        "bbdsId"
    ]
}

restructured_payload = restructure_payload(payload, keys)
print(restructured_payload)
