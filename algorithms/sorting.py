from abc import ABC, abstractmethod


class Sorter(ABC):

    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.steps = []

    @abstractmethod
    def sort(self, arr: list) -> list:
        pass

    def reset_stats(self):
        self.comparisons = 0
        self.swaps = 0
        self.steps = []

    def get_stats(self):
        return {
            "comparisons": self.comparisons,
            "swaps": self.swaps,
            "steps": len(self.steps)
        }


class BubbleSort(Sorter):

    def sort(self, arr: list) -> list:
        self.reset_stats()
        arr = arr.copy()
        n = len(arr)

        self.steps.append(arr.copy())

        for i in range(n):
            for j in range(0, n - i - 1):
                self.comparisons += 1

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.swaps += 1
                    self.steps.append(arr.copy())

        return arr


class SelectionSort(Sorter):

    def sort(self, arr: list) -> list:
        self.reset_stats()
        arr = arr.copy()
        n = len(arr)

        self.steps.append(arr.copy())

        for i in range(n):
            min_idx = i

            for j in range(i + 1, n):
                self.comparisons += 1
                if arr[j] < arr[min_idx]:
                    min_idx = j

            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                self.swaps += 1
                self.steps.append(arr.copy())

        return arr



class MergeSort(Sorter):

    def sort(self, arr: list) -> list:
        self.reset_stats()
        arr = arr.copy()
        self.steps.append(arr.copy())       # snapshot: initial state
        self._merge_sort(arr, 0, len(arr) - 1)
        return arr

    def _merge_sort(self, arr, left, right):
        # base case: a single element is already sorted
        if left >= right:
            return

        mid = (left + right) // 2          # find the middle index

        self._merge_sort(arr, left, mid)    # sort left half
        self._merge_sort(arr, mid + 1, right) # sort right half
        self._merge(arr, left, mid, right)  # merge the two sorted halves

    def _merge(self, arr, left, mid, right):
        # copy both halves into temporary arrays
        left_part  = arr[left : mid + 1]
        right_part = arr[mid + 1 : right + 1]

        i = 0  # pointer for left_part
        j = 0  # pointer for right_part
        k = left  # pointer for main arr

        while i < len(left_part) and j < len(right_part):
            self.comparisons += 1
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1
            self.steps.append(arr.copy())   # snapshot after every placement

        # copy any remaining elements
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1
            self.steps.append(arr.copy())

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1
            self.steps.append(arr.copy())



class QuickSort(Sorter):

    def sort(self, arr: list) -> list:
        self.reset_stats()
        arr = arr.copy()
        self.steps.append(arr.copy())       # snapshot: initial state
        self._quick_sort(arr, 0, len(arr) - 1)
        return arr

    def _quick_sort(self, arr, low, high):
        # base case: section has 1 or 0 elements
        if low >= high:
            return

        pivot_idx = self._partition(arr, low, high)
        self._quick_sort(arr, low, pivot_idx - 1)   # sort left of pivot
        self._quick_sort(arr, pivot_idx + 1, high)  # sort right of pivot

    def _partition(self, arr, low, high):
        pivot = arr[high]   # always pick last element as pivot
        i = low - 1         # i tracks the boundary of "smaller than pivot"

        for j in range(low, high):
            self.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]   # swap into left partition
                self.swaps += 1
                self.steps.append(arr.copy())      # snapshot after swap

        # place pivot in its correct final position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.swaps += 1
        self.steps.append(arr.copy())

        return i + 1   # return pivot's final index



