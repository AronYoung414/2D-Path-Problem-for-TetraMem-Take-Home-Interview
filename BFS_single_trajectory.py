import random

import numpy as np
from collections import deque
import imageio.v3 as imageio


def path_exists(
        universe: np.ndarray,
        start_x: int, start_y: int,
        end_x: int, end_y: int,
        output_file: str = "path.png"
) -> bool:
    height, width = universe.shape
    BLACK = 0

    def in_bounds(x, y):
        return 0 <= x < height and 0 <= y < width

    if not in_bounds(start_x, start_y) or not in_bounds(end_x, end_y):
        return False
    if universe[start_x, start_y] != BLACK or universe[end_x, end_y] != BLACK:
        return False

    visited = np.zeros((height, width), dtype=bool)
    parent = dict()

    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x, start_y] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    found = False

    while queue:
        x, y = queue.popleft()

        if (x, y) == (end_x, end_y):
            found = True
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                    in_bounds(nx, ny)
                    and not visited[nx, ny]
                    and universe[nx, ny] == BLACK
            ):
                visited[nx, ny] = True
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    if not found:
        return False

    # -----------------------
    # Reconstruct path
    # -----------------------
    path = []
    cur = (end_x, end_y)
    while cur != (start_x, start_y):
        path.append(cur)
        cur = parent[cur]
    path.append((start_x, start_y))
    path.reverse()

    # -----------------------
    # Visualization
    # -----------------------
    vis = np.stack([universe] * 3, axis=-1)  # grayscale → RGB

    for x, y in path:
        vis[x, y] = [128, 128, 128]  # path = gray

    vis[start_x, start_y] = [0, 255, 0]  # start = green
    vis[end_x, end_y] = [255, 0, 0]  # end = red

    imageio.imwrite(output_file, vis.astype(np.uint8))

    return True


def random_black_points(universe: np.ndarray):
    """
    Randomly select two distinct black pixels from the universe.
    Assumes black pixels have value 0.
    Returns: (sx, sy), (ex, ey)
    """

    BLACK = 0

    # Find all black pixel coordinates
    black_pixels = np.argwhere(universe == BLACK)

    if len(black_pixels) < 2:
        raise ValueError("Not enough black pixels to choose start and end.")

    # Randomly sample two different pixels
    (sx, sy), (ex, ey) = random.sample(list(map(tuple, black_pixels)), 2)

    return (sx, sy), (ex, ey)


def main():
    universe = imageio.imread("images/bars.png")

    # (start_x, start_y), (end_x, end_y) = random_black_points(universe)
    (start_x, start_y), (end_x, end_y) = (0, 0), (2, 8)
    print("Start:", "(" + str(start_x) + "," + str(start_y) + ")")
    print("End:", "(" + str(end_x) + "," + str(end_y) + ")")

    exists = path_exists(
        universe,
        start_x, start_y,
        end_x, end_y,
        output_file="solution.png"
    )

    print("Path exists:", exists)


if __name__ == "__main__":
    main()
