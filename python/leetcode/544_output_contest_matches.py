#%%
"""
- Output Contest Matches
- https://leetcode.com/problems/output-contest-matches/
- Medium
"""

#%%
"""
During the NBA playoffs, we always arrange the rather strong team to play with the rather weak team, like make the rank 1 team play with the rank nth team, which is a good strategy to make the contest more interesting. Now, you're given n teams, you need to output their final contest matches in the form of a string.

The n teams are given in the form of positive integers from 1 to n, which represents their initial rank. (Rank 1 is the strongest team and Rank n is the weakest team.) We'll use parentheses('(', ')') and commas(',') to represent the contest team pairing - parentheses('(' , ')') for pairing and commas(',') for partition. During the pairing process in each round, you always need to follow the strategy of making the rather strong one pair with the rather weak one.

Example 1:

Input: 2
Output: (1,2)
Explanation: 
Initially, we have the team 1 and the team 2, placed like: 1,2.
Then we pair the team (1,2) together with '(', ')' and ',', which is the final answer.
Example 2:

Input: 4
Output: ((1,4),(2,3))
Explanation: 
In the first round, we pair the team 1 and 4, the team 2 and 3 together, as we need to make the strong team and weak team together.
And we got (1,4),(2,3).
In the second round, the winners of (1,4) and (2,3) need to play again to generate the final winner, so you need to add the paratheses outside them.
And we got the final answer ((1,4),(2,3)).
Example 3:

Input: 8
Output: (((1,8),(4,5)),((2,7),(3,6)))
Explanation: 
First round: (1,8),(2,7),(3,6),(4,5)
Second round: ((1,8),(4,5)),((2,7),(3,6))
Third round: (((1,8),(4,5)),((2,7),(3,6)))
Since the third round will generate the final winner, you need to output the answer (((1,8),(4,5)),((2,7),(3,6))).
Note:

The n is in range [2, 212].
We ensure that the input n can be converted into the form 2k, where k is a positive integer.
"""

#%%
# recursion
class S1:
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        def helper(array):
            if len(array) == 1: return array[0]

            res = []
            m = len(array)
            for i in range(m//2):
                res.append('('+array[i]+','+array[m-1-i]+')')
            return helper(res)

        a = list(map(str, range(1, n+1)))
        return helper(a)

#%%
class S2:
    def findContestMatch(self, n):
        a = tuple(range(1, n+1))
        while len(a) > 2:
            a = tuple(zip(a, a[:len(a)//2-1:-1]))
        return str(a).replace(' ', '')

#%%
###  
# iteration
class S3:
    def findContestMatch(self, n):
        cur_round = [str(i) for i in range(1, n+1)]
        nxt_round = []
        while n//2 > 0:
            l, r = 0, n-1
            while l < r:
                t1, t2 = cur_round[l], cur_round[r]
                nxt_round.append('('+t1+','+t2+')')
                l += 1
                r -= 1
            cur_round = nxt_round
            nxt_round = []
            n //= 2
        return cur_round[0]
