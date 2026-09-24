class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_list(head):
    current = head

    while current is not None:
        print(current.value, end=" -> ")
        current = current.next

    print("None")


def find_node(head, target):
    current = head

    while current is not None:
        if current.value == target:
            return True

        current = current.next

    return False


def count_node(head):
    current = head
    count = 0

    while current is not None:
        count += 1
        current = current.next

    return count


def find_max(head):
    current = head
    maximum = head.value

    while current is not None:
        if current.value > maximum:
            maximum = current.value

        current = current.next

    return maximum


def find_min(head):
    current = head
    minimum = head.value

    while current is not None:
        if current.value < minimum:
            minimum = current.value

        current = current.next

    return minimum


def sum_nodes(head):
    current = head
    total = 0

    while current is not None:
        total += current.value
        current = current.next

    return total


def count_target(head, target):
    current = head
    count = 0

    while current is not None:
        if current.value == target:
            count += 1

        current = current.next

    return count


def delete_node(head, target):
    if head is None:
        return None

    if head.value == target:
        return head.next

    current = head

    while current.next is not None:
        if current.next.value == target:
            current.next = current.next.next
            return head

        current = current.next

    return head


# Create linked list
A = Node(10)
B = Node(25)
C = Node(7)
D = Node(25)
E = Node(17)

A.next = B
B.next = C
C.next = D
D.next = E

head = A


# Tests
print("Linked list:")
print_list(head)

print("Find 25:", find_node(head, 25))
print("Find 100:", find_node(head, 100))

print("Number of nodes:", count_node(head))
print("Maximum:", find_max(head))
print("Minimum:", find_min(head))
print("Sum:", sum_nodes(head))

print("Number of 25:", count_target(head, 25))

head = delete_node(head, 25)

print("After deleting first 25:")
print_list(head)
