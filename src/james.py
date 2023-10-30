import jmespath


def restructure_dictionary(input_dict, query):
    """
    Restructures a non-nested dictionary using JMESPath query.

    Args:
        input_dict (dict): The dictionary to be restructured.
        query (str): The JMESPath query specifying the new structure.

    Returns:
        dict: The restructured dictionary.
    """
    result = jmespath.search(query, input_dict)
    return result


# Example dictionary
data = {
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
}

# JMESPath query to restructure the dictionary
query = "{bbdsId: bbdsId, tickerDetails: {ticker: ticker, historyType: historyType, frequency: frequency}, data: {scale: scale}}"

# Restructure the dictionary using the function
restructured_data = restructure_dictionary(data, query)
print(restructured_data)

{
    'TICKER': ['GFLX_SINITA_GR', 'GFLX_RONQUE_FE'],
    'MINDATE': "01-01-2022",  #DD-MM-YYYY
    'MAXDATE': "01-02-2022"  #DD-MM-YYYY
}


