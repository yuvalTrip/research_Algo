from abc import ABC
from typing import List, Any
from tsp_core import *
### To answer this problem, I got assistant GPT, my dad and my boyfriend.

# Abstract base class for defining output types for TSP solutions
class OutputType(ABC):
    @classmethod
    def create_handler(cls, distance_data: Any) -> TSPHandler:
        raise NotImplementedError("Choose a specific output type") # Abstract method to create the appropriate handler

    @classmethod
    def extract_output_from_track(cls, handler: TSPHandler, track: Any) -> Any:
        raise NotImplementedError("Choose a specific output type")# Abstract method to extract output from the track
# Output type that returns the full track
class Track(OutputType):
    @classmethod
    def create_handler(cls, distance_data: Any) -> TSPHandler:
        # Create the appropriate handler based on the type of distance data
        if isinstance(distance_data, list):
            return MatrixTSPHandler(distance_data)
        elif isinstance(distance_data, dict):
            return DictTSPHandler(distance_data)
        else:
            raise ValueError("Unsupported distance data type")

    @classmethod
    def extract_output_from_track(cls, handler: TSPHandler, track: Any) -> Any:
        return track # Return the track as-is

# Output type that returns the length of the track
class TrackLength(OutputType):
    @classmethod
    def create_handler(cls, distance_data: Any) -> TSPHandler:
        # Create the appropriate handler based on the type of distance data
        if isinstance(distance_data, list):
            return MatrixTSPHandler(distance_data)
        elif isinstance(distance_data, dict):
            return DictTSPHandler(distance_data)
        else:
            raise ValueError("Unsupported distance data type")

    @classmethod
    def extract_output_from_track(cls, handler: TSPHandler, track: Any) -> float:
        return handler.track_length(track) # Return the length of the track
