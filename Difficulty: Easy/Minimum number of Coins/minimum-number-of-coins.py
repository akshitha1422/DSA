#User function Template for python3

class Solution:
    def minPartition(self, N):
        coins = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
        used=[]
        for i in coins:
            if i <= N:
                curr = N // i
                for j in range(curr):
                    used.append(i)
                N -= i * curr
            if N == 0:
                break
        return used
