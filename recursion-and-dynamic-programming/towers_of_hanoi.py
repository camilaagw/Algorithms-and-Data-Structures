"""In the classic problem of towers of Hanoi, you have 3 towers and N disks of
different sizes which can slide onto any tower. The puzzle starts with disks sorted
in ascending order of size from top to bottom (i.e. each disk sits on top)

1) Only one disk can be moved at a time
2) A disk is slid off the top of one tower onto another tower
3) A disk cannot be placed on top of a smaller disk"""


def towers_of_hanoi(N: int):
    stack = {'A': [], 'B': [], 'C': []}

    for i in range(N, 0, -1):
        stack['A'].append(i)

    def move_disks(n: int, source: str, dest: str, buffer: str):
        if n <= 0:
            return
            print("*******")
            print('stack_a:', stack['A'])
            print('stack_b:', stack['B'])
            print('stack_c:', stack['C'])
        else:
            move_disks(n - 1, source, buffer, dest)
            temp = stack[source].pop()
            stack[dest].append(temp)
            print("*******")
            print('stack_a:', stack['A'])
            print('stack_b:', stack['B'])
            print('stack_c:', stack['C'])
            move_disks(n - 1, buffer, dest, source)


    print("*******")
    print('stack_a:', stack['A'])
    print('stack_b:', stack['B'])
    print('stack_c:', stack['C'])
    move_disks(N, source='A', dest='C', buffer='C')


if __name__ == "__main__":
    towers_of_hanoi(3)

