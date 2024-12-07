def solve_puzzle(grid):
    # Directions in order: up, right, down, left
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    DIR_SYMBOLS = {'^': 0, '>': 1, 'v': 2, '<': 3}

    rows = len(grid)
    cols = len(grid[0])

    # Convert grid to list of lists for easy manipulation
    lab = [list(row) for row in grid]

    # Find guard start position and direction
    start_pos = None
    start_dir = None
    for r in range(rows):
        for c in range(cols):
            if lab[r][c] in DIR_SYMBOLS:
                start_pos = (r, c)
                start_dir = DIR_SYMBOLS[lab[r][c]]
                lab[r][c] = '.'  # replace with floor
                break
        if start_pos is not None:
            break

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def step(lab, start_pos, start_dir):
        # Simulate the guard movement until leaving map
        visited_positions = set()
        pos = start_pos
        d = start_dir
        visited_positions.add(pos)
        while True:
            dr, dc = DIRECTIONS[d]
            fr, fc = pos[0] + dr, pos[1] + dc
            # If obstacle ahead, turn right
            if in_bounds(fr, fc) and lab[fr][fc] == '#':
                d = (d + 1) % 4
            else:
                # Move forward if possible
                nr, nc = pos[0] + DIRECTIONS[d][0], pos[1] + DIRECTIONS[d][1]
                if not in_bounds(nr, nc):
                    # Guard leaves the area
                    return visited_positions
                pos = (nr, nc)
                visited_positions.add(pos)

    # Part one: how many distinct positions visited without modification
    visited_without_obstacle = step(lab, start_pos, start_dir)

    # Part two: find all positions where placing a new obstacle causes a loop
    # To detect a loop, we keep track of (pos, direction) states visited.
    def causes_loop(lab, start_pos, start_dir, obstruction_pos):
        r, c = obstruction_pos
        lab[r][c] = '#'
        pos = start_pos
        d = start_dir
        seen_states = set()
        # If we ever revisit the same state (pos+dir), we have a loop
        while True:
            state = (pos, d)
            if state in seen_states:
                lab[r][c] = '.'  # revert
                return True
            seen_states.add(state)
            dr, dc = DIRECTIONS[d]
            fr, fc = pos[0] + dr, pos[1] + dc
            if in_bounds(fr, fc) and lab[fr][fc] == '#':
                d = (d + 1) % 4
            else:
                nr, nc = pos[0] + DIRECTIONS[d][0], pos[1] + DIRECTIONS[d][1]
                if not in_bounds(nr, nc):
                    # No loop, guard leaves
                    lab[r][c] = '.'  # revert
                    return False
                pos = (nr, nc)

    # Find all possible loop-causing positions
    loop_positions = []
    for r in range(rows):
        for c in range(cols):
            if (r, c) != start_pos and lab[r][c] == '.':
                if causes_loop(lab, start_pos, start_dir, (r, c)):
                    loop_positions.append((r, c))

    return len(visited_without_obstacle), len(loop_positions)


# Example usage:
data = open("2024//advent_06.txt", "r")

grid = []

for line in data:
    grid.append(list(line.strip("\n")))

part_one, part_two = solve_puzzle(grid)
print("Part One:", part_one)  # Distinct positions visited before leaving
print("Part Two:", part_two)  # Count of positions where adding an obstacle causes a loop

# Suggestions:
# - You could try different input grids.
# - You could visualize the path or the loops by modifying the code.
# - Consider optimizing loop detection if the grid is large.
