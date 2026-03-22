from algorithms.sorting import BubbleSort, SelectionSort, MergeSort, QuickSort
from visualizer.sort_viz import SortVisualizer
from utils.colors import Colors


def run_sort(sorter, arr, label):
    viz = SortVisualizer(delay=0.05)
    print(Colors.color(f"\n  Running {label} on {arr}\n", Colors.BOLD))
    input("  Press Enter to start...")
    result = viz.animate(sorter, arr)
    print(Colors.color(f"  Result: {result}\n", Colors.GREEN))


def main():
    test_array = [64, 34, 25, 12, 22, 11, 90]

    print(Colors.color("\n  DSA Visualizer — Sorting Algorithms", Colors.BOLD))
    print(Colors.color("  =====================================", Colors.CYAN))

    run_sort(BubbleSort(),    test_array.copy(), "Bubble Sort")
    run_sort(SelectionSort(), test_array.copy(), "Selection Sort")
    run_sort(MergeSort(),     test_array.copy(), "Merge Sort")
    run_sort(QuickSort(),     test_array.copy(), "Quick Sort")


if __name__ == "__main__":
    main()