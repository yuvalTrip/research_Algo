from itertools import permutations
### To answer this problem, I got assistant GPT, and my boyfriend.
## https://github.com/erelsgl-at-ariel/research-5784/blob/2fde0548bd7b2c1b4b59b55c64ecf317edc38c2b/05-python-design-patterns/code/50-flyweight.py#L4
class TSPInputProcessor:
    # Test 1: Invalid input type
    """
    >>> input_data1 = [
    ...    [0, 10, 15, 20],
    ...    [10, 0, 35, 25],
    ...    [15, 35, 0, 30],
    ...    [20, 25, 30, 0]
    ... ]
          >>> TSPmainFunc(input_data1, 'invalid_type', 'track', 'nearest_neighbor')
          Traceback (most recent call last):
              ...
          ValueError: Invalid input type

          # Test 2: Invalid output type
          >>> TSPmainFunc(input_data1, 'distances_only', 'invalid_type', 'nearest_neighbor')
          Traceback (most recent call last):
              ...
          ValueError: Invalid output type

          # Test 3: Invalid algorithm
          >>> TSPmainFunc(input_data1, 'distances_only', 'track', 'invalid_algorithm')
          Traceback (most recent call last):
              ...
          ValueError: Invalid algorithm

          # Test 4: Empty input
          >>> TSPmainFunc({}, 'distances_only', 'length', 'nearest_neighbor')
          Traceback (most recent call last):
              ...
          ValueError: Input data is empty

          # Test 5: Single city input
          >>> TSPmainFunc({'A': {}}, 'distances_with_names', 'length', 'nearest_neighbor')
          Traceback (most recent call last):
              ...
          ValueError: TSP requires at least 2 cities

        # Test 6: Single city input with track output
        >>> TSPmainFunc({'A': {}}, 'distances_with_names', 'track', 'nearest_neighbor')
        Traceback (most recent call last):
            ...
        ValueError: TSP requires at least 2 cities

         # Test 7: Two cities with same distances

    >>> input_data3 = [
    ...     [0, 10, 10],
    ...     [10, 0, 10],
    ...     [10, 10, 0]
    ... ]
    >>> TSPmainFunc(input_data3, 'distances_only', 'length', 'brute_force')
    30
    >>> TSPmainFunc(input_data3, 'distances_only', 'track', 'brute_force')
    ([0, 1, 2, 0], 30)

    # Test 8: Three cities with different distances

    >>> input_data4 = [
    ...     [0, 10, 15],
    ...     [10, 0, 35],
    ...     [15, 35, 0]
    ... ]
    >>> TSPmainFunc(input_data4, 'distances_only', 'length', 'nearest_neighbor')
    60
    >>> TSPmainFunc(input_data4, 'distances_only', 'track', 'nearest_neighbor')
    ([0, 1, 2, 0], 60)

    # Test 9: Four cities with different distances
    >>> input_data5 = [
    ...     [0, 10, 15, 20],
    ...     [10, 0, 35, 25],
    ...     [15, 35, 0, 30],
    ...     [20, 25, 30, 0]
    ... ]

    >>> TSPmainFunc(input_data5, 'distances_only', 'length', 'brute_force')
    80
    >>> TSPmainFunc(input_data5, 'distances_only', 'track', 'brute_force')
    ([0, 1, 3, 2, 0], 80)

    >>> input_data1 = [
    ...    [0, 10, 15, 20],
    ...    [10, 0, 35, 25],
    ...    [15, 35, 0, 30],
    ...    [20, 25, 30, 0]
    ... ]

    >>> TSPmainFunc(input_data1, 'distances_only', 'length', 'brute_force')# Test 1: distances_only, length, brute_force
    80

    >>> TSPmainFunc(input_data1, 'distances_only', 'track', 'nearest_neighbor') # Test 3: distances_only, track, nearest_neighbor
    ([0, 1, 3, 2, 0], 80)

    >>> TSPmainFunc(input_data1, 'distances_only', 'track', 'brute_force')# Test 5: distances_only, track, brute_force
    ([0, 1, 3, 2, 0], 80)


    >>> TSPmainFunc(input_data1, 'distances_only', 'length', 'nearest_neighbor')# Test 7: distances_only, length, nearest_neighbor
    80


    >>> input_data2 = {
    ...    'A': {'B': 10, 'C': 15, 'D': 20},
    ...    'B': {'A': 10, 'C': 35, 'D': 25},
    ...    'C': {'A': 15, 'B': 35, 'D': 30},
    ...    'D': {'A': 20, 'B': 25, 'C': 30}
    ... }

    >>> TSPmainFunc(input_data2, 'distances_with_names', 'track', 'brute_force') # Test 2: distances_with_names, track, brute_force
    (['A', 'B', 'D', 'C', 'A'], 80)


    # Test 4: distances_with_names, length, nearest_neighbor
    result = TSPmainFunc(input_data2, 'distances_with_names', 'length', 'nearest_neighbor')
    #print(result)  # Expected output: 80



    # Test 6: distances_with_names, length, brute_force
    result = TSPmainFunc(input_data2, 'distances_with_names', 'length', 'brute_force')
   # print(result)  # Expected output: 80



    # Test 8: distances_with_names, track, nearest_neighbor
    result = TSPmainFunc(input_data2, 'distances_with_names', 'track', 'nearest_neighbor')
    #print(result)  # Expected output: (['A', 'B', 'D', 'C', 'A'], 80)

     # Test with different results for brute_force and nearest_neighbor

    >>> input_data_diff = [
    ...    [0, 2, 9, 10],
    ...    [1, 0, 6, 4],
    ...    [15, 7, 0, 8],
    ...    [6, 3, 12, 0]
    ... ]

    >>> TSPmainFunc(input_data_diff, 'distances_only', 'track', 'nearest_neighbor')
    ([0, 1, 3, 2, 0], 33)

    >>> TSPmainFunc(input_data_diff, 'distances_only', 'track', 'brute_force')
    ([0, 2, 3, 1, 0], 21)
    """

    def __init__(self, input_data, input_type):
        self.input_data = input_data
        self.input_type = input_type

    def process(self):
        if self.input_type == 'distances_only':
            return self.input_data
        elif self.input_type == 'distances_with_names':
            cities = list(self.input_data.keys())
            size = len(cities)
            if size < 2:
                raise ValueError("TSP requires at least 2 cities")
            distance_matrix = [[0] * size for _ in range(size)]
            for i in range(size):
                for j in range(size):
                    if i != j:
                        distance_matrix[i][j] = self.input_data[cities[i]][cities[j]]
            return distance_matrix, cities
        else:
            raise ValueError("Invalid input type")


class TSPOutputProcessor:
    def __init__(self, output_type):
        self.output_type = output_type

    def process(self, route, distance, cities=None):
        if self.output_type == 'track':
            if cities:
                return [cities[i] for i in route], distance
            else:
                return route, distance
        elif self.output_type == 'length':
            return distance
        else:
            raise ValueError("Invalid output type")


class TSPSolver:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def solve(self, distance_matrix):
        if self.algorithm == 'brute_force':
            return self._brute_force(distance_matrix)
        elif self.algorithm == 'nearest_neighbor':
            return self._nearest_neighbor(distance_matrix)
        else:
            raise ValueError("Invalid algorithm")

    def _brute_force(self, distance_matrix):
        n = len(distance_matrix)
        min_path = float('inf')
        best_route = None
        for perm in permutations(range(1, n)):
            current_path = 0
            k = 0
            for i in perm:
                current_path += distance_matrix[k][i]
                k = i
            current_path += distance_matrix[k][0]
            #print("Current path:", current_path)  # Debug
            if current_path < min_path:
                min_path = current_path
                best_route = (0,) + perm + (0,)
            #print("Min path:", min_path)  # Debug
        # Convert the tuple to a list before returning
        return list(best_route), min_path

    def _nearest_neighbor(self, distance_matrix):
        n = len(distance_matrix)
        if n == 0:
            raise ValueError("Input data is empty")
        unvisited = set(range(1, n))
        current = 0
        route = [current]
        total_distance = 0
        while unvisited:
            next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
            total_distance += distance_matrix[current][next_city]
            current = next_city
            route.append(current)
            unvisited.remove(current)
        total_distance += distance_matrix[current][0]
        route.append(0)
        return route, total_distance


def TSPmainFunc(input_data, input_type, output_type, algorithm):
    # Process input
    processor = TSPInputProcessor(input_data, input_type)
    processed_input = processor.process()

    # If processed input has cities list, unpack it
    if input_type == 'distances_with_names':
        distance_matrix, cities = processed_input
    else:
        distance_matrix = processed_input
        cities = None

    # Solve TSP
    solver = TSPSolver(algorithm)
    route, distance = solver.solve(distance_matrix)

    # Process output
    output_processor = TSPOutputProcessor(output_type)
    result = output_processor.process(route, distance, cities)
    return result


# Example usage
if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
