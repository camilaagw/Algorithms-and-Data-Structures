""""""

from typing import List, Tuple
from collections import defaultdict


def get_build_order(edges: List[Tuple[int, int]]):
    edges_dict = defaultdict(list)
    for from_, to_ in edges:
        edges_dict[from_].append(to_)

    build_order = []
    origins = set()
    for from_, to_s in edges_dict.items():
        origins.add(from_)
    while edges_dict:
        for to_s in edges_dict.values():
            origins.difference_update(to_s)

        if not origins:
            return None
        build_order.extend(origins)

        next_origins = set()
        for origin in origins:
            next_origins.update(edges_dict[origin])
            del edges_dict[origin]
        origins = next_origins

    build_order.extend(origins)

    return build_order  # case in which there is a clycle


if __name__ == "__main__":
    assert get_build_order([(1, 1)]) is None
    assert get_build_order([(1, 2), (2, 3), (3, 1)]) == None
    assert get_build_order(
        [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)]) == [1 ,2, 3, 4, 5]
