from typing import Callable, Any, List
import tsp_output as out
import tsp_algorithms as alg

# Function to solve the TSP using a specified algorithm and output type
def solve_tsp(algorithm: Callable, distance_data: Any, outputtype: out.OutputType) -> Any:
    """
    Function to solve the TSP using a specified algorithm and output type.

    Args:
        algorithm (Callable): The algorithm to solve the TSP.
        distance_data (Any): The distance data for the TSP.
        outputtype (out.OutputType): The output type for the TSP solution.

    Returns:
        Any: The result of the TSP solution.

    Examples:
        >>> input_data1 = [
        ...     [0, 10, 15, 20],
        ...     [10, 0, 35, 25],
        ...     [15, 35, 0, 30],
        ...     [20, 25, 30, 0]
        ... ]
        >>> solve_tsp(alg.nearest_neighbor, input_data1, out.Track)
        [0, 1, 3, 2, 0]
        >>> solve_tsp(alg.brute_force, input_data1, out.Track)
        [0, 1, 3, 2, 0]
        >>> solve_tsp(alg.nearest_neighbor, input_data1, out.TrackLength)
        80
        >>> solve_tsp(alg.brute_force, input_data1, out.TrackLength)
        80

        >>> input_data2 = {
        ...     'A': {'B': 10, 'C': 15, 'D': 20},
        ...     'B': {'A': 10, 'C': 35, 'D': 25},
        ...     'C': {'A': 15, 'B': 35, 'D': 30},
        ...     'D': {'A': 20, 'B': 25, 'C': 30}
        ... }
        >>> solve_tsp(alg.nearest_neighbor, input_data2, out.Track)
        ['A', 'B', 'D', 'C', 'A']
        >>> solve_tsp(alg.brute_force, input_data2, out.Track)
        ['A', 'B', 'D', 'C', 'A']
        >>> solve_tsp(alg.nearest_neighbor, input_data2, out.TrackLength)
        80
        >>> solve_tsp(alg.brute_force, input_data2, out.TrackLength)
        80

        >>> input_data3 = [
        ...     [0, 2, 9, 10],
        ...     [1, 0, 6, 4],
        ...     [15, 7, 0, 8],
        ...     [6, 3, 12, 0]
        ... ]
        >>> solve_tsp(alg.nearest_neighbor, input_data3, out.Track)
        [0, 1, 3, 2, 0]
        >>> solve_tsp(alg.brute_force, input_data3, out.Track)
        [0, 2, 3, 1, 0]
        >>> solve_tsp(alg.nearest_neighbor, input_data3, out.TrackLength)
        33
        >>> solve_tsp(alg.brute_force, input_data3, out.TrackLength)
        21
    """
    # Create the appropriate handler for the distance data
    handler = outputtype.create_handler(distance_data)
    # Get the list of cities from the distance data
    cities = list(distance_data.keys()) if isinstance(distance_data, dict) else list(range(len(distance_data)))
    # Solve the TSP using the specified algorithm
    track = algorithm(handler, cities)
    # Extract the output from the track using the specified output type
    return outputtype.extract_output_from_track(handler, track)

# Main block to test the TSP solution with different data sets and algorithms
if __name__ == "__main__":
    import doctest
    doctest.testmod()
