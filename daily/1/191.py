class Solution:
    def brute_force(self, n: int) -> int:
        count = 0
        while n:
            if n & 1 == 1:
                count += 1
            
            n = n >> 1
            
        return count
    
    def bin_lib(self, n: int) -> int:
        # print(type(bin(n))) # string
        return bin(n).count('1')
    
    def bit_manipulation(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= (n-1)
            
        return count
        
    def hammingWeight(self, n: int) -> int:
        # return self.brute_force(n)
        # return self.bin_lib(n)
        return self.bit_manipulation(n)