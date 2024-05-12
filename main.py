def deep_sorted(data):
    """
      Returns a string describing the sorted structure of the given deep data structure.

      The function sorts the elements at all levels:
      - Values in lists, tuples, and sets are arranged in ascending order.
      - Values in dictionaries are arranged in ascending order of keys.

      Args:
      data (dict, list, tuple, set, int, str, etc.): Input deep data structure.

      Returns:
      str: String describing the sorted structure of the input data.

      Examples:
      >>> deep_sorted({"a": 5, "c": 6, "b": [1, 3, 2, 4]})
      '{"a":5, "b":[1, 2, 3, 4], "c":6}'

      >>> deep_sorted(((((1, 2), 3), 4), 5, 6))
      '((((1, 2), 3), 4), 5, 6)'

      >>> deep_sorted([(5, 4), {'a': 9, 'b': 7, 'c': 8}, {3, 2, 1}])
      '[(4, 5), {"a":9, "b":7, "c":8}, {1, 2, 3}]'

      >>> deep_sorted({'b': [3, 6, {'x': 9, 'y': 7}, 2, 7, 0], 'c': 7, 'a': 6})
      '{"a":6, "b":[0, 2, 3, 6, 7, {"x":9,"y":7}], "c":7}'

      >>> deep_sorted({})
      '{}'

      >>> deep_sorted([])
      '[]'

      >>> deep_sorted(())
      '()'

      >>> deep_sorted(set())
      '{}'

      >>> deep_sorted(5)
      '5'

      >>> deep_sorted("hello")
      'hello'
      """
    if isinstance(data, dict):
        sorted_dict = {}
        for key in sorted(data.keys()):
            sorted_dict[key] = deep_sorted(data[key])
        return "{" + ", ".join(f'"{k}":{v}' for k, v in sorted_dict.items()) + "}"
    elif isinstance(data, (list, tuple, set)):
        sorted_data = sorted(map(deep_sorted, data))
        if isinstance(data, tuple):
            return "(" + ", ".join(sorted_data) + ")"
        elif isinstance(data, set):
            return "{" + ", ".join(sorted_data) + "}"
        else:
            return "[" + ", ".join(sorted_data) + "]"
    else:
        return str(data)

if _name_ == '_main_':
    x = eval(input())
    print(deep_sorted(x))