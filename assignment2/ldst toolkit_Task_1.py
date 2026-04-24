"""Unit-2 Linear Data Structures Toolkit"""


class DynamicArray:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.data = []

    def _is_full(self):
        return len(self.data) >= self.capacity

    def insert(self, value):
        if self._is_full():
            old_capacity = self.capacity
            self.capacity *= 2
            print(f"Capacity full. Resized from {old_capacity} to {self.capacity}.")
        self.data.append(value)

    def delete_at(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Invalid index")
        return self.data.pop(index)

    def traverse(self):
        return self.data.copy()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def delete_value(self, value):
        if self.head is None:
            return False

        if self.head.data == value:
            self.head = self.head.next
            return True

        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.data == value:
                prev.next = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    def search(self, value):
        index = 0
        curr = self.head
        while curr is not None:
            if curr.data == value:
                return index
            curr = curr.next
            index += 1
        return -1

    def traverse(self):
        out = []
        curr = self.head
        while curr is not None:
            out.append(curr.data)
            curr = curr.next
        return out


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            raise IndexError("Stack underflow")
        return self.items.pop()

    def peek(self):
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items[-1]

    def traverse(self):
        return self.items.copy()


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.items:
            raise IndexError("Queue underflow")
        return self.items.pop(0)

    def front(self):
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items[0]

    def traverse(self):
        return self.items.copy()


def read_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.")


def dynamic_array_menu(ds):
    while True:
        print("\nDynamic Array Menu")
        print("1. Insert")
        print("2. Delete by index")
        print("3. Traverse")
        print("4. Back")
        choice = read_int("Enter choice: ")

        if choice == 1:
            ds.insert(read_int("Enter value: "))
        elif choice == 2:
            try:
                removed = ds.delete_at(read_int("Enter index: "))
                print(f"Deleted: {removed}")
            except IndexError as err:
                print(err)
        elif choice == 3:
            print("Array:", ds.traverse(), f"(size={len(ds.data)}, capacity={ds.capacity})")
        elif choice == 4:
            return
        else:
            print("Invalid choice")


def linked_list_menu(ds):
    while True:
        print("\nSingly Linked List Menu")
        print("1. Insert at end")
        print("2. Delete by value")
        print("3. Search")
        print("4. Traverse")
        print("5. Back")
        choice = read_int("Enter choice: ")

        if choice == 1:
            ds.insert_end(read_int("Enter value: "))
        elif choice == 2:
            deleted = ds.delete_value(read_int("Enter value to delete: "))
            print("Deleted" if deleted else "Value not found")
        elif choice == 3:
            pos = ds.search(read_int("Enter value to search: "))
            print(f"Found at position {pos}" if pos != -1 else "Not found")
        elif choice == 4:
            print("List:", ds.traverse())
        elif choice == 5:
            return
        else:
            print("Invalid choice")


def stack_menu(ds):
    while True:
        print("\nStack Menu (LIFO)")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("5. Back")
        choice = read_int("Enter choice: ")

        if choice == 1:
            ds.push(read_int("Enter value: "))
        elif choice == 2:
            try:
                print("Popped:", ds.pop())
            except IndexError as err:
                print(err)
        elif choice == 3:
            try:
                print("Top:", ds.peek())
            except IndexError as err:
                print(err)
        elif choice == 4:
            print("Stack:", ds.traverse())
        elif choice == 5:
            return
        else:
            print("Invalid choice")


def queue_menu(ds):
    while True:
        print("\nQueue Menu (FIFO)")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Traverse")
        print("5. Back")
        choice = read_int("Enter choice: ")

        if choice == 1:
            ds.enqueue(read_int("Enter value: "))
        elif choice == 2:
            try:
                print("Dequeued:", ds.dequeue())
            except IndexError as err:
                print(err)
        elif choice == 3:
            try:
                print("Front:", ds.front())
            except IndexError as err:
                print(err)
        elif choice == 4:
            print("Queue:", ds.traverse())
        elif choice == 5:
            return
        else:
            print("Invalid choice")


def main_menu():
    dynamic_array = DynamicArray()
    linked_list = SinglyLinkedList()
    stack = Stack()
    queue = Queue()

    while True:
        print("\nETCCDS202 Unit-2: Linear Data Structures Toolkit")
        print("1. Dynamic Array")
        print("2. Singly Linked List")
        print("3. Stack")
        print("4. Queue")
        print("5. Exit")
        choice = read_int("Enter choice: ")

        if choice == 1:
            dynamic_array_menu(dynamic_array)
        elif choice == 2:
            linked_list_menu(linked_list)
        elif choice == 3:
            stack_menu(stack)
        elif choice == 4:
            queue_menu(queue)
        elif choice == 5:
            print("Exiting toolkit.")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")