# 2D Grid Path Finding with BFS

This project implements BFS-based path finding on a 2D black-and-white image grid.

Black pixels (`0`) are traversable; white pixels are obstacles. Connectivity is 4-directional (up, down, left, right).

---

## Files

```text
BFS_single_trajectory.py   # Find and visualize a single path
BFS_two_trajectories.py   # Find two vertex-disjoint paths
images/bars.png           # Example input image
````

---

## Single Path (Visualization)

**`BFS_single_trajectory.py`**

* Uses BFS to find a path between two points
* Reconstructs the path using parent pointers
* Saves an output image

**Color legend**

* Green: start
* Red: end
* Gray: path
* Black: free space
* White: obstacle

Run:

```bash
python BFS_single_trajectory.py
```

---

## Two Disjoint Paths

**`BFS_two_trajectories.py`**

* Finds first path using BFS
* Marks its pixels as forbidden
* Finds second path avoiding forbidden pixels
* Ensures no pixel is shared by both paths

Run:

```bash
python BFS_two_trajectories.py
```

---

## Dependencies

```bash
pip install numpy imageio
```

---

## Complexity

* Time: `O(H × W)` per BFS
* Space: `O(H × W)`

---

## Notes

* Coordinates are `(row, column)`
* Greedy disjoint-path strategy (not globally optimal)
