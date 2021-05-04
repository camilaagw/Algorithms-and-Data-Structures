"""Single direction linked list"""


class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

    def __str__(self):
        current_node = self
        vals = []
        while current_node:
            vals.append(current_node.data)
            current_node = current_node.next
        return ' -> '.join(map(str, vals))


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

        return self  # Note: This method returns the list for testing purposes

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

    def remove_duplicates(self):
        """Implementation using a set"""
        current_node = self.head
        prev = None
        visited = set()
        while current_node:
            if current_node.data in visited:
                prev.next = current_node.next
            else:
                visited.add(current_node.data)
                prev = current_node
            current_node = current_node.next
        return self  # Note: This method returns the list for testing purposes

    def remove_duplicates2(self):
        """Implementation without a buffer"""
        node = self.head
        while node:
            current_node = node.next
            prev = node
            while current_node:
                if current_node.data == node.data:
                    prev.next = current_node.next
                else:
                    prev = current_node
                current_node = current_node.next
            node = node.next
        return self  # Note: This method returns the list for testing purposes

    def return_kth_to_last(self, k):
        first_pointer = self.head
        last_pointer = self.head

        # Move last pointer, k positions
        count = 0
        while count < k and last_pointer:
            last_pointer = last_pointer.next
            count += 1

        # Move first pointer, until last pointer is null
        while last_pointer:
            first_pointer = first_pointer.next
            last_pointer = last_pointer.next

        return first_pointer

    def delete_middle_node(self, node):
        """`node` is any node but the first and the last node"""
        current_node = node
        while current_node.next:
            current_node.data = current_node.next.data
            current_node = current_node.next


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
    my_list.reverse()

    # Test remove duplicates (with an external buffer)
    my_list.insert_after_tail(42)
    my_list.insert_after_tail(24)
    my_list.insert_after_tail(98)
    my_list.insert_after_tail(789)
    assert_eq(str(my_list.remove_duplicates()), display_values(*values, 789))

    # Test remove duplicates (without an external buffer)
    my_list.insert_after_tail(42)
    my_list.insert_after_tail(24)
    my_list.insert_after_tail(98)
    my_list.insert_after_tail(789)
    assert_eq(str(my_list.remove_duplicates2()), display_values(*values, 789))

    # Test - kth to last
    assert_eq(str(my_list.return_kth_to_last(20)), display_values(*values, 789))
    assert_eq(str(my_list.return_kth_to_last(2)), display_values(98, 789))
    assert_eq(str(my_list.return_kth_to_last(3)), display_values(1, 98, 789))
    assert_eq(LinkedList().return_kth_to_last(10), None)

    # Delete middle node
    # TODO

