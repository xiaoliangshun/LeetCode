class Solution:
    def plusOne(self, digits):
        leng = len(digits)
        digits[leng-1] += 1         #末位+1
        for i in range(leng-1,-1,-1):           #range(start, stop[, step])
            if digits[i] <= 9:
                return digits
            else:           ##  ==10
                if i == 0:          #最前边的进位
                    digits[0] = 0
                    digits.insert(0,1)
                else:
                    digits[i] = 0
                    digits[i-1] += 1
        return digits

print(Solution().plusOne([9,9,9,9]))
