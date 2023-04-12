
class Solution:
    def bfs(self, grid: List[List[int]], start_index):
        
        self.visited.add(start_index)
        
        queue = deque()
        queue.append(start_index)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            node = queue.popleft()
            
            for move in moves:
                r = node[0] + move[0]
                c = node[1] + move[1]
                rc = tuple([r, c])
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                    continue
                else:
                    if grid[r][c] == 1 and rc not in self.visited:
                        self.visited.add(rc)
                        queue.append(rc)
            
            
    
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.visited = set()
        count = 0
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(0, m):
            if tuple([i, 0]) not in self.visited and grid[i][0] == 1:
                self.bfs(grid, tuple([i, 0]))
            if tuple([i, n - 1]) not in self.visited and grid[i][n - 1] == 1:
                self.bfs(grid, tuple([i, n - 1]))
        
        for i in range(0, n):
            if tuple([0, i]) not in self.visited and grid[0][i]:
                self.bfs(grid, tuple([0, i]))
            if tuple([m - 1, i]) not in self.visited and grid[m - 1][i] == 1:
                self.bfs(grid, tuple([m - 1, i]))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and tuple([i, j]) not in self.visited:
                    count += 1
                    
        return count