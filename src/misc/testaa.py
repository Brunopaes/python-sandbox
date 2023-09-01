from collections import defaultdict

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


def aggregate_dicts(input_list):
    aggregated_dict = defaultdict(list)

    for item in input_list:
        catalog_key = tuple(item["catalogKey"].items())
        aggregated_dict[catalog_key].append(item["data"])

    output_list = [{"catalogKey": dict(key), "data": value} for key, value in aggregated_dict.items()]
    return output_list


if __name__ == '__main__':
    input_ = [
        {
            "seriesId": "SOLAR.GENERATION.01.SUM",  # BAIT
            "seriesType": "GENERATION",  # BAIT
            "aggregationHour": "01",  # BAIT
            "bbdsId": "generate-from-key",
            "ticker": "CLCGSOLA HR1 Index",
            "frequency": "Daily",
            "historyType": "Close",
            "periodicity": "DAY",
            "periodicityAggregationMethod": "SUM",
            "transformation": "NOMINAL",
            "technology": "SOLAR",  # BAIT
            "powerPlantId": "NA",
            "powerPlantName": "NA",
            "generatorName": "NA",
            "companyOwner": "NA",
            "regionCode": "CL",
            "regionName": "Chile",
            "ardUnit": "MWh",
            "unit": "MWh",
            "scale": 1,
            "precision": 0,
            "seasonality": "NSA",
            "referencePeriodEndDate": "2023-08-01",  # BAIT
            "reportTime": "2023-08-01T03:00:00+00:00",  # BAIT
            "reportTimeType": "BBG_DATA_PROCESSED_DATETIME",
            "ardValue": 10.4,  # BAIT
            "value": 10.4  # BAIT
        },
        {
            "seriesId": "SOLAR.GENERATION.01.SUM",  # BAIT
            "seriesType": "GENERATION",  # BAIT
            "aggregationHour": "01",  # BAIT
            "bbdsId": "generate-from-key",
            "ticker": "CLCGSOLA HR1 Index",
            "frequency": "Daily",
            "historyType": "Close",
            "periodicity": "DAY",
            "periodicityAggregationMethod": "SUM",
            "transformation": "NOMINAL",
            "technology": "SOLAR",  # BAIT
            "powerPlantId": "NA",
            "powerPlantName": "NA",
            "generatorName": "NA",
            "companyOwner": "NA",
            "regionCode": "CL",
            "regionName": "Chile",
            "ardUnit": "MWh",
            "unit": "MWh",
            "scale": 1,
            "precision": 0,
            "seasonality": "NSA",
            "referencePeriodEndDate": "2023-08-02",  # BAIT
            "reportTime": "2023-08-01T03:00:00+00:00",  # BAIT
            "reportTimeType": "BBG_DATA_PROCESSED_DATETIME",
            "ardValue": 10.4,  # BAIT
            "value": 10.4  # BAIT
        },
        {
            "seriesId": "SOLAR.GENERATION.02.SUM",  # BAIT
            "seriesType": "GENERATION",  # BAIT
            "aggregationHour": "02",  # BAIT
            "bbdsId": "generate-from-key",
            "ticker": "CLCGSOLA HR1 Index",
            "frequency": "Daily",
            "historyType": "Close",
            "periodicity": "DAY",
            "periodicityAggregationMethod": "SUM",
            "transformation": "NOMINAL",
            "technology": "SOLAR",  # BAIT
            "powerPlantId": "NA",
            "powerPlantName": "NA",
            "generatorName": "NA",
            "companyOwner": "NA",
            "regionCode": "CL",
            "regionName": "Chile",
            "ardUnit": "MWh",
            "unit": "MWh",
            "scale": 1,
            "precision": 0,
            "seasonality": "NSA",
            "referencePeriodEndDate": "2023-08-02",  # BAIT
            "reportTime": "2023-08-01T03:00:00+00:00",  # BAIT
            "reportTimeType": "BBG_DATA_PROCESSED_DATETIME",
            "ardValue": 10.4,  # BAIT
            "value": 10.4  # BAIT
        },
    ]

    data_format = {
        "catalogKey": ["aggregationHour", "seriesId", "seriesType"],
        "data": {
            "Key": ["bbdsId", "referencePeriodEndDate"],
            "data": {
                "ardUnit": "ardUnit",
                "ardValue": "ardValue",
                "periodicity": "periodicity",
                "precision": "precision",
                "referencePeriodEndDate": "referencePeriodEndDate",
                "reportTimeType": "reportTimeType",
                "scale": "scale",
                "unit": "unit",
                "value": "value"
            },
            "metadata": [],
            "version": "1.0"
        }
    }

    response = [restructure_dict(
        i,
        data_format
    ) for i in input_]

    # print(response)

    res = aggregate_dicts(response)

    print(res)