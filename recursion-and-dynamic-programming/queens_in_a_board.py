"""Write a function to determine all ways of arranging eight queens on a N by N
board so that none of them share the same row, column or diagonal
"""

class Diagonals:
    def __init__(self, forbidden_sum=[], forbidden_diff=[]):
        self.forbidden_sum = forbidden_sum
        self.forbidden_diff = forbidden_diff

    def without(self, row, col):
        return Diagonals(
            self.forbidden_sum + [row + col],
            self.forbidden_diff + [row - col]
        )

    def is_valid(self, row, col):
        return (row + col not in self.forbidden_sum) and \
               (row - col not in self.forbidden_diff)


def get_num_combinations(rows, col, diagonals):
    if col < 0:
        return 1
    result = 0
    for row in rows:
        if diagonals.is_valid(row, col):
            result += get_num_combinations(
                rows - {row},
                col - 1,
                diagonals.(row, col)
            )
    return result



def get_combinations(rows, col, forbiden_sum, forbiden_diff):
    if col == 0:
        if (rows[0]+col not in forbiden_sum) and (rows[0] - col not in forbiden_diff):
            return [[rows[0]]]
        return []
    result = []
    for i, row in enumerate(rows):
        if (row + col not in forbiden_sum) and (row - col not in forbiden_diff):
            new_forbiden_sum = forbiden_sum + [row + col]
            new_forbiden_res = forbiden_diff + [row - col]
            children_results = get_combinations(
                rows[:i]+rows[i+1:], col - 1,
                new_forbiden_sum,
                new_forbiden_res
            )
            if children_results:
                for child in children_results:
                    result.append([row]+child)
    return result


if __name__ == "__main__":
    rows = set(range(4))
    assert get_num_combinations(rows, 3, Diagonals()) == 2

    # print(get_combinations(rows, 3, [], []))

    rows = set(range(8))
    assert get_num_combinations(rows, 7, Diagonals()) == 92
