"""You are on the side of the river. You are given a m liter jug and a n liter jug where 0 < m < n.
Both the jugs are initially empty. The jugs don’t have markings to allow measuring smaller quantities.
You have to use the jugs to measure d liters of water where d < n. Determine the minimum no of operations
to be performed to obtain d liters of water in one of jug.
"""
from collections import deque


def get_steps_for_water_pouring(n, m, target):
    """Solution for the water pouring problem with two jugs
    :param n: Capacity of jug 1
    :param m: Capacity of jug 2
    :param target: Desired number of units of water
    :return: List of states to achieve a desired target. If target is not possible [] is returned
    """
    visited_states = {(0, 0): None}
    queue = deque()
    queue.append((0, 0))

    while queue:
        state = queue.popleft()
        if state[0] == target or state[1] == target:
            return list(get_steps_back(state, visited_states))
        for next_s in get_possible_transitions(state, n, m):
            if next_s not in visited_states:
                queue.append(next_s)
                visited_states[next_s] = state

    return []


def get_possible_transitions(state, n, m):
    x, y = state
    yield x, m
    yield n, y
    yield x, 0
    yield 0, y
    if x > 0:
        yield max(x - m + y, 0), min(x + y, m)
    if y > 0:
        yield min(x + y, n), max(x - n + y, 0)


def get_steps_back(current, visited_states):
    yield current
    while visited_states[current]:
        current = visited_states[current]
        yield current


if __name__ == "__main__":

    assert len(get_steps_for_water_pouring(9, 4, 5)) == 3
    assert len(get_steps_for_water_pouring(9, 4, 6)) == 9
    assert len(get_steps_for_water_pouring(9, 4, 0)) == 1
    assert len(get_steps_for_water_pouring(9, 4, -1000)) == 0
    assert len(get_steps_for_water_pouring(0, 0, 5)) == 0
    assert len(get_steps_for_water_pouring(0, 0, 0)) == 1

