class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        all_binaries = {"".join(bits) for bits in product("01", repeat=n)}
        
        for binary in all_binaries:
            if binary not in nums:
                return binary
        return ""