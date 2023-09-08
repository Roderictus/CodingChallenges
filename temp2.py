def aggregate_dicts(dict_list):
    aggregated = {}

    for d in dict_list:
        # Each dictionary in the list contains just one key-value pair.
        key, value = list(d.items())[0]

        if value in aggregated:
            aggregated[value].append(key)
        else:
            aggregated[value] = [key]

    return aggregated


data = [{'M': 1}, {'s': 4}, {'p': 2}, {'i': 4}]
result = aggregate_dicts(data)
print(result)
