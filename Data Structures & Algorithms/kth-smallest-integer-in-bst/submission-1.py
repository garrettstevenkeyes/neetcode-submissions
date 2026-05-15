class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #num elements weve visited from tree
        n = 0
        #iterative 
        stack = []
        #node we are at
        cur = root
        #while cur is not null or stack is not empty
        while cur or stack:
            while cur:
                #add cur to stack so
                #we can go back up to it
                stack.append(cur)
                #go left, we want to hit the min
                cur = cur.left
            #when you go to to far take the last item from the stack
            cur = stack.pop()
            # now we have visited an item, increment 
            n += 1
            # if we have hit our increment limit return cur val
            if n == k:
                return cur.val
            cur = cur.right