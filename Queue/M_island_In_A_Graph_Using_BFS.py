'''
Islands in a graph using BFS.
Given a binary 2D matrix, find the number of islands. A group of connected 1s forms an island.

Examples: 

Input: M[][] = {{‘1’, ‘1’, ‘0’, ‘0’, ‘0’},
                         {‘0’, ‘1’, ‘0’, ‘0’, ‘1’},
                         {‘1’, ‘0’, ‘0’, ‘1’, ‘1’},
                        {‘0’, ‘0’, ‘0’, ‘0’, ‘0’},
                       {‘1’, ‘0’, ‘1’, ‘1’, ‘0’}}
Output: 4
'''
# Python Program to find the number of islands using Space Optimized BFS

from collections import deque

# A function to check if a given cell (r, c) can be included in BFS
def isSafe(M, r, c):
    rows = len(M)
    cols = len(M[0])
    return (r >= 0) and (r < rows) and (c >= 0) and \
           (c < cols) and (M[r][c] == '1')

# Breadth-First-Search to visit all cells in the current island
def BFS(M, sr, sc):
    # These arrays are used to get row and column numbers of 8 neighbours of a given cell
    rNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
    cNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

    # Simple BFS first step, we enqueue
    # source and mark it as visited
    q = deque()
    q.append((sr, sc))
    M[sr][sc] = '0'

    # Next step of BFS. We take out
    # items one by one from queue and
    # enqueue their unvisited adjacent
    while q:
        r, c = q.popleft()

        # Go through all 8 adjacent
        for k in range(8):
            newR = r + rNbr[k]
            newC = c + cNbr[k]
            if isSafe(M, newR, newC):
                M[newR][newC] = '0'
                q.append((newR, newC))

# This function returns the number of islands 
# (connected components) in a graph
def countIslands(M):
    
    # Mark all cells as not visited
    rows = len(M)
    cols = len(M[0])

    # Call BFS for every unvisited vertex
    # Whenever we see an unvisited vertex,
    # we increment res (number of islands) also.
    res = 0
    for r in range(rows):
        for c in range(cols):
            if M[r][c] == '1':
                BFS(M, r, c)
                res += 1

    return res

if __name__ == "__main__":
    M = [
        ['1', '1', '0', '0', '0'],
        ['0', '1', '0', '0', '1'],
        ['1', '0', '0', '1', '1'],
        ['0', '0', '0', '0', '0'],
        ['1', '0', '1', '1', '0']
    ]

    print(countIslands(M))
