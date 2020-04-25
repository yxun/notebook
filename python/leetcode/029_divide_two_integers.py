#%%
"""
- Divide Two Integers
- https://leetcode.com/problems/divide-two-integers/
- Medium

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
"""

#%%
class S:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        intMax, intMin = 2**31 -1, -2 ** 31

        if divisor == 0:
            return intMax
        if dividend == intMin:
            if divisor == 1:
                return intMin
            elif divisor == -1:
                return intMax

        sign = 1
        if dividend * divisor < 0:
            sign = -1
        
        dividend, divisor = abs(dividend), abs(divisor)

        quo = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= (divisor << shift):
                shift += 1
            dividend -= divisor<<(shift-1)
            quo += 1<<(shift-1)

        if sign*quo < intMin or sign*quo > intMax:
            return intMax
        else:
            return sign*quo


#%%
