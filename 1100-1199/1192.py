"""
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network
where connections[i] = [a, b] represents a connection between servers a and b.
Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

Constraints:
    1 <= n <= 10**5
    n-1 <= connections.length <= 10**5
    connections[i][0] != connections[i][1]
    There are no repeated connections.
"""
from collections import defaultdict
from typing import Optional, List


def critical_connections(n: int, connections: List[List[int]]) -> List[List[int]]:
    graph: defaultdict[int, List[int]] = defaultdict(list)

    for conn in connections:
        graph[conn[0]].append(conn[1])
        graph[conn[1]].append(conn[0])

    low: List[Optional[int]] = [None for _ in range(n)]
    dfn: List[Optional[int]] = [None for _ in range(n)]
    current: int = 0

    def dfs(node, parent):
        nonlocal current

        if dfn[node] is None:
            dfn[node] = current
            low[node] = current
            current += 1

            for conn_node in graph[node]:
                if dfn[conn_node] is None:
                    dfs(conn_node, node)

            if parent is not None:
                low[node] = min([low[idx] for idx in graph[node] if idx != parent] + [low[node]])
            else:
                low[node] = min([low[idx] for idx in graph[node]] + [low[node]])

    dfs(0, None)
    result: List[List[int]] = []

    for conn in connections:
        if low[conn[0]] > dfn[conn[1]] or low[conn[1]] > dfn[conn[0]]:
            result.append(conn)

    return result


if __name__ == '__main__':
    assert critical_connections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]) == [[1, 3]]
