# **1.两数之和**

![题目](Img/1两数之和.png)

## 我的解法 暴力求解

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1 , n):
                    res = nums[i] + nums[j]
                    if res == target:
                        return [i, j]
        return [] 
```
## 哈希表求解
由于采用两个for循环时的时间复杂度是$\color{#ff0000}{O(N^2)}$空间复杂度是$\color{#ff0000}{O(1)}$\
因此可以采用哈希表用复杂空间换简单时间\
哈希表其实有一个$\color{#ff0000}{记忆}$功能，在暴力求解的时候中的第二个for循环会遍历多次重复的值所以通过速度慢了\
这个容器就叫做哈希表\
例如：\
2  -> 0\
7  -> 1\
11 -> 2\
15 -> 3

```python
class Solution_1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 在python中哈希表的数据结构是字典 cache -> 缓存
        cache = {} # 哈希表
        for i, item in enumerate(nums):
            cache[item] = i # 制表
        for i, item in enumerate(nums):
            other = target - item
            if other in cache and cache[other] != i:
                return [i, cache[other]] 
        return []

# 边遍历边判断 因此只需要一个for循环
class Solution_2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cache = {} # 哈希表
        for i, item in enumerate(nums):
            other = target - item
            if other in cache:
                return [i, cache[other]] 
            cache[item] = i # 记忆存储
        return []
```

## $\color{#ff0000}{什么时候要用哈希表？}$
当你$\color{#ff0000}{重复}$的去遍历一个数组时可以采用并且可以边遍历边记录值\
或者是当你需要$\color{#ff0000}{记忆}$一个数据的时候采用，有点类似与控制里面的$\color{#ff0000}{info}$

# **167.两数之和Ⅱ（$\color{#ff0000}{有序，两数，唯一解 -> 考虑双指针}$）**
![题目](Img/167两数之和.png)

## 我的解题方法 哈希表

```python
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        cache = {}
        for i, item in enumerate(numbers):
            other = target - item
            if other in cache:
                return [min(i + 1, cache[other] + 1),  max(i + 1, cache[other] + 1)]
            cache[item] = i
        return []
```

由于数组的前提是有序的，$\color{#ff0000}{非递减顺序排列}$，所以 i 一定是大的 cache[other]一定是小的\
因此不需要再去判断大小了，可以直接写了

```python
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        cache = {}
        for i, item in enumerate(numbers):
            other = target - item
            if other in cache:
                return [cache[other] + 1, i + 1]
            cache[item] = i
        return []
```

$\color{#ff0000}{有问题你所设计的解决方案必须只使用常数级的额外空间}$
哈希表并不是常量空间，他的$\color{#ff0000}{空间复杂度是O(N)}$ 

## 正确方法双指针
![左右双指针](Img/167.png)

```python
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        # 一个好方法：在使用while循环的时候先写True让循环跑起来，可以反向思考循环什么时候结束，然后取反就得到了进入循环的条件
        while not left == right: 
            if numbers[left] + numbers [right] > target:
                right -= 1
            elif numbers[left] + numbers [right] < target:
                left += 1
            elif numbers[left] + numbers [right] == target:
                return[left + 1, right + 1]
        return []
```

# **209.长度最小的子数组**
![题目](Img/209长度最小的子数组.png)

## 暴力求解 $\color{#ff0000}{O(N^2)}$
```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total >= s:
                    ans = min(ans, j - i + 1)
                    break
        
        return 0 if ans == n + 1 else ans
```

## 滑动窗口/快慢指针 $\color{#ff0000}{O(N)}$
```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        slow = 0 # 慢指针
        fast = 0 # 快指针
        my_sum = 0
        min_len = float('inf')

        while fast < len(nums):  # 注意小于号不能有等于 等于缩索引不了数组
            my_sum += nums[fast]

            while my_sum >= target:  # 注意这里可能会写成if 不要忘记slow是要一直往前更新的写成if就只会更新一次
                min_len = min(min_len, fast - slow + 1)
                my_sum -= nums[slow]
                slow += 1
            
            fast += 1
        
        if min_len == float('inf'):
            return 0
        else:
            return min_len
```
$\color{#ff0000}{当不满足条件的时候，快指针往前探路；当满足条件的时候慢指针，开始起步}$\
如果题目中包含$\color{#ff0000}{连续、子数组}$ 等就要想到$\color{#ff0000}{滑动窗口，快慢指针}$ \
还有一点就是这个题目中的要求是正整数，所以你区间增大sum才会增大如果不是这样，那么你的快指针将没有什么意义

# **3.无重复字符的最长子串**
![题目](Img/3无重复字符的最长子串.png)

## 滑动窗口/快慢指针 $\color{#ff0000}{O(N)}$

$\color{#ff0000}{看见无重复字符就可以想到set}$

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            left = 0 
            right = 0
            my_set = set()
            max_len = 0

            while right < len(s): 

                if s[right] in my_set: # 如果当前记录过
                    my_set.remove(s[left])
                    left += 1
                else:                  # 如果当前没记录过
                    my_set.add(s[right])
                    max_len = max(max_len, len(my_set))
                    right += 1

            return max_len
```

$\color{#ff0000}{或者是字典或者哈希表}$
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            left = 0 
            Pos = {}
            max_len = 0
            
            for right, char in enumerate(s):

                if char in Pos:
                    left = max(left, Pos[char] + 1)
                Pos[char] = right
                max_len = max(max_len, right - left + 1)

            return max_len
```

类似于滑动窗口由于是连续可以直接截断并且找最长
```python
class Solution:
   def lengthOfLongestSubstring(self, s: str) -> int:
       sub = ""
       res = 0
       for ch in s:
           if ch in sub:
               # 找到重复位置，把重复点之前部分截掉
               idx = sub.index(ch)
               sub = sub[idx + 1:]
           sub += ch
           res = max(res, len(sub))
       return res
```
# 26.删除有序数组中的重复项
![题目](Img/26删除有序数组中的重复项.png)

题目中一提到重复想到$\color{#ff0000}{哈希表或者集合}$是正确的\
但是题目要求原地修改就应该想到$\color{#ff0000}{读写指针}$也是快慢指针的一种，同时$\color{#ff0000}{空间复杂度为常数项}$也是提示词

## 算法图解
![读写指针](Img/26.png)

```python
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        read = 0 
        write = 0 
        while read < len(nums):
            if nums[read] == nums[write]:
                read += 1
            else:
                write += 1
                nums[write] = nums[read]
        return write + 1
```

# 704.二分查找$\color{#ff0000}{O(logN)}$
![题目](Img/704二分查找.png)

题目中一提到$\color{#ff0000}{有序、查找}$想到$\color{#ff0000}{二分查找}$\
这个题目要注意的是$\color{#ff0000}{边界条件}$\
对于大部分的代码来讲习惯用$\color{#ff0000}{左闭右开}$

## 算法图解
![读写指针](Img/704.png)

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)
        mid = (left + right) // 2 # 这是向左取整
        while left < right: # 由于你定义的区间是[left, right)你必须left < right
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # 这里加一的原因是：首先你的区间是左闭右开
                # 由于你中了elif之后你一定已经判断完成mid这个位置的数据了，因此你不要重复判断就需要+1移位
                left = mid + 1    
            elif nums[mid] > target:
                # 这里没有加一的原因是：首先你的区间是左闭右开
                # 由于你中了elif之后你已经判断完成mid这个位置的数据了，但是右边是开区间因此取不到不用加一了
                right = mid 
            mid = (left + right) // 2 # 不要忘记更新mid
        return -1
```

# 59.螺旋矩阵Ⅱ
![题目](Img/59螺旋矩阵.png)

螺旋矩阵这类题是模拟题，即为所见即所得但是这种题很恼火的是$\color{#ff0000}{扣边界条件以及细节}$扣边界条件以及细节记得$\color{#ff0000}{debug}$\
主要考察的是对代码边界能力，记住区间设置原则$\color{#ff0000}{左闭右开}$

## 常规解法

就按照题设的要求来\
思路就是写右->下->左->上，四个for循环再用一个while去填满不同的层
![](Img/59_1.1.png)

```python
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]             # 申请一个nxn的zeros矩阵
        count = 1                                        # 准备填入的数字从1开始的
        start_index = 0                                  # 循环起始点，0 -> (0,0), 1 -> (1,1) ...
        # while范围的确定 如果用 != 的话如果n为偶数最后的count > n**2 会在条件之内
        # 因此while会继续循环，会出现一些问题
        # 所以我们可以以后这种判断估摸着结束条件写>=比较保险
        while not count >= n**2:                         
            # 首先range的范围刚好是左闭右开由于索引是从0开始的
            # 并且引入start_index，因此是(start_index, n - 1 - start_index)
            # 画个矩阵看看就明白了
            # 右循环
            for j in range(start_index, n - 1 - start_index):
                matrix[start_index][j] = count
                count += 1
            # 下循环
            for i in range(start_index, n-1-start_index):
                matrix[i][n-1-start_index] = count
                count += 1
            # 左循环
            for j in range(n-1-start_index, start_index, -1):
                matrix[n-1-start_index][j] = count
                count += 1
            # 上循环
            for i in range(n-1-start_index, start_index, -1):
                matrix[i][start_index] = count
                count += 1
            
            start_index += 1                             # 别忘记给起始点加一了
        
        # 注意这种矩阵的题由于你是四个for为一个大循环因此当n是偶数的时候没有问题
        # 但是当n为奇数的时候中级的数是填不了的
        # 因此需要自己打一个补丁
        if n%2 != 0:
            matrix[n // 2][n // 2] = n**2
        
        return matrix
```

## 边界收缩法
这种是一种特殊方法主要是针对矩阵的特殊操作的方法比如$\color{#ff0000}{螺旋矩阵，对角线，旋转等操作}$

![](Img/59_2.1.png)
![](Img/59_2.2.png)
![](Img/59_2.3.png)

```python
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]             # 申请一个nxn的zeros矩阵
        count = 1                                        # 准备填入的数字从1开始的
        # 准备边界
        top, bottom = 0, n-1                             
        left, right = 0, n-1
        while count <= n**2:

            for j in range(left, right + 1):             # 左闭右开要取到第一行的第n个元素
                matrix[top][j] = count
                count += 1
            top += 1
            for i in range(top, bottom + 1):
                matrix[i][right] = count
                count += 1
            right -= 1
            # 注意边界条件
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = count
                count += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = count
                count += 1
            left += 1

        return matrix
```

## 贪吃蛇法

```python
DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)  # 右下左上
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        i = j = di = 0
        for val in range(1, n * n + 1):  # 要填入的数
            matrix[i][j] = val
            x, y = i + DIRS[di][0], j + DIRS[di][1]  # 下一步的位置
            # 如果 (x, y) 出界或者已经填入数字
            if x < 0 or x >= n or y < 0 or y >= n or matrix[x][y]:
                di = (di + 1) % 4  # 右转 90°
            i += DIRS[di][0]
            j += DIRS[di][1]  # 走一步
        return matrix
```

# 54.螺旋矩阵
![题目](Img/54螺旋矩阵.png)
## 常规解法
```python
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        mat = [0] * m * n
        count = 0
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        while count < m * n:
            for j in range(left, right + 1):
                mat[count] = matrix[top][j]
                count += 1
            top += 1 
            for i in range(top, bottom + 1):
                mat[count] =  matrix[i][right]
                count += 1
            right -= 1
            if top <= bottom:   # 如果是n*n的话总会剩下4个或者一个不存在超出索引
                for j in range(right, left - 1, -1):
                    mat[count] =  matrix[bottom][j]
                    count += 1
                bottom -= 1 
            if left <= right:   # 如果是n*n的话总会剩下4个或者一个不存在超出索引
                for i in range(bottom, top - 1, -1):
                    mat[count] =  matrix[i][left]
                    count += 1
                left += 1 
        return mat
```

## 边界收缩法
注意$\color{#ff0000}{n*n和m*n，不一样会多一个边界}$\
例如是4*3的矩阵会在第九个元素记录结束的时候上下边界会重合\
但是n*n不会

```python
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        mat = [0] * m * n
        count = 0
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        while count < m * n:
            for j in range(left, right + 1):
                mat[count] = matrix[top][j]
                count += 1
            top += 1 
            for i in range(top, bottom + 1):
                mat[count] =  matrix[i][right]
                count += 1
            right -= 1
            if top <= bottom:   # 如果是n*n的话总会剩下4个或者一个不存在超出索引
                for j in range(right, left - 1, -1):
                    mat[count] =  matrix[bottom][j]
                    count += 1
                bottom -= 1 
            if left <= right:   # 如果是n*n的话总会剩下4个或者一个不存在超出索引
                for i in range(bottom, top - 1, -1):
                    mat[count] =  matrix[i][left]
                    count += 1
                left += 1 
        return mat
```

## 贪吃蛇法

```python
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        i = j = 0
        x = y = di = 0
        # 前进方向
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        count = 0
        mat = [0] * m * n

        while count < m * n:

            mat[count] = matrix[i][j]
            visited[i][j] = True
            
            x = i + dirs[di][0]
            y = j + dirs[di][1]

            # 注意这题和旋转矩阵Ⅱ不同的是不用再次记录数组的内容
            # 但是要判断你遇到已读到的格子
            # 因此需要建立一个visited[x][y]里面存放True 和 False表示是否访问过
            # 注意不要认为简单就直接采用matrix[i][j] in mat 如果说有重复数据或者是又0就会产生冲突
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y]:
                di += 1
                di = di % 4 
            i += dirs[di][0]
            j += dirs[di][1]
            count += 1
            
        return mat
```

# 303.区域和检索-数组不可变
![题目](Img/303区域和检索-数组不可变.png)

## 常规解法
这里的时间复杂度取决于left到right的长度，而且会多次调用sumRange

```python
class NumArray:

    def __init__(self, nums: list[int]):

        #初始化数组
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:

        self.my_sum = 0
        for i in range(left, right + 1): # 要求包含下标的数
            self.my_sum += self.nums[i]
            
        return self.my_sum
```

## 我的解法（邪修版前缀和）
这个其实有点小问题，由于我的前缀和的元素数量和原始数组元素数量$\color{#ff0000}{相同}$\
这个就会导致$\color{#ff0000}{边界问题}$\
当在计算(0,2)这种边界，由于前缀和的元素数量和原始数组元素数量相同，你在做差时容易把$\color{#ff0000}{第一位}$减去结果错误

```python
class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.Sum = 0
        # 其实这里没必要用哈希表
        # 因为最后采用的索引方式时下标索引
        # 因此你用list和dict是一样的效果
        # 用dict反而会稍微加大一点空间复杂度
        self.preSum = {} 

        for i, item in enumerate(nums):
            self.Sum += item
            self.preSum[i] = self.Sum

    def sumRange(self, left: int, right: int) -> int:
        
        # 注意扣边界条件，做补丁
        if left == 0:
            return self.preSum[right]
        # 最后返回的索引下表 S_n - S_n-2 = a_n + a_n-1, 所以是 right 对应的值减去left - 1 对应的值
        return self.preSum[right] - self.preSum[left - 1] 
```

## 前缀和

![题目](Img/303.png)

```python
class NumArray:

    def __init__(self, nums: list[int]):

        # 初试化数组
        self.nums = nums
        self.preSum = [0] * (len(nums) + 1)

        # 创建前缀和
        for i in range(len(nums)):
            self.preSum[i + 1] = self.preSum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        
        # 需要注意的是右加一是因为第一位空位了
        return self.preSum[right + 1] - self.preSum[left]
    
```

# 560.和为K的子数组

![题目](Img/560和为K的子数组.png)

## $\color{#ff0000}{错误解法}$

滑动指针其实是错误的\
为什么之前的滑动指针是正确的呢？\
之前的题目中说了$\color{#ff0000}{正整数}$，由于你中间利用了my_sum >= k，就必须要保证是单调的\
因此是不能够使用滑动指针的\
数组必须$\color{#ff0000}{单调}$才能使用

```python
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        left = 0
        right = 0
        my_sum = 0
        count = 0 
        while right < len(nums):

            my_sum += nums[right]
            while my_sum >= k and left < len(nums):
                    if my_sum == k:
                        count += 1
                    my_sum -= nums[left]
                    left += 1 
            right += 1

        return count
    
```

## 正确解法 前缀和+哈希表

以后看到子数组和就要想到前缀和滑动窗口\
如果是$\color{#ff0000}{单调数组}$直接滑动窗口\
如果只是普通数组无脑前缀和然后再通过别的方法去完成任务\
当你得到前缀和这个数组时不就梦回第一题两数之和了吗\
需要在一个数组里面找到两个数之差为k，当然由于你是前缀和因此时要有左右顺序的

```python
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:

        preSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            preSum[i + 1] = preSum[i] + nums[i]

        cache = {}  # 记录的是每个 item 出现的次数，而不是之前的下标索引，这里是和两数之和不同的地方
        count = 0
        
        for i, item in enumerate(preSum):

            # 这边要自己理清楚这个逻辑
            # 由于你是后保存的cache，因此你other的数据一定是已经记录的
            # 换而言之就是前缀和中靠左边的元素
            # 根据要求子数组的和为k 不就是preSum(右) - preSum(左) 即 item - other = k
            other = item - k

            if other in cache:
                # 因此这里count理应加的不是1而是other，也就是要找到的另外一个前缀和出现的次数
                count += cache[other]

            # 因为你不是单调的所以对于当前这个 item 会出现很多次重复的item
            # 因此cache记录的是每个 item 出现的次数
            # 通过cache.get(item, 0)取出对应的key值，如果没有就赋值为0再加一赋值回去，如果存在就直接拿出来加一
            cache[item] = cache.get(item, 0) + 1

        return count
```

## 更简单的写法(与上一个方法原理相同只不过用一个for循环快一点)

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        cache = defaultdict(int)     # cache = defaultdict(int) 会把不存在的key值对应的val写为0
        cache[0] = 1                 # 注意前缀和要要比正常是数组多以为要自己补充 s[0]=0 单独统计
        count = preSum = 0
        
        for item in nums:
            
            preSum += item

            # 这里注意没有判断是否preSum - k存在与cache中
            # 一般来讲key不存在会报错
            # 单数上面初始化的时候不是cache = {} 而是 cache = defaultdict(int)
            # 会把不存在的key值对应的val写为0
            count += cache[preSum - k] 
            cache[preSum] += 1
        
        return count
```