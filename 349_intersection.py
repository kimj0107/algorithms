class Solution(object):
    def intersection(self, nums1, nums2):
        
        nums1.sort()
        nums2.sort()

        li1 = []

        for n in nums1:
            L = 0
            R = len(nums2) - 1
            

            while L <= R:
                m = (L + R)// 2
                if nums2[m] == n:
                    if not li1 or n > li1[-1]:
                        li1.append(n)
                    break
                    
                elif nums2[m] < n:
                    L = m + 1

                else:
                    R = m - 1

        return li1
