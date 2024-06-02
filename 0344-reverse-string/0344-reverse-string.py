class Solution(object):
    def reverseString(self, s):
        # char = s.split()
        # reverse_char = reverse.char
        # return reverse_char
        # l1 = []
        # for i in range (s):
        # s = s.split()         
        # return s[::-1]

        # for i in range(s):
        #     # print(i)
        #     i[::-1]
        # return i
        l1 = 0
        l2 = len(s)-1
        # arr = []
        while l1 < l2:
           s[l1], s[l2] = s[l2],s[l1]
           l1+=1
           l2-=1
        return s
            