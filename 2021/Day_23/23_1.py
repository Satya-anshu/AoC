# Thanks to https://github.com/anthonywritescode/aoc2021/blob/main/day23/part1.py!
import os
from typing import Generator, NamedTuple
import heapq

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

POS = {'A': 0, 'B': 1, 'C': 2, 'D': 3}


class State(NamedTuple):
    top: dict[int, int]
    row1: dict[int, int]
    row2: dict[int, int]

    def __hash__(self) -> int:
        return hash((
            tuple(self.top.items()),
            tuple(self.row1.items()),
            tuple(self.row2.items()),
        ))

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, State):
            return NotImplemented
        else:
            return id(self) < id(other)

    @property
    def completed(self) -> bool:
        return (
            all(k == v for k, v in self.row1.items()) and
            all(k == v for k, v in self.row2.items())
        )

    @classmethod
    def parse(cls, s: str):
        lines = s.splitlines()
        return cls(
            dict.fromkeys((1, 3, 5, 7, 9), None),
            {
                0: POS[lines[2][3]],
                1: POS[lines[2][5]],
                2: POS[lines[2][7]],
                3: POS[lines[2][9]],
            },
            {
                0: POS[lines[3][3]],
                1: POS[lines[3][5]],
                2: POS[lines[3][7]],
                3: POS[lines[3][9]],
            },
        )

    def __repr__(self) -> str:
        return (
            f'State(\n'
            f'    top={self.top!r},\n'
            f'    row1={self.row1!r},\n'
            f'    row2={self.row2!r},\n'
            f')'
        )


def next_states(
        score: int,
        state: State,
) -> Generator[tuple[int, State], None, None]:
    for k, v in state.top.items():
        if v is None:
            continue

        target_col = 2 + v * 2
        max_c = max(target_col, k)
        min_c = min(target_col, k)
        to_move_top = max_c - min_c

        if all(
            k2 <= min_c or k2 >= max_c or v2 is None
            for k2, v2 in state.top.items()
        ):
            if state.row2[v] is None:
                yield (
                    score + (to_move_top + 2) * 10 ** v,
                    state._replace(
                        top={**state.top, k: None},
                        row2={**state.row2, v: v},
                    )
                )
            elif state.row2[v] == v and state.row1[v] is None:
                yield (
                    score + (to_move_top + 1) * 10 ** v,
                    state._replace(
                        top={**state.top, k: None},
                        row1={**state.row1, v: v},
                    ),
                )

    potential_targets = {k for k, v in state.top.items() if v is None}
    for i in range(4):
        row1_val = state.row1[i]
        row2_val = state.row2[i]
        # this row is done! do not move!
        if row1_val == i and row2_val == i:
            continue

        for target in potential_targets:
            src_col = 2 + i * 2
            max_c = max(src_col, target)
            min_c = min(src_col, target)
            to_move_top = max_c - min_c

            if all(
                k2 <= min_c or k2 >= max_c or v2 is None
                for k2, v2 in state.top.items()
            ):
                if row1_val is not None:
                    yield (
                        score + (to_move_top + 1) * 10 ** row1_val,
                        state._replace(
                            top={**state.top, target: row1_val},
                            row1={**state.row1, i: None},
                        )
                    )
                elif row2_val != i and row2_val is not None:
                    yield (
                        score + (to_move_top + 2) * 10 ** row2_val,
                        state._replace(
                            top={**state.top, target: row2_val},
                            row2={**state.row2, i: None},
                        ),
                    )


def compute(s: str) -> int:
    initial = State.parse(s)

    seen = set()
    todo = [(0, initial)]
    while todo:
        score, state = heapq.heappop(todo)

        if state.completed:
            return score
        elif state in seen:
            continue
        else:
            seen.add(state)

        for tp in next_states(score, state):
            heapq.heappush(todo, tp)

    raise AssertionError('unreachable!')


if __name__ == "__main__":
    lines = open("input.txt","r").read()
    print('Part 1: ',compute(lines))