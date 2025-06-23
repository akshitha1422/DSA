class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        n=len(senate)
        rad=deque()
        dire=deque()
        for i in range(len(senate)):
            if senate[i]=='R':
                rad.append(i)
            else:
                dire.append(i)
        while rad and dire:
            r=rad.popleft()
            d=dire.popleft()
            if r<d:
                rad.append(r+n)
            else:
                dire.append(d+n)
        return 'Radiant' if rad else 'Dire'