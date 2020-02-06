"""Citiations:Prasun Chail"""
class MinimumEditDistance:
    
    def del_cost(self):
        return 1
    
    def ins_cost(self):
        return 1
    
    def sub_cost(self, x, y):
        if x == y:
            return 0
        return self.del_cost() + self.ins_cost()
    
    def dfs(self, x, y, dp, L, L1, source, dest):
        if x == 0 and y == 0:
            if L1 != []:
                L.append(L1)
            return
        
        one = dp[x][y] - self.del_cost()
        two = dp[x][y] - self.ins_cost()
        three = dp[x][y] - self.sub_cost(source[x], dest[y])
        
        if x != 0 and one == dp[x - 1][y]:
            L2 = L1[:]
            L2.append(('delete', source[x]))
            self.dfs(x - 1, y, dp, L, L2, source, dest)
            
        if y != 0 and two == dp[x][y - 1]:
            L2 = L1[:]
            L2.append(('insert', dest[y]))
            self.dfs(x, y - 1, dp, L, L2, source, dest)
            
        if x != 0 and y != 0 and three == dp[x - 1][y - 1]:
            L2 = L1[:]
            if source[x] == dest[y]:
                L2.append(('copy', source[x]))
            else:
                L2.append(('substitute', source[x], dest[y]))
            self.dfs(x - 1, y - 1, dp, L, L2, source, dest)
    
    def soln(self, source1, dest1):
        source = '#' + source1
        dest = '#' + dest1
        N = len(source)
        M = len(dest)
        dp = [[0 for i in range(M)] for j in range(N)]
        
        for i in range(1, N):
            dp[i][0] = dp[i - 1][0] + self.del_cost()
        for j in range(1, M):
            dp[0][j] = dp[0][j - 1] + self.ins_cost()
            
        for i in range(1, N):
            for j in range(1, M):
                one = dp[i - 1][j] + self.del_cost()
                two = dp[i][j - 1] + self.ins_cost()
                three = dp[i - 1][j - 1] + self.sub_cost(source[i], dest[j])
                dp[i][j] = min(one, two, three)
                
        #print(dp)
        L1 = []
        L = []
        self.dfs(N - 1, M - 1, dp, L, L1, source, dest)
        return (dp[N - 1][M - 1], L)
    
obj = MinimumEditDistance()
source = 'stall'
dest = 'table'
#source = input('Enter source string : ')
#dest = input('Enter destination string : ')
L = obj.soln(source, dest)
print('Minimum Edit Distance : ' + str(L[0]))
print('Total Possible Paths : ' + str(len(L[1])))
for i in L[1]:
    print(i)
      
