
# bfs_dfs_astar1.py
# spring 2024 (updated spring 2026)
# prof. lehman
#
# code implements BFS, DFS, and A* algorithms
# to traverse a maze from A to B
# maze contains walls "X" and open spaces "."
# code generated (mostly) using chat GPT4 prompts
#
#  A..X...
#  ...X..B
#  .......
#  ...XX..
#
#  code displays steps taken and final path marked with "P"
#  code displays steps explored ie. tried, by each algorithm
#

from collections import deque
import heapq


steps_explored = 0

def read_maze(filename):
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file]
    return maze

def find_start_end(maze):
    start = end = None
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'A':
                start = (i, j)
            elif cell == 'B':
                end = (i, j)
    return start, end

def bfs(maze, start, end):
    global steps_explored
    
    queue = deque([start])
    visited = {start: None}

    while queue:
        current = queue.popleft()
        steps_explored += 1
        
        if current == end:
            break
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            i, j = current[0] + direction[0], current[1] + direction[1]
            if 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] != 'X' and (i, j) not in visited:
                queue.append((i, j))
                visited[(i, j)] = current

    path = []
    while end:
        path.append(end)
        end = visited[end]
    return path[::-1]

def dfs(maze, start, end):
    global steps_explored
    
    stack = [start]
    visited = {start: None}

    while stack:
        current = stack.pop()
        steps_explored += 1
        if current == end:
            break
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            i, j = current[0] + direction[0], current[1] + direction[1]
            if 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] != 'X' and (i, j) not in visited:
                stack.append((i, j))
                visited[(i, j)] = current

    path = []
    while end:
        path.append(end)
        end = visited[end]
    return path[::-1]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, end):
    global steps_explored
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {start: None}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        current = heapq.heappop(open_set)[1]

        steps_explored += 1
        
        if current == end:
            break

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            tentative_g_score = g_score[current] + 1

            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] != 'X':
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

    path = []
    while end:
        path.append(end)
        end = came_from[end]
    return path[::-1]

def display_maze(maze, path):
    for step in path:
        if maze[step[0]][step[1]] != 'A' and maze[step[0]][step[1]] != 'B':
            maze[step[0]][step[1]] = 'P'
    for row in maze:
        print(''.join(row))

# *** main ***
maze = read_maze('harvard_maze.txt')
start, end = find_start_end(maze)
search_method = input("Enter search method (BFS, DFS, or A*): ").strip().upper()

if search_method == "BFS":
    path = bfs(maze, start, end)
elif search_method == "DFS":
    path = dfs(maze, start, end)
elif search_method == "A*":
    path = a_star(maze, start, end)
else:
    print("Invalid search method. Please enter 'BFS', 'DFS', or 'A*'.")

print()
display_maze(maze, path)
print()
print(f"Number of steps: {len(path) - 1}")
print(f"Number of steps explored {steps_explored}")


