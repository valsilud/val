from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node("S")
root.left = Node("I")
root.right = Node("L")
root.left.left = Node("U")
root.left.right = Node("D")


def binary_tree_bfs(root):
    if root is None:
        return []

    queue = deque([root])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.data)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return result


def binary_tree_dfs(root):
    if root is None:
        return []

    result = [root.data]
    result += binary_tree_dfs(root.left)
    result += binary_tree_dfs(root.right)
    return result


graph = {
    "S": ["I", "L"],
    "I": ["S", "U", "D"],
    "L": ["S", "U"],
    "U": ["I", "L", "D"],
    "D": ["I", "U"]
}


def graph_bfs(graph, start):
    visited = {start}
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in sorted(graph[vertex]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def graph_dfs(graph, start):
    visited = set()
    result = []

    def visit(vertex):
        visited.add(vertex)
        result.append(vertex)

        for neighbor in sorted(graph[vertex]):
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return result


def main():
    print("=" * 50)
    print("ASSESSMENT 3.3")
    print("NON-LINEAR DATA STRUCTURE")
    print("NAME: VAL CHRISTIAN V. SILUD")
    print("LAST NAME: SILUD")
    print("=" * 50)

    print("\n1. BINARY TREE")
    print("------------------------------")
    print("          S")
    print("        /   \\")
    print("       I     L")
    print("      / \\")
    print("     U   D")

    print("\nBinary Tree BFS:")
    print(" -> ".join(binary_tree_bfs(root)))

    print("\nBinary Tree DFS (Preorder):")
    print(" -> ".join(binary_tree_dfs(root)))

    print("\n2. GRAPH")
    print("------------------------------")
    for vertex in graph:
        print(f"{vertex}: {graph[vertex]}")

    print("\nGraph BFS (Starting from S):")
    print(" -> ".join(graph_bfs(graph, "S")))

    print("\nGraph DFS (Starting from S):")
    print(" -> ".join(graph_dfs(graph, "S")))

    print("\n3. TRAVERSAL SUMMARY")
    print("------------------------------")
    print("BINARY TREE:")
    print("BFS:", " -> ".join(binary_tree_bfs(root)))
    print("DFS:", " -> ".join(binary_tree_dfs(root)))
