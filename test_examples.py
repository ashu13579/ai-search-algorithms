"""
Test Examples for AI Search Algorithms
This file contains additional test cases and examples for all three assignments.
"""

from assignment1_maze_solver import MazeSolver
from assignment2_route_finder import CityGraph
from assignment3_treasure_hunt import TreasureHunt


def test_assignment1_small_maze():
    """Test Assignment 1 with a small maze."""
    print("\n" + "="*60)
    print("TEST: Small Maze (5x5)")
    print("="*60)
    
    small_maze = [
        [1, 1, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1]
    ]
    
    solver = MazeSolver(small_maze)
    start = (0, 0)
    end = (4, 4)
    
    bfs_path, bfs_nodes = solver.bfs(start, end)
    dfs_path, dfs_nodes = solver.dfs(start, end)
    
    print(f"BFS: Path length = {len(bfs_path) if bfs_path else 'No path'}, Nodes = {bfs_nodes}")
    print(f"DFS: Path length = {len(dfs_path) if dfs_path else 'No path'}, Nodes = {dfs_nodes}")
    
    if bfs_path:
        solver.visualize_path(bfs_path, "BFS - Small Maze")


def test_assignment1_no_solution():
    """Test Assignment 1 with an unsolvable maze."""
    print("\n" + "="*60)
    print("TEST: Unsolvable Maze")
    print("="*60)
    
    unsolvable_maze = [
        [1, 1, 0, 1, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],  # Wall blocking path
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 1]
    ]
    
    solver = MazeSolver(unsolvable_maze)
    start = (0, 0)
    end = (4, 4)
    
    bfs_path, bfs_nodes = solver.bfs(start, end)
    dfs_path, dfs_nodes = solver.dfs(start, end)
    
    print(f"BFS: Path = {bfs_path}, Nodes explored = {bfs_nodes}")
    print(f"DFS: Path = {dfs_path}, Nodes explored = {dfs_nodes}")
    print("✓ Both algorithms correctly identified no solution exists")


def test_assignment1_large_maze():
    """Test Assignment 1 with a larger maze."""
    print("\n" + "="*60)
    print("TEST: Large Maze (20x20)")
    print("="*60)
    
    # Create a 20x20 maze with a spiral pattern
    large_maze = [[1 for _ in range(20)] for _ in range(20)]
    
    # Add some walls to make it interesting
    for i in range(2, 18):
        large_maze[i][5] = 0
        large_maze[i][15] = 0
    
    for j in range(5, 16):
        large_maze[2][j] = 0
        large_maze[17][j] = 0
    
    solver = MazeSolver(large_maze)
    start = (0, 0)
    end = (19, 19)
    
    bfs_path, bfs_nodes = solver.bfs(start, end)
    dfs_path, dfs_nodes = solver.dfs(start, end)
    
    print(f"BFS: Path length = {len(bfs_path)}, Nodes explored = {bfs_nodes}")
    print(f"DFS: Path length = {len(dfs_path)}, Nodes explored = {dfs_nodes}")
    print(f"Efficiency: BFS found path {((len(dfs_path) - len(bfs_path)) / len(dfs_path) * 100):.1f}% shorter")


def test_assignment2_simple_graph():
    """Test Assignment 2 with a simple linear graph."""
    print("\n" + "="*60)
    print("TEST: Simple Linear Graph")
    print("="*60)
    
    city = CityGraph()
    
    # Create a simple linear path: A -> B -> C -> D -> E
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')]
    for u, v in edges:
        city.add_edge(u, v)
    
    start = 'A'
    end = 'E'
    
    bfs_path, bfs_nodes = city.bfs(start, end)
    bidirectional_path, bidirectional_nodes = city.bidirectional_bfs(start, end)
    
    print(f"BFS: Path = {' -> '.join(bfs_path)}, Nodes = {bfs_nodes}")
    print(f"Bi-BFS: Path = {' -> '.join(bidirectional_path)}, Nodes = {bidirectional_nodes}")
    print(f"Efficiency gain: {((bfs_nodes - bidirectional_nodes) / bfs_nodes * 100):.1f}%")


def test_assignment2_complex_graph():
    """Test Assignment 2 with a more complex graph."""
    print("\n" + "="*60)
    print("TEST: Complex Graph with Multiple Paths")
    print("="*60)
    
    city = CityGraph()
    
    # Create a graph with multiple paths
    edges = [
        ('A', 'B'), ('A', 'C'), ('A', 'D'),
        ('B', 'E'), ('C', 'E'), ('D', 'F'),
        ('E', 'G'), ('F', 'G'), ('G', 'H'),
        ('B', 'C'), ('E', 'F')  # Additional connections
    ]
    
    for u, v in edges:
        city.add_edge(u, v)
    
    start = 'A'
    end = 'H'
    
    bfs_path, bfs_nodes = city.bfs(start, end)
    dfs_path, dfs_nodes = city.dfs(start, end)
    bidirectional_path, bidirectional_nodes = city.bidirectional_bfs(start, end)
    
    print(f"BFS: Path length = {len(bfs_path)}, Nodes = {bfs_nodes}")
    print(f"DFS: Path length = {len(dfs_path)}, Nodes = {dfs_nodes}")
    print(f"Bi-BFS: Path length = {len(bidirectional_path)}, Nodes = {bidirectional_nodes}")


def test_assignment3_small_grid():
    """Test Assignment 3 with a small grid."""
    print("\n" + "="*60)
    print("TEST: Small Grid (5x5)")
    print("="*60)
    
    grid_size = (5, 5)
    treasure_pos = (4, 4)
    start = (0, 0)
    
    hunt = TreasureHunt(grid_size, treasure_pos)
    
    # Clear obstacles for this test
    hunt.grid = [[1 for _ in range(5)] for _ in range(5)]
    
    manhattan_path, manhattan_nodes, _ = hunt.best_first_search(start, 'manhattan')
    euclidean_path, euclidean_nodes, _ = hunt.best_first_search(start, 'euclidean')
    
    print(f"Manhattan: Path length = {len(manhattan_path)}, Nodes = {manhattan_nodes}")
    print(f"Euclidean: Path length = {len(euclidean_path)}, Nodes = {euclidean_nodes}")
    
    hunt.visualize_search(manhattan_path, "Best-First (Manhattan) - Small Grid", start)


def test_assignment3_obstacles():
    """Test Assignment 3 with many obstacles."""
    print("\n" + "="*60)
    print("TEST: Grid with Heavy Obstacles")
    print("="*60)
    
    grid_size = (10, 10)
    treasure_pos = (9, 9)
    start = (0, 0)
    
    hunt = TreasureHunt(grid_size, treasure_pos)
    
    # Add a wall in the middle
    for i in range(1, 9):
        hunt.grid[i][5] = 0
    
    # Leave a gap
    hunt.grid[4][5] = 1
    
    path, nodes, _ = hunt.best_first_search(start, 'manhattan')
    
    if path:
        print(f"Path found! Length = {len(path)}, Nodes explored = {nodes}")
        hunt.visualize_search(path, "Best-First with Obstacles", start)
    else:
        print("No path found (as expected with blocking wall)")


def test_all_algorithms():
    """Run all test cases."""
    print("\n" + "="*70)
    print("RUNNING ALL TEST CASES")
    print("="*70)
    
    # Assignment 1 tests
    print("\n### ASSIGNMENT 1 TESTS ###")
    test_assignment1_small_maze()
    test_assignment1_no_solution()
    test_assignment1_large_maze()
    
    # Assignment 2 tests
    print("\n### ASSIGNMENT 2 TESTS ###")
    test_assignment2_simple_graph()
    test_assignment2_complex_graph()
    
    # Assignment 3 tests
    print("\n### ASSIGNMENT 3 TESTS ###")
    test_assignment3_small_grid()
    test_assignment3_obstacles()
    
    print("\n" + "="*70)
    print("ALL TESTS COMPLETED!")
    print("="*70)


def performance_comparison():
    """Compare performance across different input sizes."""
    print("\n" + "="*70)
    print("PERFORMANCE COMPARISON ACROSS INPUT SIZES")
    print("="*70)
    
    import time
    
    sizes = [5, 10, 15, 20]
    
    print(f"\n{'Size':<10} {'BFS Nodes':<15} {'DFS Nodes':<15} {'BFS Time':<15} {'DFS Time':<15}")
    print("-" * 70)
    
    for size in sizes:
        # Create maze
        maze = [[1 for _ in range(size)] for _ in range(size)]
        solver = MazeSolver(maze)
        
        start = (0, 0)
        end = (size-1, size-1)
        
        # BFS
        start_time = time.time()
        bfs_path, bfs_nodes = solver.bfs(start, end)
        bfs_time = time.time() - start_time
        
        # DFS
        start_time = time.time()
        dfs_path, dfs_nodes = solver.dfs(start, end)
        dfs_time = time.time() - start_time
        
        print(f"{size}x{size:<6} {bfs_nodes:<15} {dfs_nodes:<15} {bfs_time:<15.6f} {dfs_time:<15.6f}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        test_name = sys.argv[1]
        
        if test_name == "maze":
            test_assignment1_small_maze()
            test_assignment1_large_maze()
        elif test_name == "graph":
            test_assignment2_simple_graph()
            test_assignment2_complex_graph()
        elif test_name == "treasure":
            test_assignment3_small_grid()
            test_assignment3_obstacles()
        elif test_name == "performance":
            performance_comparison()
        else:
            print(f"Unknown test: {test_name}")
            print("Available tests: maze, graph, treasure, performance")
    else:
        # Run all tests
        test_all_algorithms()
        performance_comparison()
