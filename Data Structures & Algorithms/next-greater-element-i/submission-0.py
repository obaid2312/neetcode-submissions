class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsIdx = {n:i for i, n in enumerate(nums1)}
        res = [-1] * (len(nums1))

        st = []

        for i in range(len(nums2)):
            curr = nums2[i]

            while st and curr > st[-1]:
                val = st.pop()
                idx = numsIdx[val]
                res[idx] = curr
            if curr in numsIdx:
                st.append(curr)
        return res