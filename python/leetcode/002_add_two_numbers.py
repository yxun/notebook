#%%
from nose.tools import assert_equal

#%% [markdown]
'''
- Add Two Numbers
- https://leetcode.com/problems/add-two-numbers/
- Medium
'''

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

#%%
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


#%%
class S1:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        head = ListNode(0)
        tail = head
        carry = 0
        while p1 and p2:
            num = p1.val + p2.val + carry
            if num > 9:
                num -= 10
                carry = 1
            else:
                carry = 0
            tail.next = ListNode(num)
            tail = tail.next
            p1 = p1.next
            p2 = p2.next
        
        if p2:
            p1 = p2
        
        while p1:
            num = p1.val + carry
            if num > 9:
                num -= 10
                carry = 1
            else:
                carry = 0
            tail.next = ListNode(num)
            tail = tail.next

            p1 = p1.next
        
        if carry:
            tail.next = ListNode(1)
            tail = tail.next
        
        tail.next = None
        return head.next


#%%
t1 = ListNode(2)
t1.next = ListNode(4)
t1.next.next = ListNode(3)

t2 = ListNode(5)
t2.next = ListNode(6)
t2.next.next = ListNode(4)

s = S1()
expected = s.addTwoNumbers(t1, t2)
assert_equal(expected.val, 7)
assert_equal(expected.next.val, 0)
assert_equal(expected.next.next.val, 8)
assert_equal(expected.next.next.next, None)
print('Success')


#%%
class S2:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l1.val + l2.val < 10:
            l3 = ListNode(l1.val + l2.val)
            l3.next = self.addTwoNumbers(l1.next, l2.next)
        elif l1.val + l2.val >= 10:
            l3 = ListNode(l1.val + l2.val - 10)
            tmp = ListNode(1)
            tmp.next = None
            l3.next = self.addTwoNumbers(l1.next, self.addTwoNumbers(l2.next, tmp))
        return l3


#%%
t1 = ListNode(2)
t1.next = ListNode(4)
t1.next.next = ListNode(3)

t2 = ListNode(5)
t2.next = ListNode(6)
t2.next.next = ListNode(4)

s = S2()
expected = s.addTwoNumbers(t1, t2)
assert_equal(expected.val, 7)
assert_equal(expected.next.val, 0)
assert_equal(expected.next.next.val, 8)
assert_equal(expected.next.next.next, None)
print('Success')


#%%
class S3:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2
        if not l2:
            return l1
        
        val1, val2 = [l1.val], [l2.val]
        while l1.next:
            val1.append(l1.next.val)
            l1 = l1.next
        while l2.next:
            val2.append(l2.next.val)
            l2 = l2.next

        num1 = ''.join([str(i) for i in val1[::-1]])
        num2 = ''.join([str(i) for i in val2[::-1]])

        tmp = str(int(num1) + int(num2))[::-1]
        res = ListNode(int(tmp[0]))
        run_res = res
        for i in range(1, len(tmp)):
            run_res.next = ListNode(int(tmp[i]))
            run_res = run_res.next
        return res


#%%
t1 = ListNode(2)
t1.next = ListNode(4)
t1.next.next = ListNode(3)

t2 = ListNode(5)
t2.next = ListNode(6)
t2.next.next = ListNode(4)

s = S3()
expected = s.addTwoNumbers(t1, t2)
assert_equal(expected.val, 7)
assert_equal(expected.next.val, 0)
assert_equal(expected.next.next.val, 8)
assert_equal(expected.next.next.next, None)
print('Success')

#%%
