import collections


def dfs(graph, start, visited=None, path=[]):
    if visited is None:
        visited = set()
    visited.add(start)
    path.append(start)
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited, path)
    return path


def bfs(graph, root, target,  path=[]):
    visited = set()
    queue = collections.deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()

        if vertex == target:
            return path
        path.append(vertex)
        for next in graph[vertex]:
            if next not in visited:
                visited.add(next)
                queue.append(next)
    return []


if __name__ == "__main__":
    graph = {
        0: [1, 2, 3],
        1: [3, 4],
        2: [3],
        3: [4],
        4: []
    }

    print(dfs(graph, 0))
    print(bfs(graph, 2, 4))
