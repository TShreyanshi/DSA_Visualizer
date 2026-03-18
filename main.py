from algorithms.sorting import Sorter
from algorithms.graph import Graph, Node
from utils.colors import Colors

def main():
    print(Colors.color("DSA Visualizer", Colors.BOLD))
    print(Colors.color("==================", Colors.CYAN))
    print("Project structure loaded successfully!")

    # Quick smoke test
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    print(f"\nTest Graph: {g}")

if __name__ == "__main__":
    main()