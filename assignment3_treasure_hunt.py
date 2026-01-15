"""
Assignment 3: Search for Treasure using Best-First Search
Objective: Use Best-First Search to find a treasure in a grid.

Problem Statement: The treasure is hidden in a grid, and each cell has a heuristic
value representing its "closeness" to the treasure. Implement Best-First Search to
locate the treasure.
"""

import heapq
import time
import random


class TreasureHunt:
    def __init__(self, grid_size, treasure_pos):
        """
        Initialize the treasure hunt grid.
        
        Args:
            grid_size: Tuple (rows, cols) for grid dimensions
            treasure_pos: Tuple (row, col) for treasure location
        """
        self.rows, self.cols = grid_size
        self.treasure_pos = treasure_pos
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        
        # Create grid with some obstacles (0 = obstacle, 1 = walkable)
        self.grid = [[1 for _ in range(self.cols)] for _ in range(self.rows)]
        self._add_random_obstacles()
    
    def _add_random_obstacles(self, obstacle_ratio=0.2):
        """Add random obstacles to the grid."""
        num_obstacles = int(self.rows * self.cols * obstacle_ratio)
        for _ in range(num_obstacles):
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            # Don't place obstacle on treasure
            if (row, col) != self.treasure_pos:
                self.grid[row][col] = 0
    
    def manhattan_distance(self, pos1, pos2):
        """
        Calculate Manhattan distance between two positions.
        
        Manhattan distance = |x1 - x2| + |y1 - y2|
        """
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def euclidean_distance(self, pos1, pos2):
        """
        Calculate Euclidean distance between two positions.
        
        Euclidean distance = sqrt((x1 - x2)^2 + (y1 - y2)^2)
        """
        return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5
    
    def is_valid(self, row, col, visited):
        """Check if a cell is valid to visit."""
        return (0 <= row < self.rows and 
                0 <= col < self.cols and 
                self.grid[row][col] == 1 and 
                not visited[row][col])
    
    def best_first_search(self, start, heuristic='manhattan'):
        """
        Best-First Search using a heuristic function.
        Always moves to the most promising cell first (minimum heuristic value).
        
        Args:
            start: Tuple (row, col) for start position
            heuristic: 'manhattan' or 'euclidean' distance
            
        Returns:
            Tuple (path, nodes_explored, heuristic_values)
        """
        if heuristic == 'manhattan':
            heuristic_func = self.manhattan_distance
        else:
            heuristic_func = self.euclidean_distance
        
        visited = [[False] * self.cols for _ in range(self.rows)]
        parent = [[None] * self.cols for _ in range(self.rows)]
        
        # Priority queue: (heuristic_value, position)
        pq = [(heuristic_func(start, self.treasure_pos), start)]
        visited[start[0]][start[1]] = True
        
        nodes_explored = 0
        heuristic_values = []
        
        while pq:
            h_value, (row, col) = heapq.heappop(pq)
            nodes_explored += 1
            heuristic_values.append(h_value)
            
            # Check if we found the treasure
            if (row, col) == self.treasure_pos:
                # Reconstruct path
                path = []
                current = self.treasure_pos
                while current is not None:
                    path.append(current)
                    current = parent[current[0]][current[1]]
                path.reverse()
                return path, nodes_explored, heuristic_values
            
            # Explore neighbors
            for dr, dc in self.directions:
                new_row, new_col = row + dr, col + dc
                
                if self.is_valid(new_row, new_col, visited):
                    visited[new_row][new_col] = True
                    parent[new_row][new_col] = (row, col)
                    
                    # Calculate heuristic for new position
                    h = heuristic_func((new_row, new_col), self.treasure_pos)
                    heapq.heappush(pq, (h, (new_row, new_col)))
        
        return None, nodes_explored, heuristic_values
    
    def greedy_best_first(self, start):
        """
        Greedy Best-First Search (always picks the neighbor with lowest heuristic).
        This is a simpler version that doesn't use a priority queue.
        """
        visited = [[False] * self.cols for _ in range(self.rows)]
        path = [start]
        current = start
        nodes_explored = 0
        
        while current != self.treasure_pos:
            row, col = current
            visited[row][col] = True
            nodes_explored += 1
            
            # Find the best neighbor
            best_neighbor = None
            best_heuristic = float('inf')
            
            for dr, dc in self.directions:
                new_row, new_col = row + dr, col + dc
                
                if self.is_valid(new_row, new_col, visited):
                    h = self.manhattan_distance((new_row, new_col), self.treasure_pos)
                    if h < best_heuristic:
                        best_heuristic = h
                        best_neighbor = (new_row, new_col)
            
            if best_neighbor is None:
                return None, nodes_explored  # No path found (stuck)
            
            current = best_neighbor
            path.append(current)
        
        return path, nodes_explored
    
    def visualize_search(self, path, algorithm_name, start):
        """Visualize the grid with the search path."""
        if path is None:
            print(f"\n{algorithm_name}: No path found!")
            return
        
        # Create visualization grid
        visual = [['█' if cell == 0 else '·' for cell in row] for row in self.grid]
        
        # Mark the path
        for i, (row, col) in enumerate(path):
            if i == 0:
                visual[row][col] = 'S'  # Start
            elif (row, col) == self.treasure_pos:
                visual[row][col] = '💎'  # Treasure
            else:
                visual[row][col] = '•'  # Path
        
        print(f"\n{algorithm_name} - Path Visualization:")
        print("Legend: S=Start, 💎=Treasure, •=Path, █=Obstacle, ·=Walkable")
        print(f"Treasure at: {self.treasure_pos}")
        print()
        
        for row in visual:
            print(' '.join(row))


def compare_heuristics(grid_size, treasure_pos, start):
    """Compare different heuristic functions."""
    print("\n" + "=" * 70)
    print("HEURISTIC COMPARISON")
    print("=" * 70)
    
    results = []
    
    for heuristic in ['manhattan', 'euclidean']:
        hunt = TreasureHunt(grid_size, treasure_pos)
        
        start_time = time.time()
        path, nodes, h_values = hunt.best_first_search(start, heuristic)
        elapsed = time.time() - start_time
        
        results.append({
            'heuristic': heuristic,
            'path': path,
            'nodes': nodes,
            'time': elapsed,
            'h_values': h_values
        })
        
        print(f"\n{heuristic.upper()} Distance Heuristic:")
        if path:
            print(f"  ✓ Treasure found!")
            print(f"  Path length: {len(path)} steps")
            print(f"  Nodes explored: {nodes}")
            print(f"  Time: {elapsed:.6f} seconds")
            print(f"  Average heuristic value: {sum(h_values)/len(h_values):.2f}")
            hunt.visualize_search(path, f"Best-First ({heuristic})", start)
    
    return results


def main():
    print("=" * 70)
    print("ASSIGNMENT 3: TREASURE HUNT USING BEST-FIRST SEARCH")
    print("=" * 70)
    
    # Set random seed for reproducibility
    random.seed(42)
    
    # Configuration
    grid_size = (15, 15)
    treasure_pos = (12, 13)
    start = (0, 0)
    
    print(f"\nGrid Size: {grid_size[0]} x {grid_size[1]}")
    print(f"Start Position: {start}")
    print(f"Treasure Position: {treasure_pos}")
    print(f"Manhattan Distance to Treasure: {abs(start[0] - treasure_pos[0]) + abs(start[1] - treasure_pos[1])}")
    
    # Create treasure hunt instance
    hunt = TreasureHunt(grid_size, treasure_pos)
    
    # Best-First Search with Manhattan Distance
    print("\n" + "-" * 70)
    print("1. BEST-FIRST SEARCH (Manhattan Distance)")
    print("-" * 70)
    start_time = time.time()
    bfs_path, bfs_nodes, bfs_h_values = hunt.best_first_search(start, 'manhattan')
    bfs_time = time.time() - start_time
    
    if bfs_path:
        print(f"✓ Treasure found!")
        print(f"  Path length: {len(bfs_path)} steps")
        print(f"  Nodes explored: {bfs_nodes}")
        print(f"  Time: {bfs_time:.6f} seconds")
        print(f"  Path: {bfs_path[:5]}...{bfs_path[-3:]}")
        hunt.visualize_search(bfs_path, "Best-First Search (Manhattan)", start)
    
    # Greedy Best-First Search
    print("\n" + "-" * 70)
    print("2. GREEDY BEST-FIRST SEARCH")
    print("-" * 70)
    start_time = time.time()
    greedy_path, greedy_nodes = hunt.greedy_best_first(start)
    greedy_time = time.time() - start_time
    
    if greedy_path:
        print(f"✓ Treasure found!")
        print(f"  Path length: {len(greedy_path)} steps")
        print(f"  Nodes explored: {greedy_nodes}")
        print(f"  Time: {greedy_time:.6f} seconds")
        print(f"  Path: {greedy_path[:5]}...{greedy_path[-3:]}")
        hunt.visualize_search(greedy_path, "Greedy Best-First Search", start)
    
    # Compare different heuristics
    heuristic_results = compare_heuristics(grid_size, treasure_pos, start)
    
    # Analysis
    print("\n" + "=" * 70)
    print("ANALYSIS: HEURISTIC CHOICE IMPACT")
    print("=" * 70)
    
    print(f"\n{'Heuristic':<20} {'Path Length':<15} {'Nodes Explored':<20} {'Time (s)':<15}")
    print("-" * 70)
    for result in heuristic_results:
        if result['path']:
            print(f"{result['heuristic'].capitalize():<20} {len(result['path']):<15} {result['nodes']:<20} {result['time']:<15.6f}")
    
    print("\n" + "=" * 70)
    print("KEY INSIGHTS")
    print("=" * 70)
    print("• Manhattan Distance:")
    print("  - Better for grid-based movement (4-directional)")
    print("  - Admissible heuristic (never overestimates)")
    print("  - More accurate for this problem")
    print("\n• Euclidean Distance:")
    print("  - Better for diagonal/free movement")
    print("  - Also admissible")
    print("  - May explore slightly different paths")
    print("\n• Best-First Search Characteristics:")
    print("  - Greedy approach: always picks most promising cell")
    print("  - Not guaranteed to find shortest path")
    print("  - Very efficient when heuristic is good")
    print("  - Can get stuck in local minima")
    print(f"\n• Performance:")
    print(f"  - Explored {bfs_nodes} nodes to find treasure")
    print(f"  - Path length: {len(bfs_path) if bfs_path else 'N/A'} steps")
    print(f"  - Heuristic guided search efficiently toward goal")


if __name__ == "__main__":
    main()
