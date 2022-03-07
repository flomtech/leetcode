# Merge two sorted linked lists and return it as a sorted list. 
# The list should be made by splicing together the 
# nodes of the first two lists.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # define the two memory addresses pointing to node to be created
        nodeHead = nodeTrackerCurrent = ListNode()
        
        while l1 and l2:
            if l1.val <= l2.val:
                nodeTrackerCurrent.next = l1
                l1 = l1.next
            else:
                nodeTrackerCurrent.next = l2
                l2 = l2.next
                
            nodeTrackerCurrent = nodeTrackerCurrent.next
            
        if l1: nodeTrackerCurrent.next = l1
        if l2: nodeTrackerCurrent.next = l2
            
        return (nodeHead.next)
        
        