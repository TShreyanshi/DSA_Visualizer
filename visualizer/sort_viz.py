import time
from visualizer.base import BaseVisualizer
from utils.colors import Colors


class SortVisualizer(BaseVisualizer):

    def __init__(self, delay=0.1):
        self.delay = delay    # seconds between frames

    def visualize(self, data):
        """Render one snapshot of the array as a bar chart."""
        arr = data["arr"]
        comparing = data.get("comparing", [])   # indices being compared (highlight red)
        sorted_until = data.get("sorted_until", -1)  # everything before this is sorted

        max_val = max(arr) if arr else 1
        bar_width = 3

        print("\033[2J\033[H", end="")           # clear terminal screen

        for i, val in enumerate(arr):
            bar_len = int((val / max_val) * 20)  # scale bar to max 20 chars

            if i in comparing:
                color = Colors.RED
            elif i <= sorted_until:
                color = Colors.GREEN
            else:
                color = Colors.CYAN

            bar = "█" * bar_len
            print(Colors.color(f"  {val:3} │{bar}", color))

        print()
        time.sleep(self.delay)


    def show_complexity(self, algorithm_name):
        complexity = {
            "BubbleSort":    {"best": "O(n)",      "average": "O(n²)",     "worst": "O(n²)",     "space": "O(1)"},
            "SelectionSort": {"best": "O(n²)",     "average": "O(n²)",     "worst": "O(n²)",     "space": "O(1)"},
            "MergeSort":     {"best": "O(n log n)","average": "O(n log n)","worst": "O(n log n)","space": "O(n)"},
            "QuickSort":     {"best": "O(n log n)","average": "O(n log n)","worst": "O(n²)",     "space": "O(log n)"},
        }
        info = complexity.get(algorithm_name, {})
        print(Colors.color(f"\n  {algorithm_name} complexity", Colors.BOLD))
        print(Colors.color(f"  Best:    {info.get('best')}", Colors.GREEN))
        print(Colors.color(f"  Average: {info.get('average')}", Colors.YELLOW))
        print(Colors.color(f"  Worst:   {info.get('worst')}", Colors.RED))
        print(Colors.color(f"  Space:   {info.get('space')}", Colors.CYAN))

    def animate(self, sorter, arr):
        """Run a sort and animate every step."""
        sorted_arr = sorter.sort(arr)

        for step_idx, step in enumerate(sorter.steps):
            self.visualize({
                "arr": step,
                "comparing": [],
                "sorted_until": -1
            })

        # Final state — show fully green
        self.visualize({
            "arr": sorted_arr,
            "comparing": [],
            "sorted_until": len(sorted_arr) - 1
        })

        stats = sorter.get_stats()
        print(Colors.color(f"\n  Done! Comparisons: {stats['comparisons']}  Swaps: {stats['swaps']}  Steps: {stats['steps']}", Colors.GREEN))
        self.show_complexity(type(sorter).__name__)

        return sorted_arr