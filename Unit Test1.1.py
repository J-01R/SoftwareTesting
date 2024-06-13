import matplotlib.pyplot as plt
import numpy as np

def move_robot(x, y, x_goal, y_goal, obstacles):
    path = [(x, y)]
    while (x, y) != (x_goal, y_goal):
        # Check if up, down, left, or right mopive is possible
        possible_moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for move in possible_moves:
            if move == (x_goal, y_goal):
                path.append(move)
                return path
            elif move not in obstacles and move[0] >= 0 and move[1] >= 0:
                x, y = move
                path.append(move)
                break
    return path

def plot_path(path):
    plt.plot([point[0] for point in path], [point[1] for point in path], 'ro-')
    plt.show()

if __name__ == '__main__':
    obstacles = [(1,1), (1,2), (2,2)]
    path = move_robot(0, 0, 3, 3, obstacles)
    plot_path(path)
