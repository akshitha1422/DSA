class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
        teams=n//2
        total=sum(skill)
        if total%teams!=0:
            return -1
        team_sum=total//teams
        skill.sort()
        left=0
        right=len(skill)-1
        res=[]
        chem=0
        while left<right:
            if skill[left]+skill[right]!=team_sum:
                return -1
            chem+=skill[left]*skill[right]
            left+=1
            right-=1
        return chem
        # while left<right:
        #     if skill[left]+skill[right]==team_sum:
        #         res.append([skill[left],skill[right]])
        #         left+=1
        #         right-=1
        #     elif skill[left]+skill[right]<team_sum:
        #         left+=1
        #     else:
        #         right-=1
        # if len(res)!=teams:
        #     return -1
        # st=0
        # for l,r in res:
        #     st+=l*r
        # return st