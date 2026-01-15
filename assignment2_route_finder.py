"""
Assignment 2: Route Finder Using Bi-Directional BFS/DFS
Objective: Use Bi-directional BFS/DFS to solve a navigation problem.

Problem Statement: Represent a city map as a graph where intersections are nodes
and roads are edges. Find the shortest path between two locations.
"""

from collections import deque
import time
import matplotlib.pyplot as plt
import networkx as nx


class CityGraph:
    def __init__(self):
        """Initialize an empty city graph."""
        self.graph = {}
        
    def add_edge(self, u, v, bidirectional=True):
        """Add an edge between two nodes."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append(v)
        if bidirectional:
            self.graph[v].append(u)
    
    def bfs(self, start, end):
        """Standard BFS implementation."""
        if start not in self.graph or end not in self.graph:
            return None, 0
        
        visited = {start}
        queue = deque([(start, [start])])
        nodes_explored = 0
        
        while queue:
            node, path = queue.popleft()
            nodes_explored += 1
            
            if node == end:
                return path, nodes_explored
            
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None, nodes_explored
    
    def dfs(self, start, end):
        """Standard DFS implementation."""
        if start not in self.graph or end not in self.graph:
            return None, 0
        
        visited = set()
        nodes_explored = [0]
        
        def dfs_recursive(node, path):
            visited.add(node)
            nodes_explored[0] += 1
            
            if node == end:
                return path
            
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    result = dfs_recursive(neighbor, path + [neighbor])
                    if result:
                        return result
            
            return None
        
        path = dfs_recursive(start, [start])
        return path, nodes_explored[0]
    
    def bidirectional_bfs(self, start, end):
        """
        Bi-directional BFS: Search from both start and end simultaneously.
        Stops when the two searches meet.
        """
        if start not in self.graph or end not in self.graph:
            return None, 0
        
        if start == end:
            return [start], 1
        
        # Forward search from start
        visited_forward = {start: None}
        queue_forward = deque([start])
        
        # Backward search from end
        visited_backward = {end: None}
        queue_backward = deque([end])
        
        nodes_explored = 0
        
        while queue_forward and queue_backward:
            # Expand forward search
            if queue_forward:
                current_forward = queue_forward.popleft()
                nodes_explored += 1
                
                for neighbor in self.graph.get(current_forward, []):
                    if neighbor in visited_backward:
                        # Found intersection point!
                        return self._construct_bidirectional_path(
                            visited_forward, visited_backward, 
                            current_forward, neighbor, start, end
                        ), nodes_explored
                    
                    if neighbor not in visited_forward:
                        visited_forward[neighbor] = current_forward
                        queue_forward.append(neighbor)
            
            # Expand backward search
            if queue_backward:
                current_backward = queue_backward.popleft()
                nodes_explored += 1
                
                for neighbor in self.graph.get(current_backward, []):
                    if neighbor in visited_forward:
                        # Found intersection point!
                        return self._construct_bidirectional_path(
                            visited_forward, visited_backward,
                            neighbor, current_backward, start, end
                        ), nodes_explored
                    
                    if neighbor not in visited_backward:
                        visited_backward[neighbor] = current_backward
                        queue_backward.append(neighbor)
        
        return None, nodes_explored
    
    def _construct_bidirectional_path(self, visited_forward, visited_backward, 
                                     meet_forward, meet_backward, start, end):
        """Construct the complete path from bidirectional search."""
        # Build path from start to meeting point
        path_forward = []
        node = meet_forward
        while node is not None:
            path_forward.append(node)
            node = visited_forward[node]
        path_forward.reverse()
        
        # Build path from meeting point to end
        path_backward = []
        node = meet_backward
        while node is not None:
            path_backward.append(node)
            node = visited_backward[node]
        
        # Combine paths
        return path_forward + path_backward
    
    def visualize_graph(self, path=None, algorithm_name="Graph", explored_nodes=None):
        """Visualize the graph using networkx and matplotlib."""
        try:
            G = nx.Graph()
            
            # Add edges
            for node, neighbors in self.graph.items():
                for neighbor in neighbors:
                    G.add_edge(node, neighbor)
            
            plt.figure(figsize=(12, 8))
            pos = nx.spring_layout(G, k=2, iterations=50)
            
            # Draw all nodes
            nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                                  node_size=500, alpha=0.6)
            
            # Draw all edges
            nx.draw_networkx_edges(G, pos, alpha=0.2)
            
            # Highlight path if provided
            if path:
                path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
                nx.draw_networkx_edges(G, pos, path_edges, edge_color='red', 
                                      width=3, alpha=0.8)
                
                # Highlight path nodes
                nx.draw_networkx_nodes(G, pos, path, node_color='orange', 
                                      node_size=600, alpha=0.9)
                
                # Highlight start and end
                nx.draw_networkx_nodes(G, pos, [path[0]], node_color='green', 
                                      node_size=700, alpha=1)
                nx.draw_networkx_nodes(G, pos, [path[-1]], node_color='red', 
                                      node_size=700, alpha=1)
            
            # Draw labels
            nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
            
            plt.title(f"{algorithm_name} - Path Visualization", fontsize=16, fontweight='bold')
            plt.axis('off')
            plt.tight_layout()
            
            # Save the figure
            filename = f"{algorithm_name.lower().replace(' ', '_')}_visualization.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"Visualization saved as: {filename}")
            plt.close()
            
        except Exception as e:
            print(f"Visualization requires matplotlib and networkx: {e}")
            print("Install with: pip install matplotlib networkx")


def create_city_map():
    """Create a sample city map graph."""
    city = CityGraph()
    
    # Define city intersections and roads
    roads = [
        ('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'),
        ('C', 'F'), ('D', 'G'), ('E', 'G'), ('E', 'H'),
        ('F', 'I'), ('G', 'J'), ('H', 'J'), ('H', 'K'),
        ('I', 'L'), ('J', 'M'), ('K', 'M'), ('K', 'N'),
        ('L', 'O'), ('M', 'O'), ('N', 'O'), ('C', 'D'),
        ('F', 'G'), ('I', 'J'), ('L', 'M')
    ]
    
    for u, v in roads:
        city.add_edge(u, v)
    
    return city


def main():
    print("=" * 70)
    print("ASSIGNMENT 2: ROUTE FINDER USING BI-DIRECTIONAL BFS/DFS")
    print("=" * 70)
    
    # Create city map
    city = create_city_map()
    
    start = 'A'
    end = 'O'
    
    print(f"\nFinding route from {start} to {end}")
    print(f"City Map Nodes: {sorted(city.graph.keys())}")
    print(f"Total Intersections: {len(city.graph)}")
    
    # Standard BFS
    print("\n" + "-" * 70)
    print("1. STANDARD BFS")
    print("-" * 70)
    start_time = time.time()
    bfs_path, bfs_nodes = city.bfs(start, end)
    bfs_time = time.time() - start_time
    
    if bfs_path:
        print(f"✓ Path found: {' → '.join(bfs_path)}")
        print(f"  Path length: {len(bfs_path)} nodes")
        print(f"  Nodes explored: {bfs_nodes}")
        print(f"  Time: {bfs_time:.6f} seconds")
        city.visualize_graph(bfs_path, "Standard BFS")
    
    # Standard DFS
    print("\n" + "-" * 70)
    print("2. STANDARD DFS")
    print("-" * 70)
    start_time = time.time()
    dfs_path, dfs_nodes = city.dfs(start, end)
    dfs_time = time.time() - start_time
    
    if dfs_path:
        print(f"✓ Path found: {' → '.join(dfs_path)}")
        print(f"  Path length: {len(dfs_path)} nodes")
        print(f"  Nodes explored: {dfs_nodes}")
        print(f"  Time: {dfs_time:.6f} seconds")
        city.visualize_graph(dfs_path, "Standard DFS")
    
    # Bi-directional BFS
    print("\n" + "-" * 70)
    print("3. BI-DIRECTIONAL BFS")
    print("-" * 70)
    start_time = time.time()
    bidirectional_path, bidirectional_nodes = city.bidirectional_bfs(start, end)
    bidirectional_time = time.time() - start_time
    
    if bidirectional_path:
        print(f"✓ Path found: {' → '.join(bidirectional_path)}")
        print(f"  Path length: {len(bidirectional_path)} nodes")
        print(f"  Nodes explored: {bidirectional_nodes}")
        print(f"  Time: {bidirectional_time:.6f} seconds")
        city.visualize_graph(bidirectional_path, "Bi-directional BFS")
    
    # Performance Comparison
    print("\n" + "=" * 70)
    print("PERFORMANCE COMPARISON")
    print("=" * 70)
    print(f"{'Algorithm':<25} {'Path Length':<15} {'Nodes Explored':<20} {'Time (s)':<15}")
    print("-" * 70)
    print(f"{'Standard BFS':<25} {len(bfs_path) if bfs_path else 'N/A':<15} {bfs_nodes:<20} {bfs_time:<15.6f}")
    print(f"{'Standard DFS':<25} {len(dfs_path) if dfs_path else 'N/A':<15} {dfs_nodes:<20} {dfs_time:<15.6f}")
    print(f"{'Bi-directional BFS':<25} {len(bidirectional_path) if bidirectional_path else 'N/A':<15} {bidirectional_nodes:<20} {bidirectional_time:<15.6f}")
    
    # Analysis
    print("\n" + "=" * 70)
    print("ANALYSIS")
    print("=" * 70)
    print(f"• Bi-directional BFS explored {bidirectional_nodes} nodes")
    print(f"• Standard BFS explored {bfs_nodes} nodes")
    print(f"• Efficiency gain: {((bfs_nodes - bidirectional_nodes) / bfs_nodes * 100):.1f}% fewer nodes explored")
    print(f"• Both BFS methods found optimal path of length {len(bfs_path) if bfs_path else 'N/A'}")
    print(f"• DFS found a path of length {len(dfs_path) if dfs_path else 'N/A'} (may not be optimal)")
    print("\nKey Insights:")
    print("  → Bi-directional BFS is more efficient for large graphs")
    print("  → It searches from both ends, meeting in the middle")
    print("  → Reduces search space significantly (O(b^(d/2)) vs O(b^d))")
    print("  → Guarantees shortest path like standard BFS")


if __name__ == "__main__":
    main()
