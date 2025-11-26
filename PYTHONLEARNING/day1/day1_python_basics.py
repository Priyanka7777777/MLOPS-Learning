# -----------------------------------------
# Function using *args
# -----------------------------------------
def sum_all_numbers(*args):
    """Returns the sum of all numbers passed as arguments."""
    total = sum(args)
    return total


# -----------------------------------------
# Function using **kwargs
# -----------------------------------------
def print_details(**kwargs):
    """Prints key-value pairs passed as keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# -----------------------------------------
# Function with type hints + returns multiple values
# -----------------------------------------
def analyze_dict(d: dict) -> tuple[str, int, str, int, float]:
    """
    Returns:
    - max key and its value
    - min key and its value
    - average value
    """
    max_key = max(d, key=d.get)
    min_key = min(d, key=d.get)

    max_value = d[max_key]
    min_value = d[min_key]
    avg_value = sum(d.values()) / len(d)

    return max_key, max_value, min_key, min_value, avg_value


# -----------------------------------------
# Script section that calls all functions
# -----------------------------------------
if __name__ == "__main__":

    print("---- Calling *args function ----")
    print("Sum is:", sum_all_numbers(1, 2, 3, 4, 5))

    print("\n---- Calling **kwargs function ----")
    print_details(name="Anjali", course="MLOps", score=95)

    print("\n---- Calling typed + multi-return function ----")
    result = analyze_dict({'a': 10, 'b': 5, 'c': 15})
    print(f"Max key: {result[0]} with value: {result[1]}")
    print(f"Min key: {result[2]} with value: {result[3]}")
    print(f"Average value: {result[4]}")
