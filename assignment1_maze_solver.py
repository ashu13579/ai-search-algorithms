"""
Assignment 1: Maze Solver using BFS and DFS
Objective: Implement BFS and DFS to solve a maze.

Problem Statement: Given a grid-based maze where 0 represents walls and 1
represents walkable paths, find the shortest path from a start cell to an end cell.
"""

from collections import deque
import time


class MazeSolver:
    def __init__(self, maze):
        """
        Initialize the maze solver.
        
        Args:
            maze: 2D list where 0 = wall, 1 = walkable path
        """
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0]) if maze else 0
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        
    def is_valid(self, row, col, visited):
        """Check if a cell is valid to visit."""
        return (0 <= row < self.rows and 
                0 <= col < self.cols and 
                self.maze[row][col] == 1 and 
                not visited[row][col])
    
    def bfs(self, start, end):
        """
        Breadth-First Search to find the shortest path.
        
        Args:
            start: Tuple (row, col) for start position
            end: Tuple (row, col) for end position
            
        Returns:
            Tuple (path, nodes_explored)
        """
        visited = [[False] * self.cols for _ in range(self.rows)]
        parent = [[None] * self.cols for _ in range(self.rows)]
        queue = deque([start])
        visited[start[0]][start[1]] = True
        nodes_explored = 0
        
        while queue:
            row, col = queue.popleft()
            nodes_explored += 1
            
            # Check if we reached the end
            if (row, col) == end:
                # Reconstruct path
                path = []
                current = end
                while current is not None:
                    path.append(current)
                    current = parent[current[0]][current[1]]
                path.reverse()
                return path, nodes_explored
            
            # Explore neighbors
            for dr, dc in self.directions:
                new_row, new_col = row + dr, col + dc
                
                if self.is_valid(new_row, new_col, visited):
                    visited[new_row][new_col] = True
                    parent[new_row][new_col] = (row, col)
                    queue.append((new_row, new_col))
        
        return None, nodes_explored  # No path found
    
    def dfs(self, start, end):
        """
        Depth-First Search to find a valid path (not necessarily shortest).
        
        Args:
            start: Tuple (row, col) for start position
            end: Tuple (row, col) for end position
            
        Returns:
            Tuple (path, nodes_explored)
        """
        visited = [[False] * self.cols for _ in range(self.rows)]
        path = []
        nodes_explored = [0]  # Using list to maintain reference in recursion
        
        def dfs_recursive(row, col):
            # Mark as visited
            visited[row][col] = True
            nodes_explored[0] += 1
            path.append((row, col))
            
            # Check if we reached the end
            if (row, col) == end:
                return True
            
            # Explore neighbors
            for dr, dc in self.directions:
                new_row, new_col = row + dr, col + dc
                
                if self.is_valid(new_row, new_col, visited):
                    if dfs_recursive(new_row, new_col):
                        return True
            
            # Backtrack
            path.pop()
            return False
        
        if dfs_recursive(start[0], start[1]):
            return path, nodes_explored[0]
        return None, nodes_explored[0]
    
    def visualize_path(self, path, algorithm_name):
        """Visualize the maze with the path."""
        if path is None:
            print(f"\n{algorithm_name}: No path found!")
            return
        
        # Create a copy of the maze for visualization
        visual = [['█' if cell == 0 else ' ' for cell in row] for row in self.maze]
        
        # Mark the path
        for i, (row, col) in enumerate(path):
            if i == 0:
                visual[row][col] = 'S'  # Start
            elif i == len(path) - 1:
                visual[row][col] = 'E'  # End
            else:
                visual[row][col] = '•'  # Path
        
        print(f"\n{algorithm_name} Path Visualization:")
        print("Legend: S=Start, E=End, •=Path, █=Wall, ' '=Walkable")
        for row in visual:
            print(''.join(row))


def main():
    # Example maze: 0 = wall, 1 = walkable path
    maze = [
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ]
    
    start = (0, 0)
    end = (9, 9)
    
    solver = MazeSolver(maze)
    
    print("=" * 60)
    print("ASSIGNMENT 1: MAZE SOLVER USING BFS AND DFS")
    print("=" * 60)
    
    # BFS Solution
    print("\n--- Breadth-First Search (BFS) ---")
    start_time = time.time()
    bfs_path, bfs_nodes = solver.bfs(start, end)
    bfs_time = time.time() - start_time
    
    if bfs_path:
        print(f"Path found! Length: {len(bfs_path)}")
        print(f"Nodes explored: {bfs_nodes}")
        print(f"Time taken: {bfs_time:.6f} seconds")
        print(f"Path: {bfs_path[:5]}...{bfs_path[-3:]}")  # Show first 5 and last 3
        solver.visualize_path(bfs_path, "BFS")
    
    # DFS Solution
    print("\n--- Depth-First Search (DFS) ---")
    start_time = time.time()
    dfs_path, dfs_nodes = solver.dfs(start, end)
    dfs_time = time.time() - start_time
    
    if dfs_path:
        print(f"Path found! Length: {len(dfs_path)}")
        print(f"Nodes explored: {dfs_nodes}")
        print(f"Time taken: {dfs_time:.6f} seconds")
        print(f"Path: {dfs_path[:5]}...{dfs_path[-3:]}")
        solver.visualize_path(dfs_path, "DFS")
    
    # Comparison
    print("\n" + "=" * 60)
    print("COMPARISON: BFS vs DFS")
    print("=" * 60)
    print(f"{'Metric':<25} {'BFS':<15} {'DFS':<15}")
    print("-" * 60)
    print(f"{'Path Length':<25} {len(bfs_path) if bfs_path else 'N/A':<15} {len(dfs_path) if dfs_path else 'N/A':<15}")
    print(f"{'Nodes Explored':<25} {bfs_nodes:<15} {dfs_nodes:<15}")
    print(f"{'Time (seconds)':<25} {bfs_time:<15.6f} {dfs_time:<15.6f}")
    print(f"{'Optimal Path?':<25} {'Yes':<15} {'No':<15}")
    
    print("\n" + "=" * 60)
    print("ANALYSIS:")
    print("=" * 60)
    print("• BFS guarantees the SHORTEST path in unweighted graphs")
    print("• DFS finds A valid path but not necessarily the shortest")
    print(f"• BFS explored {bfs_nodes} nodes vs DFS explored {dfs_nodes} nodes")
    print(f"• BFS path length: {len(bfs_path) if bfs_path else 'N/A'} vs DFS path length: {len(dfs_path) if dfs_path else 'N/A'}")
    print("• BFS uses more memory (queue) but guarantees optimality")
    print("• DFS uses less memory (stack/recursion) but may find longer paths")


if __name__ == "__main__":
    main()
