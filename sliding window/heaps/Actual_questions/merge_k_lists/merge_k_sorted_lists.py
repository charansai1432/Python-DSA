import heapq

class Listnode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Convert Python list into Linked List
def create_linked_list(values):

    dummy = Listnode(0)
    current = dummy

    for value in values:
        current.next = Listnode(value)
        current = current.next

    return dummy.next


# Merge K Sorted Lists
def merge_k_sorted_lists(lists):

    dummy = Listnode(0)
    current = dummy

    min_heap = []

    # Insert first node of every linked list
    for i in range(len(lists)):

        if lists[i] is not None:
            heapq.heappush(
                min_heap,
                (lists[i].val, i, lists[i])
            )

    # Process the heap
    while min_heap:

        val, i, node = heapq.heappop(min_heap)

        current.next = node
        current = current.next

        if node.next is not None:
            heapq.heappush(
                min_heap,
                (node.next.val, i, node.next)
            )

    current.next = None

    return dummy.next


# Print Linked List
def print_linked_list(head):

    while head is not None:
        print(head.val, end=" -> ")
        head = head.next

    print("None")


# Input
lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

# Convert Python lists into Linked Lists
linked_lists = []

for values in lists:
    linked_lists.append(create_linked_list(values))

# Merge
result = merge_k_sorted_lists(linked_lists)

# Display result
print_linked_list(result)