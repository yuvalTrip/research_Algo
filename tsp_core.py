from abc import ABC, abstractmethod
from typing import List, Dict, Any, Callable

class TSPHandler(ABC):
    def __init__(self, distance_data: Any):
        self.distance_data = distance_data

    @abstractmethod
    def new_track(self) -> Any:
        pass

    @abstractmethod
    def add_city_to_track(self, track: Any, city: Any) -> Any:
        pass

    @abstractmethod
    def track_length(self, track: Any) -> float:
        pass

class MatrixTSPHandler(TSPHandler):
    def new_track(self) -> List[int]:
        return []

    def add_city_to_track(self, track: List[int], city: int) -> List[int]:
        track.append(city)
        return track

    def track_length(self, track: List[int]) -> float:
        total_distance = 0
        for i in range(len(track) - 1):
            total_distance += self.distance_data[track[i]][track[i + 1]]
        if len(track) > 1:
            total_distance += self.distance_data[track[-1]][track[0]]  # Return to the origin
        return total_distance

# class DictTSPHandler(TSPHandler):
#     def new_track(self) -> List[str]:
#         return []
#
#     def add_city_to_track(self, track: List[str], city: str) -> List[str]:
#         track.append(city)
#         return track
#
#     def track_length(self, track: List[str]) -> float:
#         total_distance = 0
#         for i in range(len(track) - 1):
#             total_distance += self.distance_data[track[i]][track[i + 1]]
#         if len(track) > 1:
#             total_distance += self.distance_data[track[-1]][track[0]]  # Return to the origin
#         return total_distance

# class DictTSPHandler(TSPHandler):
#     def new_track(self) -> List[str]:
#         return []
#
#     def add_city_to_track(self, track: List[str], city: str) -> List[str]:
#         track.append(city)
#         return track
#
#     def track_length(self, track: List[str]) -> float:
#         total_distance = 0
#         for i in range(len(track) - 1):
#             total_distance += self.distance_data[track[i]][track[i + 1]]
#         if len(track) > 1:
#             try:
#                 total_distance += self.distance_data[track[-1]][track[0]]  # Return to the origin
#             except KeyError:
#                 raise ValueError(f"Missing distance data for returning from {track[-1]} to {track[0]}")
#         return total_distance

class DictTSPHandler(TSPHandler):
    def new_track(self) -> List[str]:
        return []

    def add_city_to_track(self, track: List[str], city: str) -> List[str]:
        track.append(city)
        return track

    def track_length(self, track: List[str]) -> float:
        total_distance = 0
        for i in range(len(track) - 1):
            total_distance += self.distance_data[track[i]][track[i + 1]]
        if len(track) > 1 and track[0] != track[-1]:
            try:
                total_distance += self.distance_data[track[-1]][track[0]]  # Return to the origin
            except KeyError:
                raise ValueError(f"Missing distance data for returning from {track[-1]} to {track[0]}")
        return total_distance

