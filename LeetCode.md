# **1.两数之和**

![题目](Img\1两数之和.png)

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
![题目](Img\167两数之和.png)

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
![左右双指针](Img\167.png)

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
![题目](Img\209长度最小的子数组.png)

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
![题目](Img\3无重复字符的最长子串.png)

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
![题目](Img\26删除有序数组中的重复项.png)

题目中一提到重复想到$\color{#ff0000}{哈希表或者集合}$是正确的\
但是题目要求原地修改就应该想到$\color{#ff0000}{读写指针}$也是快慢指针的一种，同时$\color{#ff0000}{空间复杂度为常数项}$也是提示词

## 算法图解
![读写指针](Img\26.png)

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
![题目](Img\704二分查找.png)

题目中一提到$\color{#ff0000}{有序、查找}$想到$\color{#ff0000}{二分查找}$\
这个题目要注意的是$\color{#ff0000}{边界条件}$\
对于大部分的代码来讲习惯用$\color{#ff0000}{左闭右开}$

## 算法图解
![读写指针](Img\704.png)

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