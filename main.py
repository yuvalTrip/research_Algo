from typing import Callable, Any, List
import tsp_output as out
import tsp_algorithms as alg
### To answer this problem, I got assistant GPT, my dad and my boyfriend.

# Function to solve the TSP using a specified algorithm and output type
def solve_tsp(algorithm: Callable, distance_data: Any, outputtype: out.OutputType) -> Any:
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
    # Distance matrix input data
    input_data1 = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    # Distance dictionary input data
    input_data2 = {
        'A': {'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30}
    }
    # Another distance matrix input data for testing
    input_data3 = [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ]

    # Test all combinations of algorithms and output types with input_data1
    print("Testing input_data1:")
    for algorithm in [alg.nearest_neighbor, alg.brute_force]:
        for outputtype in [out.Track, out.TrackLength]:
            result = solve_tsp(algorithm, input_data1, outputtype)
            print(f"{algorithm.__name__}, {outputtype.__name__}: {result}")

    # Test all combinations of algorithms and output types with input_data2
    print("\nTesting input_data2:")
    for algorithm in [alg.nearest_neighbor, alg.brute_force]:
        for outputtype in [out.Track, out.TrackLength]:
            result = solve_tsp(algorithm, input_data2, outputtype)
            print(f"{algorithm.__name__}, {outputtype.__name__}: {result}")

    # Test all combinations of algorithms and output types with input_data3
    print("\nTesting input_data3:")
    for algorithm in [alg.nearest_neighbor, alg.brute_force]:
        for outputtype in [out.Track, out.TrackLength]:
            result = solve_tsp(algorithm, input_data3, outputtype)
            print(f"{algorithm.__name__}, {outputtype.__name__}: {result}")