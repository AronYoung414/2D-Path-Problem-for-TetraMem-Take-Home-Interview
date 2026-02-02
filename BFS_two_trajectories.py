from BFS_single_trajectory import *


def path_exists_disjoint(
        universe: np.ndarray,
        start_x: int, start_y: int,
        end_x: int, end_y: int,
        forbidden: set = None
):
    height, width = universe.shape
    BLACK = 0

    if forbidden is None:
        forbidden = set()

    def in_bounds(x, y):
        return 0 <= x < height and 0 <= y < width

    if not in_bounds(start_x, start_y) or not in_bounds(end_x, end_y):
        return None
    if universe[start_x, start_y] != BLACK or universe[end_x, end_y] != BLACK:
        return None
    if (start_x, start_y) in forbidden or (end_x, end_y) in forbidden:
        return None

    visited = np.zeros((height, width), dtype=bool)
    parent = {}

    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x, start_y] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == (end_x, end_y):
            # reconstruct path
            path = []
            cur = (x, y)
            while cur != (start_x, start_y):
                path.append(cur)
                cur = parent[cur]
            path.append((start_x, start_y))
            return path[::-1]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                    in_bounds(nx, ny)
                    and not visited[nx, ny]
                    and universe[nx, ny] == BLACK
                    and (nx, ny) not in forbidden
            ):
                visited[nx, ny] = True
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    return None


def main():
    universe = imageio.imread("images/bars.png")

    # (start1_x, start1_y), (end1_x, end1_y) = random_black_points(universe)
    # (start2_x, start2_y), (end2_x, end2_y) = random_black_points(universe)
    (start1_x, start1_y), (end1_x, end1_y) = (8, 0), (8, 2)
    (start2_x, start2_y), (end2_x, end2_y) = (8, 6), (8, 8)
    print("Start 1:", "(" + str(start1_x) + "," + str(start1_y) + ")")
    print("End 1:", "(" + str(end1_x) + "," + str(end1_y) + ")")
    print("Start 2:", "(" + str(start2_x) + "," + str(start2_y) + ")")
    print("End 2:", "(" + str(end2_x) + "," + str(end2_y) + ")")

    # First path
    path1 = path_exists_disjoint(
        universe,
        start1_x, start1_y,
        end1_x, end1_y
    )

    if path1 is None:
        print("No path for pair 1")
        return

    # Block path1 pixels
    forbidden = set(path1)

    # Second path
    path2 = path_exists_disjoint(
        universe,
        start2_x, start2_y,
        end2_x, end2_y,
        forbidden=forbidden
    )

    if path2 is None:
        print("No disjoint path for pair 2")
        return

    print("Both paths found and disjoint!")


if __name__ == "__main__":
    main()
