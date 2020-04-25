#%%
"""
- Plus One Linked List
- https://leetcode.com/problems/plus-one-linked-list/
- Medium
"""

#%%
"""
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example :

Input: [1,2,3]
Output: [1,2,4]
"""

#%%
"""
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example :

Input: [1,2,3]
Output: [1,2,4]
"""

#%%
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#%%
class S1:

    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst = []
        cur = head

        while cur:
            lst.append(cur)
            cur = cur.next

        carry = 1
        for i in range(len(lst)-1, -1, -1):
            lst[i].val += carry
            if lst[i].val < 10:
                carry = 0
                break
            else:
                lst[i].val -= 10
        
        if carry == 1:
            node = ListNode(1)
            node.next = head
            return node
        else:
            return head

#%%
class S2:
    def plusOne(self, head):
        dummy = ListNode(0)
        dummy.next = head

        lastNot9 = dummy
        cur = head
        while cur:
            if cur.val != 9:
                lastNot9 = cur
            cur = cur.next

        lastNot9.val += 1

        cur = lastNot9.next
        while cur and cur.val == 9:
            cur.val = 0
            cur = cur.next

        if dummy.val == 0:
            return dummy.next
        else:
            return dummy

#%%
class S3:
    def plusOne(self, head):
        def dfs(cur):
            if not cur:
                return 1

            carry = dfs(cur.next)
            v = cur.val + carry
            cur.val = v % 10

            return v // 10

        c = dfs(head)
        if not c:
            return head

        new_head = ListNode(c)
        new_head.next = head
        return new_head
