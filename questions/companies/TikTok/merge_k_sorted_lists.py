'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists):
    if not lists or len(lists) == 0:
        return None
    
    while (len(lists) > 1):
        temp = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i+1 < len(lists) else None
            temp.append(merge_lists(l1,l2))
        lists = temp

    return lists[0]
def merge_lists(l1,l2):
    node = ListNode()
    answer = node

    while l1 and l2:
        if l1.val > l2.val:
            node.next = l2
            l2 = l2.next
        else:
            node.next = l1
            l1 = l1.next
        node = node.next
    if l1:
        node.next = l1
    else:
        node.next = l2

    return answer.next
    
      

l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

merged_node = merge_k_sorted_lists([l1,l2,l3])
while merged_node:
    print(merged_node.val)
    merged_node = merged_node.next