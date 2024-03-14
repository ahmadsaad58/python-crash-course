from collections import defaultdict, deque
from typing import List, Optional

# Number of Distinct Islands
def numDistinctIslands(grid: List[List[int]]) -> int:
    directions = [(1, 0, 'U'), (0, 1, 'R'), (-1, 0, 'D'), (0, -1, 'L')]

    def bfs(row, col, grid):
        q = deque([(row, col)])
        s = 'S'
        
        while q: 
            row, col = q.popleft()
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                for x, y, shape in directions:
                    grid[row][col] = 0
                    q.append((row + x, col + y))
                    s += shape
            else:
                s += 'X'

        return s

    ret = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                ret.add(bfs(i, j, grid))
    return len(ret)


# Number of Islands
def numIslands(grid: List[List[str]]) -> int:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def bfs(row, col, grid):
        q = deque([row, col])

        while q: 
            row, col = q.popleft()
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '1':
                for x, y in directions: 
                    grid[row][col] = '0'
                    q.append((row + x, col + y))
                    

    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                bfs(i, j, grid)
                counter += 1	

    return counter		


# Course Schedule 1
def course_schedule(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
  # build adjacency dict
  pre_map = {i:[] for i in range(numCourses)}
  for crs, pre in prerequisites:
    pre_map[crs].append(pre)

    # create visit set
    visit_set, cycle = set(), set()


    # DFS 
    def dfs(crs):
        # base case
        if crs in cycle:
            return False
        if crs in visit_set: 
            return True

        # DFS now and use visited set for cycles
        cycle.add(crs)
        for pre in pre_map[crs]: 
            if not dfs(pre): 
                return False
        
        cycle.remove(crs)
        visit_set.add(crs)
        return True


    for i in range(numCourses):
        if not dfs(i):
            return False
    return True

# Course Schedule II
def course_schedule_two(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # build adjacency dict
    pre_map = {i:[] for i in range(numCourses)}
    for crs, pre in prerequisites:
        pre_map[crs].append(pre)

    # create visit set
    visit_set, cycle = set(), set()
    ret = []

    # DFS 
    def dfs(crs):
        # base case
        if crs in cycle:
            return False
        if crs in visit_set: 
            return True

        # DFS now and use visited set for cycles
        cycle.add(crs)
        for pre in pre_map[crs]: 
            if not dfs(pre): 
                return False
        
        cycle.remove(crs)
        visit_set.add(crs)
        ret.append(crs)
        return True


    for i in range(numCourses):
        if not dfs(i):
            return []
    return ret



# 3 Sum
def threeSum(nums: List[int]) -> List[List[int]]:
    ret = []
    nums.sort()
    for i, a in enumerate(nums):
        # skip a duplicate for a
        if i > 0 and nums[i-1] == a:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r: 
            sum_ = a + nums[l] + nums[r]
            if sum_ > 0: 
                r -= 1
            elif sum_ < 0: 
                l += 1
            else: # == 0
                ret.append((a, nums[l], nums[r]))
                # update the pointers
                l += 1
                while nums[l] == nums[l-1] and l < r: 
                    l += 1

    return ret

# 3 sum smaller
def threeSumSmaller(self, nums: List[int], target: int) -> int:
    count = 0
    nums.sort() 
    for i, num in enumerate(nums):
        l, r, = i + 1, len(nums) - 1

        while l < r: 
            s = num + nums[l] + nums[r]
            if s < target: 
                count += r-l
                l += 1
            else:
                r -= 1

    return count


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Kth Smallest Element in a BST
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    ret = []
    
    def inorder(node):
        if not node:
            return 

        inorder(node.left)
        if len(ret) == k:
            return
        ret.append(node.val)
        inorder(node.right)

    inorder(root)
    return ret[-1]
        


# Optimal Account Balancing

def minTransfers(transactions: List[List[int]]) -> int:
    # make a map for vals to calculate nodes +/-
    score = defaultdict(int)
    for f, t, a in transactions:
        score[f] -= a
        score[t] += a

    positives = [val for val in score.values() if val > 0]
    negatives = [val for val in score.values() if val < 0]

    def recurse(positives, negatives):
        if len(positives) + len(negatives) == 0: 
            return 0

        neg = negatives[0]

        count = float('inf')

        for pos in positives:
            new_pos = positives.copy()
            new_neg = negatives.copy()

            new_pos.remove(pos)
            new_neg.remove(neg)

            if pos == -neg:
                pass
            elif pos < -neg:
                # add to new negs list
                new_neg.append(pos + neg)
            else:
                # add to new pos list
                new_pos.append(pos + neg)

            count = min(count, recurse(new_pos, new_neg))
        
        return count + 1



    return recurse(positives, negatives)