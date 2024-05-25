from typing import Callable, Any, List
import tsp_output as out
import tsp_algorithms as alg


def solve_tsp(algorithm: Callable, distance_data: Any, outputtype: out.OutputType) -> Any:
    handler = outputtype.create_handler(distance_data)
    cities = list(distance_data.keys()) if isinstance(distance_data, dict) else list(range(len(distance_data)))
    track = algorithm(handler, cities)
    return outputtype.extract_output_from_track(handler, track)


if __name__ == "__main__":
    input_data1 = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    input_data2 = {
        'A': {'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30}
    }

    input_data3 = [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ]

    # Test all combinations with input_data1
    print("Testing input_data1:")
    for algorithm in [alg.nearest_neighbor, alg.brute_force]:
        for outputtype in [out.Track, out.TrackLength]:
            result = solve_tsp(algorithm, input_data1, outputtype)
            print(f"{algorithm.__name__}, {outputtype.__name__}: {result}")

    # Test all combinations with input_data2
    print("\nTesting input_data2:")
    for algorithm in [alg.nearest_neighbor, alg.brute_force]:
        for outputtype in [out.Track, out.TrackLength]:
            result = solve_tsp(algorithm, input_data2, outputtype)
            print(f"{algorithm.__name__}, {outputtype.__name__}: {result}")

        # Test all combinations with input_data3
    print("\nTesting input_data3:")
    for algorithm in [alg.nearest_neighbor, alg.brute_force]:
        for outputtype in [out.Track, out.TrackLength]:
            result = solve_tsp(algorithm, input_data3, outputtype)
            print(f"{algorithm.__name__}, {outputtype.__name__}: {result}")