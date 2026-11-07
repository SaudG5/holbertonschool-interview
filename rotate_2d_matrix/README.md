# Rotate 2D Matrix

Rotates an `n` x `n` 2D matrix 90 degrees clockwise, in place.

## File

| File | Description |
| ---- | ----------- |
| `0-rotate_2d_matrix.py` | `rotate_2d_matrix(matrix)`: rotates the matrix in place and returns nothing |

## How it works

1. **Transpose** the matrix: swap `matrix[i][j]` with `matrix[j][i]` for every pair above the diagonal.
2. **Reverse each row.**

Together these two steps give a 90° clockwise rotation using O(1) extra space and O(n²) time.

## Example

```
[[1, 2, 3],        [[7, 4, 1],
 [4, 5, 6],   ->    [8, 5, 2],
 [7, 8, 9]]         [9, 6, 3]]
```

## Requirements

* Ubuntu 14.04 LTS, `python3` (3.4.3)
* PEP 8 style (1.7.x)
* No imported modules