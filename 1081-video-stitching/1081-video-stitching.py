class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x:x[0])
        need=0
        end=0
        i=0
        while end<time:
            far=end
            while i<len(clips) and clips[i][0]<=end:
                far=max(far,clips[i][1])
                i+=1
            if far==end:
                return -1
            need+=1
            end=far
        return need