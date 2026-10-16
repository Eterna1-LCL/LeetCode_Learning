class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort(key=lambda x: x[0])
        cur = intervals[0]
        ans = []

        for i in range(len(intervals) - 1):

            Next = intervals[i + 1]
            if cur[1] >=  Next[0] :
                cur = [cur[0], max(cur[1], Next[1])]     
            else:
                ans.append(cur)
                cur = Next

        ans.append(cur)
        
        return ans
    
if __name__ == "__main__":
    s = Solution()
    ans = s.merge([[1,3],[2,6],[8,10],[15,18]])
    print(ans)