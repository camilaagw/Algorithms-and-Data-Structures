"""
Given a set of 𝑛 segments {[𝑎0, 𝑏0], [𝑎1, 𝑏1], . . . , [𝑎𝑛−1, 𝑏𝑛−1]} with integer coordinates on a line, find
the minimum number 𝑚 of points such that each segment contains at least one point. That is, find a
set of integers 𝑋 of the minimum size such that for any segment [𝑎𝑖, 𝑏𝑖] there is a point 𝑥 ∈ 𝑋 such
that 𝑎𝑖 ≤ 𝑥 ≤ 𝑏𝑖.
"""
from typing import Tuple, List


def min_continuous_segments(segments: List[List[int]]) -> Tuple[int, List]:
    """Find the minimum number of continuous segments that can be formed with segments"""
    min_segments = []
    overlaps = []

    for start, end in segments:
        overlap = False
        for seg, ovp in zip(min_segments, overlaps):
            if seg[0] <= start <= seg[1]:
                seg[1] = max(end, seg[1])
                ovp[0] = start
                overlap = True
                break
            elif seg[0] <= end <= seg[1]:
                seg[0] = min(start, seg[0])
                ovp[1] = end
                overlap = True
                break
        if not overlap:
            min_segments.append([start, end])
            overlaps.append([start, end])

    return len(min_segments), [ovp[0] for ovp in overlaps]


if __name__ == "__main__":
    assert min_continuous_segments([[1, 3], [2, 5], [3, 6]]) == (1, [3])
    assert min_continuous_segments([[3, 6], [2, 5], [1, 6]]) == (1, [3])
    assert min_continuous_segments([[4, 7], [1, 3], [2, 5], [5, 6]]) == (2, [5, 1])
