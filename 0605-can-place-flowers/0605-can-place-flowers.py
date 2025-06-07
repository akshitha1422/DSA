class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        place=[None]*len(flowerbed)
        for i in range(len(flowerbed)):
            if flowerbed[i]==1:
                place[i]=False
            else:
                if i==0:
                    if len(flowerbed)==1 or flowerbed[i+1]==0:
                        place[i]=True
                        flowerbed[i]=1
                    else:
                        place[i]=False
                elif i==len(flowerbed)-1:
                    if flowerbed[i]==0 and flowerbed[i-1]==0:
                        place[i]=True
                        flowerbed[i]=1
                    else:
                        place[i]=False
                else:
                    if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                        place[i]=True
                        flowerbed[i]=1
                    else:
                        place[i]=False
        can=place.count(True)
        if can>=n:
            return True
        else:
            return False