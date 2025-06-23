class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n=len(senate)
        rad=[]
        dire=[]
        for i in range(len(senate)):
            if senate[i]=='R':
                rad.append(i)
            else:
                dire.append(i)
        while rad and dire:
            r=rad.pop(0)
            d=dire.pop(0)
            if r<d:
                rad.append(r+n)
            else:
                dire.append(d+n)
        return 'Radiant' if rad else 'Dire'