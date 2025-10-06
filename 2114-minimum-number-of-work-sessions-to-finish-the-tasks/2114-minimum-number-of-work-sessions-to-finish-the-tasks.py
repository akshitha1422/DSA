class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort(reverse=True)
        n=len(tasks)
        ans=n
        sessions=[]
        def dfs(i):
            nonlocal ans
            if len(sessions)>=ans:
                return
            if i==n:
                ans=min(ans,len(sessions))
                return
            for j in range(len(sessions)):
                if sessions[j]+tasks[i]<=sessionTime:
                    sessions[j]+=tasks[i]
                    dfs(i+1)
                    sessions[j]-=tasks[i]
            sessions.append(tasks[i])
            dfs(i+1)
            sessions.pop()
        dfs(0) 
        return ans