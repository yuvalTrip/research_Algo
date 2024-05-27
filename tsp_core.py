from abc import ABC, abstractmethod
from typing import List, Dict, Any, Callable
### To answer this problem, I got assistant GPT, my dad and my boyfriend.

# Abstract base class for handling TSP data and operations
class TSPHandler(ABC):
    def __init__(self, distance_data: Any):
        self.distance_data = distance_data # Store the distance data

    @abstractmethod
    def new_track(self) -> Any:
        pass  # Abstract method to create a new track

    @abstractmethod
    def add_city_to_track(self, track: Any, city: Any) -> Any:
        pass # Abstract method to add a city to the track

    @abstractmethod
    def track_length(self, track: Any) -> float:
        pass # Abstract method to calculate the length of the track

# Handler for distance data represented as a matrix (2D list)
class MatrixTSPHandler(TSPHandler):
    def new_track(self) -> List[int]:
        return [] # Return an empty list as the new track

    def add_city_to_track(self, track: List[int], city: int) -> List[int]:
        track.append(city)# Add the city to the track
        return track# Return the updated track

    def track_length(self, track: List[int]) -> float:
        total_distance = 0
        # Calculate the total distance for the track
        for i in range(len(track) - 1):
            total_distance += self.distance_data[track[i]][track[i + 1]]
        if len(track) > 1:
            total_distance += self.distance_data[track[-1]][track[0]]  # Return to the original city
        return total_distance# Return the total distance

# Handler for distance data represented as a dictionary
class DictTSPHandler(TSPHandler):
    def new_track(self) -> List[str]:
        return []# Return an empty list as the new track

    def add_city_to_track(self, track: List[str], city: str) -> List[str]:
        track.append(city)
        return track  # Return the updated track

    def track_length(self, track: List[str]) -> float:
        total_distance = 0
        # Calculate the total distance for the track
        for i in range(len(track) - 1):
            total_distance += self.distance_data[track[i]][track[i + 1]]
        if len(track) > 1 and track[0] != track[-1]:
            try:
                total_distance += self.distance_data[track[-1]][track[0]]  # Return to the original city
            except KeyError:
                raise ValueError(f"Missing distance data for returning from {track[-1]} to {track[0]}")
        return total_distance # Return the total distance

