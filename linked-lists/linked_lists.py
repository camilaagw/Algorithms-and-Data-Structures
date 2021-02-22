"""Single direction linked list"""


class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self, *values):
        self.head = None
        for val in reversed(values):
            self.insert_before_head(val)

    def __str__(self):
        current_node = self.head
        vals = []
        while current_node:
            vals.append(current_node.data)
            current_node = current_node.next
        return ' -> '.join(map(str, vals))

    def get_last_2(self):

        if self.head is None:
            return None, None

        # Find last node and node before it
        last_node = self.head
        previous_node = None
        while last_node.next:
            previous_node, last_node = last_node, last_node.next

        return previous_node, last_node

    def reverse(self):
        temp_head = None
        current_node = self.head

        while current_node:
            next = current_node.next
            current_node.next = temp_head
            temp_head = current_node
            current_node = next

        self.head = temp_head

        return self

    def insert_before_head(self, value):
        temp = Node(value)
        temp.next, self.head = self.head, temp

    def insert_after_tail(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(value)


def assert_eq(actual, expected):
    assert actual == expected, '\nactual: ' + str(actual) + '\nexpected: ' + str(expected)


def display_values(*values):
    return ' -> '.join(map(str, values))


if __name__ == "__main__":

    my_list = LinkedList()
    my_list_reversed = LinkedList()

    # Initialize lists
    values = [42, 24, 46453, 1, 98]
    for i in values:
        my_list.insert_after_tail(i)
        my_list_reversed.insert_before_head(i)

    # Test insert after tail
    assert_eq(str(my_list), display_values(*values))

    # Test insert before tail
    assert_eq(str(my_list_reversed), display_values(*reversed(values)))

    # Test get last 2 nodes
    assert_eq(
        [node.data for node in my_list.get_last_2()],
        values[-2:])

    # Test reverse
    assert_eq(str(my_list.reverse()), str(my_list_reversed))
    assert_eq(LinkedList().reverse().head, None)
    assert_eq(str(LinkedList(42).reverse()), '42')
    assert_eq(str(LinkedList(42, 24).reverse()), display_values('24', '42'))
