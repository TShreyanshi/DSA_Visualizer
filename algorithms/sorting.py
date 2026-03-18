from abc import ABC, abstractmethod

class Sorter(ABC):
    """Base class for all sorting algorithms."""

    def __init__(self):
        self.comparisons = 0   # count every time we compare two elements
        self.swaps = 0         # count every swap

    @abstractmethod
    def sort(self, arr: list) -> list:
        """Sort array and return sorted copy."""
        pass

    def reset_stats(self):
        self.comparisons = 0
        self.swaps = 0

    def get_stats(self):
        return {
            "comparisons": self.comparisons,
            "swaps": self.swaps
        }