class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        q = deque()
        
        push_size = len(pushed)
        pop_size = len(popped)
        popCounter = 0
        
        for i in range(push_size):
            q.append(pushed[i])
            while q and popped[popCounter] == q[-1] and popCounter < pop_size:
                q.pop()
                popCounter += 1
        
        if q:
            return False
        else:
            return True