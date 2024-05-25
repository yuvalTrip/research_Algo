import itertools
from typing import List, Any
from tsp_core import *

def nearest_neighbor(handler: TSPHandler, cities: List[Any]) -> Any:
    track = handler.new_track()
    visited = set()
    current_city = cities[0]
    while len(visited) < len(cities):
        handler.add_city_to_track(track, current_city)
        visited.add(current_city)
        next_city = min((c for c in cities if c not in visited), key=lambda c: handler.distance_data[current_city][c], default=None)
        if next_city is None:
            break
        current_city = next_city
    handler.add_city_to_track(track, track[0])  # Return to origin
    return track

def brute_force(handler: TSPHandler, cities: List[Any]) -> Any:
    best_track = None
    min_length = float('inf')

    for perm in itertools.permutations(cities):
        track = handler.new_track()
        for city in perm:
            handler.add_city_to_track(track, city)
        handler.add_city_to_track(track, track[0])  # Return to origin
        length = handler.track_length(track)
        if length < min_length:
            best_track = track
            min_length = length

    return best_track
