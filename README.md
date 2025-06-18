
---
# 🐍 Python Sandbox 

**A sandbox for random classes, model, scripts, etc.**

Created and maintained by [@rj-carey](https://github.com/rj-carey)

---
## 🧪 About
This repository is a collection of miscellaneous Python code snippets, models, experiments, and small-scale projects. It's not meant to be production-ready code, but rather a space to try things out, learn, and iterate quickly.

## 📁 Project Structure
While the structure may evolve, here's a general layout:
- `structures/` – From-scratch data structures.
- `algorithms/` – From-scratch basic algorithms.
- `utils/` – Helper functions and modules.
- `experiments/` – Small, self-contained scripts for testing.
- `tests/` - Tests to ensure correctness of implementations.
- `requirements.txt` – List of dependencies, if any.
- `gitignore` - List of ignored files for git control.
- `LICENSE` - MIT License.
- `README.md` – You're here!

## 🧱 Data Structures
This repo includes Python implementations of classic data structures from scratch, without using built-in types like `dict`, `set`, or `heapq`. Useful for educational purposes, interviews, or just brushing up.

Implemented so far: <br> <!--✅⬜-->
✅ Singularly Linked List <br>
✅ Doubly Linked List <br>
✅ Stack <br>
✅ Queue <br>
✅ Priority Queue <br>
✅ Sparse Graph (Adjacency List) <br>
✅ Dense Graph (Adjacency Matrix) <br>
✅ Binary Tree <br>
⬜ AVL Tree <br>
⬜ Heap (Min/Max) <br>
⬜ Hash Table

Each module is self-contained and has associated tests in the `tests/` directory.

## 🧑‍💻 Algorithms
This repo also includes implementations of classic algorithms from scratch, focusing on understanding the underlying principles and how they work. By building these from scratch, you'll gain a deeper understanding of algorithmic thinking and complexity.

Implemented so far: <br> <!--✅⬜-->
⬜ Bubble Sort <br>
⬜ Insertion Sort <br>
⬜ Selection Sort <br>
⬜ Merge Sort <br>
⬜ Quick Sort <br>
⬜ Heap Sort <br>
⬜ Linear Search <br>
⬜ Binary Search <br>
⬜ Dynamic Programming (Fibonacci) <br>
⬜ Depth-First Search <br>
⬜ Breadth-First Search (BFS) <br>
⬜ Dijkstra’s Shortest Path <br>
⬜ Bellman-Ford Algorithm <br>
⬜ Kruskal’s Algorithm <br>
⬜ Floyd-Warshall Algorithm

Each algorithm is implemented with examples and tested for correctness.

## 🚀 Getting Started
To get up and running with the sandbox environment:

### 1. Clone the repository
```bash
git clone https://github.com/rj-carey/sandbox_py.git
cd sandbox_py
```

### 2. Create and activate a virtual environment (recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install dependencies (if applicable)
```bash
pip install -r requirements.txt
```
**Note: If requirements.txt is empty, it's likely no external dependencies are required.**

## ✅ Usage
Use this space to:
* Try out new Python features or libraries
* Prototype scripts quickly
* Store reusable code snippets
* Create structures/algorithms from scratch

## 🧹 Cleanup
To remove the virtual environment (if needed):
```bash
deactivate  # exit virtual env
rm -rf venv  # remove environment folder
```

---
## 📜 License
This project is open source under the [MIT License](LICENSE).

---