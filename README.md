# 🔍 AI Search Algorithms

A comprehensive implementation of fundamental AI search algorithms including BFS, DFS, Bi-directional Search, and Best-First Search for solving maze navigation, route finding, and treasure hunt problems.

## 📚 Assignments Overview

### Assignment 1: Maze Solver using BFS and DFS
**Objective:** Implement BFS and DFS to solve a maze.

**Features:**
- ✅ BFS implementation for finding the shortest path
- ✅ DFS implementation for finding any valid path
- ✅ Visual path representation in terminal
- ✅ Performance comparison (nodes explored, time, path length)
- ✅ Detailed analysis of both algorithms

**Key Concepts:**
- Breadth-First Search guarantees shortest path
- Depth-First Search uses less memory but may find longer paths
- Queue vs Stack data structures

---

### Assignment 2: Route Finder Using Bi-Directional BFS/DFS
**Objective:** Use Bi-directional BFS/DFS to solve a navigation problem.

**Features:**
- ✅ Standard BFS implementation
- ✅ Standard DFS implementation
- ✅ Bi-directional BFS (searches from both ends)
- ✅ Graph visualization using NetworkX and Matplotlib
- ✅ Performance comparison showing efficiency gains

**Key Concepts:**
- Bi-directional search reduces search space from O(b^d) to O(b^(d/2))
- Searches meet in the middle
- Significant performance improvement for large graphs

---

### Assignment 3: Treasure Hunt using Best-First Search
**Objective:** Use Best-First Search to find a treasure in a grid.

**Features:**
- ✅ Best-First Search with priority queue
- ✅ Manhattan distance heuristic
- ✅ Euclidean distance heuristic
- ✅ Greedy Best-First Search variant
- ✅ Heuristic comparison and analysis
- ✅ Random obstacle generation

**Key Concepts:**
- Heuristic-guided search
- Priority queue for selecting most promising nodes
- Manhattan vs Euclidean distance trade-offs
- Admissible heuristics

---

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.7 or higher
```

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/ashu13579/ai-search-algorithms.git
cd ai-search-algorithms
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Running the Assignments

**Assignment 1 - Maze Solver:**
```bash
python assignment1_maze_solver.py
```

**Assignment 2 - Route Finder:**
```bash
python assignment2_route_finder.py
```

**Assignment 3 - Treasure Hunt:**
```bash
python assignment3_treasure_hunt.py
```

---

## 📊 Sample Output

### Assignment 1: Maze Solver
```
==============================================================
ASSIGNMENT 1: MAZE SOLVER USING BFS AND DFS
==============================================================

--- Breadth-First Search (BFS) ---
Path found! Length: 19
Nodes explored: 45
Time taken: 0.000123 seconds

BFS Path Visualization:
Legend: S=Start, E=End, •=Path, █=Wall, ' '=Walkable
S•        
 •••      
   •      
   ••••   
      •   
      •   
      •   
      ••••
        •E
```

### Assignment 2: Route Finder
```
PERFORMANCE COMPARISON
======================================================================
Algorithm                 Path Length     Nodes Explored       Time (s)       
----------------------------------------------------------------------
Standard BFS              6               15                   0.000089
Standard DFS              8               12                   0.000067
Bi-directional BFS        6               8                    0.000045

• Bi-directional BFS explored 8 nodes
• Standard BFS explored 15 nodes
• Efficiency gain: 46.7% fewer nodes explored
```

### Assignment 3: Treasure Hunt
```
BEST-FIRST SEARCH (Manhattan Distance)
----------------------------------------------------------------------
✓ Treasure found!
  Path length: 26 steps
  Nodes explored: 28
  Time: 0.000156 seconds

KEY INSIGHTS
======================================================================
• Manhattan Distance:
  - Better for grid-based movement (4-directional)
  - Admissible heuristic (never overestimates)
  - More accurate for this problem
```

---

## 🧠 Algorithm Comparison

| Algorithm | Time Complexity | Space Complexity | Optimal? | Complete? |
|-----------|----------------|------------------|----------|-----------|
| BFS | O(b^d) | O(b^d) | ✅ Yes | ✅ Yes |
| DFS | O(b^m) | O(bm) | ❌ No | ✅ Yes* |
| Bi-directional BFS | O(b^(d/2)) | O(b^(d/2)) | ✅ Yes | ✅ Yes |
| Best-First Search | O(b^d) | O(b^d) | ❌ No | ✅ Yes |

*DFS is complete for finite graphs

**Legend:**
- b = branching factor
- d = depth of solution
- m = maximum depth

---

## 📁 Project Structure

```
ai-search-algorithms/
│
├── assignment1_maze_solver.py      # BFS & DFS maze solver
├── assignment2_route_finder.py     # Bi-directional BFS/DFS
├── assignment3_treasure_hunt.py    # Best-First Search
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

---

## 🔧 Customization

### Modify Maze (Assignment 1)
Edit the `maze` variable in `assignment1_maze_solver.py`:
```python
maze = [
    [1, 1, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 1, 1, 1]
]
```

### Modify City Graph (Assignment 2)
Edit the `roads` list in `assignment2_route_finder.py`:
```python
roads = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'),
    # Add more roads...
]
```

### Modify Grid Size (Assignment 3)
Change parameters in `assignment3_treasure_hunt.py`:
```python
grid_size = (20, 20)  # Larger grid
treasure_pos = (18, 18)  # New treasure location
```

---

## 📖 Learning Outcomes

After completing these assignments, you will understand:

1. **Search Strategies:**
   - Uninformed search (BFS, DFS)
   - Informed search (Best-First)
   - Bi-directional search optimization

2. **Data Structures:**
   - Queue (BFS)
   - Stack (DFS)
   - Priority Queue (Best-First)

3. **Algorithm Analysis:**
   - Time and space complexity
   - Optimality guarantees
   - Trade-offs between algorithms

4. **Heuristic Design:**
   - Manhattan distance
   - Euclidean distance
   - Admissibility and consistency

---

## 🎯 Key Takeaways

### When to Use Each Algorithm:

**BFS:**
- ✅ Need shortest path
- ✅ Graph is not too large
- ✅ All edges have equal weight

**DFS:**
- ✅ Memory is limited
- ✅ Any solution is acceptable
- ✅ Exploring all possibilities

**Bi-directional BFS:**
- ✅ Large search space
- ✅ Both start and goal are known
- ✅ Need optimal solution efficiently

**Best-First Search:**
- ✅ Good heuristic available
- ✅ Want fast solutions
- ✅ Optimal solution not critical

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for:
- Bug fixes
- Performance improvements
- Additional algorithms (A*, IDA*, etc.)
- Better visualizations
- More test cases

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

**ASHUTOSH YADAV**
- Email: 23053934@kiit.ac.in
- GitHub: [@ashu13579](https://github.com/ashu13579)

---

## 🙏 Acknowledgments

- Course: Artificial Intelligence
- Institution: KIIT University
- Concepts based on classic AI search algorithms from Russell & Norvig's "Artificial Intelligence: A Modern Approach"

---

## 📚 References

1. Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.)
2. Cormen, T. H., et al. (2009). *Introduction to Algorithms* (3rd ed.)
3. NetworkX Documentation: https://networkx.org/
4. Python heapq Documentation: https://docs.python.org/3/library/heapq.html

---

## 🐛 Known Issues

- Assignment 2 visualization requires matplotlib and networkx
- Large grids in Assignment 3 may take longer to process
- Terminal visualization works best with monospace fonts

---

## 🔮 Future Enhancements

- [ ] Add A* algorithm implementation
- [ ] Add IDA* (Iterative Deepening A*)
- [ ] Interactive GUI for visualizations
- [ ] Performance benchmarking suite
- [ ] 3D maze solver
- [ ] Animated search process

---

**Happy Coding! 🚀**
