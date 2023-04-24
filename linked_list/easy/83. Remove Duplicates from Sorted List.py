# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 建立變數curr指向當下的node
# 變數post指向下一個node
# 持續檢查post是否存在且值和curr相同
# 直到節點不存在或值不相同，將post接在curr後面(等於跳過中間重複的值)
# 接著curr移動到下個值curr.next開始繼續檢查
# 檢查完畢後回傳head
# O(n);O(1)


# 犯錯1: 沒有用curr指向當下的node
# 犯錯2: 沒有用第二層while檢查post
# 犯錯3: post.val == curr.val應作為whil的條件，否則while post會遍歷所有node
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr:
            post = curr.next
            while post and post.val == curr.val:
                post = post.next

            curr.next = post
            curr = curr.next

        return head
