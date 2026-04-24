"""Unit-3 Assignment: Sorting Algorithms Toolkit."""


def bubble_sort(arr):
	out = arr.copy()
	n = len(out)
	for i in range(n - 1):
		swapped = False
		for j in range(n - 1 - i):
			if out[j] > out[j + 1]:
				out[j], out[j + 1] = out[j + 1], out[j]
				swapped = True
		if not swapped:
			break
	return out


def selection_sort(arr):
	out = arr.copy()
	n = len(out)
	for i in range(n - 1):
		min_idx = i
		for j in range(i + 1, n):
			if out[j] < out[min_idx]:
				min_idx = j
		out[i], out[min_idx] = out[min_idx], out[i]
	return out


def insertion_sort(arr):
	out = arr.copy()
	for i in range(1, len(out)):
		key = out[i]
		j = i - 1
		while j >= 0 and out[j] > key:
			out[j + 1] = out[j]
			j -= 1
		out[j + 1] = key
	return out


def merge_sort(arr):
	if len(arr) <= 1:
		return arr.copy()

	mid = len(arr) // 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	return _merge(left, right)


def _merge(left, right):
	merged = []
	i = 0
	j = 0

	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			merged.append(left[i])
			i += 1
		else:
			merged.append(right[j])
			j += 1

	merged.extend(left[i:])
	merged.extend(right[j:])
	return merged


def quick_sort(arr):
	out = arr.copy()
	_quick_sort_recursive(out, 0, len(out) - 1)
	return out


def _quick_sort_recursive(arr, low, high):
	if low < high:
		p = _partition(arr, low, high)
		_quick_sort_recursive(arr, low, p - 1)
		_quick_sort_recursive(arr, p + 1, high)


def _partition(arr, low, high):
	pivot = arr[high]
	i = low - 1

	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1


def heap_sort(arr):
	out = arr.copy()
	n = len(out)

	for i in range(n // 2 - 1, -1, -1):
		_heapify(out, n, i)

	for i in range(n - 1, 0, -1):
		out[0], out[i] = out[i], out[0]
		_heapify(out, i, 0)

	return out


def _heapify(arr, n, i):
	largest = i
	left = 2 * i + 1
	right = 2 * i + 2

	if left < n and arr[left] > arr[largest]:
		largest = left
	if right < n and arr[right] > arr[largest]:
		largest = right

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		_heapify(arr, n, largest)


def counting_sort(arr):
	if not arr:
		return []
	if min(arr) < 0:
		raise ValueError("Counting sort requires non-negative integers.")

	max_val = max(arr)
	count = [0] * (max_val + 1)

	for num in arr:
		count[num] += 1

	result = []
	for value, freq in enumerate(count):
		result.extend([value] * freq)
	return result


def radix_sort(arr):
	if not arr:
		return []
	if min(arr) < 0:
		raise ValueError("Radix sort requires non-negative integers.")

	out = arr.copy()
	exp = 1
	max_val = max(out)

	while max_val // exp > 0:
		out = _counting_sort_by_digit(out, exp)
		exp *= 10

	return out


def _counting_sort_by_digit(arr, exp):
	count = [0] * 10
	output = [0] * len(arr)

	for num in arr:
		digit = (num // exp) % 10
		count[digit] += 1

	for i in range(1, 10):
		count[i] += count[i - 1]

	for i in range(len(arr) - 1, -1, -1):
		digit = (arr[i] // exp) % 10
		output[count[digit] - 1] = arr[i]
		count[digit] -= 1

	return output


SORT_INFO = {
	1: {
		"name": "Bubble Sort",
		"func": bubble_sort,
		"time": "Best: O(n), Avg/Worst: O(n^2)",
		"space": "O(1)",
		"stable": "Yes",
		"in_place": "Yes",
	},
	2: {
		"name": "Selection Sort",
		"func": selection_sort,
		"time": "Best/Avg/Worst: O(n^2)",
		"space": "O(1)",
		"stable": "No",
		"in_place": "Yes",
	},
	3: {
		"name": "Insertion Sort",
		"func": insertion_sort,
		"time": "Best: O(n), Avg/Worst: O(n^2)",
		"space": "O(1)",
		"stable": "Yes",
		"in_place": "Yes",
	},
	4: {
		"name": "Merge Sort",
		"func": merge_sort,
		"time": "Best/Avg/Worst: O(n log n)",
		"space": "O(n)",
		"stable": "Yes",
		"in_place": "No",
	},
	5: {
		"name": "Quick Sort",
		"func": quick_sort,
		"time": "Best/Avg: O(n log n), Worst: O(n^2)",
		"space": "O(log n) recursion stack",
		"stable": "No",
		"in_place": "Yes",
	},
	6: {
		"name": "Heap Sort",
		"func": heap_sort,
		"time": "Best/Avg/Worst: O(n log n)",
		"space": "O(1)",
		"stable": "No",
		"in_place": "Yes",
	},
	7: {
		"name": "Counting Sort",
		"func": counting_sort,
		"time": "O(n + k)",
		"space": "O(k)",
		"stable": "Can be stable",
		"in_place": "No",
	},
	8: {
		"name": "Radix Sort",
		"func": radix_sort,
		"time": "O(d * (n + b))",
		"space": "O(n + b)",
		"stable": "Yes (with stable digit sort)",
		"in_place": "No",
	},
}


def parse_input_array(raw_text):
	raw_text = raw_text.strip()
	if not raw_text:
		raise ValueError("Input cannot be empty.")
	return [int(token.strip()) for token in raw_text.split(",")]


def print_sort_basics():
	print("\nSorting Basics")
	print("- Comparison sort: compares values directly (Bubble, Merge, Quick, Heap).")
	print("- Non-comparison sort: uses value properties (Counting, Radix).")
	print("- Stable sort: equal keys keep original order.")
	print("- In-place sort: requires very little extra memory.")


def print_algorithm_menu():
	print("\nChoose Sorting Algorithm")
	print("1. Bubble Sort")
	print("2. Selection Sort")
	print("3. Insertion Sort")
	print("4. Merge Sort")
	print("5. Quick Sort")
	print("6. Heap Sort")
	print("7. Counting Sort (non-negative integers)")
	print("8. Radix Sort (non-negative integers)")
	print("9. Show Sorting Basics")
	print("10. Exit")


def run_toolkit():
	print("ETCCDS202 Unit-3: Sorting Algorithms Toolkit")

	while True:
		print_algorithm_menu()
		choice_raw = input("Enter choice: ").strip()

		if not choice_raw.isdigit():
			print("Please enter a valid numeric choice.")
			continue

		choice = int(choice_raw)

		if choice == 10:
			print("Exiting toolkit.")
			break

		if choice == 9:
			print_sort_basics()
			continue

		if choice not in SORT_INFO:
			print("Invalid choice.")
			continue

		try:
			raw = input("Enter elements as comma-separated integers: ")
			arr = parse_input_array(raw)
			info = SORT_INFO[choice]
			sorted_arr = info["func"](arr)

			print(f"\nAlgorithm: {info['name']}")
			print("Input:", arr)
			print("Output:", sorted_arr)
			print("Time Complexity:", info["time"])
			print("Space Complexity:", info["space"])
			print("Stable:", info["stable"])
			print("In-place:", info["in_place"])
		except ValueError as err:
			print("Error:", err)


if __name__ == "__main__":
	try:
		run_toolkit()
	except KeyboardInterrupt:
		print("\nProgram interrupted by user.")
