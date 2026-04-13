class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sortnum = sorted(nums)
        for i in range(len(sortnum) - 2):
            if i > 0 and sortnum[i] == sortnum[i-1]:
                continue
            j = i + 1
            k = len(sortnum) - 1
            while k > j:
                if sortnum[i] + sortnum[j] + sortnum[k] == 0:
                    res.append([sortnum[i], sortnum[j], sortnum[k]])
                    while k > j and sortnum[j] == sortnum[j+1]:
                        j+=1
                    while k > j and sortnum[k] == sortnum[k-1]:
                        k-=1
                    j += 1
                    k -= 1
                    
                elif sortnum[i] + sortnum[j] + sortnum[k] > 0:
                    k -= 1
                else:
                    j += 1

        return res
        