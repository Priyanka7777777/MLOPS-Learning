def analyse_dict(d):
    max_key = max(d, key=d.get)
    min_key = min(d, key=d.get)

    average_value = sum(d.values()) / len(d)

    max_pair = f"max key - {max_key} with value - {d[max_key]}"
    min_pair = f"min key - {min_key} with value - {d[min_key]}"
    average_value = f"average value - {average_value}"

    return max_pair, min_pair, average_value

print(analyse_dict({'a': 10, 'b': 5, 'c': 15}))

