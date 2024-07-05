# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]  # If less than 3 nodes, no critical points


        a = []
        current = head
        while current:
            a.append(current.val)
            current = current.next

        l = []
        for i in range(1, len(a) - 1):  # Iterate over indices from 1 to len(a) - 2
            if (a[i-1] < a[i] and a[i+1] < a[i]) or (a[i-1] > a[i] and a[i+1] > a[i]):
                l.append(i)
        
        if len(l) < 2:
            return [-1, -1]  # If less than 2 critical points found, cannot calculate


        l.sort()

        maxi = l[-1] - l[0]

        mini = 100000000
        for i in range(len(l)-1):
            x = l[i+1] - l[i]
            if x < mini:
                mini = x

        return [mini,maxi]


        
        
