import itertools
from typing import List, Any
from tsp_core import *
### To answer this problem, I got assistant GPT, my dad and my boyfriend.

# Nearest neighbor algorithm for solving the TSP
def nearest_neighbor(handler: TSPHandler, cities: List[Any]) -> Any:
    track = handler.new_track() # Create a new track
    visited = set() # Set to keep track of visited cities
    current_city = cities[0]  # Start from the first city
    while len(visited) < len(cities):
        # Add current city to the track
        handler.add_city_to_track(track, current_city)
        # Mark current city as visited
        visited.add(current_city)
        # Find the nearest unvisited city
        next_city = min((c for c in cities if c not in visited), key=lambda c: handler.distance_data[current_city][c], default=None)
        if next_city is None:
            # If no unvisited cities are left, break the loop
            break
        current_city = next_city # Move to the next city
    handler.add_city_to_track(track, track[0])  # Return to the city we started from
    return track # Return the constructed track

# Brute force algorithm for solving the TSP
def brute_force(handler: TSPHandler, cities: List[Any]) -> Any:
    best_track = None  # Variable to store the best track
    min_length = float('inf') # Variable to store the minimum track length

    # Iterate over all possible permutations of cities
    for perm in itertools.permutations(cities):
        track = handler.new_track()  # Create a new track
        for city in perm:
            handler.add_city_to_track(track, city) # Add city to the track
        handler.add_city_to_track(track, track[0])  # Return to the city we started in
        length = handler.track_length(track) # Calculate the track length
        if length < min_length:
            best_track = track # Update the best track
            min_length = length # Update the minimum length

    return best_track # Return the best track found
