/**
 * 1091. Shortest Path in Binary Matrix
 * In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.
 */

import java.util.Queue;
import javafx.util.Pair;
import java.util.LinkedList;


public class shortest_path_matrix {
    // BFS , find shortest path
    // use queue to store each node
    // mark node to avoid repeating

    public int shortestPathBinaryMatrix(int[][] grid) {
        int[][] direction = {{1,-1}, {1,0}, {1,1}, {0,-1}, {0,1}, {-1,-1}, {-1,0}, {-1,1}};
        int m = grid.length, n = grid[0].length;
        if (grid[0][0] == 1 || grid[m-1][n-1] == 1) {
            return -1;
        }
        Queue<Pair<Integer, Integer>> queue = new LinkedList<>();
        queue.add(new Pair<>(0,0));
        int pathLength = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            pathLength++;
            for (int i = 0; i < size; i++) {
                Pair<Integer, Integer> cur = queue.poll();
                int cr = cur.getKey(), cc = cur.getValue();
                grid[cr][cc] = 1;  // mark
                if (cr == m-1 && cc == n-1) {
                    return pathLength;
                }
                
                for (int[] d : direction) {
                    int nr = cr + d[0], nc = cc + d[1];
                    if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 1) {
                        continue;
                    } 
                    queue.add(new Pair<>(nr, nc));  
                    grid[nr][nc] = 1;  // mark
                }
            } 
        }
        return -1;
    }

}