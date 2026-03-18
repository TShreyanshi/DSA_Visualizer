from abc import ABC, abstractmethod

class BaseVisualizer(ABC):
    """All visualizers must implement these two methods."""

    @abstractmethod
    def visualize(self, data):
        """Render a single state of the data."""
        pass

    @abstractmethod
    def show_complexity(self):
        """Print the Big-O analysis for this algorithm."""
        pass