# 🚀 Quick Start Guide

Get up and running with AI Search Algorithms in 5 minutes!

## ⚡ Fast Setup

### 1. Clone & Install
```bash
# Clone the repository
git clone https://github.com/ashu13579/ai-search-algorithms.git
cd ai-search-algorithms

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Your First Algorithm
```bash
# Run the maze solver
python assignment1_maze_solver.py
```

That's it! You should see the BFS and DFS algorithms solving a maze.

---

## 📋 What Each Assignment Does

### Assignment 1: Maze Solver
**What it does:** Finds paths through a maze using BFS and DFS

**Run it:**
```bash
python assignment1_maze_solver.py
```

**What you'll see:**
- Visual maze with path marked
- Comparison of BFS vs DFS
- Performance metrics

**Modify it:**
Change the maze in the code:
```python
maze = [
    [1, 1, 0],  # 1 = walkable, 0 = wall
    [0, 1, 1],
    [0, 0, 1]
]
```

---

### Assignment 2: Route Finder
**What it does:** Finds shortest route in a city graph using Bi-directional BFS

**Run it:**
```bash
python assignment2_route_finder.py
```

**What you'll see:**
- Graph visualization (saved as PNG)
- Comparison of BFS, DFS, and Bi-directional BFS
- Efficiency analysis

**Modify it:**
Add more roads to the city:
```python
roads = [
    ('A', 'B'), ('B', 'C'),  # Add your own!
]
```

---

### Assignment 3: Treasure Hunt
**What it does:** Finds treasure using Best-First Search with heuristics

**Run it:**
```bash
python assignment3_treasure_hunt.py
```

**What you'll see:**
- Grid with obstacles and treasure
- Path visualization
- Heuristic comparison (Manhattan vs Euclidean)

**Modify it:**
Change grid size and treasure location:
```python
grid_size = (20, 20)
treasure_pos = (18, 18)
```

---

## 🎓 Learning Path

### Beginner
1. Run all three assignments
2. Read the output and understand the metrics
3. Try modifying the mazes/graphs/grids

### Intermediate
1. Change algorithm parameters
2. Add your own test cases
3. Compare performance on different inputs

### Advanced
1. Implement A* algorithm
2. Add new heuristics
3. Optimize the code
4. Add unit tests

---

## 💡 Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'networkx'"
**Solution:**
```bash
pip install networkx matplotlib
```

### Issue: Visualization not showing
**Solution:** 
- Assignment 2 saves visualizations as PNG files
- Check the current directory for `*_visualization.png` files

### Issue: "No path found"
**Solution:**
- Make sure start and end positions are on walkable cells (1, not 0)
- Ensure there's a valid path between start and end

---

## 🎯 Quick Experiments

### Experiment 1: Compare Algorithm Efficiency
Run Assignment 1 and note:
- Which algorithm explores fewer nodes?
- Which finds the shorter path?
- Which is faster?

### Experiment 2: Test Bi-directional Search
Run Assignment 2 and observe:
- How many fewer nodes does Bi-directional BFS explore?
- Is the path still optimal?

### Experiment 3: Heuristic Impact
Run Assignment 3 and compare:
- Manhattan vs Euclidean distance
- Which explores fewer nodes?
- Which finds a better path?

---

## 📊 Expected Results

### Assignment 1
```
BFS: Shortest path ✓
DFS: Valid path (may be longer)
BFS explores more nodes but guarantees optimal solution
```

### Assignment 2
```
Bi-directional BFS: ~50% fewer nodes explored
Same optimal path as standard BFS
Significant speedup on large graphs
```

### Assignment 3
```
Best-First Search: Fast but not always optimal
Manhattan distance: Better for grid movement
Greedy approach: Efficient but can get stuck
```

---

## 🔧 Customization Examples

### Create Your Own Maze
```python
# In assignment1_maze_solver.py
my_maze = [
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]
start = (0, 0)
end = (4, 4)
```

### Create Your Own City
```python
# In assignment2_route_finder.py
my_roads = [
    ('Home', 'School'), 
    ('School', 'Park'),
    ('Park', 'Mall'),
    ('Mall', 'Home')
]
```

### Create Your Own Grid
```python
# In assignment3_treasure_hunt.py
grid_size = (10, 10)
treasure_pos = (8, 8)
start = (0, 0)
```

---

## 📚 Next Steps

1. **Understand the Code:**
   - Read through each algorithm implementation
   - Understand the data structures used
   - Follow the logic step by step

2. **Experiment:**
   - Try different maze configurations
   - Test with larger graphs
   - Compare performance

3. **Extend:**
   - Add A* algorithm
   - Implement different heuristics
   - Add GUI visualization

4. **Learn More:**
   - Read about informed vs uninformed search
   - Study heuristic design
   - Explore other AI algorithms

---

## 🆘 Need Help?

- Check the main [README.md](README.md) for detailed documentation
- Review the code comments for explanations
- Experiment with smaller examples first
- Compare your output with the expected results

---

## ✅ Checklist

- [ ] Cloned repository
- [ ] Installed dependencies
- [ ] Ran Assignment 1
- [ ] Ran Assignment 2
- [ ] Ran Assignment 3
- [ ] Understood BFS vs DFS
- [ ] Understood Bi-directional search
- [ ] Understood Best-First search
- [ ] Modified at least one example
- [ ] Compared algorithm performance

---

**Ready to dive deeper? Check out the full [README.md](README.md)!**
