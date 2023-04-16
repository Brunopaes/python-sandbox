import datetime
import random
from collections import defaultdict
from operator import itemgetter

import pandas


def generate_payload(records=1000):
    """Generates mocked payloads to test aggregator function.

    Parameters
    ----------
    records : int, optional
        Records to generate.

    Returns
    -------
    payload : list
        Generated payload's list.

    """
    payload = []
    for i in range(records):
        item = {
            "technology": random.choice(technologies),
            "date": datetime.date.today().replace(day=random.randint(1, 30)),
            "variable": random.choice(variables),
            "value": random.randint(1, 100)
        }
        payload.append(item)

    return payload


def aggregate_payload(payload, keys, values):
    """Given a list of keys and values, aggregates a list of
    dictionaries.

    Parameters
    ----------
    payload : list
        Data payload.

    keys : list
        Keys to aggregate.

    values : str
        Values to be aggregated.

    Returns
    -------
    result : list
        Aggregated data dictionaries.

    Examples
    --------
    >>> payload_ = [
    >>>     {"technology": "hydro", "date": datetime.date.today(), "variable": "hour_01", "value": 20}
    >>>     {"technology": "hydro", "date": datetime.date.today(), "variable": "hour_01", "value": 10}
    >>>     {"technology": "hydro", "date": datetime.date.today(), "variable": "hour_02", "value": 20}
    >>> ]

    >>> aggregate_payload(payload_, keys=["technology", "date", "variable"], value="value")

    >>> [
    >>>     {"technology": "hydro", "date": datetime.date.today(), "variable": "hour_01", "value": 30},
    >>>     {"technology": "hydro", "date": datetime.date.today(), "variable": "hour_02", "value": 20}
    >>> ]

    """
    key_fn = itemgetter(*keys)
    groups = defaultdict(int)
    for item in payload:
        key = key_fn(item)
        groups[key] += item[values]

    return [dict(
        zip(keys + [values], key + (value,))
    ) for key, value in groups.items()]


if __name__ == '__main__':
    technologies = ["hydro", "solar", "wind", "thermal", "geothermal"]
    variables = [f"hour_{i:02d}" for i in range(1, 26)]

    result = aggregate_payload(
        generate_payload(10000),
        ["technology", "date", "variable"],
        "value"
    )

    print(pandas.DataFrame.from_records(result).sort_values(by=[
        "technology", "date", "variable"
    ]))
