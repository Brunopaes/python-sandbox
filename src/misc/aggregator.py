from collections import defaultdict

def aggregate_nested_dicts(payload_map, keys, values):
    aggregated_map = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    for item in payload_map:
        key_values = tuple((k, item.get(k, None)) for k in keys)
        data_values = tuple((k, item.get(k, None)) for k in values)

        for v in values:
            aggregated_map[key_values][v] += item.get(v, 0)

    aggregated_list = []
    for key_values, value_map in aggregated_map.items():
        data_dict = dict(key_values)
        data_dict.update(value_map)
        aggregated_list.append(data_dict)

    return aggregated_list

# Example input
input_payload = [
    {"a": 1, "b": 2, "fd": 1, "gd": 5},
    {"a": 1, "b": 2, "fd": 1, "gd": 10}
]
groupby_keys = ["a", "b"]
values_to_aggregate = ["fd", "gd"]

aggregated_result = aggregate_nested_dicts(input_payload, groupby_keys, values_to_aggregate)
print(aggregated_result)
