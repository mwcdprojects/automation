class Solution:
    def reverse(self, x):
        print (type(x))
        if x > -2 ** 31 and x < 2 ** 31 :
            if x > 0 and int(str(x)[::-1])<2**31:
                return int(str(x)[::-1])
            elif x < 0 and int("-"+str(x).replace("-","")[::-1]) > -2**31:
                return int("-"+str(x).replace("-","")[::-1])
            elif x == 0:
                return 0
            else:
                return 0
        else:
            return 0

# if __name__ == "__main__":
#     print (Solution().reverse(123))
#     print (Solution().reverse(-321))
#     print (Solution().reverse(120))
#     print (Solution().reverse(76263287))