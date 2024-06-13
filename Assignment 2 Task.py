import matplotlib.pyplot as plt
import numpy as np
import heapq

# Define the grid size and obstacles
GRID_SIZE = 4
obstacles = [(1, 1), (1, 2), (2, 2)]

# Define the heuristic function for A*
def heuristic(a, b):
    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

# Define the A* search algorithm
def astar(start, goal, obstacles):
    # Define the open and closed sets
    open_set = []
    closed_set = set()
    heapq.heappush(open_set, (0, start))

    # Define the parent and g-score dictionaries
    parent = {}
    g_score = {start: 0}

    # Iterate until the open set is empty
    while open_set:
        # Get the node with the lowest f-score from the open set
        current = heapq.heappop(open_set)[1]

        # Check if we have reached the goal
        if current == goal:
            path = [current]
            while current in parent:
                current = parent[current]
                path.append(current)
            path.reverse()
            return path

        # Add the current node to the closed set
        closed_set.add(current)

        # Check the neighboring nodes
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                # Skip the current node
                if dx == 0 and dy == 0:
                    continue

                # Calculate the neighbor's position
                neighbor = (current[0] + dx, current[1] + dy)

                # Check if the neighbor is inside the grid
                if neighbor[0] < 0 or neighbor[0] >= GRID_SIZE or neighbor[1] < 0 or neighbor[1] >= GRID_SIZE:
                    continue

                # Check if the neighbor is an obstacle
                if neighbor in obstacles:
                    continue

                # Calculate the tentative g-score for the neighbor
                tentative_g_score = g_score[current] + heuristic(current, neighbor)

                # Check if the neighbor is already in the closed set and if the tentative g-score is greater than the current g-score
                if neighbor in closed_set and tentative_g_score >= g_score.get(neighbor, float('inf')):
                    continue

                # Add the neighbor to the open set if it's not already there or if the tentative g-score is lower than the current g-score
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    heapq.heappush(open_set, (tentative_g_score + heuristic(neighbor, goal), neighbor))
                    parent[neighbor] = current
                    g_score[neighbor] = tentative_g_score

    # If we reach here, it means there's no path to the goal
    return None

# Define the start and goal positions
start = (0, 0)
goal = (3, 3)

# Find the path using A*
path = astar(start, goal, obstacles)

# Plot the path
fig, ax = plt.subplots()
ax.set_xticks(np.arange(-0.5, GRID_SIZE, 1))
ax.set_yticks(np.arange(-0.5, GRID_SIZE, 1))
ax.grid(True)

for obstacle in obstacles:
    ax.add_patch(plt.Rectangle(obstacle, 1, 1, color='gray'))

ax.plot(*start, 'bo', markersize=10)
ax.plot(*goal, 'go', markersize=10)

for i in range(len(path)-1
