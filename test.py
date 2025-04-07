'''
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。



示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：

输入：nums = [1], k = 1
输出：[1]


提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''


def solve(nums, k):

        import math
        inf = math.inf

        res = []
        l, r = 0, k - 1
        preI = -1
        mx = inf
        while r < len(nums):

            bd = mx - 2
            lval, rval = nums[l], nums[r]
            print(lval, rval, bd, mx)
            if l <= preI:
                if rval >= mx:
                    preI, mx = r, rval
            elif lval > bd:
                preI, mx = l, lval
            elif rval > bd:
                preI, mx = r, rval
            else:
                mx = -inf
                for i, e in enumerate(nums[l:r + 1]):
                    if e >= mx:
                        mx = e
                        preI = i + l
            res.append(mx)
            l += 1
            r += 1
        return res

'''
给你一个字符串 s，找到 s 中最长的 回文 子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
'''
def solve2(s):

    n = len(s)
    sub_str = ''
    res = ''
    for i in range(n):
        sub_str = s[i]
        for j in range(i + 1, n):
            sub_str += s[j]
            if check(sub_str):
                if len(sub_str)  > len(res):
                    res = sub_str
    return res

def check(s):

    half = len(s) // 2
    for i in range(half):
        if s[len(s) - i - 1] != s[i]:
            return False
    return True


'''
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的 排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。

 

示例 1：

输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
示例 2：

输入：s1= "ab" s2 = "eidboaoo"
输出：false
'''



def solve3(s1, s2):

    k, n = len(s1), len(s2)
    if k > n: return False

    map1 = [0] * 26
    for c in s1: map1[ord(c) - 97] += 1
    map2 = [0] * 26
    l, r = 0, k
    for c in s2[l:r]: map2[ord(c) - 97] += 1
    
    if check2(map1, map2): return True

    while r < n:

        map2[ord(s2[r]) - 97] += 1
        map2[ord(s2[l]) - 97] -= 1
        if(check2(map1, map2)): return True
        r += 1
        l += 1

    return False

def check2(arr1, arr2):

    ln = len(arr1)
    for i in range(ln):
        if arr1[i] != arr2[i]:
            return False
    return True

if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    res = solve(nums, 3)
    print(res)
    # res = solve2("cbbd")
    # print(res)
    s1, s2 = "ab", "eidbaooo"
    res = solve3(s1, s2)
    print(res)
    s1, s2 = "ab", "eidboaoo"
    res = solve3(s1, s2)
    print(res)