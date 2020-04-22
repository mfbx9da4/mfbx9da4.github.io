from typing import List, NamedTuple, Set
import string

Grid = List[List[str]]
letters = list(string.ascii_uppercase)


class Pos(NamedTuple):
    r: int
    c: int

    def as_string(self):
        return "{row}{col}".format(row=letters[self.r], col=self.c + 1)


def parse_grid(grid_str: str) -> Grid:
    ret = []
    rows = grid_str.split('\n')
    for row in rows:
        stripped = row.strip()
        if stripped != '':
            row_list = list(stripped)
            ret.append(row_list)
    return ret


def find_locations(grid: Grid, color: str) -> List[Pos]:
    ret = []
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == color:
                ret.append(Pos(r, c))
    return ret


def in_range(grid: Grid, pos: Pos) -> bool:
    if pos.r >= 0 and pos.r < len(grid) and pos.c >= 0 and pos.c < len(grid[0]):
        return True
    return False


def find_available_moves(grid: Grid, pos: Pos, color: str) -> Set[str]:
    ret = set()
    moves = [
        # top
        (Pos(pos.r - 1, pos.c), Pos(pos.r - 2, pos.c)),
        # bottom
        (Pos(pos.r + 1, pos.c), Pos(pos.r + 2, pos.c)),
        # left
        (Pos(pos.r, pos.c - 1), Pos(pos.r, pos.c - 2)),
        # right
        (Pos(pos.r, pos.c + 1), Pos(pos.r, pos.c + 2)),
    ]
    color2 = 'B' if color == 'W' else 'W'
    for sib, sib2 in moves:
        if not (in_range(grid, sib) and in_range(grid, sib2)):
            continue
        if grid[sib.r][sib.c] == color2 and grid[sib2.r][sib2.c] == '.':
            ret.add(sib2.as_string())
    return ret


def solve(grid_str: str, color: str) -> Set[str]:
    ret: Set[str] = set()
    grid = parse_grid(grid_str)
    players_locations = find_locations(grid, color)
    for location in players_locations:
        ans = find_available_moves(grid, location, color)
        ret = ret.union(ans)
    return ret
