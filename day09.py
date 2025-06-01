# Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.

# Cases for atoi() conversion:

# Skip any leading whitespaces.
# Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
# Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
# If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231.
#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here
        i =0 
        n = len(s)
        result = 0
        sign =1
        max = 2**31 -1
        min = -2**31
        while i < n and s[i] == ' ':
            i += 1
        if i < n and ( s[i] == '+' or s[i]<= '-'):
            sign = -1 if s[i] == '-' else 1 
            i += 1
                
                
        while i< n and '0'<= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            if result >(max - digit)// 10:
                return max if sign == 1 else min
            result = result* 10 +digit
            i +=1
        return sign * result   
            

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends
