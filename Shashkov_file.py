import random
import heapq

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def generate(self):
        stack = [(0, 0)]
        while stack:
            current_cell = stack[-1]
            x, y = current_cell
            self.grid[y][x] = 1
            neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
            unvisited_neighbors = [n for n in neighbors if 0 <= n[0] < self.width and 0 <= n[1] < self.height and self.grid[n[1]][n[0]] == 0]
            if unvisited_neighbors:
                next_cell = random.choice(unvisited_neighbors)
                nx, ny = next_cell
                wall_x = (nx + x) // 2
                wall_y = (ny + y) // 2
                self.grid[wall_y][wall_x] = 1
                stack.append(next_cell)
            else:
                stack.pop()

    def solve(self, start, end):
        open_set = []
        closed_set = set()
        heapq.heappush(open_set, (0, start, []))
        while open_set:
            f, current, path = heapq.heappop(open_set)
            if current == end:
                return path
            closed_set.add(current)
            for neighbor in self.get_neighbors(current):
                if neighbor in closed_set:
                    continue
                new_path = path + [current]
                heapq.heappush(open_set, (len(new_path) + self.heuristic(neighbor, end), neighbor, new_path))

    def heuristic(self, a, b):
        return abs(b[0] - a[0]) + abs(b[1] - a[1])

    def get_neighbors(self, cell):
        x, y = cell
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [(nx, ny) for nx, ny in neighbors if 0 <= nx < self.width and 0 <= ny < self.height and self.grid[ny][nx] == 1]

    def __str__(self):
        maze_str = ""
        for row in self.grid:
            maze_str += "".join(["#" if cell == 1 else " " for cell in row]) + "
"
        return maze_str

if __name__ == "__main__":
    width = 21
    height = 21
    maze = Maze(width, height)
    maze.generate()
    print("Generated Maze:")
    print(maze)
    start = (1, 1)
    end = (width-2, height-2)
    path = maze.solve(start, end)
    print("Solved Maze:")
    for cell in path:
        x, y = cell
        maze.grid[y][x] = 2
    print(maze)

