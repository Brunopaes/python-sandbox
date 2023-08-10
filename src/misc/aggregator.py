from collections import defaultdict
from typing import Any, DefaultDict, Dict, List, Optional, Tuple


def aggregate(
    payload,
    aggregation_keys,
    values,
    aggregation_function="sum",
):
    return reducing_dimensionality(
        aggregated_map=filtering_keys(payload, aggregation_keys, values),
        aggregation_function=aggregation_function,
    )


def filtering_keys(
    payload,
    keys,
    values,
):
    aggregated_map = defaultdict(
        lambda: defaultdict(lambda: defaultdict(list))
    )

    for item in payload:
        key_values = tuple(
            (k, item.get(k)) for k in keys if k in item
        )
        data_values = tuple(
            (k, item.get(k)) for k in values if k in item
        )

        for value in values:
            aggregated_map[key_values][data_values][value].append(
                item.get(value, 0)
            )

    return aggregated_map


def reducing_dimensionality(
    aggregated_map: DefaultDict[Tuple[Tuple[str, str], Tuple[str, str]], Dict],
    aggregation_function: Optional[str] = "sum",
) -> List[Dict[str, Any]]:
    aggregated_list = []
    for key_values, data_values_map in aggregated_map.items():
        for data_values, values_map in data_values_map.items():
            aggregated_list.append(
                {
                    **dict(key_values),
                    **dict(data_values, **aggregation_functions(
                        values_map, aggregation_function
                    )),
                }
            )

    return aggregated_list


def aggregation_functions(
    value_map: DefaultDict[str, List],
    aggregation_function: Optional[str] = "sum"
) -> DefaultDict[Any, int]:
    aggregated_dict = defaultdict(int)
    for key, value_list in value_map.items():
        aggregated_dict[key] = {
            "sum": sum,
            "min": min,
            "max": max,
            "count": len,
            "avg": arithmetic_average
        }.get(aggregation_function, sum)(value_list)

    return aggregated_dict


def arithmetic_average(values_list: List[Any]) -> float:
    return sum(values_list) / len(values_list)


if __name__ == '__main__':
    from src.misc.testaa import restructure_dict
    payload = [
        {"name": "bruno", "id": "1ad", "date": "2023-01-01", "ardValue": 8, "value": 10},
        {"name": "bruno", "id": "1ad", "date": "2023-01-01", "ardValue": 9, "value": 10},
        {"name": "bruno", "id": "1ad", "date": "2023-01-01", "ardValue": 9, "value": 10}
    ]
    keys = ["name", "id", "date", "ardValue"]
    values = ["ardValue", "value"]

    result = aggregate(payload, keys, values, aggregation_function="avg")

    catalog_format = {
        "catalogKey": ["name", "id"],
        "Key": ["name", "id"],
        "data": {
            "date": "date",
            "nameDetails": ["name", "id"],
            "ardValue": "ardValue",
            "value": "value"
        },
        "metadata": [],
        "version": "1.0"
    }

    result_2 = [restructure_dict(result_, catalog_format) for result_ in result]
    print(result_2)
