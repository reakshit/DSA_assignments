"""ETCCDS202 Unit-4 Assignment: Non-Linear and Advanced Data Structures."""

from collections import deque


class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class BinaryTree:
	def __init__(self):
		self.root = None

	def insert_level_order(self, value):
		new_node = TreeNode(value)
		if self.root is None:
			self.root = new_node
			return

		queue = deque([self.root])
		while queue:
			current = queue.popleft()
			if current.left is None:
				current.left = new_node
				return
			queue.append(current.left)

			if current.right is None:
				current.right = new_node
				return
			queue.append(current.right)

	def inorder(self):
		result = []
		self._inorder_recursive(self.root, result)
		return result

	def _inorder_recursive(self, node, result):
		if node is None:
			return
		self._inorder_recursive(node.left, result)
		result.append(node.data)
		self._inorder_recursive(node.right, result)

	def preorder(self):
		result = []
		self._preorder_recursive(self.root, result)
		return result

	def _preorder_recursive(self, node, result):
		if node is None:
			return
		result.append(node.data)
		self._preorder_recursive(node.left, result)
		self._preorder_recursive(node.right, result)

	def postorder(self):
		result = []
		self._postorder_recursive(self.root, result)
		return result

	def _postorder_recursive(self, node, result):
		if node is None:
			return
		self._postorder_recursive(node.left, result)
		self._postorder_recursive(node.right, result)
		result.append(node.data)

	def level_order(self):
		if self.root is None:
			return []

		result = []
		queue = deque([self.root])
		while queue:
			current = queue.popleft()
			result.append(current.data)
			if current.left is not None:
				queue.append(current.left)
			if current.right is not None:
				queue.append(current.right)
		return result


class BST:
	def __init__(self):
		self.root = None

	def insert(self, value):
		self.root = self._insert_recursive(self.root, value)

	def _insert_recursive(self, node, value):
		if node is None:
			return TreeNode(value)
		if value < node.data:
			node.left = self._insert_recursive(node.left, value)
		elif value > node.data:
			node.right = self._insert_recursive(node.right, value)
		return node

	def search(self, value):
		return self._search_recursive(self.root, value)

	def _search_recursive(self, node, value):
		if node is None:
			return False
		if node.data == value:
			return True
		if value < node.data:
			return self._search_recursive(node.left, value)
		return self._search_recursive(node.right, value)

	def delete(self, value):
		deleted, self.root = self._delete_recursive(self.root, value)
		return deleted

	def _delete_recursive(self, node, value):
		if node is None:
			return False, None

		if value < node.data:
			deleted, node.left = self._delete_recursive(node.left, value)
			return deleted, node

		if value > node.data:
			deleted, node.right = self._delete_recursive(node.right, value)
			return deleted, node

		if node.left is None and node.right is None:
			return True, None
		if node.left is None:
			return True, node.right
		if node.right is None:
			return True, node.left

		successor = self._min_node(node.right)
		node.data = successor.data
		_, node.right = self._delete_recursive(node.right, successor.data)
		return True, node

	def _min_node(self, node):
		current = node
		while current.left is not None:
			current = current.left
		return current

	def inorder(self):
		result = []
		self._inorder_recursive(self.root, result)
		return result

	def _inorder_recursive(self, node, result):
		if node is None:
			return
		self._inorder_recursive(node.left, result)
		result.append(node.data)
		self._inorder_recursive(node.right, result)


class BinaryHeap:
	def __init__(self, is_min_heap=True):
		self.data = []
		self.is_min_heap = is_min_heap

	def _higher_priority(self, a, b):
		if self.is_min_heap:
			return a < b
		return a > b

	def insert(self, value):
		self.data.append(value)
		self._heapify_up(len(self.data) - 1)

	def _heapify_up(self, idx):
		while idx > 0:
			parent = (idx - 1) // 2
			if self._higher_priority(self.data[idx], self.data[parent]):
				self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
				idx = parent
			else:
				break

	def extract_top(self):
		if not self.data:
			raise IndexError("Heap is empty")

		top_value = self.data[0]
		last = self.data.pop()
		if self.data:
			self.data[0] = last
			self._heapify_down(0)
		return top_value

	def _heapify_down(self, idx):
		n = len(self.data)
		while True:
			left = 2 * idx + 1
			right = 2 * idx + 2
			target = idx

			if left < n and self._higher_priority(self.data[left], self.data[target]):
				target = left
			if right < n and self._higher_priority(self.data[right], self.data[target]):
				target = right

			if target == idx:
				break

			self.data[idx], self.data[target] = self.data[target], self.data[idx]
			idx = target

	def peek(self):
		if not self.data:
			raise IndexError("Heap is empty")
		return self.data[0]

	def as_list(self):
		return self.data.copy()


class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.adj_list = {i: [] for i in range(vertices)}

	def add_edge(self, u, v, undirected=True):
		if not (0 <= u < self.vertices and 0 <= v < self.vertices):
			raise ValueError("Vertex out of range")
		self.adj_list[u].append(v)
		if undirected:
			self.adj_list[v].append(u)

	def adjacency_matrix(self):
		matrix = [[0] * self.vertices for _ in range(self.vertices)]
		for u in range(self.vertices):
			for v in self.adj_list[u]:
				matrix[u][v] = 1
		return matrix

	def bfs(self, start):
		if not (0 <= start < self.vertices):
			raise ValueError("Start vertex out of range")

		visited = [False] * self.vertices
		order = []
		queue = deque([start])
		visited[start] = True

		while queue:
			node = queue.popleft()
			order.append(node)
			for neighbor in self.adj_list[node]:
				if not visited[neighbor]:
					visited[neighbor] = True
					queue.append(neighbor)
		return order

	def dfs(self, start):
		if not (0 <= start < self.vertices):
			raise ValueError("Start vertex out of range")

		visited = [False] * self.vertices
		order = []
		stack = [start]

		while stack:
			node = stack.pop()
			if visited[node]:
				continue
			visited[node] = True
			order.append(node)

			for neighbor in reversed(self.adj_list[node]):
				if not visited[neighbor]:
					stack.append(neighbor)
		return order


def read_int(prompt):
	while True:
		raw = input(prompt).strip()
		try:
			return int(raw)
		except ValueError:
			print("Please enter a valid integer.")


def read_int_list(prompt):
	raw = input(prompt).strip()
	if not raw:
		return []
	try:
		return [int(token.strip()) for token in raw.split(",")]
	except ValueError as err:
		raise ValueError("Enter comma-separated integers only.") from err


def print_tree_theory():
	print("\nTree Terminology and Types")
	print("- Root: top-most node")
	print("- Parent/Child: connected nodes at adjacent levels")
	print("- Leaf: node with no children")
	print("- Height: longest path (in edges) from node to leaf")
	print("- Full Binary Tree: each node has 0 or 2 children")
	print("- Complete Binary Tree: all levels full except possibly last, filled left to right")
	print("- Perfect Binary Tree: all internal nodes have 2 children and all leaves at same level")


def tree_menu():
	tree = BinaryTree()
	while True:
		print("\nBinary Tree Menu")
		print("1. Show tree terminology")
		print("2. Insert nodes (level-order) from comma-separated input")
		print("3. Inorder traversal")
		print("4. Preorder traversal")
		print("5. Postorder traversal")
		print("6. Level-order traversal")
		print("7. Back")

		choice = read_int("Enter choice: ")

		if choice == 1:
			print_tree_theory()
		elif choice == 2:
			try:
				values = read_int_list("Enter values (e.g., 10,20,30): ")
				for value in values:
					tree.insert_level_order(value)
				print("Nodes inserted.")
			except ValueError as err:
				print(err)
		elif choice == 3:
			print("Inorder:", tree.inorder())
		elif choice == 4:
			print("Preorder:", tree.preorder())
		elif choice == 5:
			print("Postorder:", tree.postorder())
		elif choice == 6:
			print("Level-order:", tree.level_order())
		elif choice == 7:
			return
		else:
			print("Invalid choice")


def bst_menu():
	bst = BST()
	while True:
		print("\nBST Menu")
		print("1. Insert")
		print("2. Search")
		print("3. Delete")
		print("4. Inorder traversal (sorted)")
		print("5. Back")

		choice = read_int("Enter choice: ")

		if choice == 1:
			bst.insert(read_int("Enter value: "))
			print("Inserted.")
		elif choice == 2:
			value = read_int("Enter value to search: ")
			print("Found" if bst.search(value) else "Not found")
		elif choice == 3:
			value = read_int("Enter value to delete: ")
			print("Deleted" if bst.delete(value) else "Value not found")
		elif choice == 4:
			print("Inorder:", bst.inorder())
		elif choice == 5:
			return
		else:
			print("Invalid choice")


def heap_menu():
	min_heap = BinaryHeap(is_min_heap=True)
	max_heap = BinaryHeap(is_min_heap=False)

	while True:
		print("\nHeap Menu")
		print("1. Insert into Min Heap")
		print("2. Extract top from Min Heap")
		print("3. Peek Min Heap")
		print("4. Show Min Heap array")
		print("5. Insert into Max Heap")
		print("6. Extract top from Max Heap")
		print("7. Peek Max Heap")
		print("8. Show Max Heap array")
		print("9. Priority Queue idea")
		print("10. Back")

		choice = read_int("Enter choice: ")

		try:
			if choice == 1:
				min_heap.insert(read_int("Enter value: "))
				print("Inserted into Min Heap.")
			elif choice == 2:
				print("Extracted:", min_heap.extract_top())
			elif choice == 3:
				print("Top:", min_heap.peek())
			elif choice == 4:
				print("Min Heap:", min_heap.as_list())
			elif choice == 5:
				max_heap.insert(read_int("Enter value: "))
				print("Inserted into Max Heap.")
			elif choice == 6:
				print("Extracted:", max_heap.extract_top())
			elif choice == 7:
				print("Top:", max_heap.peek())
			elif choice == 8:
				print("Max Heap:", max_heap.as_list())
			elif choice == 9:
				print("Priority Queue: highest-priority element is served first.")
				print("- Min Heap based PQ serves smallest key first.")
				print("- Max Heap based PQ serves largest key first.")
			elif choice == 10:
				return
			else:
				print("Invalid choice")
		except IndexError as err:
			print(err)


def graph_menu():
	graph = None
	while True:
		print("\nGraph Menu")
		print("1. Create graph")
		print("2. Add edge")
		print("3. Show adjacency list")
		print("4. Show adjacency matrix")
		print("5. BFS traversal")
		print("6. DFS traversal")
		print("7. Back")

		choice = read_int("Enter choice: ")

		try:
			if choice == 1:
				vertices = read_int("Enter number of vertices: ")
				if vertices <= 0:
					print("Vertices must be positive.")
				else:
					graph = Graph(vertices)
					print("Graph created with vertices 0 to", vertices - 1)
			elif choice == 2:
				if graph is None:
					print("Create graph first.")
					continue
				u = read_int("Enter u: ")
				v = read_int("Enter v: ")
				graph.add_edge(u, v, undirected=True)
				print("Edge added (undirected).")
			elif choice == 3:
				if graph is None:
					print("Create graph first.")
					continue
				print("Adjacency List:")
				for node, neighbors in graph.adj_list.items():
					print(node, "->", neighbors)
			elif choice == 4:
				if graph is None:
					print("Create graph first.")
					continue
				matrix = graph.adjacency_matrix()
				print("Adjacency Matrix:")
				for row in matrix:
					print(row)
			elif choice == 5:
				if graph is None:
					print("Create graph first.")
					continue
				start = read_int("Enter start vertex: ")
				print("BFS:", graph.bfs(start))
			elif choice == 6:
				if graph is None:
					print("Create graph first.")
					continue
				start = read_int("Enter start vertex: ")
				print("DFS:", graph.dfs(start))
			elif choice == 7:
				return
			else:
				print("Invalid choice")
		except ValueError as err:
			print(err)


def print_balanced_trees_concepts():
	print("\nBalanced Trees (Conceptual)")
	print("AVL Tree:")
	print("- Self-balancing BST with strict height balance.")
	print("- Balance factor is in {-1, 0, 1} for every node.")
	print("- Uses rotations after insert/delete.")

	print("Red-Black Tree:")
	print("- Balanced BST with node colors and color rules.")
	print("- Height remains O(log n) in worst case.")
	print("- Fewer rotations on average than AVL in updates.")

	print("B-Tree:")
	print("- Multi-way balanced search tree used in databases and file systems.")
	print("- Stores multiple keys per node and minimizes disk I/O.")
	print("- Indexing structure in DBMS and storage engines.")


def main_menu():
	while True:
		print("\nETCCDS202 Unit-4: Non-Linear and Advanced Data Structures")
		print("1. Trees (terminology and traversals)")
		print("2. Binary Search Tree (insert/search/delete)")
		print("3. Heaps (min/max, heapify, priority queue)")
		print("4. Graphs (adjacency list/matrix, BFS, DFS)")
		print("5. Balanced Trees concepts (AVL, Red-Black, B-Tree)")
		print("6. Exit")

		choice = read_int("Enter choice: ")

		if choice == 1:
			tree_menu()
		elif choice == 2:
			bst_menu()
		elif choice == 3:
			heap_menu()
		elif choice == 4:
			graph_menu()
		elif choice == 5:
			print_balanced_trees_concepts()
		elif choice == 6:
			print("Exiting toolkit.")
			break
		else:
			print("Invalid choice")


if __name__ == "__main__":
	try:
		main_menu()
	except KeyboardInterrupt:
		print("\nProgram interrupted by user.")
