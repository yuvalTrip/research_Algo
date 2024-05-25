"""
Traveling Salesman Problem (TSP) - FlyWeight pattern.

Author: Erel Segal-Halevi
Since: 2024-05
"""

from typing import Callable, List, Tuple, Union
import itertools
import numpy as np


# Define the OutputType enum
class OutputType:
    Route = 1
    TotalDistance = 2


# Helper function to calculate distance between two points
def calculate_distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Brute force algorithm to solve TSP
def brute_force_tsp(distance_matrix: np.ndarray) -> List[int]:
    num_cities = len(distance_matrix)
    shortest_route = None
    min_distance = float('inf')

    for perm in itertools.permutations(range(num_cities)):
        current_distance = sum(distance_matrix[perm[i], perm[i + 1]] for i in range(num_cities - 1))
        current_distance += distance_matrix[perm[-1], perm[0]]  # Return to start
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_route = perm
    return list(shortest_route)


# Nearest neighbor algorithm to solve TSP
def nearest_neighbor_tsp(distance_matrix: np.ndarray) -> List[int]:
    num_cities = len(distance_matrix)
    unvisited = set(range(num_cities))
    current_city = 0
    route = [current_city]
    unvisited.remove(current_city)

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city, city])
        route.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    return route


# Flyweight function to solve TSP
def solve_tsp(algorithm: Callable, input_data: Union[List[Tuple[float, float]], np.ndarray],
              output_type: OutputType = OutputType.Route, **kwargs) -> Union[List[int], float]:
    if isinstance(input_data, list):
        num_cities = len(input_data)
        distance_matrix = np.zeros((num_cities, num_cities))
        for i in range(num_cities):
            for j in range(i + 1, num_cities):
                distance = calculate_distance(input_data[i], input_data[j])
                distance_matrix[i, j] = distance
                distance_matrix[j, i] = distance
    else:
        distance_matrix = input_data

    route = algorithm(distance_matrix)

    if output_type == OutputType.Route:
        return route
    elif output_type == OutputType.TotalDistance:
        total_distance = sum(distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))
        total_distance += distance_matrix[route[-1], route[0]]  # Return to start
        return total_distance


# Example usage and doctests
if __name__ == "__main__":
    import doctest


    def test_solve_tsp():
        """
        >>> coords = [(0,0), (1,1), (2,0)]
        >>> solve_tsp(algorithm=brute_force_tsp, input_data=coords, output_type=OutputType.Route)
        [0, 1, 2]

        >>> solve_tsp(algorithm=brute_force_tsp, input_data=coords, output_type=OutputType.TotalDistance)
        4.82842712474619

        >>> distance_matrix = np.array([[0, 1, 2], [1, 0, 1], [2, 1, 0]])
        >>> solve_tsp(algorithm=nearest_neighbor_tsp, input_data=distance_matrix, output_type=OutputType.Route)
        [0, 1, 2]

        >>> solve_tsp(algorithm=nearest_neighbor_tsp, input_data=distance_matrix, output_type=OutputType.TotalDistance)
        4.0
        """
        pass


    (failures, tests) = doctest.testmod()
    print(f"{failures} failures, {tests} tests")
