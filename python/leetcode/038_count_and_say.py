#%%
"""
- Count and Say
- https://leetcode.com/problems/count-and-say/
- Easy

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.
"""


#%%
##
class S1:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        say = "1"
        if n == 1:
            return say


        def nextSay(say):
            count = 0
            pre = say[0]
            res = ''
            for i in range(len(say)):
                if i < len(say)-1:
                    if say[i] == pre:
                        count += 1
                    else:
                        res += (str(count) + pre)
                        pre = say[i]
                        count = 1
                else:
                    if say[i] == pre:
                        count += 1
                    else:
                        res += (str(count) + pre)
                        pre = say[i]
                        count = 1
                    res += (str(count) + pre)
            return res

        for i in range(n-1):
            say = nextSay(say)

        return say

#%%
s = S1()
n = 4
s.countAndSay(n)

#%%
class S2:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = self.countAndSay(n-1) + '*'
        res, count = '', 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                res += str(count) + str(s[i])
                count = 1
        return res


#%%
s = S2()
n = 4
s.countAndSay(n)

#%%
import itertools

class S3:
    def countAndSay(self, n):
        res = '1'
        for i in range(n-1):
            res = ''.join([str(len(list(group))) + digit for digit, group in itertools.groupby(res)])
        return res

#%%
s = S3()
n = 4
s.countAndSay(n)

#%%
